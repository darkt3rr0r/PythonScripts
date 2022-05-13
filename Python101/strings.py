string0 = 'dark'
string1 = "Hello World"
string2 = "Welcome to Python basics"

print(string1)
print(string2)

string3 = """This is an example
of a long
string with 3 double quotes"""

print(string3)

string4 = "I'am using both single and double quotes"
print(string4)

string5 = 'I"am reverse of string4'

## Using \ escape

string6 = "I\"m using both double quotes inside and outside.\nAlso using the newline character"
print(string6)

string7 = "aaaaaaaaaaa"
print(string7)

string8 = "a"*10
print(string8)

print(len(string7))
print(len(string8))


print("abhi" in string0)
print(string4.startswith("I"))
print(string4.startswith("a"))

print(string4.index("single"))
print(string4.upper())
print(string4.lower())

messy_string = "  This is Ugly! No, you are, not  "

print(messy_string)
print(messy_string.strip())

print(messy_string.replace("!","?"))
#print(messy_string).replace("Ugly","Veryugly")

print(messy_string.split()) # Converts string into a list of words

#split can be done with reference to charactes

print(messy_string.split(','))

#using just we can have spaces/justification
txt = "banana"
x = txt.rjust(20,"Y")
print(txt.rjust(24))
print(x)
x= txt.ljust(20,"Y")
print(x)

# Simple Concat

print("I am" + "a string")
print("String 4 is " + str(len(string4))+" characters long")

print(1+1)
print("1"+"1")

# F-string

print(f"String4 is {str(len(string4))} characters long")

# Format string

print("{2} {0} {1}".format(len(string4),5.0,0x12))


print("String4 is {length:.2f} characters long".format(length=len(string4)))

print("String4 is {length:o} characters long".format(length=len(string4)))

