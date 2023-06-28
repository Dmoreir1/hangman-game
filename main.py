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

#guess_pool: array of all letters guessed


## trying out the error reporting
if eachLetter == False and guesses > 0:
    print("You have this many chances:" guesses)

    if len(guesses) ==1:
        if guesses in word:
            letter_guess_pool.append(guesses)



