import argparse
import subprocess
import sys
from pathlib import Path


PYPROJECT_CONTENT = """[project]
name = \"softwaredesigne-kal\"
version = \"0.1.0\"
description = \"Self study sessions B-E\"
readme = \"README.md\"
requires-python = \">=3.11\"
dependencies = [
  \"numpy\",
  \"pandas\",
  \"matplotlib\",
  \"pydantic\",
  \"jupyter\",
  \"nbconvert\",
  \"ipykernel\"
]

[tool.pdm]
distribution = false

[tool.pdm.scripts]
check = \"python -c \\\"import numpy, pandas, matplotlib, pydantic, jupyter; print('Imports OK')\\\"\"
notebook = \"jupyter notebook\"
run-notebooks = \"python project_setup/run_all_notebooks.py\"
"""


def run(cmd: list[str]) -> None:
    print('>', ' '.join(cmd))
    subprocess.run(cmd, check=True)


def ensure_pdm() -> None:
    try:
        subprocess.run([sys.executable, '-m', 'pdm', '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except (subprocess.CalledProcessError, FileNotFoundError):
        run([sys.executable, '-m', 'pip', 'install', 'pdm'])


def ensure_pyproject(repo_root: Path) -> None:
    pyproject = repo_root / 'pyproject.toml'
    if not pyproject.exists():
        # Write UTF-8 without BOM so TOML parser and PDM read it reliably.
        pyproject.write_text(PYPROJECT_CONTENT, encoding='utf-8')


def pdm_cmd(*args: str) -> list[str]:
    # -n avoids interactive prompts (important for one-click Run in VS Code).
    return [sys.executable, '-m', 'pdm', '-n', *args]


def main() -> None:
    parser = argparse.ArgumentParser(description='Project setup helper for Softwaredesigne-KAL')
    parser.add_argument('--no-check', action='store_true', help='Skip pdm run check')
    parser.add_argument('--open-notebook', action='store_true', help='Start Jupyter notebook at the end')
    parser.add_argument('--run-notebooks', action='store_true', help='Execute all notebooks via pdm script')
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]

    ensure_pdm()
    ensure_pyproject(repo_root)

    run(pdm_cmd('install'))

    if not args.no_check:
        run(pdm_cmd('run', 'check'))

    if args.run_notebooks:
        run(pdm_cmd('run', 'run-notebooks'))

    if args.open_notebook:
        run(pdm_cmd('run', 'notebook'))


if __name__ == '__main__':
    try:
        main()
    except subprocess.CalledProcessError as exc:
        sys.exit(exc.returncode)

