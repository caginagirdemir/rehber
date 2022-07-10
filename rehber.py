import sys
from pydoc import pager
import os

def check_file(F_NAME):
    os.chdir("/home/" + os.getenv('USER') + "/rehber/data/")
    obj = os.scandir(".")
    for entry in obj :
        if (entry.is_file() & entry.name.endswith(".txt")):
            with open(entry) as f:
                if(entry.name == F_NAME+'.txt'):
                    contents = f.read()
                    pager(contents)
                    return
    print("Parametre Bulunamadi!")
 

os.chdir("/home/" + os.getenv('USER') + "/rehber")
os.system("git pull https://github.com/caginagirdemir/rehber")
if(len(sys.argv) == 1):
    check_file("yardim")
elif(len(sys.argv) == 2):
    if (sys.argv[1].lower() == "rehber"):
        print("yardim")
        check_file("yardim")
    else:
        check_file(sys.argv[1].lower())

        ###test
