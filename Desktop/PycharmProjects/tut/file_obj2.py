
with open('abc.txt','r') as rf:
    with open('abc_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
