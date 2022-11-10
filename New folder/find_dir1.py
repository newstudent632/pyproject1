import os.path
#import pathlib
from os import path
path1 = path.exists('py1.txt')
print('path idenfitied')
dir1 = path.isdir('E:/raaji')
def result_disp():
    print('file_path',path1)
 #  if dir1.exists():
    print('file_direcorty',dir1)
#    else:
#    print('no file found')

if __name__== "__main__":
    result_disp()
