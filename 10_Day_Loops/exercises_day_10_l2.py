
#*** *** E x e r c i s e s :  L e v e l  1 *** ***#

'''
1. Use for loop to iterate from 0 to 100 and print 
the sum of all numbers.

– The sum of all numbers is 5050.
'''
suma_nums = sum(range(0, 101))

''' for nums in range(0, 101):
    suma_nums += nums '''
print(f"The sum of all numbers with sum() is: {suma_nums}. \n")

total = 0

for i in range(101):
    total += i
print(f"The sum of all numbers with for loop is: {total}. \n")

while i <= 99:
    total += i
    i += i
print(f"The sum of all numbers with while loop is: {total}. \n")

'''
2. Use for loop to iterate from 0 to 100 and print
the sum of all evens and the sum of all odd numbers.

– The sum of all evens is 2550.
– The sum of all odds is 2500.
'''
total_even = 0

for num in range(101):
    if num % 2 == 0:
        total_even += num
print(f"The sum of all evens is: {total_even}\n")

total_odd = 0
for odd in range(101):
    if odd % 2 != 0:
        total_odd += odd
print(f"The sum of all odds is: {total_odd}\n")
