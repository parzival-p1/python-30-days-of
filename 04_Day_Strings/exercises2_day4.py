
###*** E x e r c i s e s  D a y  4 ***###

"""_Exercise-21_
Use index to determine the position of 
the first occurrence of F in Coding For All.
"""
idx_pos = "Coding For All"
print(idx_pos.index('F')) # 7

"""_Exercise-22_
Use rfind to determine the position of the 
last occurrence of l in Coding For All People.
"""
rfind_pos = 'Coding For All People'
print(rfind_pos.rfind('l')) # 19

"""_Exercise-23_
Use index or find to find the position of
the first occurrence of the word 'because'
in the following sentence:
'You cannot end a sentence with because because because is a conjunction'
"""
idx_pos_cause = 'You cannot end a sentence with because because because is a conjunction'
print(idx_pos_cause.index('because')) # 31

"""_Exercise-24_
Use rindex to find the position of the last 
occurrence of the word because in the following 
sentence: 'You cannot end a sentence with because because because is a conjunction'
"""
last_idx =  'You cannot end a sentence with because because because is a conjunction'
print(last_idx.rindex('because')) # 47

"""_Exercise-25_
Slice out the phrase 'because because because' 
in the following sentence: 
'You cannot end a sentence with because because because is a conjunction'
"""
slice_out = 'You cannot end a sentence with because because because is a conjunction'
print(slice_out[31:54])

"""_Exercise-26_
Find the position of the first occurrence of 
the word 'because' in the following sentence: 
'You cannot end a sentence with because because because is a conjunction'
"""
fst_ocurr = 'You cannot end a sentence with because because because is a conjunction'
print(fst_ocurr.find('because')) # 31

"""_Exercise-27_
Slice out the phrase 'because because because'
in the following sentence:
'You cannot end a sentence with because because because is aconjunction'Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
"""

"""_Exercise-28_
Does 'Coding For All' start with a substring Coding?
"""
start_with = 'Coding For All'
print(start_with.startswith('Coding'))      # True

"""_Exercise-29_
Does 'Coding For All' start with a substring coding?
"""
start_with = 'Coding For All'
print(start_with.startswith('coding'))      # False

"""_Exercise-30_
'   Coding For All      '  , remove the left 
and right trailing spaces in the given string.
"""
remove_white = '   Coding For All      '
print(remove_white.strip(' ')) # 'Coding for All'

"""_Exerecise_31_
Which one of the following variables return True 
when we use the method isidentifier():
– 30DaysOfPython
– thirty_days_of_python
"""
identi_1 = '30DaysOfPython'
identi_2 = 'thirty_days_of_python'

print(identi_1.isidentifier())  # False
print(identi_2.isidentifier())  # True

"""_Exercise_32_
The following list contains the names of some of 
python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
Join the list with a hash with space string.
"""

lib_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(map(str, lib_list)))

"""_Exercise_33_
Use the new line escape sequence to separate 
the following sentences.
    I am enjoying this challenge.
    just wonder what is next.
"""
print('I am enjoying this challenge.\njust wonder what is next.')

"""_Exercise_34_
Use a tab escape sequence to write the 
following lines
"""
print('Name\tAge\tCountry\tCity')
print('Paco\t30\tMexico\tMexico City')

"""_Exercise_35_
Use the string formatting method to display 
the following:
The area of a circle with radius 10 is 314 meters square.
"""
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area:.0f} meters square")


"""_Exercise_36_
Make the following using string formatting 
methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
"""

a = 8
b = 6
print(f"8 + 6 = {a + b}")
print(f"8 - 6 = {a - b}")
print(f"8 * 6 = {a * b}")
print(f"8 / 6 = {a / b:.2f}")
print(f"8 % 6 = {a % b}")
print(f"8 // 6 = {a // b}")
print(f"8 ** 6 = {a ** b}")
