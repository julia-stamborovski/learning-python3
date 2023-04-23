print("welcome to the project guessing.py!")

number = 10 

number_input = input("type a number: ")
print("you type the number:", number_input)

number_input = int(number_input) 

victory = number_input == number
greater = number_input > number
less    = number_input < number

if victory:
    print("victory!")
else:
    if greater:
        print("defeat!, your number is greater than the misterious number...")
    elif less:
        print("defeat!, your number is less than the misterious number...")

idade_str = input("Digite sua idade: ")
idade = int(idade_str)

maior_idade = idade > 18
crianca     = idade < 12
adolescente = idade > 12

age = int(input("type an age here: "))

