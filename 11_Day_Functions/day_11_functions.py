
###*** F U N C T I O N S  I N  P Y T H O N ***###

###^ Defining a function ^###
'''
A function is a reusable block of code or programming
statements designed to perform a certain task.
To define or declare a function, Python provides
the def keyword.
The following is the syntax for defining a function.
The function block of code is executed only if the
function is called or invoked.
'''

###^ Defining a function ^###
codes = 0
def function_name():
    ''' declaring a function '''
    codes
    codes
function_name() # calling a function

###^ Function without Parameters ^###

def add_two_nums ():
    ''' Function can be declarde without parameters '''
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_nums() # calling a function

###*** *** Function Returning a Value - Part 1 *** ***###
'''
Function can also return values,
if a function does not have a return statement, the
value of the function is None.
'''

def add_nums():
    ''' we get a value from a function when we call
    the function and print it. '''
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_nums())

###^ Function with Parameters ^###
'''
In a function we can pass different data types
(number, string, boolean, list, tuple, dictionary or set) 
as a parameter
'''

def greetings(name): #* parameter here

    ''' Single Parameter: If our function takes a
    parameter we should call our function with an
    argument '''
    message = name + ', welcome to my repo kiddos!'
    return message
print(greetings('This is Parzival')) #* Funtion call + argument

def circle_area(radius): #* radius as a param
    ''' get the area of a circle '''

    PI = 3.14
    area = PI * radius ** 2 # a = pi * r^2
    return area
print(circle_area(5)) # 78.5

###^ function with 2 parameters ^###
def calculate_age (curr_year, birth_year): #* 2 params
    ''' calculates your current age '''

    age = curr_year - birth_year
    return age
print('Your age is:',calculate_age(2023, 1998)) #* two args

###^ Passing arguments with key and value ^###

def add_numbers(num1, num2):
    ''' sum of two numbers '''
    
    total = num1 + num2
    print(total)

add_numbers(num1 = 5, num2 = 5) # 10

###*** *** Function Returning a Value - Part 2 *** ***###
'''
If we do not return a value with a function, then our
function is returning None by default. To return a
value with a function we use the keyword return
followed by the variable we are returning.
'''
###^ Returning a string ^###
def print_name(fst_name): # func receives the 1st arg
    return fst_name
print_name('Francisco') # Francisco

def print_full_name(fst_name, last_name):
    ''' Prints full name '''

    space = ' '
    full_name = fst_name + space + last_name
    return full_name
print_full_name(fst_name="Paco", last_name="Hdez")

###^ Returning a number ^###
def print_age(curr_year, b_year):

    ''' calculates your age '''

    age = curr_year - b_year
    return age
print('Your age is:', print_age(2023, 1989))

###^ Returning a boolean ^###
def is_even(n):
    if n % 2 == 0:
        print(f"{n} Is an even number!")
        return True
    else:
        print(f"{n} Is not an even number!")
        return False

print(is_even(10)) # True
print(is_even(29)) # False

###^ Functin with default parameters ^###
'''
If we do not pass arguments when calling the function,
their default values will be used.
'''
def weight_of_obj(mass, gravity = 9.81): # gravity is a constant
    ''' calculates the weight of an object '''

    weight = str(mass * gravity) + ' N' # the value has to be changed to string first
    return weight
print('The weight of an object in Newtons is:', weight_of_obj(100)) # 9.81 N - average gravity on Earth's surface
print('The weight of an object in Newtons is:', weight_of_obj(100, 1.62)) # 1.62 N - gravity on the surface of the Moon

###^ Arbitrary Number of Arguments ^###
''' 
If we do not know the number of arguments we pass to 
our function, we can create a function which can take 
arbitrary number of arguments by adding * before the 
parameter name.
'''
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sum_all_nums(10, 20 ,30))

###^ Arbitrary Number of Arguments ^###
def gen_groups(team, *args): # unkown nnumber of args
    print(team)
    for item in args:
        print(item)
print(gen_groups('Team-1', 'Paco', 'Hugo', 'Luis'))

###^ Function as a Parameter of Another Function ^###
def sqr_num(num):
    ''' calculates the sqr '''
    return  num * num

def do_some(func, param):
    return func(param)

#^          function(), param
print(do_some(sqr_num, 3)) # 9
