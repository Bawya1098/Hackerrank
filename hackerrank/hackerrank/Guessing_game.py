print(" Welcome to Hangman!")
print("Guess your letter")
guess_Word = str("CAT")
print("-  " * len(guess_Word))
guess_Dict = {}
for letter in range(0, len(guess_Word)):
    key = guess_Word[letter]
    value = ord(guess_Word[letter])
    guess_Dict[key] = value
print(guess_Dict)
user_input = input("Enter any alphabet to play:")
user_input = user_input.upper()
guess_value = ord(user_input)
for element in guess_Dict.values():
    if guess_value != element:
        continue
    elif guess_value == element:
        print(chr(element))
        break
