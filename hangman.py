def splice(text, index, new_text): # Replaces the letter at specified index with string new_text

   text = text[:index] + new_text + text[index+1:]
   return text

gallows = ["  ___ ", " |   |", "     |", "     |", "   __|__"]

def print_gallows():

   for i in range(5):
     print(" " * (len(word) - 1) + gallows[i])

   print(correct, end=" ")

   for i in guesses: # For every guess that is not correct, print
      if i not in correct:
         print(i, end=" ")

   print("")
   print("")

mistakes = 0
def mistake():

   global mistakes
   mistakes += 1
   gallows[int("233344"[mistakes - 1])] = splice(gallows[int("233344"[mistakes - 1])], int("110202"[mistakes - 1]), "O|/\\/\\"[mistakes - 1])

word = input("What word would you like to guesser to pick? ").upper()
for i in range(33):
   print("")

guesses = []
correct = "_" * len(word)

included_letters = (" ", ",", ".", "?", "!", "-", "=", "+", "'", '"', ":", "/")
for letter in included_letters:
   for i in range(len(word)):
      if word[i] == "_":
         correct = splice(correct, i, "-")
      elif word[i] == letter:
         correct = splice(correct, i, letter)

def game():

   global correct

   print_gallows()

   guess = input("Which letter would you like to guess? ").upper()

   if guess in guesses:

      print("You've already guessed that letter. Try again!")

   elif len(guess) != 1:

      print("Your guess has to be only one letter. Try again!")

   elif guess in included_letters:

      print("That's not a valid character. Try again!")

   else:

      guesses.append(guess) # Adds guess to list of guessed letters
      
      if guess in word:

         for i in range(len(word)): # Adds letters in the word that match the guess to the string of correct letters at the correct indeces
            if word[i] == guess:
               correct = splice(correct, i, guess)

      else:

         mistake()

   if mistakes > 5:

      print_gallows()
      print(f"You lost. Better luck next time! (The word was {word})")

   elif "_" not in correct:

      print_gallows()
      print("You won! Want to try again?")

   else:      

      game()

game()