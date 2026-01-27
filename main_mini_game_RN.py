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

        if start == "q":
            return None
        elif start == "a":
            return 1, 10, "a"
        elif start == "b":
            return 1, 100, "b"
        else:
            print("Incorrect input")


def play_round(low, high):
    secret = random.randint(low, high)
    attempts = 0

    while True:
        s = input(f"I thought of a number between {low} and {high}. Enter q to menu: ").strip().lower()

        if s == "q":
            print("return to the menu...")
            return None

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
            print(f"Congratulations! Attempts: {attempts}")

            ag = input("Back to difficulty menu? (y/n): ").strip().lower()
            if ag == "y":
                return attempts
            else:
                return "exit"


def main():
    global best_10, best_100

    while True:
        choice = choose_difficulty()
        if choice is None:
            print("Bye!")
            return

        low, high, mode = choice

        result = play_round(low, high)

        if result is None:
            # игрок нажал q во время угадывания -> назад в меню сложности
            continue

        if result == "exit":
            print("Bye!")
            return

        # сюда мы попадаем только если игрок угадал и вернулся в меню
        attempts = result

        if mode == "a":
            if best_10 == 0 or attempts < best_10:
                best_10 = attempts
            print(f"Best for 1..10: {best_10}")
        else:
            if best_100 == 0 or attempts < best_100:
                best_100 = attempts
            print(f"Best for 1..100: {best_100}")


if __name__ == "__main__":
    main()
