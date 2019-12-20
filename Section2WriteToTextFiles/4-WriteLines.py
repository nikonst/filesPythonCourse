fo = open("writelines.txt", "w")

fo.writelines("Madrid")
fo.writelines("Barcelona")

citiesInSpain =["Valencia\n", "Seville\n", "Bilbao\n"]
for c in citiesInSpain:
    fo.writelines(c)

fo.close()