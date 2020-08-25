import time
import random

wel = (
    "Welcome to the trainer! Here we'll get you upto speed with morse and how it works!"
)
for i in wel:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.04)
print(180 * "-")
print()
q = input('Press Enter to Continue ')
print()
qool = (
    "So let's begin off with all the letter; we'll show you the letters and corresponding morse code, you have to type them out; Simple right?"
)
for i in qool:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.04)
    
print()    

for i in range(26):
    print(morseBase[i[1]], end = "")
    print(morseBase[i[2]])
    ans = input('Enter in the dots you see; use periods and hyphens: ')
    print()
    if ans == morseBase[i[2]]:
        j = random.randint(3)
        print(Congo[j])
        print()
    else:
        j = random.randint(3)
        print(nocongo[j])
        print()
        while a!=0:
            anss = input('Try again: ')
            if anss = morseBase[i[2]]:
                j = random.randint(3)
                print(Congo[j])
                print()
                a=0
            else:
                j = random.randint(3)
                print(nocongo[j])
                print()

hool = (
    "Now we'll show you the Morse and then it's corresponding letter, you have to type them out; Easy as that?"
)
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
        j = random.randint(3)
        print(Congo[j])
        print()
    else:
        j = random.randint(3)
        print(nocongo[j])
        print()
        a=2
        while a!=0:
            anss = input('Try again: ')
            if anss = morseBase[i[0]]:
                j = random.randint(3)
                print(Congo[j])
                print()
                a=0
            else:
                j = random.randint(3)
                print(nocongo[j])
                print()
