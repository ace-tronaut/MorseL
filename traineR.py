import datetime
import random
import csv
import os
#import mysql.connector
import sys
import time

morseBase = [['A','.-'], ['B','-...'], ['C','-.-.'], ['D','-..'], ['E','.'], ['F','..-.'], ['G','--.'], ['H','....'], ['I','..'], ['J','.---'], ['K','-.-'], ['L','.-..'], ['M','--'], ['N','-.'], ['O','---'], ['P','.--.'], ['Q','--.-'], ['R','.-.'], ['S','...'], ['T','-'], ['U','..-'], ['V','...-'], ['W','.--'], ['X','-..-'], ['Y','-.--'], ['Z','--..']]

# Declare Congo list element here
Congo = ["Congratulations!", "Amazing!", "Incredible!", "Yippee!", "Huzzah!", "Hooray!", "That was a good round!", "You got it!", "Call for the fireworks! It's time for a CELEBRATION!", "That's how it's done!"]

# Declare noCongo list element here
noCongo = ["Oh, try again", "It's fine, have another shot", "The stars are for your taking, try again!", "Ooop- try it again", "*BUZZER* I'm afraid that was not correct!", "Have another shot at it....."]




def traineR(a, b, tracker):

    if tracker == 0:
        #This is only for new users. It introduces traineR in more detail.
        tracker = 0

        trainerIntro = ("") # This is yet to be filled; it should explain the working of the traineR.
        for i in trainerIntro:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.04)
        cont = input("click Enter to continue: ")
        tracker = 1
    
    elif tracker == 1:
        # Here, the code runs through all the letters and the user enters the Morse equivalent of the alphabet shown. Morse is also shown.

        i = random.randint(0, 25)

        print(morseBase[i[1]], end = "")
        print(morseBase[i[2]])
        ans = input('Enter in the dots you see; use periods and hyphens: ')
        print()
        if ans == morseBase[i[2]]:
            j = random.randint(0, len(Congo))
            print(Congo[j])
            print()
        else:
            j = random.randint(0, len(Congo))
            print(noCongo[j])
            print()
            a = 1
            while a!=0:
                anss = input('Try again: ')
                if anss == morseBase[i[2]]:
                    j = random.randint(0, len(Congo))
                    print(Congo[j])
                    print()
                    a=0
                else:
                    j = random.randint(0, len(Congo))
                    print(noCongo[j])
                    print()

        cont = input("click Enter to continue: ")
        tracker = 2

    elif tracker == 2:
        # This part of the code serves the function of runs through all the Morse letters and the user enters the English equivalent of the Morse shown. The alphabets are also shown.

        hool = ("Now we'll show you the Morse and then it's corresponding letter, you have to type them out; Easy as that?")

        for i in hool:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.04)

        for i in range(26):
            print(morseBase[i[1]], end = "")
            print(morseBase[i[2]])
            ans = input('Enter in the letter of the Morse: ')
            print()
            if ans == morseBase[i[0]]:
                j = random.randint(0, len(Congo))
                print(Congo[j])
                print()
            else:
                j = random.randint(0, len(Congo))
                print(noCongo[j])
                print()
                a=2
                while a!=0:
                    anss = input('Try again: ')
                    if anss == morseBase[i[0]]:
                        j = random.randint(0, len(Congo))
                        print(Congo[j])
                        print()
                        a=0
                    else:
                        j = random.randint(0, len(Congo))
                        print(noCongo[j])
                        print()
            cont = input("click Enter to continue: ")
            tracker = 3

    # We are yet to decide on the next step, but I [Johnson] guess that it'll be tracker1 without showing the answers, and then tracker2 w/o answers, and then randomized.
    pass
