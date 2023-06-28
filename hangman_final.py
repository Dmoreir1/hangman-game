import random




def main():

  badGuesses = 0


  guesses = ""

  # word = "".lower()

  word = random.choice(["Rosie", "Karina", "Nicole", "Leo", "Samira", "Sacoya", "Xani", "Valentina", "Dan", "Rob", "Dhruv", "Reid", "Caridad", "Mel", "Ethan", "Tunisia", "Valerie"]).lower()

  for letter in word:

    guesses += "_"

  while badGuesses < 6 and not guesses == word:

    letter = input("Guess a letter: ").lower()
    # print(hangmanPicture(0))
    print("You have this many guesses left:", 6 - badGuesses)
    # print("You've guessed this so far:", guesses)
    if letter in word:

      for i in range(len(word)):

        if letter == word[i]:

          guesses = guesses[:i] + letter + guesses[i+1:]
      print("You've guessed this so far:", letter)
    else:

      badGuesses += 1

      hangmanPicture(badGuesses)
      print("Wrong Guess!")
      print("You've guessed this so far:", guesses)
  if guesses == word:
    print("Congratulations! You guessed the word!")
    print("WOOO YOU WON!!!")

  else:

    print("You are hung!")
    print("You have this many guesses left:",guesses)





def hangmanPicture(badGuesses):

  if badGuesses == 0:

    print("_" * 17)

    print("|               |")

    print("|")

    print("|")

    print("|")

    print("|")

    print("|")

    print("_______")

  elif badGuesses == 1:

    print("_" * 17)

    print("|               |")

    print("|               O")

    print("|")

    print("|")

    print("|")

    print("|")

    print("_______")

  elif badGuesses == 2:

    print("_" * 17)

    print("|               |")

    print("|               O")

    print("|               |")

    print("|               |")

    print("|")

    print("|")

    print("_______")

  elif badGuesses == 3:

    print("_" * 17)

    print("|               |")

    print("|             \ O")

    print("|              \|")

    print("|               |")

    print("|")

    print("|")

    print("_______")

  elif badGuesses  == 4:

    print("_" * 17)

    print("|               |")

    print("|             \ O /")

    print("|              \|/")

    print("|               |")

    print("|")

    print("|")

    print("_______")

  elif badGuesses == 5:

    print("_" * 17)

    print("|               |")

    print("|             \ O /")

    print("|              \|/")

    print("|               | ")

    print('|                \ ')

    print('|                 \ ')

    print("_______")

  elif badGuesses == 6:

    print("_" * 17)

    print("|               |")

    print("|             \ O /")

    print("|              \|/")

    print("|               | ")

    print("|              /|\ ")

    print("|             /   \ ")

    print("_______    You are Hung! ")




if __name__ == "__main__":

  main()