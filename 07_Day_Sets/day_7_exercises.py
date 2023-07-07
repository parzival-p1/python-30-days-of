# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

'''#*Exercises: Level 1
1. Find the length of the set it_companies
2. Add 'Twitter' to it_companies
3. Insert multiple IT companies at once to the 
set it_companies
4. Remove one of the companies from the set 
it_companies
5. What is the difference between remove and 
discard
'''

#^ Exercise 1
print(len(it_companies)) # 7

#^ Exercise 2
it_companies.add('Twitter')
print(it_companies) # {'Google', 'Facebook', 'Amazon', 'IBM', 'Twitter' ...}

#^ Exercise 3
it_co = {'Tesla', 'Intel', 'Ryzen', 'EA'}
it_companies.update(it_co)
print(it_companies)

#^ Exercise 4
print(it_companies.pop()) # Twitter

#^ Exercise 5
'''remove() raise error if the item isn't found
while discard() doesn't raise any.
'''

'''#*Exercises: Level 2
1. Join A and B
2. Find A intersection B
3. Is A subset of B
4. Are A and B disjoint sets
5. Join A with B and B with A
6. What is the symmetric difference between A and B
7. Delete the sets completely
'''
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#^ Exercise 1
uni = A.union(B) # False
print(uni) # {19, 20, 22, 24, 25, 26, 27, 28}

#^ Exercise 2
inter = A.intersection(B)
print(inter) # {19, 20, 22, 24, 25, 26}

#^ Exercise 3
sub = A.issubset(B) 
print(sub)  # True

#^ Exercise 4
disj = A.isdisjoint(B)
print(disj) # False

#^ Exercise 5
joining = A.union(B) # union A + B
print(joining.union(A)) # {19, 20, 22, 24, 25, 26, 27, 28}

#^ Exercise 6
simetric = A.symmetric_difference(B)
print(simetric) # {27, 28}

#^ Exercise 7
A.clear()
B.clear()

print(A)    # set()
print(B)    # set()

'''#*Exercises: Level 2
1. Convert the ages to a set and compare the
length of the list and the set, which one is
bigger?

2. Explain the difference between the following
data types: string, list, tuple and set

'I am a teacher and I love to inspire and teach people.'

How many unique words have been used in the sentence? 
Use the split methods and set to get the unique words.
'''
age = [22, 19, 24, 25, 26, 24, 25, 24]

#^ Exercise 1
print(len(age))     # 8
print(len(set(age))) # 5

#^ Exercise 2
'''
str
'''