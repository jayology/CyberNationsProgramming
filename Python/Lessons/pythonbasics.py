#######################
# Python Basic Syntax #
######################

# What is a comment?
# A comment is a line of code that is ignored by the interpreter.
# It is used to explain the code.
# In python anything that starts with the # symbol is a comment.


# What is a variable?
# A variable is a name given to a value.
# It is used to store the value in computer memory.

#Age is a variable that stores the value 12. Because you are storing a number in a variable, it is called an integer.
age = 12

#However this is not a number instead its a string of text because its wrapped in double quotes
age = "12"

# Difference between assignment and equality
age = 12 # assignment

age == 12 # equality we check for equality using the double equals

age != 12 #This checks for inequality

##############################| Python Methods |#####################################
#Because im new to python myself i only know a few right now

#Print
#The first method you would be learn is the print method. WHat it does is it prints information out to the console

print("Hello World") # This prints a string
print(123) # This prints a number
print(123, "Hello World") # This prints a number and a string

#Input
#The input method is used to get input from the user.
name = input("What is your name? ") # This asks the user for their name and stores it in the variable called name

#You can then print it out using the print method
print("Hello", name) # This prints the string "Hello" and the value of the variable name
#For example Hello John

#str
#The str method is used to convert a value to a string.
age = 12
print(str(age)) # This prints the value of age as a string. The str methods converts anything to a string

#it can also be written like this
myage = str(12)
print(myage)


#isnumeric
#The isnumeric method is used to check if a value is numeric.
#example 1
print("123".isnumeric()) # This prints True because the string "123" is a numeric value


##############################| Conditionals |#####################################
#These are a few ways to do conditionals in python

#If
#The if statement is used to check if a condition is true.
if 2 < 5:
	print("It is true. 2 is less than 5")

#example 2
wetfloor = True
if wetfloor == True:
	print("Take extra caution walking")

#else
#The else statement is used to run a block of code if the condition is false.
if wetfloor == True:
	print("Take extra caution walking")
else:
	print("It is not wet feel free to run if you want")

#elif
#The elif statement is used to run a block of code if the first condition was false.
# Elif is a combination of else and if called elif
if 5 + 2 == 5:
	print("This is incorrect")
elif 5 + 2 == 7:
	print("This is correct")


##############################| Block Scope |#####################################
# Other languages like Java, C++, Javascript, C# and a few more uses curly brackets to define a block of code.
# For example this is how you define a block scope in javascript

# let name = "John"
# if (name == "") {
# 	console.log("Name is empty")
# } else {
# 	console.log("Name is not empty")
# }

# Unlike javascript and other languages python uses indentation to define a block of code instead of using curly brackets.

# this code wont work

# name = "John"
# if name == "":
# print("Name is empty")

# But this will because its indented this tell python the print method belongs to the code above it
# name = "John"
# if name == "":
# 	print("Name is empty")

##############################| Functions |#####################################


##############################| Loops |#####################################

##############################| Classes and Objects |#####################################

##############################| Data Structures |#####################################




