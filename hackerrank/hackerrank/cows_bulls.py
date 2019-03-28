import random


def guess_number():
    print(" Welcome to the Cows and Bulls Game!")

    number_to_guess = str(random.randint(1000, 9999))
    print(number_to_guess)
    digits_in_number_to_guess = list(number_to_guess)
    count_cow = 0
    length_of_number = len(number_to_guess)

    while count_cow < len(str(number_to_guess)):
        count_cow = 0
        count_bull = 0

        user_input = input("enter the 4-digit number:")

        digits_in_user_input = list(user_input)
        for index in range(0, length_of_number):
            for user_input_index in range(0, len(digits_in_user_input)):
                if digits_in_number_to_guess[index] == digits_in_user_input[index]:
                    count_cow += 1
                    break

                elif digits_in_number_to_guess[index] == digits_in_user_input[user_input_index]:
                    count_bull += 1
                    break

        if count_cow == length_of_number:
            print("You won!!!!")

        elif count_bull == length_of_number:
            print("Good Guess ; Rearrange and try again")

        print("cows:", count_cow)
        print("Bulls:", count_bull)


guess_number()
