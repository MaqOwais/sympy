import os

os.chdir('/Users/muhammedabdulquadirowais/Desktop/')

print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'),'maqo_rety.txt')
print(file_path)

with open(file_path, 'w') as f:
    x = f.writelines('here is maqo rettty so please let me know you clearly and start the particular observations while typing')
    x

    print(x)