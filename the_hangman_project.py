import random
import hangman_art
import hangman_phrases
import hangman_bank

print(hangman_phrases.title)

bank_of_words=hangman_bank.bank_of_words
chosen_word=random.choice(bank_of_words)
word_lenght=len(chosen_word)
display=[]

for letter in chosen_word:
    display.append('_')
print(display)

end_of_game=False
gallows=7
hangman_stages=hangman_art.hangman_stages
used_letters=[]

while not end_of_game:
  guess=input("Guess a letter: ").lower()
  if guess in used_letters:
     print(f"You already used {guess}.")
  for position in range(word_lenght):
    letter=chosen_word[position]
    if letter==guess:
      display[position]=letter
      used_letters.append(guess)
  if guess not in chosen_word and guess not in used_letters:
      gallows-=1
      print (f"{guess} is not in the word.")
  if guess not in chosen_word:
      used_letters.append(guess)
      if gallows==0:
         print(hangman_phrases.lose) 
         end_of_game=True   
      print(hangman_stages[gallows])
  print(display)
  if "_" not in display:
     end_of_game=True
     print(hangman_phrases.win)
if end_of_game==True:
  print(f"The word was {chosen_word}")