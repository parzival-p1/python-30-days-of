
#*** *** E x e r c i s e s :  L e v e l  3 *** ***#

'''
4. Here we have a person dictionary.
Feel free to modify it!
 * Check if the person dictionary has skills key,
    if so print out the middle skill in the skills list.

 * Check if the person dictionary has skills key,
    if so check if the person has 'Python' skill and
    print out the result.

 * If a person skills has only JavaScript and React,
    print('He is a front end developer'), if the person
    skills has Node, Python, MongoDB,
    print('He is a backend developer'),
    if the person skills has React, Node and MongoDB,
    Print('He is a fullstack developer'),
    else print('unknown title') - for more accurate results more conditions can be nested!

 * If the person is married and if he lives in Finland,
    print the information in the following format
Asabeneh Yetayeh lives in Finland. He is married.

'''

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    print(person['skills'][2])
if 'Python' in person['skills']:
    print("He has Python skills")
if 'is_married' in person:
    print("Asabeneh Yetayeh lives in Finland. He is married.")
