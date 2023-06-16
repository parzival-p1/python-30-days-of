import math

###*** Exercises in Python ***###

#^2. Using the len() built-in function, find the length of your first name
first_name = 'Francisco'
print(len(first_name)) # 9

#^3. Compare the length of your first name and your last name
last_name = 'Hernandez'
print(len(last_name))
str_compare = len(first_name) == len(last_name) # True
print(str_compare)

#^4. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#& Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total) # 9

#& Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(diff) # 1

#& Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
print(product) # 20

#& Divide num_one by num_two and assign the value to a variable division
div = num_one / num_two
print(div) # 1.25

#& Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
reminder = num_two & num_one
print(reminder) # 4

#& Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp) # 625

#& Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_div = num_one // num_two
print(floor_div) # 1

#^ The radius of a circle is 30 meters.
radius = 3
pi = 3.1416
area_of_circle = pi * (radius ** 2)
print(area_of_circle) # 2826.0

#& Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = radius * radius
print(circum_of_circle) # 9

#& Take radius as user input and calculate the area.
user_radius = input("Pls give me a radius: ")
int_user_radius = int(user_radius)
area = pi * (int_user_radius ** 2)
print(f'The area of the circle is: {area}')

"""#^ 6
    Use the built-in input function to get 
    first name, last name, country and 
    age from a user and store the value to 
    their corresponding variable names
"""
first_name = input("Write down your first name: ")
last_name = input("Write down your last name: ")
age = input("Write down your age: ")

iam = f'My name is {first_name} {last_name}, I am {age} years old'
print(iam)