### File Handling ###

import os


txt_file = open("C:/Users/mamabase/Desktop/curso-python/python-medium/python-medium/my_file.txt","w+") #Escribir y leer
txt_file.write("Mi nombre es Sergio\nMi apellido es Marin\nmi edad es 36\nmi lenguaje favorito es Python")


#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
for line in txt_file.readlines():
    print(line)
txt_file.write("\nAlgo mas")
print(txt_file.readline())


txt_file.close()

#os.remove("C:/Users/mamabase/Desktop/curso-python/python-medium/python-medium/my_file.txt")


#Ficheros Json

import json

json_file = open("C:/Users/mamabase/Desktop/curso-python/python-medium/python-medium/my_file.json","w+")

json_text = {
    "Nombre":"Sergio", 
    "Apellido": "Marin", 
    "Edad":36,
    "Lenguajes": ["Python", "Swift", "Kotlin"]
    }

json.dump(json_text,json_file,indent=4)

json_file.close()

with open("C:/Users/mamabase/Desktop/curso-python/python-medium/python-medium/my_file.json") as other_json_file:
    for line in other_json_file.readlines():
        print(line)

json_dict = json.load(open("C:/Users/mamabase/Desktop/curso-python/python-medium/python-medium/my_file.json"))
print(json_dict)


print(type(json_dict))

print(json_dict["Nombre"])


#CSV files

import csv

csv_file = open("C:/Users/mamabase/Desktop/curso-python/python-medium/python-medium/my_file.csv","w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Nombre","Apellido","Edad","Lenguajes"])
csv_writer.writerow(["Sergio","Marin","36","Python"])
csv_writer.writerow(["Cristina","Reyes","37",""])

csv_file.close()


with open("C:/Users/mamabase/Desktop/curso-python/python-medium/python-medium/my_file.csv") as other_csv_file:
    for line in other_csv_file.readlines():
        print(line)
#xlxs files

# import xlrd, debe instalarse el modulo

#xml files
        


import xml

xml_file = open("C:/Users/mamabase/Desktop/curso-python/python-medium/python-medium/my_file.xml","w+")

xml_file.write("<Persona>\n")
xml_file.write("\t<Nombre>\n")
xml_file.write("\t\tSergio\n")
xml_file.write("\t</Nombre>\n")
xml_file.write("</Persona>\n")

with open("C:/Users/mamabase/Desktop/curso-python/python-medium/python-medium/my_file.xml") as other_xml_file:
    for line in other_xml_file.readlines():
        print(line)


