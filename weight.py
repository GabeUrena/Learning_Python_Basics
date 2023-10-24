#asks for weight, asks for kg or lbs? cover weight

weight = float(input("Enter a weight: "))
userInput = input("Is this weight in Kg or Lbs?: ").lower()

if userInput == "kg":
    print(weight,"Kilograms is " + str(weight / 0.45359237) + " Pounds.")
elif userInput == "lbs":
    print(weight,"Pounds is " + str(weight * 0.45359237) + " Kilograms.")
