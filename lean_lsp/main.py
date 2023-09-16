import pathlib
import shutil
import subprocess
import sys

LAKE = shutil.which("lake")

def main():
    p = subprocess.Popen(
        [LAKE, 'serve', *sys.argv[1:]],
        stdin=sys.stdin, stdout=sys.stdout
    )
    sys.exit(p.wait())


def load(app):
    return {
        "lean-language-server": {
            "version": 2,
            "argv": ['lean-lsp'],
            "languages": ["lean4", "lean"],
            "mime_types": [
                "text/lean",
                "text/x-lean",
                "text/lean4",
                "text/x-lean4"
            ]
        }
    }


if __name__ == "__main__":
    main()