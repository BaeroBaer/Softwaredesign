import subprocess
import sys
from pathlib import Path


def run(cmd: list[str]) -> None:
    print('>', ' '.join(cmd))
    subprocess.run(cmd, check=True)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    python_exe = sys.executable

    notebooks = [
        repo_root / 'Selfstudysession_B' / 'Selfstudysession_B2#KAL.ipynb',
        repo_root / 'Selfstudysession_C' / 'Sefstudysession_C#KAL.ipynb',
        repo_root / 'Selfstudysession_D' / 'Selfstudysession_D#KAL.ipynb',
        repo_root / 'Selfstudysession_E' / 'Selfstudysession_E#KAL.ipynb',
    ]

    for nb in notebooks:
        if nb.exists():
            run([
                python_exe,
                '-m',
                'jupyter',
                'nbconvert',
                '--to',
                'notebook',
                '--execute',
                '--inplace',
                str(nb),
            ])
        else:
            print(f'Skipped (not found): {nb}')

    print('Finished executing all found notebooks.')


if __name__ == '__main__':
    main()
