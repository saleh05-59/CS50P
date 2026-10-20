user_weight = int(input("please enter your wright in kg: "))

def e_calc(weight=int):
    energy = weight * (300000000 ** 2)
    return energy
print(e_calc(user_weight))

