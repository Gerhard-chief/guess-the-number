import random
 
best_10 = 0
best_100 = 0
attempts = 0

def main():
    while True:
        start = input(f"Hi. I suggest you play a game of guess the number. There are two difficulty levels:\n a) 1 to 10\n b) 1 to 100\nEnter 'a' or 'b', or 'q' to exit.").strip().lower()
        if start == 'q':
            print('Bye!')
            return
        elif start == 'a':
            low = 1
            high = 10
        elif start == 'b':
            low = 1
            high = 100
        else:
            print('Incorrect input')
            continue

        secret = random.randint(low, high)
        attempts = 0
        max_attempts = 0

        while True:
            guess = input(f"I thought of a number between {low} and {high}. Try to guess (enter 'q' to back to menu): ").strip().lower() 
            if guess == 'q':
                    print('return to the menu...')
                    break
            try:
                guess = int(guess)
                if not (low <= guess <= high):
                    print(f'Out of range. Enter from {low} to {high}')
                    continue
                attempts+=1
                if guess > secret:
                    print('Too big. Try again.')
                elif guess < secret:
                    print('Too small. Try again.')
                else:
                    if start == 'a':
                        if best_10 == 0 or attempts < best_10:
                            best_10 = attempts
                        best_attempts = best_10
                    else:
                        if best_100 == 0 or attempts < best_100:
                            best_100 = attempts
                        best_attempts = best_100 
                    print(f'Congratulations! You guessed it! Number of attempts: {attempts}. Best attempts: {best_attempts}')
                    ag = input('Shall we play again?: Y/N').strip().lower()
                    if ag == 'y':
                        break
                    else:
                        print('Bye!')
                        return
            except ValueError:
                print('You had to enter a number')
                continue
            
if __name__ == "__main__":
    main()