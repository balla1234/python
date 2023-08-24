marks = {"english" : 95, "chemistry" : 92, } 
print(marks["chemistry"])  
marks["physics"] = 96
print(marks)

car = dict(colour = 'Black', brand = "Ford", model = "Mustang", year = 2021)
print(car)
print(car['colour'])
print(car['brand'])

car = dict(colour = 'Black', brand = "Ford", model = "Mustang", year = 2021)
car['city'] = 'Hyderabad'
print(car)

car = dict(colour = 'Black', brand = "Ford", model = "Mustang", year = 2021)
del car['brand']
print(car)

# clear()
dict1 = {'a': 100, 'b': 200, 'c': 300}
print(dict1)
print("Perform Clear on Dict")
dict1.clear()
print(dict1)

# get()
dict1 = {'a': 100, 'b': 200, 'c': 300}
print("\n")
print(dict1)
print("Get value of the key b")
val = dict1.get('b')
print(val)

print("\n Get value of the key b")
print(dict1.get('z'))

# returned default instead of None.
print("\n Get value of the key z")
print(dict1.get('z', -1))

# items()
print("\n All items in dict1")
print(list(dict1.items()))
print(list(dict1.items())[1][0])
print(list(dict1.items())[1][1])

# keys()
# Returns a iterable object of all keys in dict1
print("\n keys in dict1")
print(dict1.keys())

# values()
#Returns a iterable object of values in dict1
print("\n Values in dict1")
print(dict1.values())

# pop()
# Removes a key from a dictionary.
value = dict1.pop('b')
print(value)
print("\n Items after pop")
print(dict1)

# popitem()
dict1 = {'a': 100, 'b': 200, 'c': 300}
#Removes the last key-value pair added from dict1 and returns it as a tuple
value = dict1.popitem()
print(value)
print("\n Items after popitem")
print(dict1)
print(dict1.popitem())


# update
dict1 = {'a': 100, 'b': 200, 'c': 300}
#To update an entry, you can just assign a new value to an existing key
dict1['b'] = 101
print("\n Items after update")
print(dict1)

dic1 = {10: 100, 20: 200}
dic2 = {30: 300, 40: 400}
dic3 = {50: 500, 60: 600}

new_dict1 = {**dic1, **dic2, **dic3}

print(new_dict1)

n = 3
new_dict1 = {}

# Generate keys and values in the format (n, nnn)
for i in range(1, n + 1):
    key = i
    value = int(str(n) * 3)
    new_dict1[key] = value

print(new_dict1)
