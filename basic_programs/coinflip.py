from random import*
flip_num = 10


def flip():
    heads = 0
    tails = 0
    for num in range (1, flip_num + 1):
        if randint(0,10) % 2 == 0:
            print("You flipped a coin and got heads!")
            heads = heads + 1
        else:
            print("You flipped a coin and got tails!")
            tails = tails + 1
    print("\nYou flipped a coin " + str(flip_num) + " times and got heads " + str(heads) + " times and tails "
    + str(tails) + " times!")
flip()
