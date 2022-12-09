import random
ran_num = random.randint(50,60)

enter_key = input("PRESS ANY KEY TO CONTINUE ")
attempts = 0
print(' YOU HAVE 3 ATTEMPTS!!!')


while attempts < 3:
    print(' Guessing a number between 50 and 60:')
    userGuess = int(input())
    attempts += 1
    if userGuess < 50:
        print('Your attempt is lower than 50. ONLY VALUES FROM 50-60')
    if userGuess < ran_num:
        print('Your guess is too low')
    if userGuess > ran_num:
        print('Your guess is too high')
    if userGuess == ran_num:
        break

if userGuess == ran_num:
    print('You got the number in ' + str(attempts) + ' attempts!')
else:
    print('YOU LOSE!!! The number was ' + str(ran_num))