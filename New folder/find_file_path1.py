import shutil
from os import path
f1 = path.exists('py1.txt')

def path_disp():
    
    (head, tail) = path.split(f1)
    print('Dir path',+head)
    print('File name',+tail)

if __name__ == "__main()__"
    path_disp()

