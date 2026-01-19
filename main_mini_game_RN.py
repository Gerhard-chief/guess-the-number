import random
secret = random.randint(1, 10)
while True:
    guess = input("I thought of a number between 1 and 10. Try to guess (enter q to exit): ").strip()
    if guess.lower() == 'q':
             print('Bye!')
             break
    try:
        guess = int(guess)
        if guess > secret:
            print('Too big. Try again.')
        elif guess < secret:
            print('Too small. Try again.')
        else:
            print('Congratulations! You guessed it!')
            ag = input('Shall we play again?: Y/N').strip().lower()
            if ag == 'y':
                secret = random.randint(1, 10)
                continue
            else:
                print('Bye!')
                break
    except ValueError:
        print('You had to enter a number')
        continue