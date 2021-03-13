import random

def main():
  # print('You rolled a die')
  # roll =  random.randint(1,6)
  # print(f'You rolled {roll}')

  total_dice = 2
  dice_sum = 0

  for i in range(0,total_dice):
    roll = random.randint(1,6)
    dice_sum += roll
    print(f'You rolled {roll}')
  print(f'You have rolled a total of {dice_sum}')
  

if __name__== "__main__":
  main()