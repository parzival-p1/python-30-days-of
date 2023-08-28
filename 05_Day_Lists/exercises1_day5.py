
###*** E X E R C I S E S   L 1   D A Y 5 ***###

my_list = []
print(type(my_list))    # <class 'list'>

my_fruits = ['pineapple', 'banana', 'kiwi', 'maracuja', 'lulo', 'acai']
print(len(my_fruits))   # 6

fst_item, snd_item, trd_item, frth_item, fifth_item, sth_item = my_fruits
print(fst_item, trd_item, sth_item) # pineapple kiwi acai


mixed_data_types = [
    "Paco",
    30,
    1.60,
    "single",
    "garita 68"
]

it_companies = [
    "Facebook",
    "Google",
    "Microsoft",
    "Apple",
    "IBM",
    "Oracle",
    "Amazon"
]

print("Number of companies:", len(it_companies))    # Number of companies: 7

fst_co, snd_co, thrd_co, frt_co, fifth_co, six_co, sth_co = it_companies
print(f"{fst_co}, {thrd_co}, {sth_co}") # Facebook, Microsoft, Amazon

it_companies.append('Uber')
print(it_companies) # [...'Oracle', 'Amazon', 'Uber']

it_companies.insert(4, 'Didi')
print(it_companies) # ['Facebook', 'Google', 'Microsoft', 'Apple', 'Didi'...]

it_companies[0] = "FACEBOOK"
print(it_companies) # ['FACEBOOK', 'Google', 'Microsoft',...]

tech_co = '#; '.join(it_companies)
print(tech_co)  # FACEBOOK#; Google#; Microsoft#...

existence = 'Zappos' in it_companies
print(existence) # False

it_companies.sort()
print(it_companies) # ['Amazon', 'Apple', 'Didi',...]

it_companies.sort(reverse=True)
print(it_companies) # ['Uber', 'Oracle', 'Microsoft',...]

print(it_companies[:3]) # ['Uber', 'Oracle', 'Microsoft']

print(it_companies[-3:]) # ['Didi', 'Apple', 'Amazon']

first, second, third, fourth, fifth, sixth, seventh, eight, nineth = it_companies
print(fourth) # IBM

it_companies.remove('Uber')
print(it_companies) # ['Oracle', 'Microsoft', 'IBM'...]

it_companies.remove('Google')
it_companies.remove('FACEBOOK')
print(it_companies) # ['Oracle', 'Microsoft', 'IBM', 'Didi', 'Apple', 'Amazon']

it_companies.pop()
print(it_companies) # ['Oracle', 'Microsoft', 'IBM', 'Didi', 'Apple']

#^ *** 25 Destroy the IT companies list *** ^#
it_companies.clear()
print(it_companies) # []

#^ *** 26.  Join the following lists: *** ^#
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

tech_stack = front_end + back_end
print(tech_stack) # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']

full_stack = tech_stack.copy()
print(full_stack) # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
