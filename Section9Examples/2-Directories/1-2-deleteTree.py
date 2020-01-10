import shutil

try:
    shutil.rmtree('testDir3')
except:
    print('Error')
