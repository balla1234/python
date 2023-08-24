name = "Tony Shark"

print(name.upper())
print(name.lower())
print(name.find('S'))
print(name.replace("Tony Shark", "Ironman"))
print("T" in name)     #shows true or false


#Immutable data type
my_string = "hello"
new_string = my_string.upper()  # Creating a new string with modifications
print(new_string)