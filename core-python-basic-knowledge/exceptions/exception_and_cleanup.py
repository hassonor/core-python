import os
import sys


def make_at(path, dir_name):
    original_path = os.getcwd()
    os.chdir(path)
    try:
        os.mkdir(dir_name)

    except OSError as e:
        print(e, file=sys.stderr)
        raise

    finally:
        os.chdir(original_path)