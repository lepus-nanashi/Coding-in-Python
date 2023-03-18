import random
easy_level_attempts = 0
hard_level_attempts = 0

def difficulty_level():
  difficulty = input ("Choose a difficulty. Type 'easy' or 'hard: ")
  if difficulty == "easy":
    return 10
  if difficulty == "hard":
    return 5
  else:
    print("Please select one of the options!")
    return difficulty_level()

def compare_numbers(guess_attempt, right_number, tries):
   if guess_attempt > right_number:
      print ("Too high\nGuess again")
      return tries-1
   if guess_attempt < right_number:
      print("Too low\nGuess again")
      return tries-1

def game_over():
   restart = input("Would you like to play again? Types 'yes' or 'no'")
   restart.lower()
   if restart == "yes":
      import os
      from time import sleep
      print("This screen will clear out in a moment.")
      sleep(1)
      os.system('cls')
      play_game()
   if restart == "no":
      import os
      from time import sleep
      print("This screen will clear out in a moment.")
      sleep(1)
      os.system('cls')
      quit()

      
   
def play_game():
   from guess_the_number_art import logo
   lst_numbers = list(range(1,101))
   number = random.choice(lst_numbers)
   attempts = 0
   user_guess = 0

   print("Welcome to the Number Guessing Game!")
   print("I'm thinking of a number between 1 and 100")
   attempts = difficulty_level()
   print(f"Your have {attempts} attempts remaining to guess the number")

   user_guess = int(input("Make a guess: "))

   while user_guess != number:
        attempts = compare_numbers(guess_attempt = user_guess, right_number = number, tries = attempts)
        print(f"Your have {attempts} attempts remaining to guess the number")
        user_guess = int(input("Make a guess again: "))
        if attempts == 1:
          print("Oops! Looks like you run out of attempts")
          game_over()
   if user_guess == number:
      print (f"୧(๑•̀ヮ•́)૭ LET'S GO! You got it! The answer was {number}!")
      game_over()
   
play_game()