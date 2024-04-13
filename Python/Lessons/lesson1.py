# Request input from the user. Whatever the user types in will be stored in the variable as a integer
num1 = int(input("Enter the first number: "))
# Request that the user enter +, -, *, /, <, >
operator = input("Enter a operator: ")
# Again request input from the user for the second number.
num2 = int(input("Enter the second number: "))

#These are the conditional statements
# Now you need to check what the user entered and perform the correct operation
if operator == "+":
	result = num1 + num2
elif operator == "-":
	result = num1 - num2
elif operator == "*":
	result = num1 * num2
elif operator == "/":
	result = num1 / num2
elif operator == "<":
	result = num1 < num2
	print(str(num1)+" is less than "+str(num2))
elif operator == ">":
	result = num1 > num2
	print(str(num1)+" is more than "+str(num2))
else:
	print("Invalid operator")

#Finally print the result
print("The result is "+str(result)+ "🎉🎉🎉🎉🎉🎉🎉")