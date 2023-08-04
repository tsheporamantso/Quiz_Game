print('Welcome to my computer quize game!')

playing = input('Are you keen on playing?, if you are, kindly type(Yes)! ')

if playing.lower() != 'yes':
    quit()
else:
    print('Let the game begin!')

score = 0

answer = input('Which country won the fifa world cup in 2010? ')

if answer.lower() != 'france':
    print('Incorrect!')
else:
    print('Spot-on, player!!')
    score = score + 1

answer = input('Which country hosted the fifa world cup in 2010? ')

if answer.lower() != 'south africa':
    print('Incorrect!')
else:
    print('Well done :)')
    score = score + 1

play_on = input('Would you like to proceed with computer related questions? ')

if play_on != 'yes':
    print(':( You have managed to score ' + str(score) + " out of 2")
    if score < 2:
        print('Low score, please try again')
    else:
        print('Perfect score')
    quit()
else:
    print('Ride on player ;)')

answer = input('What does CPU stand\'s for? ')

if answer.lower() != 'central processing unit':
    print('Incorrect!')
else:
    print('On your way to becoming a serious computer hacker. LOL')
    score = score + 1

answer = input('What does GPU stand\'s for? ')

if answer.lower() != 'graphic processing unit':
    print('Incorrect!')
else:
    print('You such a star')
    score = score + 1

answer = input('What does RAM stand\'s for? ')

if answer.lower() != 'random access memory':
    print('Incorrect!')
else:
    print('You such a star')
    score = score + 1

print("That concludes our game and your total score is " + str(score) + ' out of 5')

if score < 2:
    print('Low score, please try again')
elif score == 3:
    print('Average, you can most certainly do better')
else:
    print('Kudos, YOU THE BEST!!')

print('That is ' + str((score / 5 ) * 100) +'%')
