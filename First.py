#print("Hello world")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operator = input("Enter operator (+,-,*,/,%): ")
num1 = int(num1)
num2 = int(num2)
#Mini project : Calculator

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
elif operator == "%":
    print(num1 % num2)
else:
    print("Invalid Operation")
