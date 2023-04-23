print("welcome to the project guessing.py!")
# Comparing variables
number = 10 

number_input = input("type a number: ")
print("you type the number:", number_input) # input sempre volta como tipo str 
print(type(number_input))

number_input = int(number_input) # conversão para tipo int

if (number_input == number):
    print("victory!")
else:
    print("defeat!")

# Execise 
number1 = 1
number2 = 4 
if (number1 == number2):
    print("equality!")
else:
    print("not equality!")

age1 = 10 
age2 = "20"

print(age1 + age2) #TypeError: unsupported operand type(s) for +: 'int' and 'str'

name = "Nico"
last_name = "Steppat"
print(name+last_name) #NicoSteppat