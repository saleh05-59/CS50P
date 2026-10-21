def main():
    user_input = input("Greeting: ")
    if user_input.lower().strip() == "hello":
        print("$0")
    elif user_input.lower().strip().find("h") == 0:
        print("$20")
    else :
        print("$100")

main()