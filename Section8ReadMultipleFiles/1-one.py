import fileinput

'''files = fileinput.input(files=('file1.txt', 'file2.txt', 'file3.txt'))
for line in files:
    print(' -> ' + line, end='')
'''

with fileinput.input(files=('file1.txt', 'file2.txt', 'file3.txt')) as f:
    for line in f:
        print(line)

