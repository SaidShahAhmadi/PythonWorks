from pathlib import Path
from time import ctime
import os
import glob


# path = Path(".").rglob("*.py*")

# for g in path:
#     print(gs)


# path = Path("path.py")

# paths = [p for p in path.iterdir() if p.is_dir()]
# py_files = [p for p in path.rglob("*.py")]
# print(py_files)


path = Path("path.py")

size = os.path.getsize(path)
print(ctime(path.stat().st_atime))
print(size)