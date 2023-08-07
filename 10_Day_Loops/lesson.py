
#*** ***  L O O P S : F O R  A N D  W H I L E *** ***#

# *** *** F O R  L O O P S *** *** #
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
print([[c, c.upper(), c.upper()[:3], len(c)] for c in countries])

for c in countries:
    if 'land' in c:
        print(c)

data = [
    ['Finland', 'FINLAND', 'FIN', 7],
    ['Sweden', 'SWEDEN', 'SWE', 6],
    ['Norway', 'NORWAY', 'NOR', 6],
    ['Denmark', 'DENMARK', 'DEN', 7],
    ['Iceland', 'ICELAND', 'ICE', 7]]

nums = []
for lst in data:
    nums.append(lst[3])
print(nums)

#*** *** W H I L E  L O O P *** ***#
i = 100
while i >= 0:
    print(i)
    i -= 1

# 10 to 0
for i in range(10, -1, -1):
    print(i)
