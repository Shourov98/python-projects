print("Welcome to Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option = int(input("Select a calculator option: "))

if option == 1:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    print("Summation is : ", num1+num2)
elif option == 2:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    print("Subtraction is : ", num1-num2)
elif option == 3:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    print("Multiplication is : ", num1*num2)
elif option == 4:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    print("Division is : ", num1/num2)
else:
    print("Invalid Input")