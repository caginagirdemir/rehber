#/usr/bin/python

import time
import sys
import os

lines=[
"Wake up Neo ...",
"The Matrix has you",
"Follow the C Rehber...",
"Now you are ready to use C Rehber..."
]

os.system("clear")

GREEN = '\033[22;32m'
ENDC = '\033[0m'
BLUE = '\033[34m'
RED = '\033[31m'


print (GREEN)
for line in lines:
    words  = line.split()

    for word in words:
        for c in list(word):
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.15)
        sys.stdout.write(" ")
        sys.stdout.flush()

        time.sleep(0.7)

    if line.startswith("Follow"):
        time.sleep(2)

    os.system("clear")

print (ENDC)

time.sleep(3)
# lines.clear()
# lines_2=[
# "42 Istanbul Rehber'e Hosgeldin.",
# "Unutma suan icin resmi bir rehber degil.",
# "Bilgilerini rehbere yükleyerek topluluk ile paylasabilirsin.",
# "Artik rehberi kullanmaya hazirsin..."
# ]

# os.system("clear")
# for line in lines_2:
#     words  = line.split()

#     for word in words:
#         for c in list(word):
#             sys.stdout.write(c)
#             sys.stdout.flush()
#             time.sleep(0.15)
#         sys.stdout.write(" ")
#         sys.stdout.flush()

#         time.sleep(0.7)

#     if line.startswith("Follow"):
#         time.sleep(2)

#     os.system("clear")

os.chdir("/home/" + os.getenv('USER'))
os.system("mkdir rehber")
os.chdir("./rehber")
os.system("git init")
os.system("git pull https://github.com/caginagirdemir/rehber")
os.chdir("..")
with open('./.bashrc', "r") as f:
    if 'rehber.py' in f.read():
        print("alias already exist")
        exit(1)

file1 = open("./.bashrc", "a")
file1.write("alias rehber=\"python3 /home/" + os.getenv('USER') + "/rehber/rehber.py $1\"")
file1.close()