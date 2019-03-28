def list(n):
    list = []
    for element in str(n):
        list.append(element)

    sorted_ = sorted(list)
    if list == sorted_:
        print("ascending")
    elif list == sorted_[::-1]:
        print("descending")
    else:
        print('neither')


list(54321)
