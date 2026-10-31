"""Apply maintained MaaFwApp patches without changing its pinned commit."""

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def apply_patches(root=ROOT):
    frontend = root / "Android" / "MaaFwApp"
    if not (frontend / "app").is_dir():
        raise RuntimeError("Initialize submodules: git submodule update --init --recursive")
    for patch in sorted((root / "Android" / "patches").glob("*.patch")):
        command = ["git", "-C", str(frontend), "apply"]
        reverse = subprocess.run(
            [*command, "--reverse", "--check", str(patch)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        if reverse.returncode == 0:
            print(f"Already applied: {patch.name}")
            continue
        check = subprocess.run(
            [*command, "--check", str(patch)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        if check.returncode:
            raise RuntimeError(
                f"Cannot apply {patch.name}; inspect submodule changes first.\n"
                + check.stderr.decode("utf-8", errors="replace")
            )
        subprocess.run([*command, str(patch)], check=True)
        print(f"Applied: {patch.name}")


if __name__ == "__main__":
    apply_patches()
