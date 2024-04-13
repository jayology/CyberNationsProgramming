functions = "+, -, /, >, <, *"

input1 = input("Enter the first number: ")
operator = input("Enter a single operator from this list: "+functions)

#Perform Input Validation
if operator in functions:
	input2 = input("Enter the second number: ")
else:
	print("Invalid operator GOODBYE!")
	exit()


#Perform Calculation		
if operator == "+":
    print(int(input1) + int(input2))
    
