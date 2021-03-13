import random

def main():
  # print('You rolled a die')
  # roll =  random.randint(1,6)
  # print(f'You rolled {roll}')

  total_dice = int(input("How many Dice?"))
  dice_size = int(input("How many sides are the Dice?"))
  dice_sum = 0
  for i in range(0,total_dice):
    roll = random.randint(1,6)
    dice_sum += roll
    if roll == 1:
      print(f'You rolled {roll}! Critical Fail')
    elif roll == dice_size:
      print(f'You rolled {roll}! Critical Success!')
    else:
      print(f'You rolled {roll}')
  print(f'You have rolled a total of {dice_sum}')
  

if __name__== "__main__":
  main()