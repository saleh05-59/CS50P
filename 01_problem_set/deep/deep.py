def main():
    user_ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if deep_question(user_ans) :
        print("Yes")
    else:
        print("No")

def deep_question(ans):
    ans = ans.lower()
    if ans == "42" or ans == "forty two" or ans == "forty-two":
        return True
    else:
        return False

main()