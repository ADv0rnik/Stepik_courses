import os
from pathlib import Path


BASE_DIR = Path("__file__").resolve().parent.parent
SAMPLE_DIR = Path.joinpath(BASE_DIR, "./main")
OUT_FILE = Path.joinpath(BASE_DIR, "./test_out.txt")
POSTFIX = "py"
basedir_len = len(str(BASE_DIR).split("\\"))


def check_dirs(dir_path):
    target_dirs = []
    for parent, dirs, files in os.walk(dir_path):
        if any(map(lambda x: x.endswith(POSTFIX), files)):
            target_dirs.append(parent.split("\\")[basedir_len:])
    return target_dirs

dirs = check_dirs(SAMPLE_DIR)
dir_paths = ["/".join(dir_).lstrip("/") for dir_ in dirs]

with open(OUT_FILE, "w") as outf:
    for dir_ in dir_paths:
        outf.write(dir_ + "\n")


