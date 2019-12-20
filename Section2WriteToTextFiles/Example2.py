try:
    with open("oceans.txt","r") as oceansFile:
        for ocean in oceansFile:
            print(ocean)

    with open("oceans.txt","a") as oceansFile:
        oceansFile.write("Southern\n")
        oceansFile.write("Arctic\n")

except:
    print("No such file in current directory.")

#Read and Write permissions - not appending
# with open("citiesInGermany.txt","w+") as citiesFile:
#     for city in citiesFile:
#         print(city)
#     print(citiesFile.tell())
#     print(citiesFile.tell())
#     citiesFile.write("Stuttgard\n")

# Example with feet to meters : https://www.worldatlas.com/aatlas/infopage/oceans.htm

