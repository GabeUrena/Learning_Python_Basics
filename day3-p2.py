#if statements
"""
temperature = float(input("What's the temperature?"))
"""
temperature = 70

if temperature > 80:
    print("It's a hot day!")
    print("Stay hydrated")
elif temperature > 70: #else if the temp is 70 and above its a nice day
    print("It's a nice day!")
elif temperature > 60: #else if the temp is 60 and above its a bit cold
    print("It's a bit cold!")
else: #else code prints if everything above doesn't trigger
    print("It's cold!")
    print("Make sure to say warm!")
print("Done")
    
print("*************************************************************************")
print("")

#WHILE LOOP

i = 1
while i <= 10:
    print(i * '*') # multiplying a number with a string repeats the string based on the value of the number.
    i = i + 1
    
print("*************************************************************************")
print("")

#LISTS

names = ["Justin", "Angel", "Gabriel", "Lianne", "Shylin"]
names[0] = "Joting"
print(names) # return the whole list
print(names[0]) # return the first index
print(names[-1]) #negative numbers represent the index starting from the last element and moves towards the front as you make the negative number smaller
print(names[-2]) # this is the second to last element

print(names[0:3]) #return names from index 0,1, and 2
