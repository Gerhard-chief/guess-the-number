import random
low = 1
high = 10
secret = random.randint(low, high)
attempts = 0

while True:
    guess = input(f"I thought of a number between {low} and {high}. Try to guess (enter q to exit): ").strip()
    if guess.lower() == 'q':
             print('Bye!')
             break
    try:
        guess = int(guess)
        if not (low <= guess <= high):
             print(f'Out of range. Enter from {low} to {high}')
             continue
        attempts += 1
        if guess > secret:
            print('Too big. Try again.')
        elif guess < secret:
            print('Too small. Try again.')
        else:
            print(f'Congratulations! You guessed it! Number of attempts: {attempts}')
            ag = input('Shall we play again?: Y/N').strip().lower()
            if ag == 'y':
                secret = random.randint(low, high)
                attempts = 0
                continue
            else:
                print('Bye!')
                break
    except ValueError:
        print('You had to enter a number')
        continue