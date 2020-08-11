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

for i in range(26):
    rand = random.randint(26)
    print(morseBase[rand[1]])
