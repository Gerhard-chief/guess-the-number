import random

best_10 = 0
best_100 = 0

def choose_difficulty():
    while True:
        start = input(
            "Hi. Guess the number.\n"
            "a) 1 to 10\n"
            "b) 1 to 100\n"
            "Enter 'a' or 'b', or 'q' to exit: "
        ).strip().lower()

        if start == 'q':
            return None
        elif start == 'a':
            return 1, 10, 'a'
        elif start == 'b':
            return 1, 100, 'b'
        else:
            print("Incorrect input")

def main():
    global best_10, best_100

    while True:
        choice = choose_difficulty()
        if choice is None:
            print("Bye!")
            return

        low, high, mode = choice
        secret = random.randint(low, high)
        attempts = 0

        while True:
            s = input(f"I thought of a number between {low} and {high}. Enter q to menu: ").strip().lower()
            if s == 'q':
                print("return to the menu...")
                break

            try:
                guess = int(s)
            except ValueError:
                print("You had to enter a number")
                continue

            if not (low <= guess <= high):
                print(f"Out of range. Enter from {low} to {high}")
                continue

            attempts += 1

            if guess > secret:
                print("Too big. Try again.")
            elif guess < secret:
                print("Too small. Try again.")
            else:
                # обновляем лучший результат по режиму
                if mode == 'a':
                    if best_10 == 0 or attempts < best_10:
                        best_10 = attempts
                    best_attempts = best_10
                else:
                    if best_100 == 0 or attempts < best_100:
                        best_100 = attempts
                    best_attempts = best_100

                print(f"Congratulations! Attempts: {attempts}. Best: {best_attempts}")

                ag = input("Back to difficulty menu? (y/n): ").strip().lower()
                if ag == 'y':
                    break
                else:
                    print("Bye!")
                    return

if __name__ == "__main__":
    main()
