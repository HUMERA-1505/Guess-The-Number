import random
from art import logo

print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")

num = random.randint(1,100)

#print(f"correct ans is {num}")

diff = input("Choose the difficulty.Type 'easy' or 'hard':  ").lower()

def easy(numb):
  attempts = 10
  print("You have 10 attemts remaing to guess the number")
 
  while attempts != 0:
    guess = int(input("Make a guess: "))
    if guess == numb:
      print(f"You got it!! The answer was {numb}.")
      attempts = 0
    
    else:
      attempts = attempts-1
      if attempts == 0:
        print("You've run out of guesses, you lose.")
        print(f"The answer was {numb}")
      elif guess < numb :
        print("Too low.")
        print("Guess again.")
        print(f"You have {attempts} attempts left to number.")
        
      elif guess > numb :
        print("Too high.")
        print("Guess again.")
        print(f"You have {attempts} attempts left to number.")


def hard(numb):
      attempts = 5
      print("You have 5 attemts remaing to guess the number")

      while attempts != 0:
        guess = int(input("Make a guess: "))
        if guess == numb:
          print(f"You got it!! The answer was {numb}.")
          attempts = 0

        else:
          attempts = attempts-1
          if attempts == 0:
            print("You've run out of guesses, you lose.")
            print(f"The answer was {numb}")

          elif guess < numb :
            print("Too low.")
            print("Guess again.")
            print(f"You have {attempts} attempts left to number.")

          elif guess > numb :
            print("Too high.")
            print("Guess again.")
            print(f"You have {attempts} attempts left to number.")


if diff == "easy":
  easy(num)
elif diff == "hard":
  hard(num)
else:
  print("Choose a valid option")
