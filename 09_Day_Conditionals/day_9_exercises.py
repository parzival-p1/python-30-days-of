
#*** *** E x e r c i s e s :  L e v e l  1 *** ***#

'''Exercise 1
Get user input using input(“Enter your age: ”).
If user is 18 or older, give feedback:
You are old enough to drive.
If below 18 give feedback to wait for the
missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
'''

user_age = int(input("Enter your age: "))
legal_age = 18
needed = legal_age - user_age

if user_age >= legal_age:
    print("You're old enough to drive")
else:
    print(f"You need {needed} more years to learn to drive")

'''Exercise 2
Compare the values of my_age and your_age using
if … else. Who is older (me or you)?
Use input(“Enter your age: ”) to get the age
as input. You can use a nested condition to
print 'year' for 1 year difference in age, 'years'
for bigger differences, and a custom text
if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me.
'''

my_age = 30
your_age = int(input("Enter your age: "))
difference = your_age - my_age

if your_age > my_age:
    print(f"You're {difference} years older than me.")
elif my_age == your_age:
    print("We're the same age")

'''
Get two numbers from the user using input prompt.
If a is greater than b return a is greater than b, 
if a is less b return a is smaller than b, else a is
equal to b. Output:

    Enter number one: 4
    Enter number two: 3
    4 is greater than 3
'''
num_one = int(input("Enter a random number: "))
num_two = int(input("Enter another random number: "))

if num_one > num_two:
    print(f"{num_one} is greater than {num_two}")
elif num_one < num_two:
    print(f"{num_one} is less than {num_two}")
else:
    print("Number a is equal to Number b")
