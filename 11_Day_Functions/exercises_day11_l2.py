
#*** *** E x e r c i s e s :  L e v e l  2 *** ***#

''' Exercise 1
Declare a function named evens_and_odds.
It takes a positive integer as parameter and it
counts number of evens and odds in the number.
'''

def even_and_odds(integer):
    ''' sum of all evens and all odds '''
    evens = 0
    odds = 0
    lst_total = range(integer + 1)

    for integer in lst_total:
        if integer % 2 == 0:
            evens += integer
        else:
            odds += integer

    print(evens, odds)

''' Exercise 2
Call your function factorial, it takes a whole number 
as a parameter and it return a factorial of the number
'''
def factorial(number):
    fact = 1
    for num in range(number + 1):
        fact *= num
    return fact
print(factorial(10))


''' Exercise 3
Call your function is_empty, it takes a parameter 
and it checks if it is empty or not
'''
def is_empty(check):
    if check:
        return True
    else:
        return False
print(is_empty("")) # False


''' Exercise 4
Write different functions which take lists.
They should calculate_mean, calculate_median,
calculate_mode, calculate_range, calculate_variance,
calculate_std (standard deviation).
'''

