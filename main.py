import hangmanPicture.py
def main():
    guesses = []

    word = "Michael"

    for eachLetter in word:
        guesses.append("_")

    for eachLetter in word:

        letter = input("Guess a letter: ").lower()

        for i in range(len(word)):

            if letter == word[i]:
                guesses[i] = letter

                print(guesses)


# main()

