'''
Well known a "Hangman" game.
Program have capability to start after finished g ame(guess all of the letters or lose a game) as subshell instance on your local maschine.
Remember to replace hangman_data(words) and hangman_art(stages & logo), your own files.
Line 63: #remember to switch "hanged_man.py" to your own filename.
'''

import random, time, os, sys
from hangman_data import words
from hangman_art import logo
print(logo)
print("\nWELCOME TO HANGMAN !\n")
print("\nLet's play a game !\n")
time.sleep(2)
print("\nLet's start guessing our secret...")
chosen_word = random.choice(words)
word_length = len(chosen_word)
lives = 6
#Display letter at current position
display = []
for _ in range(word_length):
  display += '_'
end_of_game = False
while not end_of_game:
  guess = input("\nGuess a letter\n").lower()
    
  #Reminder for user about same guessed letter.
  if guess in display:
        print(f"You've already guessed {guess}")
  #Informing user about false input.
  if guess not in chosen_word:
        print(f"You missed ! '{guess}' does not appear in the keyword. You lose a life.")
  # Checking the guessed letter.
  i = chosen_word[0]
  for i in chosen_word:
    guess == i
  i += chosen_word[1]
    
  # If after checking guess not i the chosen word.
  if guess not in chosen_word:
        lives -= 1
        if lives == 0:
          end_of_game = True
          print("You lose.")
            
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
  print(f"{' '.join(display)}")
  # Checking if user won
  if "_" not in display:
        end_of_game = True
        print("You win.")
       
  # Import stages
  from hangman_art import stages
  print(stages[lives])
    
  while end_of_game:
    restart = input("\nDo you wanna try again ? Y/N?\n")
    if restart == 'Y':
      os.system('python hanged_man.py')
    elif restart == 'N':
      print("\nSee you later !")
      break
    elif restart != 'Y' or restart != 'N':
      print("\nPlease use only 'Y' for 'yes' or 'N' for 'no'.\n")
  
  
  
    
