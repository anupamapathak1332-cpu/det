
secret = 27
attempts = 0
won = False

while attempts < 5 and not won:
    guess = int(input("Guess a number (1–50): "))
    attempts = attempts + 1

    if guess == secret:
        print("🎉 You won!")
        won = True
    else:
        difference = abs(guess - secret)

        if difference >= 20:
            print("🧊 Ice cold!")
        elif difference >= 10:
            print("🥶 Cold!")
        elif difference >= 5:
            print("🌡️ Warm!")
        else:
            print("🔥 Hot!")

        remaining = 5 - attempts
        print("Lives remaining:")
        for heart in range(remaining):
            print("❤️", end="")
        print()

if not won:
    print("You lost. The secret number was", secret)