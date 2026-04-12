from random import seed, randint  # import seed and randint functions

seed(1) 

def dice3():
    return (randint(1, 6), randint(1, 6))
