'''text = open('abc.txt')
x = 0
for io in text:
    if ('Allah') in io:
        print(io.upper())
        x += 1
print(x)'''


text = open('abc.txt')


for io in text:

    w = io.split()

    for i in range(2):
        we = w.pop(i)
        print(w)
