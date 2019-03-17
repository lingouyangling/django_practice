import random

l = [i for i in range(100,1000) if len(set([j for j in str(i)])) == 3]

num = random.choice(l)

game_on = True

while game_on:
    guess = input('Guess a 3 digit number')
    if int(guess) == num:
        print('Match')
        game_on = False
    elif set([i for i in guess]) == set([i for i in str(num)]):
        print('Close')
    else:
        print('Nope')
