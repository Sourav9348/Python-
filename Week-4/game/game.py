import random
while True:
    try:
        n = int(input("Level: "))
        random_num = random.randint(1, n)
        guess = int(input("Guess: "))
        if guess < random_num:
            print("Too small!")
            continue
        elif guess > random_num:
            print("Too Large!")
            continue
        else:
            print("Just right!")
    except ValueError:
        continue
    break
