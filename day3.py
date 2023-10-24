# methods
course = 'Python tutorial'
print(course.find('y'))
print(course.find('Y'))
print(course.find('tutorial'))
print(course.find(' '))
#replace the word tutorial with practice, however this doesn't change the variable course
print(course.replace('tutorial','practice'))
print(course)

#boolean value checking string variables

print('Python' in course)

print("**********************************************************")

#Arithmetic Operator
print("Arthmetic operator using 10 and 3")
print("+  : " + str(10+3))
print("-  : " + str(10-3))
print("*  : " + str(10*3))
print("/  : " + str(10/3))
print("// : " + str(10//3))
print("%  : " + str(10%3))

x = 10
x += 3
x -= 5
# x = 10 -> 13 -> 8
print(x)

X = 10 + 3 * 2
print(x)

print("**********************************************************")

#comparison Operators   > >= < <= == !=

x = 3 > 2
print (x)

#Example remove comment for input
"""
num1 = float(input('Type a number: '))
num2 = float(input('tyoe a second number: '))
"""
num1 = 1
num2 = 3

print("Is " + str(num1) + " is greater than " + str(num2) + " ?:")
print(num1>num2)

print("Is " + str(num1) + " is less than " + str(num2) + " ?:")
print(num1<num2)

print("Is " + str(num1) + " is equal to " + str(num2) + " ?:")
print(num1==num2)

print("Is " + str(num1) + " not equal to " + str(num2) + " ?:")
print(num1!=num2)

print("**********************************************************")
#logical operator

price = 25
print("price =", price)
print("price is greater than 25 AND less than 75:", price > 25 and price < 75)
print("price is less than 30 OR greater than 75:", price < 30 and price > 75)
