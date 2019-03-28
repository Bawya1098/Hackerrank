from collections import Counter


def anagram():
    user_input_1 = str(input())
    user_input_2 = str(input()).rstrip()

    word = user_input_2.replace(" ", '')

    word_2 = user_input_1.replace(" ", '')

    if Counter(word) == Counter(word_2):
        print(True)
    else:
        print(False)


anagram()
