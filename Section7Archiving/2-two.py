import zipfile

with zipfile.ZipFile('newzip.zip', 'r') as zipobj:
    #print(zipobj.namelist())
    zipfilelist = zipobj.namelist()

for el in zipfilelist:
    print(el)

zipExtract = zipfile.ZipFile('newzip.zip', 'r')
zipExtract.extractall('extractDir')
zipExtract.close()
