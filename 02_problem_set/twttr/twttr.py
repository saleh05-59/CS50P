def main():
    user_input = input("Input: ")
    print(f"Output: {omitter(user_input)}")

def omitter(input):
    word_in_list = []
    for word in input:
        if word == "a" or word == "e" or word == "i" or word == "o" or word == "u" or word == "A" or word == "E" or word == "I" or word == "O" or word == "U":
            pass
        else:
            word_in_list.append(word)
    output = "".join(word_in_list)
    return output

main()
