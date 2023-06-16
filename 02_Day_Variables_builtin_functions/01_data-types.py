
###*** Data Types in Python ***###

#^Check Data types: To check the data type of certain data/variable we use the type Example:

# Different python data types
# Let's declare variables with various data types

first_name = 'Asabeneh'     #* str
last_name = 'Yetayeh'       #* str
country = 'Finland'         #* str
city= 'Helsinki'            #* str
age = 250                   #* int, it is not my real age, don't worry about it

# Printing out types
print(type('Asabeneh'))     #* str
print(type(first_name))     #* str
print(type(10))             #* int
print(type(3.14))           #* float
print(type(1 + 1j))         #* complex
print(type(True))           #* bool
print(type([1, 2, 3, 4]))   #* list
print(type({'name':'Asabeneh','age':250, 'is_married':250}))    #* dict
print(type((1,2)))                                              #* tuple
print(type(zip([1,2],[3,4])))                                   #* set

###*** Casting Data Types ***###

#^ int to float
num_int = 10
print('num_int:', num_int)
num_float = float(num_int)
print("num_float:", num_float)

#^ float to int
gravity = 9.81
print(int(gravity))

#^int to str
num_int = 10
print('num_int:', num_int) #* 10
num_str = str(num_int)
print('num_int:', num_str) #* '10'

#^str to int or float
num_str1 = '10.6'
#print('num_int', int(num_str1))     #* 10
print('num_float', float(num_str1)) #* 10.6

#* str to list
first_name = "Paco"
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list) #* ['P', 'a', 'c', 'o']
