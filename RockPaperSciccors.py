import random

while True:
      choices = ["rock","paper","scissors"]

      computer = random.choice(choices)
      player = None

      while player not in choices:
            player = input("rock, paper or scissors?: ").lower()
      if player == computer:
            print("Computer: ", computer)
            print("You: ", player)
            print("It's a tie!!!!!")
      elif player == "rock":
            if computer == "paper":
                  print("Computer: ", computer)
                  print("You: ", player)
                  print("You loose!!!!!")
            elif computer == "scissors":
                  print("Computer: ", computer)
                  print("You: ", player)
                  print("You win!!!!!")
      elif player == "paper":
            if computer == "scissors":
                  print("Computer: ", computer)
                  print("You: ", player)
                  print("You loose!!!!!")
            elif computer == "rock":
                  print("Computer: ", computer)
                  print("You: ", player)
                  print("You win!!!!!") 
      elif player == "scissors":
            if computer == "paper":
                  print("Computer: ", computer)
                  print("You: ", player)
                  print("You win!!!!!")
            elif computer == "rock":
                  print("Computer: ", computer)
                  print("You: ", player)
                  print("You loose!!!!!")
      isPlay = input("Do you want to play again?: (press y for yes/press n for no): ")
      if isPlay == "n":
            break
print("Thanks for playing with me :)")

            
