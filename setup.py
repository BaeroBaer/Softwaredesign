import subprocess
import sys
from pathlib import Path


def main() -> int:
    repo_root = Path(__file__).resolve().parent
    target = repo_root / 'project_setup' / 'setup.py'
    if not target.exists():
        print('Missing file: project_setup/setup.py')
        return 1

    cmd = [sys.executable, str(target), *sys.argv[1:]]
    print('>', ' '.join(cmd))
    completed = subprocess.run(cmd)
    return completed.returncode


if __name__ == '__main__':
    raise SystemExit(main())
