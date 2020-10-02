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



def cred():
    #this is the UDF that checks the login credentials
    pass

def newUser():
    #this needs the SQL integration and building of SQL database
    a = input("")
    b = input("")

    global a, b
    pass

def returnUser(a, b):
    #this ALSO needs the SQL integration and building of SQL database
    y = cred() 
    global a, b, tracker    
    return y

def login():
    while True:
        loginText = ("Are you new here, or have you trained before?\n\n")

        for i in loginText:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.04)

        print("[1] Never trained before! \n[2] I'm back for more! \n\n ")

        loginChoice = int(input("Enter [1] or [2] here: "))

        if loginChoice == 1:
            newUser()
            traineR(a, b, 0) # Here, [a] and [b] are global variables for username and password declared inside newUser()
            break

        elif loginChoice == 2:
            tries = 1
            while tries <= 5:
                a = input("Enter your username here: ")
                b = input("Enter your password here: ")
                x = returnUser(a, b)

                if x == True:
                    traineR(a,b, tracker)
                    break
            
            else:
                passError = ("You have incorrectly input your password 5 times. \nTry again later. \n\n")
                for i in passError:
                    sys.stdout.write(i)
                    sys.stdout.flush()
                    time.sleep(0.04)

        else:
            err = ("I'm afraid that wasn't a choice! Go back and pick one.\n\n")

            for i in err:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(0.04)
            continue
