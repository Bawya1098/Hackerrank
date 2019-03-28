def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)
    totalcost = round(meal_cost + tip + tax)
    return totalcost


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    result = solve(meal_cost, tip_percent, tax_percent)
    print(result)
