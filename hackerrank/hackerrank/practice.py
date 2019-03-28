def function(word_list):
    length = 0
    for elements in word_list:
        length1 = len(elements)
        if length < length1:
            return length1
        else:
            return length


print(function(['ece', 'Apple', 'c']))
