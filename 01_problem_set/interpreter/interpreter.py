def main():
    user_input = input("Expression: ")
    user_input = user_input.split()
    first_number = float(user_input[0])
    second_number = float(user_input[2])
    if user_input[1] == "+":
        print(first_number + second_number)
    elif user_input[1] == "-":
        print(first_number - second_number)
    elif user_input[1] == "*":
        print(first_number * second_number)
    elif user_input[1] == "/":
        print(first_number / second_number)

main()
