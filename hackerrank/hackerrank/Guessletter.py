print(" Welcome to Hangman!")
print("Guess your letter")
Guess_word = str("CAT")
list = []
guess_list = []
for letter in Guess_word:
    value = ord(letter)
    list.append(value)
for blank in range(0, len(Guess_word)):
    print('- ', end='')
game = str(input())
guess_value = ord(game)
guess_list.append(guess_value)
for element in range(0, len(list)):
    if guess_list[0] == list[element]:
        print("GUESS IS CORRECT")
