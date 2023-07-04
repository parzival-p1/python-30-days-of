from country_names import countries
###*** E X E R C I S E S   L 2   D A Y 5 ***###

#^ *** 1. The following is a list of 10 students ages: *** ^#
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
"""_Instructions_
– Sort the list and find the min and max age
– Add the min age and the max age again to the list
– Find the median age (one middle item or two middle items divided by two)
– Find the average age (sum of all items divided by their number )
– Find the range of the ages (max minus min)
– Compare the value of (min - average) and (max - average), use abs() method
"""

ages.sort()
print(ages[0]) # 19

ages.sort(reverse=True)
print(ages[0]) # 26

ages.append(19)
ages.append(26)
print(ages) # [26, 25, 25, 24, 24, 24, 22, 20, 19, 19, 19, 26]

median_age = (len(ages) - 1 / 2)
print(median_age) # 11.5

avg_age = sum(ages) / len(ages)
print(avg_age)  # 22.75

ages_range = max(ages) - min(ages)
print(f"The ages range is: {ages_range}")

abs_value = (min(ages) - avg_age) - (max(ages) - avg_age)
print(abs(abs_value)) # 7

#^ *** 2. The following is a list of 10 students ages: *** ^#
"""
1. Find the middle country(ies) in the countries list
2. Divide the countries list into two equal lists 
if it is even if not one more country for the first half.
3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
Unpack the first three countries and the rest as scandic countries.
"""

#*** 1st Problem ***
if len(countries) % 2 == 0:
    mid = len(countries) // 2
    idx = len(countries) // 2 - 1
    print(countries[mid], countries[idx])
else:
    num = len(countries) // 2
    print(countries[num]) 

#*** 2nd Problem ***
fst_country_list = len(countries) % 2
print(fst_country_list)

#*** 3rd Problem ***
northen = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, rus, usa, *scandic = northen
print(f"The non Scandianaivian countries are: {ch}, {rus} and {usa}")
print(f"The main Scandinavian countries are {scandic}") # ['Finland', 'Sweden', 'Norway', 'Denmark']
