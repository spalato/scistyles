"""Release script: test, bump version, tag, push, build, publish.

Usage: python release.py [v]X.Y.Z
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
INIT = ROOT / "src" / "scistyles" / "__init__.py"


def run(*cmd, capture=False):
    print("$", " ".join(cmd))
    res = subprocess.run(cmd, cwd=ROOT, check=True, text=True, capture_output=capture)
    return res.stdout.strip() if capture else None


def main():
    arg = sys.argv[1].removeprefix("v") if len(sys.argv) == 2 else ""
    if not re.fullmatch(r"\d+\.\d+\.\d+", arg):
        sys.exit(__doc__)
    version = arg
    tag = f"v{version}"

    if run("git", "status", "--porcelain", capture=True):
        sys.exit("Working tree not clean; commit or stash first.")
    if run("git", "tag", "--list", tag, capture=True):
        sys.exit(f"Tag {tag} already exists.")

    run(sys.executable, "-m", "pytest", "test")

    text = INIT.read_text(encoding="utf-8")
    new, n = re.subn(r"^__version__\s*=.*$", f"__version__ = '{version}'", text, flags=re.M)
    if n != 1:
        sys.exit("Could not find __version__ in __init__.py")
    INIT.write_text(new, encoding="utf-8")

    run("git", "add", str(INIT))
    run("git", "commit", "-m", f"version bump to {version}")
    run("git", "tag", tag)
    run("git", "push", "origin", "HEAD", tag)

    shutil.rmtree(ROOT / "dist", ignore_errors=True)  # avoid uploading stale builds
    run(sys.executable, "-m", "flit", "build")
    run(sys.executable, "-m", "flit", "publish")
    print(f"Released {tag}")


if __name__ == "__main__":
    main()
