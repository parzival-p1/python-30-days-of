
"""_#* Exercise 13_
Use and operator to check if 'on' is found in both 
'python' and 'dragon'
"""
print("on", "python" and "dragon")


"""_#* Exercise 14
    I hope this course is not full of jargon.
    Use in operator to check if jargon is in the sentence.
"""
print("jargon" in "I hope this course is not full of jargon.") # True

#* Exercise 15 - There is no 'on' in both dragon and python

"""#*_Exercise 16_
Find the length of the text python and convert 
the value to float and convert it to string
"""
conversion = str((float(int(len("python")))))
print(type(conversion))

"""_#* Exercise 17_
Even numbers are divisible by 2 and the 
remainder is zero. How do you check if 
a number is even or not using python?
"""
print('Modulus: ', 3 % 2)  # 1


"""_#* Exercise 18_
Check if the floor division of 7 by 3
is equal to the int converted value of 2.7
"""
print('Floor division: ', 7 // 3) # 2

"""_#* Exercise 19_
Check if type of '10' is equal to type of 10
"""
print(type(10) == type('10')) # False

"""_#* Exercise 20_
Check if int('9.8') is equal to 10
"""
# print(int('9.8') == (10)) # False

"""_#* Exercise 21_
Write a script that prompts the user to enter 
hours and rate per hour. Calculate pay of the 
person?
"""
hours = int(input("Please enter hours: "))
rate = int(input("Please enter rate: "))
earning = hours * rate
# print(f"Your earnings are: {earning}")

"""_#* Exercise 22_
Write a script that prompts the user to enter 
number of years. Calculate the number of 
seconds a person can live. 
Assume a person can live hundred years
"""
years = int(input("Enter number of years you've lived: "))
seconds_per_y = 31536000
seconds_lived = seconds_per_y / years
# print(f"You've lived: {seconds_lived} seconds")

"""_#* Exercise 23_
Write a Python script that displays 
the following table:
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
a = 1
print(a**5)