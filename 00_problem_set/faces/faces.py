def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    return text

def main():
    user_text = input("please enter your text: ")
    print(convert(user_text))
main()