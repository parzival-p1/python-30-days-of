
"""_Exercises: Level 1_

1. Create an empty tuple
2. Create a tuple containing names of your sisters
and your brothers (imaginary siblings are fine)
3. Join brothers and sisters tuples and assign
it to siblings
4. How many siblings do you have?
5. Modify the siblings tuple and add the name of
your father and mother and assign it to family_members
"""

#* Exercise 1
empty_tuple = ()
empty_tuple = tuple()

#* Exercise 2
sisters = ("Luisa", "Sara")
brothers = ("David", "Mauricio", "Charlie")

#* Exercise 3
siblings = sisters + brothers
print(siblings)

#* Exercise 4
print(len(siblings))    # 5

#* Exercise 5
parents = ("Maximo Meirdio", "Helena Troya")
familiy_mem = parents + siblings
print(familiy_mem)

"""_Exercises: Level 2_

1. Unpack siblings and parents from family_members
2. Create fruits, vegetables and animal products
tuples. Join the three tuples and assign it to
a variable called food_stuff_tp.
3. Change the about food_stuff_tp tuple to a
food_stuff_lt list
4. Slice out the middle item or items from the
food_stuff_tp tuple or food_stuff_lt list.
5. Slice out the first three items and the last
three items from food_staff_lt list
6. Delete the food_staff_tp tuple completely
7. Check if an item exists in tuple:
8. Check if 'Estonia' is a nordic country

Check if 'Iceland' is a nordic country
nordic_countries = ( 'Denmark', 'Finland','Iceland', 
    'Norway', 'Sweden')
"""
#* Exercise 1
dad, mom, sis1, sis2, bro1, bro2, bro3 = familiy_mem
print(f"{dad}, {mom}, {sis1}, {sis2}, {bro1}, {bro2}, {bro3}")

#* Exercise 2
fruits = ("apple", "banana", "mango", "maracuja", "kiwi")
veggs = ("brocoli", "carrot", "lettuce", "cucumber", "tomato")
animals = ("dog", "cat", "horse", "unicorn", "bird", "eagle")

food_stuff_tp = fruits + veggs + animals

#* Exercise 3
food_stuff_lt = list(food_stuff_tp)
print(type(food_stuff_lt))  # <class 'list'>

#* Exercise 4
print(len((food_stuff_lt)))
print(food_stuff_lt[0:7] + food_stuff_lt[9:16])

#* Exercise 5
print(food_stuff_lt[0:3] + food_stuff_lt[3:-4])