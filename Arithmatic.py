print(5 + 2)
print(5 /2)
print(5//2)
print(5%2)  #remainder
print(5 ** 2)   #5 to the power 2 *- asteras


i = 5
i += 2
i -= 2
i *= 2

result = 2 + 3 * 5
print(result)

#comparison operator
print(3>2)
print( 3 != 3)

#logical operators
print(2>3 or 2>1)
print(2>3 and 2>1)

#not - reverse 
print(not 3>2)

x = 5
y = 5

def addition(x, y):
    print("Performing Addition")
    return x + y

def subtraction(x, y):
    print("Performing Subtraction")
    return x - y

def multiplication(x, y):
    print("Performing Multiplication")
    return x * y

def division(x, y):
    print("Performing Division")
    return x / y

def modulus(x, y):
    print("Performing Modulus")
    return x % y

def exponential(x, y):
    print("Performing Exponentiation")
    return x ** y

if __name__ == '__main__':

    # You can alternatively use input() to fetch values from user.
    a = 3
    b = 2

    # Addition
    add = addition(a, b)
    print(add)
    print("\n")

    # Subtraction
    sub = subtraction(a, b)
    print(sub)
    print("\n")

    # Multiplication
    mul = multiplication(a, b)
    print(mul)
    print("\n")

    # Division
    div = division(a, b)
    print(div)
    print("\n")

    # Modulus
    mod = modulus(a, b)
    print(mod)
    print("\n")

    # Exponential
    exp = exponential(a, b)
    print(exp)
    print("\n")