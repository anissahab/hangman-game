import random
import sys

# choose random word
word_list = ['coffee', 'candies', 'pencil', 'flashlight', 'animal', 'cartoon']
word = random.choice(word_list)

# find the length of the word
length_word = len(word)


# print out board and keep track

board1 = "   ____\n  |   \n  |   \n__|__  \n"
board2 = "   ____\n  |   0\n  |   \n__|__  \n"
board3 = "   ____\n  |   0\n  |   | \n__|__  \n"
board4 = "   ____\n  |   0\n  |  /|  \n__|__  \n"
board5 = "   ____\n  |   0\n  |  /|\  \n__|__  \n"
board6 = "   ____\n  |   0\n  |  /|\  \n__|__ /\n"
board7 = "   ____\n  |   0\n  |  /|\  \n__|__ /\ \n"

board_list = []
board_list.append(board1)
board_list.append(board2)
board_list.append(board3)
board_list.append(board4)
board_list.append(board5)
board_list.append(board6)
board_list.append(board7)

print(board_list[0])
board_number = 0

# print out amount of letters
i = 0
empty_list = []
while i < length_word:
    empty_list.append('_')
    i += 1
print(*empty_list, sep='')


# ask for a guess:
while True:
    print('Guess a letter')
    letter = input().lower()
    while len(letter) != 1 and not letter.isalpha():
        print('Only guess 1 letter at a time, you cannot guess a number')
        letter = input().lower()
    if letter in word:
        for index, i in enumerate(word):
            if i == letter:
                for index2, j in enumerate(empty_list):
                    if index == index2:
                        empty_list[index] = letter
        if '_' not in empty_list:
            print('You win! Game over')
            sys.exit
    elif letter not in word:
        board_number += 1
        print(board_list[board_number])
        if board_number == 6:
            print('Out of guesses! Game over')
            sys.exit()
    print(*empty_list, sep='')
