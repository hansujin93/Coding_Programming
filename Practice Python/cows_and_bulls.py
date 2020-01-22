num = str(random.randint(1000,9999))
guess = 0
while guess != num:
    cows = 0
    bulls = 0
    guess = input("Guess Number for Cows and Bulls")
    for i in range(len(num)):
        for j in range(len(guess)):
            if guess[j] == num[i] and j == i:                      
                cows += 1                                           
            elif guess[j] == num[i] and j != i:
                bulls += 1
            else:
                pass
    print(cows, "cows", bulls, "bulls", num)
