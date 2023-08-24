marks = {95,98,97,97,97}

for score in marks:
    print(score)
    
# Create a Set
print("Create a Set s")
s = {"red", "blue", "green"}
print(s)    

print("\n Add Method")
print("Add a new color Orange")
s.add("orange")
print(s)

# Copy 
print("\n Copy Method")
print("A new Set s1 is created")
s1 = s.copy()
print(s1)

# Remove
print("\n Remove Method")
print("Remove Orange from s1")
s1.remove("orange")
print(s1)

# Discard
print("\n Discard Method")
print("Discard is similar to remove, but does not throw any error if element does not exist")
s1.discard("elephant")


s = {"red", "blue", "green", "orange"}
s1 = {"red", "blue", "green"}

print(s1.issubset(s))
print(s.issuperset(s1))

##
def intersection(a, b):
    s1 = set(a)
    s2 = set(b)
    return s1.intersection(s2)

if __name__ == "__main__":
    # Create two lists of your choice.
    a = [10, 12, 31, 44, 56]
    b = [16, 71, 98, 91, 10]
    s3 = intersection(a, b)

    if len(s3) > 0:
        print("True")
    else:
        print("False")