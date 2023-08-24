age = 2
if age >= 18:
    print("u are an adult")
    print("u can vote")
elif age < 18 and age>3:
    print("u are in school")
else:
    print("u are a child")    
#print("Thank you")


#Mini Calculator 
first = input("enter first num : ")
operator = input("enter operator (+,-,/,%)")
second = input("enter second number :")

first = int(first)
second = int(second)
if operator == "+":
 print(first + second)
elif operator == "-":
 print(first - second)
elif operator == "*":
 print(first * second)
elif operator == "/":
 print(first / second)
else:
 print("Invalid operator")
