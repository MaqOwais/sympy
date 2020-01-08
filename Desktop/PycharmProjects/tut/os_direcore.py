import os

os.chdir('/Users/muhammedabdulquadirowais/Desktop/')

for dirpath , dirnames , filenames in os.walk('/Users/muhammedabdulquadirowais/Desktop/'):
    print( "current Path :" , dirpath)
    print(' Directories :', dirnames)
    print('files :' , filenames)
    print()
