import random


class dice(object):
    def __init__(self):
        pass

    @staticmethod
    def play_dice():
        return random.randint(1, 6)


print('The program will play dice once you enter your name. The one who has bigger number will win!')
player_name = input('Enter Your Name:')
match_count = int(input('How many matches do you want to play?:'))
computer_win = 0
player_win = 0
while (computer_win + player_win) < match_count:
    player = dice()
    player_result = player.play_dice()
    computer = dice()
    computer_result = computer.play_dice()
    if player_result > computer_result:
        print(
            f'Dear {player_name},Your result is {player_result} and computer result is {computer_result}. You win this '
            f'round!')
        player_win = player_win + 1
        continue
    elif player_result < computer_result:
        print(
            f'Dear {player_name},Your result is {player_result} and computer result is {computer_result}. You lose in '
            f'this round!')
        computer_win = computer_win + 1
        continue

    else:
        print(
            f'Dear {player_name},Your result is {player_result} and computer result is {computer_result}. This round is'
            f'Draw!')
        continue
if computer_win > player_win:
    print(f"Computer has won {computer_win} times and You won{player_win} times. You LOSE! ")
elif player_win > computer_win:
    print(f"Computer has won {computer_win} times and You won{player_win} times. You WIN! ")
else:
    print('IT IS A DRAW!')
