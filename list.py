marks = [93,91,99]
print(marks)
print(marks[0])   #0 is index to particular print
print(marks[-1])
print(marks[0:2])  #0 is included, 2 index not

colors = ["red", "blue", "green"]
# Create a copy of a list.
print("\ncopy a list")
c = colors.copy()
print(str(c))

print("\nAdd a list to another")
moreColors = ["white", "black"]
colors.extend(moreColors)
print(str(colors))

# Clear or empty a list.
print("\nEmpty a list")
colors.clear()
print(str(colors))

colors = ["red", "blue", "green"]
print("\nInsert an element at a specific index")
colors.insert(0, "violet")
print(str(colors))


# Remove an element at a specific index using pop().
print("\nRemove an element at a specific index")
colors.pop(0)
print(str(colors))

# Reverse a list.
print("\nReverse list")
colors.reverse()
print(str(colors))

# Sort a list.
print("\nSort list")
colors.sort()
print(str(colors))

list1 = ["M", "ho", "to", "i", "war"]
list2 = ["y", "me", "wn", "s", "angal"]


concatenated_list = [item1 + item2 for item1, item2 in zip(list1, list2)]

print(concatenated_list)


list1 = ["Hi ", "Hey "]
list2 = ["Madam", "Sir"]

concatenated_list = [item1 + item2 for item1 in list1 for item2 in list2]

print(concatenated_list)


#New (insert)
sample_list = [1, 2, 5, 6, 7, 9]

value_to_insert_after = 5
item_to_insert = 10

index_to_insert_after = sample_list.index(value_to_insert_after) + 1
sample_list.insert(index_to_insert_after, item_to_insert)

print(sample_list)

#to find largest element in the list:
def find_largest_element(lst):
    if not lst:
        return None  # Return None for an empty list

    largest = lst[0]  # Initialize with the first element

    for item in lst:
        if item > largest:
            largest = item

    return largest

# Example list
my_list = [12, 45, 6, 72, 31, 90]
largest_element = find_largest_element(my_list)
print("Largest element:", largest_element)

#Finding the Smallest Element in a List:
def find_smallest_element(lst):
    if not lst:
        return None  # Return None for an empty list

    smallest = lst[0]  # Initialize with the first element

    for item in lst:
        if item < smallest:
            smallest = item

    return smallest

# Example list
my_list = [12, 45, 6, 72, 31, 90]
smallest_element = find_smallest_element(my_list)
print("Smallest element:", smallest_element)

#To print unique gmail ID


a = [(111, "a@gmail.com,b@gmail.com"),
     (222, "s@gmail.com,a@gmail.com"),
     (333, 444, "a@gmail.com,b@gmail.com,c@gmail.com")]
l = []
for i in a:
    for j in i:
       if "gmail.com" in str(j):
           a = j.split(",")
           l.extend(a)

print(set(l))

##Mutable datatype
myt_list = [1, 2, 3]
myt_list[0] = 10  # Modifying an element
myt_list.append(4)  # Adding an element

print(myt_list)