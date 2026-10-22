def main():
    user_input = input("camelCase: ")
    print(camel_converter(user_input))


def camel_converter(camel_case):
    word_in_list = []
    for word in camel_case:
        if word.isupper():
            word_in_list.append("_")
            word_in_list.append(word.lower())
        else:
            word_in_list.append(word)
    snake_case = "".join(word_in_list)
    return snake_case

main()
