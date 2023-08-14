def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def division(a, b):
    return a / b


print("please select the operation ")
print("1. add")
print("2. subtract")
print("3. mul")
print("4. division")

word = input("Enter the  operation number:-")
x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))

if word == '1':
    # string concatenation
    print(x, "+", y, " = ", add(x, y))
elif word == '2':
    print(x, "-", y, " = ", subtract(x, y))

elif word == '3':
    print(x, "mul", y, " = ", mul(x, y))

elif word == '4':
    print(x, "/", y, " = ", division(x, y))

else:
    print("this is the invalid input")
