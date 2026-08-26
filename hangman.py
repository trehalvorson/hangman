import random

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

dictionary = ["DICTIONARY", "SKELETON", "PINEAPPLE", "GRAPE", "APPLE", "BANANA", "BLUEBERRY", "ORANGE", "EARTH", "PLANET", "MOON", "STAR", "SUN", "SPACE", "GALAXY", "COMET", "ASTEROID", "METEOR", "OCEAN", "RIVER", "LAKE", "MOUNTAIN", "VALLEY", "FOREST", "DESERT", "ISLAND", "BEACH", "CLIFF", "TREE", "FLOWER", "GRASS", "LEAF", "ROOT", "SEED", "STONE", "ROCK", "CLOUD", "RAIN", "SNOW", "WIND", "STORM", "THUNDER", "LIGHTNING", "FIRE", "WATER", "EARTHQUAKE", "VOLCANO", "RAINBOW", "DOG", "CAT", "HORSE", "COW", "SHEEP", "GOAT", "PIG", "CHICKEN", "EAGLE", "HAWK", "OWL", "RAVEN", "DUCK", "SWAN", "FROG", "SNAKE", "TURTLE", "LIZARD", "FISH", "WHALE", "SHARK", "DOLPHIN", "OCTOPUS", "CRAB", "SPIDER", "BEE", "BUTTERFLY", "ANT", "BEETLE", "PEACH", "PEAR", "CHERRY", "LEMON", "MELON", "MANGO", "BREAD", "CHEESE", "BUTTER", "MILK", "COFFEE", "TEA", "SUGAR", "SALT", "PEPPER", "RICE", "PASTA", "PIZZA", "SOUP", "CAKE", "COOKIE", "SCHOOL", "CLASS", "TEACHER", "STUDENT", "BOOK", "PENCIL", "PAPER", "DESK", "CHAIR", "BOARD", "COMPUTER", "PHONE", "TABLE", "DOOR", "WINDOW", "HOUSE", "ROOM", "KITCHEN", "GARDEN", "BRIDGE", "ROAD", "STREET", "CITY", "TOWN", "COUNTRY", "WORLD", "CAR", "TRUCK", "BUS", "TRAIN", "PLANE", "BOAT", "BIKE", "WHEEL", "ENGINE", "LIGHT", "CLOCK", "WATCH", "KEY", "LOCK", "BAG", "BOX", "BOTTLE", "CUP", "PLATE", "SPOON", "FORK", "KNIFE", "SHIRT", "PANTS", "SHOE", "HAT", "COAT", "RING", "WATCH", "BALL", "GAME", "MUSIC", "SONG", "MOVIE", "STORY", "PICTURE", "COLOR", "SOUND", "WORD", "LETTER", "NUMBER", "QUESTION", "ANSWER", "IDEA", "DREAM", "TIME", "DAY", "NIGHT", "MORNING", "EVENING", "SUMMER", "WINTER", "SPRING", "AUTUMN", "HAPPY", "SAD", "ANGRY", "CALM", "BRAVE", "SMART", "KIND", "STRONG", "FAST", "SLOW", "BIG", "SMALL", "HOT", "COLD", "OLD", "YOUNG", "NEW", "GOOD", "BAD", "FIRST", "LAST", "BEGIN", "END", "OPEN", "CLOSE", "START", "FINISH", "CREATE", "BUILD", "LEARN", "TRANSISTOR", "THINK", "SPEAK", "WRITE", "READ", "PLAY", "MISERY", "I", "A", "INDISTINGUISHABLE", "BEGINNING", "ABOMINABLE" "WORK", "HELP", "MOVE", "RUN", "JUMP", "WALK"]

if input("Do you have two people? Y/N ").upper == "Y":

   word = input("What word would you like to guesser to pick? ").upper()
   for i in range(32):
      print("")
   
   if word in dictionary:

      print("The word is in the English Dictionary.")

   else:

      print("The word is NOT in the (very small) dictionary that this game has.")

else:

   word = dictionary[random.randint(0, len(dictionary))]

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