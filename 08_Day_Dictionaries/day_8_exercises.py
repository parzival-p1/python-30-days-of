
# *** *** DICTIONARY  EXERCISES *** ***#

'''1. Create an empty dictionary called dog'''
dog = {}
dog = dict()

'''2. Add name, color, breed, legs, age to the dog dictionary'''

doggito = {
    "Name" : "Doggo",
    "Color" : "brown",
    "Breed" : "German Sheperd",
    "Legs"  : 4,
    "Age"   : 3
}

'''3. Create a student dictionary and add
first_name, last_name, gender, age, 
marital status, skills, country, city and
address as keys for the dictionary'''
student = {
    "name" : "Fco",
    "last_name" : "Hdez",
    "gender" :  "Male",
    "age"   : 30,
    "marital_stat" : "Single",
    "skills" : ["Python", "C", "C++"],
    "country" : "Mexico",
    "city"  : "Mexico City",
    "addres" : "Av. garita 68"
}

'''4. Get the length of the student dictionary'''
print(len(student)) # 9

'''5. Get the value of skills and check the
data type, it should be a list'''

skills = student['skills']
print(type(skills)) # list

'''6. Modify the skills values by adding 
one or two skills'''

student['skills'].append("HTML, CSS")
print(student['skills'])

'''7. Get the dictionary keys as a list'''
key_vals = student.keys()
print(key_vals)

'''8. Get the dictionary values as a list'''
dict_vals = student.values()
print(dict_vals)

'''9. Change the dictionary to a list of tuples
using items() method'''
print(student.items())

'''10. Delete one of the items in the dictionary'''
student.clear()
print(student)

'''11. Delete one of the dictionaries'''
doggito.clear()

