import zipfile

files = ['sometext.txt', 'somefolder']

with zipfile.ZipFile("newzip.zip", 'w') as newzip:
    for filename in files:
        newzip.write(filename)

with zipfile.ZipFile('newzip.zip', 'a') as newzip:
    newzip.write('someothertext.txt')


