def main():
    debt_calc()

def debt_calc():
    amount_due = 50
    while amount_due > 0:
        print("Amount due:", amount_due)
        user_input = int(input("Insert Coin: "))
        if user_input == 25 :
            amount_due = amount_due - 25
        elif user_input == 10:
            amount_due = amount_due - 10
        elif user_input == 5:
            amount_due = amount_due - 5
        else:
            continue
    print("Change owed:", amount_due)

main()