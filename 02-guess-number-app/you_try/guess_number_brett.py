import random

print('-------------------------------')
print('   GUESS THAT NUMBER GAME')
print('-------------------------------')
print()

the_number = random.randint(0, 100)

# we can't compare int and str, we use transformation like this
# str_numb = str(the_number)
# we can check the kind of data types like this
# print(the_number, type(the_number))
# print(str_numb, type(str_numb))

name = input('Player, what is your name? '
             '')
# TODO: implement a looping quiz
guess = -1
while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    # Handle invalid responses
    if guess_text == "":
        print("Illegal!")
        guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)
    if guess < the_number:
        print('Sorry, {0}, Your guess of {1} was too low!'.format(name, guess))
    elif guess > the_number:
        print('Sorry, {0}, your guess of {1} was too high!'.format(name, guess))
    else:
        print('Excellent work, {0}, it was indeed {1}, you win!'.format(name, guess))
