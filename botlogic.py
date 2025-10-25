import random
def flipcoin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "орел"
    else:
        return "решка"