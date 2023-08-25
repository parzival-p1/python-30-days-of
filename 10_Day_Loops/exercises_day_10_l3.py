import sys
sys.path.append('data/')

from countries_data import data
from countries import countries


#*** *** E x e r c i s e s :  L e v e l  3 *** ***#

'''
1. Go to the data folder and use the countries.py file.
Loop through the countries and extract all the countries
containing the word land.
'''
for country in countries:
    if 'land' in country:
        print(f'{country} \n')

'''
2. This is a fruit list, 
['banana', 'orange', 'mango', 'lemon'] 
reverse the order using loop.
'''
fruits = ['banana', 'orange', 'mango', 'lemon']

#* for loop method
reverse_fruits = []

for f in range(1, len(fruits) + 1):
    reverse_fruits.append(fruits[-f])
print(reverse_fruits)

#* Slicing Method
reverse_fruits = fruits[::-1]
print(reverse_fruits)

'''
3. Go to the data folder and use the countries_data.py
file.
    I. What are the total number of languages in the data
    II. Find the ten most spoken languages from the data
    III. Find the 10 most populated countries in the world
'''
#* I. Total number of languages in the data
data_list = data
total_langs = []

for item in data_list: # itera la listta
    total_langs.extend(item["languages"]) # itera los keys #? Que hace extend?
print(f"Total langs = {len(set(total_langs))}") # devuelve el total de languages de hablados


''' II. Find the ten most spoken languages from the data '''
counts = { }
for item in total_langs:
    counts[item] = counts.get(item, 0) + 1

def sort_dict_by_value(dictionary, reverse=False):
    ''' Function to sort a dict '''
    return dict(sorted(dictionary.items(), key = lambda x: x[1], reverse=reverse))

counts = sort_dict_by_value(counts, True)
for item in list(counts.items())[:10]:
    print(item)

''' III. Find the 10 most populated countries in the world '''
populated = { }
for item in data:
    populated[item["name"]] = item["population"]
populated = sort_dict_by_value(populated, True)
for item in list(populated.items())[:10]:
    print(item)
