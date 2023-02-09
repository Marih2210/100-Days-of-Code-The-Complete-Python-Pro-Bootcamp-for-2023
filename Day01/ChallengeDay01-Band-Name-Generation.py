# This challenge addresses the topics: - print; - debugging; - input; - string manipulation and - variables.

#1. Create a greeting for your program.
print("Hello! How are you? This has the functionality to create a name for your band, so answer the questions below:\n")

#2. Ask the user for the city that they grew up in.
city = input("What city were you born in?\n")

#3. Ask the user for the name of a pet.
pet = input("\nWhat's your pet's name?\n")

#4. Combine the name of their city and pet and show them their band name.
nameOfBand = city + " " + pet 

#5. Make sure the input cursor shows on a new line:
print("\nThe name of your band is: %s" % (nameOfBand))
