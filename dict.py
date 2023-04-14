'''
pairs = {
   1: "apple",
   "orange": [2, 3, 4], 
   True: False, 
   12: "True",
}

print(pairs.get("orange"))
print(pairs.get(True, 40))
print(pairs.get(12345, "not found"))
'''


'''You are working on data that represents the economic freedom rank by country.

Each country name and rank are stored in a dictionary, with the key being the country name.

Complete the program to take the country name as input and output its corresponding economic freedom rank.

In case the provided country name is not present in the data, output "Not found".

Recall the get() method of a dictionary, that allows you to specify a default value.'''

data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}

name = input()
if name in data:
    print(data.get(name))
else:
    print(data.get(name, "Not found"))


