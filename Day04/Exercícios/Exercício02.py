import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

size_list = len(names) 
number_sort = random.randint(0, size_list - 1)
print(f"{names[number_sort]} is going to buy the meal today!")
