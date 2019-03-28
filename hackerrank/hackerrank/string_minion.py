def minion_game(s):
    def is_vowel(char):
        return char in 'AEIOU'

    count_kevin = 0
    count_stuart = 0
    for i in range(0, len(s)):
        if is_vowel(s[i]):
            count_kevin += len(s) - i
        else:
            count_stuart += len(s) - i
    if count_stuart > count_kevin:
        print("Stuart", count_stuart)
    elif count_kevin > count_stuart:
        print("Kevin", count_kevin)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
