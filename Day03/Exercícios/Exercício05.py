# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()

true1 = name1_lower.count("t") + name2_lower.count("t")
true2 = name1_lower.count("r") + name2_lower.count("r")
true3 = name1_lower.count("u") + name2_lower.count("u")
true4 = name1_lower.count("e") + name2_lower.count("e")
trueFinal = true1 + true2 + true3 + true4 

love1 = name1_lower.count("l") + name2_lower.count("l")
love2 = name1_lower.count("o") + name2_lower.count("o")
love3 = name1_lower.count("v") + name2_lower.count("v")
love4 = name1_lower.count("e") + name2_lower.count("e")
loveFinal = love1 + love2 + love3 + love4

trueFinalStr = str(trueFinal)
loveFinalStr = str(loveFinal)

loveScore = trueFinalStr + loveFinalStr
loveScoreInt = int(loveScore)

if loveScoreInt < 10 or loveScoreInt > 90:
    print(f"Your score is {loveScoreInt}, you go together like coke and mentos.")

elif 40 <= loveScoreInt <= 50:
    print(f"Your score is {loveScoreInt}, you are alright together.")

else:
    print(f"Your score is {loveScoreInt}.")
