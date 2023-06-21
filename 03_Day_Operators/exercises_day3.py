
###^ E X E C E R C I S E S  O P E R A T O R S D3 ###^

my_age = 30
my_height = 1.6
complex_num = 30 + 1j

"""#* Exercise 4
    script that prompts the user to enter base and
    height of the triangle and calculate an area
    of this triangle (area = 0.5 x b x h).
"""
base = int(input("Insert the base of the triangle: "))
height = int(input("Insert the height of the triangle: "))
area = base * height / 2
print(f"The area of the triangle is: {area}")

"""#* Exercise 5
    write a script that prompts the user to enter
    side a, side b, and side c of the triangle.
    Calculate the perimeter of the triangle
    (perimeter = a + b + c).
"""
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter}")

"""_#* Exercise-6_
    Get length and width of a rectangle using prompt.
    Calculate its area (area = length x width)
    and perimeter (perimeter = 2 x (length + width))
"""
length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
area = length * width
perimeter = 2 * (length + width)

print(f"The area of the triangle is {area}")
print(f"The perimeter of the triangle is {perimeter}")

"""_#* Exercise-7_
    Get radius of a circle using prompt. Calculate 
    the area (area = pi x r x r) and circumference 
    (c = 2 x pi x r) where pi = 3.14.
"""
pi = 3.14
radius = int(input("Enter the radius: "))
area = pi * radius ** 2
circum = 2 * pi * radius
print(f"The area of the circle is {area}")
print(f"The circumference of the circle is {circum:.2f}")

"""_#* Exercise 8_
Calculate the slope, x-intercept and y-intercept 
of y = 2x -2. Formula = m = y2-y1 / x2 - x1
"""
x1 = int(input("Enter x1 value: "))
x2 = int(input("Enter x2 value: "))
y1 = int(input("Enter y1 value: "))
y2 = int(input("Enter y2 value: "))

m = (y2 - y1) / (x2 - x1)
y = x2 - 2
print(f"The slope is: {m:.2f}")

"""_#* Exercise 9_
    Slope is (m = y2-y1/x2-x1). Find the slope and 
    Euclidean distance between point (2, 2) and 
    point (6,10)
"""
x1 = int(input("Enter x1 value: "))
x2 = int(input("Enter x2 value: "))
y1 = int(input("Enter y1 value: "))
y2 = int(input("Enter y2 value: "))
m = (y2 - y1) / (x2 - x1)
print(f"The slope is: {m}") # 2

#* Exercise 10_ Compare the slopes in tasks 8 and 9.


"""_#* Exercise 11_
Calculate the value of y (y = x^2 + 6x + 9). 
Try to use different x values and figure out at 
what x value y is going to be 0
"""
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
y_value = (x ** 2) + (6 * x) + (9)

"""_#* Exercise 12_
Find the length of 'python' and 'dragon' and 
make a falsy comparison statement.
"""
print(len("python") == len("dragon")) # False

"""_#* Exercise 13_
Use and operator to check if 'on' is found in both 
'python' and 'dragon'
"""
print("python", "on" and "dragon")
