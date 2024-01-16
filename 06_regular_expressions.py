### Regular Expressions ###

import re


#match

my_string = "Esta es la lección número 6,\n despues viene la Lección 7: expresiones Expresiones Regulares"
my_other_string = "Esta no es la lección número 5: Expresiones Regulares"

print(re.match("esta es la lección",my_string,re.I)) #Flag I: Ignore uppercase
print(re.match("Esta es la lección",my_other_string))
print(re.match("Expresiones Regulares",my_string))

match = re.match("esta es la lección",my_string,re.I)
print(match)

start, end  = match.span() #Rango de coincidencia

match = print(re.match("Esta no es la lección", my_other_string))
if not(match == None):
    print(match)

if match is not None:
    print(match)

if match != None:
    print(match)

print(my_string[start:end])


#search

search = re.search("lección",my_string,re.I) #Se diferencia del match porque puede encontrarlo en cualquier lugar
print(search)
start, end  = search.span()

print(start,end)
print(my_string[start:end])

#findall

findall = re.findall("lección",my_string)
print(findall)

#split

split = re.split("\n",my_string)
print(split)

#sub

sub = re.sub("Expresiones","expresiones",my_string)
sub = re.sub("Expresiones | expresiones "," fexpresiones ",my_string)
print(sub)


#Patters
my_string = "Esta es la lección número 6, despues viene la Lección 7: expresiones Expresiones Regulares"
pattern = r'[lL]eccion'
print(my_string)
print(re.findall(pattern,my_string))

pattern = r'[lL]ección|Expresiones'
print(re.findall(pattern,my_string))

pattern = r'[a-z]'
print(re.findall(pattern,my_string))

pattern = r'\d' #solo numeros
print(re.findall(pattern,my_string))

pattern = r'\D' #solo letras
print(re.findall(pattern,my_string))