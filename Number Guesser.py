import random
secret_number = random.randint(1, 20)
attempts = 0
while True:
    prompt = "Guess a number between 1 and 20: " if attempts == 0 else "Try again: "
    sn = int(input(prompt))
    attempts += 1
    if sn < secret_number:
        print("Your guess is too low.")
    elif sn > secret_number:
        print("Your guess is too high.")
    else:
        print("Congratulations! You guessed the number.")
        print(f"It took you {attempts} attempts.")
        break