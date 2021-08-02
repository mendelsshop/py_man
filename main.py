import random
import os
import time
class person:
    def __init__(self,names,lives,gusses):
        self.names = names
        self.lives = lives
        self.gusses = []
  

def clear():
    input("Press Enter to continue...")
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
def clear1():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def tries(lives):
        if lives == 5:
            headman()
        elif lives == 4:
            stickman()
        elif lives == 3:
            leftman()
        elif lives == 2:
            nolegmsan()
        elif lives == 1:
            leftlegman()
        elif lives == 6:
            gallows()
def worrd(word):
    lists = list(word)
    return lists
def worrds(lists):
    listtocompare = list(lists)
    listlen = len(lists)
    for x in range(listlen):
        if listtocompare[x] == ' ':
            listtocompare[x]=' '
        else:
            listtocompare[x] = '-'
    return listtocompare



l1 = "  ‗‗‗‗   "
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
def main():
    print("------hangman------")
    byyourself = input('do you want to enter your own word? (yes/no) ')
    if byyourself == 'yes':
        thewordis = input('what word do you want to use: ')
        lists = worrd(thewordis)
        listtocompare = worrds(lists)
        clear1()
    else:
        thewordis = whatshallthewordbe()
        lists = worrd(thewordis)
        listtocompare = worrds(lists)
        clear1()
    
    peoples = {} 
    times = 0
    while True:
        names = input("what is your name? ") 
        peoples[names] = person(names = names, lives = 6, gusses = ())
        while True:
            continues = input("do you want to add another person? (yes/no) ")
            if continues == 'yes':
                names = input("what is your name? ") 
                if names in peoples:
                    print('plz try another name that name is already taken')
                    continue
                else:
                    peoples[names] = person(names = names, lives = 6, gusses = ())
                    continue
            else: break
        break
    while True:
        clear1()
        print("------hangman------")
        names = input("what is your name? ")  
        clear1()
        print("------hangman------")
        print(listtocompare)          
        if names not in peoples:
            print(f'{names} is not a valid name')
            if len(peoples) == 1:
                print('this is a valid name')
            else:
                print('these are all  names:')
            for i in peoples:
                print(i)
            clear()
            continue
        tries(peoples[names].lives)
        guess = input(f'{names} what is your guess: ').lower()
        if guess in peoples[names].gusses:
            print(f'please try again  {guess} was already tried')
            clear()
            continue
        elif (len(guess)) > 1:
            print('your guess cannot be more than 1 digit')
            print('please try again')
            clear()
            continue
        elif (len(guess)) < 1:
            print('your guess cannot be less than 1 digit')
            print('please try again')
            clear()
            continue
        if guess not in ('a b c d e f g h i j k l m n o p q r s t u v w x y z').split():
            print('please enter a letter')
            print('try again')
            clear()
            continue
        else:
            peoples[names].gusses.append(guess)
        corret = False
        if guess in lists:
            print(f'{guess} is correct')
            pos = []
            for i in range(len(lists)):
                if lists[i] == guess:
                    pos.append(i)
            for z in range(len(pos)):
                listtocompare[pos[z]] = guess
        elif guess not in lists:
            print(f"{guess} is incorrect")
            peoples[names].lives = peoples[names]. lives -1
        if peoples[names].lives == 0:
            clear()
            hangedman()
            print(f'{names} is out')   
            times +=1
            del peoples[names]
        if lists == listtocompare:
            clear()
            times += 1
            tries(peoples[names].lives)
            print(f'{names} win(s)\nthe word(s) was {thewordis}')
            print(f'it took {times} trie(s) untill {names} won')
            input("Press Enter to continue...")
            break
        times += 1
        clear()
def whatshallthewordbe():
    x = random.randint(0, 9)
    words = ('hello world', 'potato kugel', 'banana shnitzel', 'hot dogs', 'funkputer', 'black hat', 'tennis racket', 'tablecloth', 'kitchen', 'your nose')
    thewords = words[x]
    return thewords
if __name__ == '__main__':
    main()
    while True:
        clear()
        print("------hangman------")
        continues = input('do you want to continue? (yes/no) ')
        clear()
        if continues == 'yes':
            main()
        elif continues == 'no':
            print('bye bye')
            quit()