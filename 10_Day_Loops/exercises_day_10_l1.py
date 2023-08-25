
#*** *** E x e r c i s e s :  L e v e l  1 *** ***#

'''
1. Iterate 0 to 10 using for loop, do the same using 
while loop.
'''
# for i in range(11):
#     print(i)
# 
# j = 0
# while j < 11:
#     print(j)
#     j +=  1
'''
2. Iterate 10 to 0 using for loop, do the same using
while loop.
'''
# for k in range(10, -1, - 1):
#     print(k)
#
# a = 10
# while a >= 0:
#     print(a)
#     a -= 1

'''
3. Write a loop that makes seven calls to print(),
so we get on the output the following triangle:

#
##
###
####
#####
######
#######
'''
# n = 7
for i in range(0, 7):
    word = ""
    for j in range(0, i):
        word += "#"
    print(word)

'''
4. Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
'''

for i in range(0, 8):
    char = ""
    for j in range(0, 8):
        char += "# "
    print(char)

'''
5. Print the following pattern:
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
'''

for a in range(11):
    #for b in range(1, 11):
    print(f"{a} x {a} = {a * a}")
    
'''
6. Iterate through the list, 
['Python', 'Numpy','Pandas','Django', 'Flask'] 
using a for loop and print out the items.
'''
py_frameworks = ['Python', 'Numpy','Pandas','Django', 'Flask']
for py in py_frameworks:
    print(py)

'''
7. Use for loop to iterate from 0 to 100 and print 
only even numbers
'''
for n in range(101):
    if n % 2 == 0:
        print(n)

'''
Use for loop to iterate from 0 to 100 and print only 
odd numbers
'''
for num in range(0, 101):
    if num % 2 != 0:
        print(num)
