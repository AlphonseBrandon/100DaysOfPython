import random
letters = ['A', 'B', 'C', 'D']
numbers = ['1', '2', '3', '4']
symbols = ['!', '#', '$', '&']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password\n"))
nr_numbers = int(input("How many numbers would you like in your password\n"))
nr_symbols = int(input("How many symbols woll you like in your password\n"))


#Eazy level
password_list = []
#nr_letters = 4
for char in range(1, nr_letters + 1):
#range is 4     
    password_list.append(random.choice(letters)) 
    
for char in range(0, nr_symbols + 1):
    password_list += random.choice(letters)

for char in range(0, nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is {password}")
     

#Hard level