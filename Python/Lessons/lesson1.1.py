#A slightly improved version of the previous lesson

print("Welcome to the calculator")
functions = "+, -, /, >, <, *"

operator = input("Enter a single operator from this list: "+functions)

match operator:
    case "+":
       print("You chose "+operator) 
    case "-":
       print("You chose "+operator)
    case "/":
       print("You chose "+operator)
    case "<":
       print("You chose "+operator)
    case ">":
       print("You chose "+operator)
    case "*":
       print("You chose "+operator)
    case _:
        print("You did not enter the required operator GOODBYE!")
        exit()

input1 = input("Enter the first number: ")
input2 = input("Enter the second number: ")

if(input1.isnumeric() and input2.isnumeric()):
     print("Valid Input")
else:
     print("Invalid input enetr a number")
     exit()

num1 = int(input1)
num2 = int(input2)

if operator == "+":
        result = num1 + num2

elif operator == "-":
         result = num1 - num2

elif operator == "/":
         result = num1 / num2
    
elif operator == "*":
         result = num1 * num2

elif operator == "<":
         result = num1 < num2
         print("Number 1 is less than " + str(num2))
        
elif operator == ">":
        result = num1 > num2
        print("Number 1 is more than " + str(num2))
else:
    print("Sorry but the input is not a number GoodBye!")
    exit()


print("🎉")
print("The result is: "+str(result))
print("🎉")


