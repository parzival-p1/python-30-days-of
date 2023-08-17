
#*** *** E x e r c i s e s :  L e v e l  2 *** ***#
'''
1. Write a code which gives grade to students
according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
'''

score = int(input("Enter your total score: "))
if score == score in range(80, 100):
    print("Your final grade is A, Congratulations! 🎉")
elif score == score in range(70, 89):
    print("Your final grade is B, good job! 👍🏼")
elif score == score in range(60, 69):
    print("Your final grade is C, you can do it better! 😉")
elif score == score in range(50, 59):
    print("Your final grade is D, you failed! 😣")
else:
    print("Your final grade is E, you completly failed! 🤐")


'''
2. Check if the season is Autumn, Winter, Spring or Summer.
If the user input is: September, October or November,
the season is Autumn. December, January or February,
the season is Winter. March, April or May, the season
is Spring June, July or August, the season is Summer
'''

month = input("Enter yor favorite month: ").lower()
winter = ["december", "january", "februay"]
spring = ["march", "april", "may"]
summer = ["june", "july", "august"]
autumn = ["september", "october", "november"]

if   month in winter:
    print("Your season is Winter ❄️")
elif month in spring:
    print("Your season is Spring 🌼")
elif month in summer:
    print("Your season is Summer 😎")
elif month in autumn:
    print("Your season is Autumn 🍁")
else:
    print("Please enter a valid month. 📅")

'''
If a fruit doesn't exist in the list add the fruit 
to the list and print the modified list. 
If the fruit exists print('That fruit already exist in the list')
'''
fruits = ['banana', 'orange', 'mango', 'lemon']

user_fruit = input("Enter your favorite fruit: ").lower()

if user_fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(user_fruit)
    print(fruits)
