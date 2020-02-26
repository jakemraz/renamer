import os
import sys

def changeName(path, src, tgt):
    i = 1
    for filename in os.listdir('./'):
        if filename == 'renamer.py':
            continue
        newfilename = filename.replace(src,tgt)
        print(str(i) + '. ' + filename + ' to ' + newfilename)
        os.rename(path+filename,path+newfilename)
        i = i + 1
    print('total ' + str(i-1) + ' files changed')

src = sys.argv[1]
tgt = sys.argv[2]

changeName('./', src, tgt)
