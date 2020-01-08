with open('owais.JPG', 'rb') as rf :
    with open('owais_cpy', 'wb') as wf :
        for line in rf:
            wf.write(line)