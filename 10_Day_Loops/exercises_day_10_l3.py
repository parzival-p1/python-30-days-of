from countries import countries
import countries_data

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
country =    {
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": [
            "Pashto",
            "Uzbek",
            "Turkmen"
        ],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
    }

for lang in country:
    if "languages" in country:
        print(f'{lang} -→ {country[lang]}')
