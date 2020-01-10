import os

for fileName in os.listdir('aDirectory'):
    if fileName.endswith('.py'):
        print(fileName)

for fileName in os.listdir('aDirectory'):
    if fileName.endswith('.txt'):
        print(fileName)
