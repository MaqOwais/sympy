# file objects

with open('abc.txt','r') as f:
    '''f_abc = f.readline()
    print(f_abc)
    for i in range(3):

        f_abc = f.readline()
        print(f_abc,end = '')'''

    for line in f:
        print(line, end='')

