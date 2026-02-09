import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import model_selection
import pandas as pd

#config InlineBackend.figure_formats = ["svg"]
np.random.seed(6020)

m = 200
n = 10

A = np.random.randn(m, n)
x = np.array([0, 0, 1, 0, 0, 0, -1, 0, 0, 0])
b = A @ x + 2 * np.random.randn(m)

# k-cross validation for the Lasso method
cv = 10
lassoCV = linear_model.LassoCV(cv=cv, random_state=6020, tol=1e-8)
lassoCV.fit(A, b)
# Recompute the lasso method for the optimal lambda selected
lasso_best = linear_model.Lasso(alpha=lassoCV.alpha_, random_state=6020)
lasso_best.fit(A, b)

# Plotting
plt.figure()
Lmean = lassoCV.mse_path_.mean(axis=-1)
error = [
    np.min(lassoCV.mse_path_, axis=-1),
    np.max(lassoCV.mse_path_, axis=-1),
] / np.sqrt(cv)
plt.errorbar(lassoCV.alphas_, Lmean, yerr=error, ecolor="lightgray")
plt.plot(lassoCV.alpha_, Lmean[lassoCV.alphas_ == lassoCV.alpha_], "go", mfc="none")
plt.xscale("log")
plt.ylabel("Means Square Error")
plt.xlabel(r"$\lambda_1$")
plt.gca().invert_xaxis()
plt.show()