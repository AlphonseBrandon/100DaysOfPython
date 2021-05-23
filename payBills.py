#import random

#test_seed = int(input("Create a seed number: "))
#random.seed(test_seed)

#nameAsCSV = input("Give me everybody's names, separeted by a comma")
#names = nameAsCSV.split(", ")


#get the total number of items in list
#num_items = len(names)
#random_choice = random.randint(0, num_items -1)
#person_who_will_pay = random.choice(names)
#print(f"{person_who_will_pay} will pay the bills")


#Find the treasure game!

row1 = ["1", "1", "1"]
row2 = ["2", "2", "2"]
row3 = ["3", "3", "3"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to study the treasure")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row = map[horizontal - 1] = "X"


print(f"{row1}\n{row2}\n{row3}")