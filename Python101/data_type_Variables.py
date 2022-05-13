name = "abhi"
print(name)

name_length = 4
print(name_length)

name,name_length = "dark", 4 # One line assignment

print(type(name))
print(type(name_length))

name_length = int("4") # Type conversion
print(type(name_length))

#name = int("a") Illegal type casting
#print(type(name))

# Declaring a list

name_list = ["abhi","dark"]
print(type(name_list))

a , b = name_list # Assignment of variable to the values in a list sequentially
print(a)
print(b)
# The key difference between the tuples and lists is that while the tuples are immutable objects the lists are mutable. This means that tuples cannot be changed while the lists can be modified. Tuples are more memory efficient than the lists

# Tuples

name_tuple = ("abhi","dark")
print(type(name_tuple))
print(name_tuple)

# Dictionary 

name_dict = {"abhi": 4,"terror":6} 
print(type(name_dict))
print(name_dict)

name_bool = True
name_booL= False

print(type(name_bool))
print(name_booL)

name_bytes = b"abhi1"
print(type(name_bytes))
print(name_bytes)

