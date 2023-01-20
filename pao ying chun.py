import random

print("Welcome to pao ying chub game!")
print("Are you ready ????")
print("Let's Start !!!!!")


count = 3

pycb = ['R','P','S']
your_turn2 = []
pycb_ran = random.choice(pycb)
  
while count > 0:
  print(f"You have {count} chances to beat me!")
  print(">>>>>>> [R]Rock  [P]Paper  [S]Scissors <<<<<<<")
  your_turn = str(input('Your turn: '))
  ## Rock
  if your_turn == 'R' and pycb_ran == 'P':
    print(f"Your choice is '{your_turn}' vs The pycb choice is '{pycb_ran}'")
    print("You Lose!!, Try Again")
    count -= 1

  elif your_turn == 'R' and pycb_ran == 'S':
    print(f"Your choice is '{your_turn}' vs The pycb choice is '{pycb_ran}'")
    print("You Win!!, Awesome")
    break

  elif your_turn == 'R' and pycb_ran == 'R':
    print(f"Your choice is '{your_turn}' vs The pycb choice is '{pycb_ran}'")
    print("Ohhh.. Draw, Next Round!!")
    count -= 1

  ## Paper
  elif your_turn == 'P' and pycb_ran == 'P':
    print(f"Your choice is '{your_turn}' vs The pycb choice is '{pycb_ran}'")
    print("Ohhh.. Draw, Next Round!!")
    count -= 1

  elif your_turn == 'P' and pycb_ran == 'S':
    print(f"Your choice is '{your_turn}' vs The pycb choice is '{pycb_ran}'")
    print("You Lose!!, Try Again")
    count -= 1

  elif your_turn == 'P' and pycb_ran == 'R':
    print(f"Your choice is '{your_turn}' vs The pycb choice is '{pycb_ran}'")
    print("You Win!!, Awesome")
    break

  ##Scissors
  elif your_turn == 'S' and pycb_ran == 'P':
    print(f"Your choice is '{your_turn}' vs The pycb choice is '{pycb_ran}'")
    print("You Win!!, Awesome")
    break

  elif your_turn == 'S' and pycb_ran == 'S':
    print(f"Your choice is '{your_turn}' vs The pycb choice is '{pycb_ran}'")
    print("Ohhh.. Draw, Next Round!!")
    count -= 1

  elif your_turn == 'S' and pycb_ran == 'R':
    print(f"Your choice is '{your_turn}' vs The pycb choice is '{pycb_ran}'")
    print("You Lose!!, Try Again")
    count -= 1
  else:
    print('Type again !!!')
