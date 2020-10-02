'''

'''


# import modules
import datetime
import random
import csv
import os
#import mysql.connector
import sys
import time

#Declare morseBase
morseBase = [['A','.-'], ['B','-...'], ['C','-.-.'], ['D','-..'], ['E','.'], ['F','..-.'], ['G','--.'], ['H','....'], ['I','..'], ['J','.---'], ['K','-.-'], ['L','.-..'], ['M','--'], ['N','-.'], ['O','---'], ['P','.--.'], ['Q','--.-'], ['R','.-.'], ['S','...'], ['T','-'], ['U','..-'], ['V','...-'], ['W','.--'], ['X','-..-'], ['Y','-.--'], ['Z','--..']]

# Declare Congo list element here
Congo = ["Congratulations!", "Amazing!", "Incredible!", "Yippee!", "Huzzah!", "Hooray!", "That was a good round!", "You got it!", "Call for the fireworks! It's time for a CELEBRATION!", "That's how it's done!"]

# Declare noCongo list element here
noCongo = ["Oh, try again", "It's fine, have another shot", "The stars are for your taking, try again!", "Ooop- try it again", "*BUZZER* I'm afraid that was not correct!", "Have another shot at it....."]




def translatoR():
    #Declare morseBase
    morseBase = [['A','.-'], ['B','-...'], ['C','-.-.'], ['D','-..'], ['E','.'], ['F','..-.'], ['G','--.'], ['H','....'], ['I','..'], ['J','.---'], ['K','-.-'], ['L','.-..'], ['M','--'], ['N','-.'], ['O','---'], ['P','.--.'], ['Q','--.-'], ['R','.-.'], ['S','...'], ['T','-'], ['U','..-'], ['V','...-'], ['W','.--'], ['X','-..-'], ['Y','-.--'], ['Z','--..']]

    while True:
        #Options to translate 
        translateMode = ("Select mode of translation:\n[1] From MORSE to ENGLISH\n[2] From ENGLISH to MORSE\n[0] EXIT Translator\n\n")

        for i in translateMode:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.04)
        try:
            C = int(input("Enter your choice using the number next to it: "))

            if C == 0:
                break

            elif C == 1:
                x = input("Enter MORSE to translate (must have spaces between whole letters) : ")
                l = x.split('  ')
                s = ''
                for i in l:
                    y = i.split()
                    for k in y:
                        for j in morseBase:
                            if k == j[1]:
                                s += j[0]
                    s += ' '
                print(s)


            elif C == 2:
                x = input("Enter ENGLISH to translate (must have spaces between words) : ")
                x = x.upper()
                l = x.split()
                s = ''
                for i in l:
                    for k in i:
                        for j in morseBase:
                            if k == j[0]:
                                s += j[1]
                        s += ' '
                    s += '  '
                print(s)
            
            else:
                err = ("I'm afraid that wasn't a choice! Go back and pick one.\n\n")

                for i in err:
                    sys.stdout.write(i)
                    sys.stdout.flush()
                    time.sleep(0.04)
                continue
        except:
            errorMessage = ("The program didn't recognize what you input. Try again! \n\n")

            for i in errorMessage:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(0.04)
            continue


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

# Declare login() and it's associated UDFs here



Title = ("                                                       /██      \n                                                      | ██      \n /██████/████   /██████   /██████   /███████  /██████ | ██      \n| ██_  ██_  ██ /██__  ██ /██__  ██ /██_____/ /██__  ██| ██      \n| ██ | ██ | ██| ██  | ██| ██  |__/|  ██████ | ████████| ██      \n| ██ | ██ | ██| ██  | ██| ██       |____  ██| ██_____/| ██      \n| ██ | ██ | ██|  ██████/| ██       /███████/|  ███████| ████████\n|__/ |__/ |__/ |______/ |__/      |_______/  |_______/|________/")

print(Title)
time.sleep(0.04)
print()
e = ("The best Morse code trainer!")
for i in e:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.04)

    
# Will redo the heading with ASCII art for "pazzaz" and effect
print()
time.sleep(1)
print(180 * "-")
time.sleep(2)


Mrse = ("\nMorse code, developed by Samuel Morse, is an intricately designed system of letters which can be communicated through dots and dashes, and can hence be delivered through a variety of media adding to it's versatility and usefulness.")

for i in Mrse:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.04)
time.sleep(2)
print()
print()

mrs = ("In this program you will be able to learn how to use Morse code through training modules and games or you can input any English text and convert it into Morse code and vice-versa.")

for i in mrs:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.04)
print()
print()
wer = ("Now let's go!\n\n")

for i in wer:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.04)
while True:
    try:
        introText = ("You can choose what you want to do! \n\nPick from the following: \n[1] translatoR \n[2] traineR \n[0] EXIT application \n\n")

        for i in introText:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.04)

        introChoice = int(input("Enter your choice from the options above: "))

        if introChoice == 1:
            translatoR()
            continue

        elif introChoice == 2:
            #login()
            continue

        elif introChoice == 0:
            time.sleep(2)
            sayonara = "Thank you for using our application 'morseL'! It has been a month long project filled with roadblocks, exploration, trial-and-error, and heaps of fun. We hope it was as useful to you as it was fun for us!"
            for i in sayonara:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(0.04)
            break
        
        else:
            err = ("I'm afraid that wasn't a choice! Go back and pick one.\n\n")

            for i in err:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(0.04)
            continue
    except:
        errorMessage = ("The program didn't recognize what you input. Try again! \n\n")

        for i in errorMessage:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.04)
        continue

