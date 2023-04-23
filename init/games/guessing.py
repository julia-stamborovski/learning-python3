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