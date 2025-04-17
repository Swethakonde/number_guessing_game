import random

def load_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except:
        return 0

def save_high_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))

def choose_difficulty():
    print("Select difficulty level:")
    print("1 - Easy (1 to 10)")
    print("2 - Medium (1 to 50)")
    print("3 - Hard (1 to 100)")

    level = input("Enter your choice (1/2/3): ")
    if level == '1':
        return 10, 5
    elif level == '2':
        return 50, 7
    elif level == '3':
        return 100, 10
    else:
        print("Invalid choice. Defaulting to Easy.")
        return 10, 5

def play():
    max_val, attempts = choose_difficulty()
    number = random.randint(1, max_val)
    score = 0

    print(f"\nGuess a number between 1 and {max_val}")
    print(f"You have {attempts} tries")

    for i in range(attempts):
        try:
            guess = int(input(f"Attempt {i+1}: "))
        except:
            print("Please enter a valid number")
            continue

        if guess == number:
            print("You got it!")
            score = (max_val - i*2) + 10    #scoring logic
            break
        elif guess < number:
            print("Too low")
        else:
            print("Too high")

    if score == 0:
        print(f"You lost. The number was {number}")
    else:
        print(f"Your score: {score}")

    high = load_high_score()
    if score > high:
        print("New high score!")
        save_high_score(score)
    else:
        print(f"High score: {high}")

# Main loop
while True:
    play()
    again = input("Play again? (y/n): ")
    if again.lower() != 'y':
        break
