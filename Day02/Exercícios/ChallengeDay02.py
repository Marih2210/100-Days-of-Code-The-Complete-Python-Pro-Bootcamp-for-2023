#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")

conta = float(input("What was the total bill? $"))
porcentagem = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
pessoas = int(input("How many people to split the bill? "))

gorjeta_porcentagem = porcentagem/100
total_gorjeta = gorjeta_porcentagem * conta

total_conta = conta + total_gorjeta
conta_pessoa = round(total_conta / pessoas, 2)
conta_pessoa = "{:.2f}".format(conta_pessoa)

print(f"Each person should pay: ${conta_pessoa}")
