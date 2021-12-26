import random
print('Well come to the dice game: ')
print("If you wanna play the game press 1...and if you don't wawnna paly press 2")
user = int(input())
print('How many times you wanna role: ')
count = int(input())
for i in range(count):
    if user == 1:
        number = random.randint(1,6)
        print(number)
    elif user == 2:
        print('Too bad, lets play next time')
    else:
        print('Not a valid option') 



#Part 2

while True:
    print('Dice Rolling.....')
    print(random.randint(1,6))
    user_input = (input('Do you wanna play again? y/n: '))
    if user_input.lower() == 'y':
        continue
    else:
        break 
        

        
