
#*** *** E x e r c i s e s :  L e v e l  11 *** ***#

''' Exercise 1. 
Declare a function add_two_numbers. 
It takes two parameters and it returns a sum.
''' 

def add_two_numbers(num1, num2):
    result = num1 + num2
    return result
print(add_two_numbers(1, 2)) # 3

''' Exercise 2
Area of a circle is calculated as follows:
area = π x r x r.
Write a function that calculates area_of_circle.
'''
def circle_area(radius):
    pi = 3.1416
    area = pi * radius ** 2
    return area

print(circle_area(5))

''' Exercise 3
Write a function called add_all_nums which takes
arbitrary number of arguments and sums all the
arguments. Check if all the list items
'''
def add_all_nums(*nums):
    ''' sum all numms passes in the arg '''

    total = 0
    for num in nums:
        total += num
    return total
print(add_all_nums(1, 1, 2 , 3, 5, 8))

''' Exercise 4
Temperature in °C can be converted to °F using
this formula: °F = (°C x 9/5) + 32.
Write a function which converts °C to °F,
convert_celsius_to-fahrenheit.
'''
def cels_to_fahren(celsius):
    ''' converts celsius to fahrenheit '''

    grad_fahr = (celsius * 9 / 5) + 32
    return grad_fahr
print('The temmperature in ºF is:', cels_to_fahren(30)) # 86.0

''' Exercise 5
Write a function called check-season, it takes a
month parameter and returns the season:
Autumn, Winter, Spring or Summer.
'''
def check_season(month):
    winter = ['december', 'january', 'february']
    spring = 'march', 'april', 'may'
    summer = 'june', 'july', 'august'
    autum = 'september', 'october', 'november'

    if month in winter:
        return 'Is winter, put your jacket on!'
    elif month in spring:
        return 'Is spring break!'
    elif month in summer:
        return 'Is summer time!'
    elif month in autum:
        return 'Is autum, fallen leafs season!'
    else:
        return 'Introduce a gregorian month'

print(check_season('month'))

''' Exercise 6
Write a function called calculate_slope which return the
slope of a linear equation

y = mx + b

'''
def calculate_slope(m, x, b):
    y = m * (x) + b

    return y
print(calculate_slope(6, 8, 10)) # 58

def slope(x1, x2, y1, y2):
    m = (y2 - y1) / (x2 - x1)
    return m
print(f"slope = {slope(5, 10, 10, 20)} ")

''' Exercise 7
Quadratic equation is calculated as follows: ax² + bx + c = 0 
Write a function which calculates solution set of a quadratic
equation, solve_quadratic_eqn.
'''
# def solve_quadratic_eqn(a, b, c):
#     D = b * b - 4 * a * c
#     x1 = (-b + D) / (2 * a)
#     x2 = (-b - D) / (2 * a)
#
# print(x1 = 1, x2 = 2)


''' Exercise 8
Declare a function named print_list. It takes a list as a 
parameter and it prints out each element of the list.
'''
def print_list(*lst):
    for i in lst:
        return lst
print(print_list(1,2,3,4))

''' Exercise 9
Declare a function named reverse_list. It takes an array as a 
parameter and it returns the reverse of the array (use loops).
'''
def reverse_list(*rvs_lst):
    return rvs_lst[::-1]

''' Exercise 10
Declare a function named capitalize_list_items. 
It takes a list as a parameter and it returns a 
capitalized list of items
'''
def capitalize_list_items(*lst):
    new_lst = []
    for item in lst:
        new_lst.append(item.upper())
    return new_lst
print(capitalize_list_items('Finland', 'Norway', 'Denmark'))

''' Exervise 11
Declare a function named add_item. It takes a list
and an item parameters. It returns a list with the
item added at the end.
'''
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9];

def add_item(lst, item):

    lst.append(item)
    return lst

print(add_item(food_staff, 'Meat'))
print(add_item(numbers, 5))

''' Exercise 12
Declare a function named remove_item. It takes a list 
and an item parameters. It returns a list with the 
item removed from it.
'''

def remove_item(lst, item):

    lst.remove(item)
    return lst

print(remove_item(food_staff, 'Mango')) # ['Potato', 'Tomato', 'Milk', 'Meat']
print(remove_item(numbers, 3)) # [2, 7, 9, 5]

''' Exercise 13
Declare a function named sum_of_numbers. It takes a
number parameter and it adds all the numbers in
that range.
'''
def sum_of_numbers(n):

    total = 0
    lst = range(n+1)

    for num in lst:
        total = total + num
    return total

print(f"The sum of all the numbers in 5 is: {sum_of_numbers(5)}") # 15
print(f"The sum of all the numbers in 10 is: {sum_of_numbers(10)}") # 55
print(f"The sum of all the numbers in 100 is: {sum_of_numbers(100)}") # 505

print("\n")

''' Exercise 14
Declare a function named sum_of_odds. It takes a number
parameter and it adds all the odd numbers in that range.
'''
def sum_of_odds(number):
    total = 0
    lst_num = range(number + 1)

    for number in lst_num:
        if number % 2 != 0:
            total += number
    return total

print(f"The sum of all odd numbers in 5 is {sum_of_odds(5)}")
print(f"The sum of all odd numbers in 10 is {sum_of_odds(10)}")
print(f"The sum of all odd numbers in 100 is {sum_of_odds(100)}")
print("\n")

''' Exercise 15
Declare a function named sum_of_even. It takes
a number parameter and it adds all the even numbers
in that - range.
'''
def sum_of_evens(num):
    total_e = 0
    num_lst = range(num + 1)

    for num in num_lst:
        if num % 2 == 0:
            total_e += num
    return total_e

print(f"The sum of all evens in 5 is: {sum_of_evens(5)}")
print(f"The sum of all evens in 10 is: {sum_of_evens(10)}")
print(f"The sum of all evens in 100 is: {sum_of_evens(100)}")
