def gradingStudents(grades):
    print("grades:", grades)
    for index in range(0, len(grades)):
        value = grades[index] + (5 - (grades[index] % 5))
        round_value = value - grades[index]
        if round_value < 3:
            final_value = grades[index] + round_value

            if final_value >= 40:

                print(final_value)

            elif final_value < 40:
                print(grades[index])

        else:
            print(grades[index])


if __name__ == '__main__':

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)
