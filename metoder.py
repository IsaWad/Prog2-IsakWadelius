def add_this(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

#add_this(1, 2, 3)

def food(food, vegan = False):
    if vegan == True:
        print(f"soja{food}")
    else:
        print(food)

food("mjölk", True)