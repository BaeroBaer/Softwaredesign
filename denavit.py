import numpy as np
import matplotlib.pyplot as plt

alpha = 1
a, b = -50, 50
L = b - a
N = 1000
x = np.linspace(a, b, N, endpoint=False)
dx = x[1] - x[0]

# Define discrete wavenumbers
kappa = np.fft.fftfreq(N, (b - a) / (N * 2 * np.pi))

# Initial condition
u0 = np.zeros_like(x)
u0[np.abs(x) < 10] = 1
u0hat = np.fft.fft(u0)

# Simulate in Fourier frequency domain
dt = 0.001
T = np.arange(0, 10, dt)

fun = lambda t, x:-(alpha * (kappa**2) * y #right hand side for the euler function
euler = lambda y, dt, t, fun: y + dt * fun(t, y) # euler step

uhat = np.zeros((len(T), len(u0hat)), dtype="complex")
uhat[0, :] = u0hat
for i, t in enumerate(T[1:]):
    uhat[i + 1, :] = euler(uhat[i, :], dt, t, fun)

u = np.zeros_like(uhat)

for k in range(len(T)):
    u[k, :] = np.fft.ifft(uhat[k, :])

u = u.real

# Waterfall plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$t$")
ax.set_zlabel(r"$u(t, x)$")
ax.set_zticks([])

u_plot = u[0 : -1 : int(1 / dt), :]
for j in range(u_plot.shape[0]):
    ys = j * np.ones(u_plot.shape[1])
    ax.plot(x, ys, u_plot[j, :])

# Image plot
plt.figure()
plt.imshow(np.flipud(u[0:-1:100]), aspect=8)
plt.xlabel(r"$x$")
plt.ylabel(r"$t \to$")
plt.gca().axes.get_xaxis().set_ticks([])
plt.gca().axes.get_yaxis().set_ticks([])
plt.show()