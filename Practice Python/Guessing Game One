import random
num = random.randint(1,9)
guess = 0
count = 0
while int(guess) != num:
    guess = input("Guess number?")
    if guess == 'exit':
        break
    elif int(guess)<num:
        print("Too low")                          
        count += 1
    elif int(guess)>num:
        print("Too high")
        count += 1
    else:
        print("Success")
        print("It took ",count, "attemps")
