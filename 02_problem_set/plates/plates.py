import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

chars = string.whitespace + string.punctuation

def is_valid(s):
    if 2 <= len(s) <=6 :
        if s[0].isalpha() and s[1].isalpha() :
            digit_identifier = False
            s_list = list(s)
            for i in range(len(s_list)):
                if s_list[i].isdigit() or s_list[i].isalpha():
                    if digit_identifier:
                        if s_list[i].isdigit():
                            if i == len(s_list)-1 :
                                return True
                            else :
                                pass
                        else :
                            return False
                    else:
                        if s_list[i].isdigit():
                            if s_list[i] == "0" :
                                return False
                            else:
                                digit_identifier = True
                                if i == len(s_list)-1 :
                                    return True
                        else:
                            if i == len(s_list)-1 :
                                return True
                else:
                    return False
        else:
            return False
    else:
        return False

main()
