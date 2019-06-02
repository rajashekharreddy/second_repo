with open('test1111.txt', 'r') as f:
    for line in iter(f.readline, ''):
        print line.encode('hex')  # Don't mess up my terminal