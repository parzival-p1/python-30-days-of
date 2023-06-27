
###* E x e r c i s e s  D a y  4 *###

"""_Exercise-1_
1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' 
to a single string, 'Thirty Days Of Python'.
"""
string = 'Thirty', 'Days', 'Of', 'Python'
print(" ".join(string))

"""_Exercise-2_
2. Concatenate the string 'Coding', 'For' , 'All'
to a single string, 'Coding For All'.
"""
string = 'Coding', 'For' , 'All'
print(' '.join(string))

"""_#* Exercise-3_
3. Declare a variable named company and assign it 
to an initial value "Coding For All".
"""
company = "Coding For All"

"""#* _Exercise_4_
4. Print the variable company using print().
"""
print(company) # "Coding For All"

"""_#* Exercise_5_
5. Print the length of the company string using 
len() method and print().
"""
print(len(company)) # 14 char

"""_#* Exercise_6_
6. Change all the characters to uppercase 
letters using upper() method.
"""
print(company.upper()) # CODING FOR ALL

"""_#* Exercise_7_
7. Change all the characters to lowercase 
letters using lower() method.
"""
print(company.lower()) # coding for all

"""_#* Exercise_8_
8. Use capitalize(), title(), swapcase() 
methods to format the value of the string 
Coding For All.
"""
str_co = "Coding For All."
print(str_co.capitalize()) # Coding for all.
print(str_co.title())     # Coding For All.
print(str_co.swapcase()) # cODING fOR aLL.

"""_#* Exercise_9_
9. Cut(slice) out the first word of 
Coding For All string.
"""
print(str_co[7:]) # For All

"""_#* Exercise_10_
10. Check if Coding For All string contains 
a word Coding using the method index, 
find or other methods.
"""
sub_str = "Coding"
print(str_co.index(sub_str)) # 0 found at index zero
str_co2 = "Coding for all"
print(str_co2.index(sub_str)) # 0 se encuentra en el index ceero

"""_#* Exercise_11_
Replace the word coding in the string 
'Coding For All' to Python. 
to Python.
"""
str_code = 'Coding For All'
print(str_code.replace("Coding", "Python")) # Python For All

"""_#* Exercise_12_
12. Change Python for Everyone to Python 
for All using the replace method or 
other methods.
"""
str_py = 'Python for Everyone'
print(str_py.replace('Everyone', 'All')) # Python for All

"""_#* Exercise_13_
13. Split the string 'Coding For All' 
using space as the separator (split())
"""
str_all = 'Coding For All'
print(str_all.split(' ')) # ['Coding', 'For', 'All']

"""_#* Exercise_14_
14. "Facebook, Google, Microsoft, Apple, IBM, 
Oracle, Amazon" split the string at the comma.
"""
str_tech_co = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(str_tech_co.split(',')) # ['Facebook', ' Google', ' Microsoft' ... ]

"""_#* Exercise_15_
15. What is the character at index 0 
in the string Coding For All.
"""
last_char = "Coding For All"
print(last_char[0]) # C is the char in index [0]

"""_#* Exercise_16_
16. What is the last index of the string 
Coding For All.
"""
last_index = "Coding For All"
print(last_index[-1:]) # l is the last idx

"""_#* Exercise_17_
17. What character is at index 10 in 
"Coding For All" string.
"""
idx_10 = "Coding For All"
print(idx_10[10]) # l is the idx 10 in the str

"""_#* Exercise_18_
18. Create an acronym or an abbreviation 
for the name 'Python For Everyone'
"""
acron = 'Python For Everyone'
print(acron[0] + acron[7] + acron[11]) # PFE

"""_#* Exercise_19_
19. Create an acronym or an abbreviation 
for the name 'Coding For All'
"""
abrev = 'Coding For All'
print(abrev[0] + abrev[7] + abrev[11]) # CFA

"""_# Exercise_20_
20. Use index to determine the position of 
the first occurrence of C in Coding For All
"""
idx_pos = 'Coding For All'
print(idx_pos.index('C')) # 0
