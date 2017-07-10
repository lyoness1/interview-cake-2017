from random import randint

def given_rand_7():
    return randint(1, 7)

def rand_5():
    pick = given_rand_7()
    if pick < 6:
        return pick
    else:
        rand_5()
    
def given_rand_5():
    return randint(0, 5)

def rand_7():
    pick = given_rand_5() + given_rand_5() + given_rand_5()
    if pick <= 14 and pick > 0:
        return pick / 2
    else:
        rand_7()

def rand_7_again():
    pick_1 = given_rand_5() 
    pick_2 = given_rand_5()
    # 25 equally possile options
    pick = pick_1 * pick_2
    if pick > 0 and pick <= 21:
        return (pick % 7) + 1
    else: 
        rand_7_again()