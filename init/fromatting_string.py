print("welcome to the project guessing.py!")

number = 10
guessing_round = 1
total_try = 3


while guessing_round <= total_try:
    print(f"round: {guessing_round} of {total_try}")
    
    number_input = input("type a number: ")
    print("you type the number:", number_input)
    number_input = int(number_input)
    victory = number_input == number
    greater = number_input > number
    less = number_input < number
    
    if victory:
        print("victory!")
    else:
        if greater:
            print("defeat!, your number is greater than the misterious number...")
        elif less:
            print("defeat!, your number is less than the misterious number...")

    guessing_round += 1
print("end")

