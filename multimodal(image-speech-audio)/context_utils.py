import os
import sys


class PathContext:
    def __init__(self, path):
        self.target_path = path
        self.previous_path = os.getcwd()

        if self.target_path not in sys.path:
            sys.path.append(self.target_path)

    def __enter__(self):
        os.chdir(self.target_path)

    def __exit__(self, _type, value, traceback):
        os.chdir(self.previous_path)
        sys.path.remove(self.target_path)

