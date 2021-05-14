import os
import time
import random

try:
  os.system('cls')
  os.system('clear')
except:
  pass

playerName = str(input("Enter your name: "))

def cubesSum():
  cube1 = random.randint(1, 6)
  cube2 = random.randint(1, 6)
  cube3 = random.randint(1, 6)
  cube4 = random.randint(1, 6)
  cube5 = random.randint(1, 6)

  sumCubes = cube1 + cube2 + cube3 + cube4 + cube5
  return (sumCubes)

def game():
  x = cubesSum()
  
  print("CPU shakes ...")
  time.sleep(2)
  print("It is " + str(x))

  y = cubesSum()

  print(playerName + " shakes Dices!")
  input("Press Enter key to throw dices....")
  print("It is " + str(y))
  
  print("CPU won, try again...") if x > y else print("You are a winner!!!")
  restart = input("Do you want to test your luck one more time? (y/n) ")
  if restart == "y" or restart == "Y":
    game()
  else:
    print("Thanks for plaing")

game()
