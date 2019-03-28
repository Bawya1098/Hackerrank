def reverse_string(str1):
    if len(str1) % 4 == 0:
        word = ''.join(reversed(str1))
        return word
    return str1


print(reverse_string('abcd'))
print(reverse_string('python'))
