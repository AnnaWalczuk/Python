import os
clear = lambda: os.system('cls')

game_dict = {
  "rock" : 1,
  "paper" : 2,
  "scissors" : 3
}



def play(who):
  player = input(who + " Please enter rock, paper or scissors: ").lower()
  if player not in ("rock", "paper", "scissors"):
    print("Wrong input")
    player = play(who)
  return player


def game():


  a = game_dict[play("Player 1")]

  clear()
  b = game_dict[play("Player 2")]

  diff = a-b

  if diff in (-2, 1):
   print("Player 1 wins. Congratulations!")

  elif diff in (2, -1):
   print("Player 2 wins. Congratulations!")

  else:
   print("It's a tie!")

  if input("Do you want to play another game? yes/no: ") == "yes":
   clear()
   game()

  else:
   print("game over")

game()