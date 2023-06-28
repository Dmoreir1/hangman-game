# def hangman_picture(badguess):
#
#     if badguess == 1:
#         print("_" * 17)
#         print("|               |")
#         print("|               O")
#         print("|")
#         print("|")
#         print("|")
#         print("|")
#         print("_______")
#         # break
#
#     elif badguess == 2:
#         print("_" * 17)
#         print("|               |")
#         print("|               O")
#         print("|               |")
#         print("|               |")
#         print("|")
#         print("|")
#         print("_______")
#     elif badguess == 3:
#         print("_" * 17)
#         print("|               |")
#         print("|             \ O")
#         print("|              \|")
#         print("|               |")
#         print("|")
#         print("|")
#         print("_______")
#     elif badguess ==  4:
#         print("_" * 17)
#         print("|               |")
#         print("|             \ O /")
#         print("|              \|/")
#         print("|               |")
#         print("|")
#         print("|")
#         print("_______")
#     elif badguess == 5:
#         print("_" * 17)
#         print("|               |")
#         print("|             \ O /")
#         print("|              \|/")
#         print("|               | ")
#         print('|                \ ')
#         print('|                 \ ')
#         print("_______")
#     else:
#         print("_" * 17)
#         print("|               |")
#         print("|             \ O /")
#         print("|              \|/")
#         print("|               | ")
#         print("|              /|\ ")
#         print("|             /   \ ")
#         print("_______    You are Hung! ")
#
# hangman_picture()


def hangman():
    guesses = []
    badguess = 0
    word = "Michael".lower()
    # print("Guess the word:")
    # print("Tries Left:")
    # print("Enter a letter:")

    for eachLetter in word:
        guesses.append("_")
        # print(guesses)

    for eachLetter in word:

        letter = input("Guess a letter: ").lower()

        for i in range(len(word)):

            if letter == word[i]:
                guesses[i] = letter
                listToStr = ' '.join([str(elem) for elem in guesses])
                print(listToStr)
            else:
                # letter != word[i]
                badguess += 1

                    # hangman_picture(badguess)


hangman()


    # if letter in pool:
    #         print("Good Guess!")
# #     # underscores will be in above array
#     word = "Michael"
#     for eachLetter in word:
#             # for all the letters in banana
#         guesses.append("_")
#     for eachLetter in word:
#         letter = input("Guess the letter: ")
#         for i in range(len(word)):
#             if letter == word[i]:
#                 guesses[i] = [word[i]]
#             else:
#                 print("Say goodbye to a body part")
#







# guess = banana

# guess = string, turn guess- string into array of letters that make up the word -->



#
