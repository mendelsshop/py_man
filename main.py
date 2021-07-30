import random
l1 = "  ‗‗‗‗‗‗   "
l2 = "  O  │   "
l3 = " -│- │   "
l4 = " / \ │   "
l5 = "    ‾‾   "


def hangedman():
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)


def headman():
    l3 = "     │   "
    l4 = "     │   "
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)


def stickman():
    l3 = "  │  │   "
    l4 = "     │   "
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)


def leftman():
    l3 = " -│  │   "
    l4 = "     │   "
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)


def nolegmsan():
    l4 = "     │   "
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)


def leftlegman():
    l4 = " /   │   "
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)


def gallows():
    l2 = "     │   "
    l3 = "     │   "
    l4 = "     │   "
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
lives = 6
game_over = False
def main():
    print(" hangman ")
    gallows()
    thewordis = whatshallthewordbe()
    lists = list(thewordis)
    listtocompare = list(lists)
    listlen = len(lists)
    for x in range(listlen):
        if listtocompare[x] == ' ':
            listtocompare[x]=' '
        else:
            listtocompare[x] = '-'
    while game_over == False:
        print(lists)
        print(listtocompare)
        if lists == listtocompare:
            print('you won')
            game_over == True
        guess = input('what is your guess: ')
        for x in lists:
            z = lists.index(x)
            corret = False
            if x == guess:
                print(f'{x} is correct')
                for x in lists:

                listtocompare[z] = x
                global corret
                corret = True
        #if corret == False:
        #    print(f"{guess} is in incorrect")
        #    global lives
        #    lives = lives - 1
        #    if lives == 5:
        #        headman()




    print(listtocompare)
def whatshallthewordbe():
    x = random.randint(0, 9)
    words = ('hello world', 'potato kugel', 'banana shnitzel', 'hot dogs', 'funkputer', 'black hat', 'tennis racket', 'tablecloth', 'kitchen', 'your nose')
    thewords = words[x]
    return thewords
if __name__ == '__main__':
    main()
