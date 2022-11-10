#first
import os.path
import pathlib
from os import path
z = path.exists('test_97.txt')
print('path identified')
w = pathlib .Path('test_97.txt')
def result_disp():
    print('file_path',z)
    print('file directory',w)

if __name__ == "__main__":
    result_disp()
