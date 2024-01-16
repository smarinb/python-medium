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
''
pattern_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
my_email = 'sergemb87@gmail.com'

print(re.match(pattern_email,my_email))
print(re.search(pattern_email,my_email))
print(re.findall(pattern_email,my_email))

'''

    []: A set of characters
        [a-c] means, a or b or c
        [a-z] means, any letter from a to z
        [A-Z] means, any character from A to Z
        [0-3] means, 0 or 1 or 2 or 3
        [0-9] means any number from 0 to 9
        [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9

    \: uses to escape special characters
        \d means: match where the string contains digits (numbers from 0-9)
        \D means: match where the string does not contain digits
    . : any character except new line character(\n)
    ^: starts with
        r'^substring' eg r'^love', a sentence that starts with a word love
        r'[^abc] means not a, not b, not c.
    $: ends with
        r'substring$' eg r'love$', sentence that ends with a word love
    *: zero or more times
        r'[a]*' means a optional or it can occur many times.
    +: one or more times
        r'[a]+' means at least once (or more)
    ?: zero or one time
        r'[a]?' means zero times or once
    {3}: Exactly 3 characters
    {3,}: At least 3 characters
    {3,8}: 3 to 8 characters
    |: Either or
        r'apple|banana' means either apple or a banana
    (): Capture and group


https://regex101.com/

'''