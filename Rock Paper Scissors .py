# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1

import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock,paper,scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(game_images[user])

computer = random.randint(0,2)
print("Computer chose")
print(game_images[computer])

if user >= 3 or user <=0:
  print("You typed an invalid number U lose!")
elif user == 0 and computer == 2:
  print("You win!")
elif user == 2 and computer == 0:
  print("You lose")
elif computer > user:
  print("You lose")
elif user > computer:
  print("You win")
elif computer == user:
  print("It Draw")


  