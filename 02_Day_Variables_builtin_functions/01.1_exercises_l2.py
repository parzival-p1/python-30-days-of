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

circum_of_circle = radius * radius
print(circum_of_circle) # 9

