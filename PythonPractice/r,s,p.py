import random
print('Let us play: ')
def play():
    user_input = input('Choose "r" for rock, "s" for scissors and "p" for paper: ').lower()
    computer_input = random.choice(["r", "s", "p"])
    score = 0
    if computer_input == user_input:
        return('Its a tie')
    if is_winner(user_input, computer_input):
        print('You Win...')
        score += 1
    return('You lost...')
def is_winner(player, opponent):
    score =0
    if player == 'r' and opponent == 's' or player == 'p' and opponent == 'r' or player == 's' and opponent == 'p':
        return True
while True:
    print(play())

