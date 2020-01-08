import os
print(os.getcwd())
os.chdir('/Users/muhammedabdulquadirowais/Desktop')
print(os.getcwd())

we = os.listdir()

print(we)

we[0] = 'help in our goal'

os.rename('bbk','politics')

we = os.listdir()

print(we)


