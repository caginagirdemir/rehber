import sys
from pydoc import pager
import os
import urllib.request

def connect():
    try:
        urllib.request.urlopen('http://github.com', timeout=1) 
        return True
    except:
        return False

def check_file(F_NAME):
    # print("/home/" + os.getenv('USER') + "/rehber/data/")
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
 
if connect():
    os.chdir("/home/" + os.getenv('USER') + "/rehber")
    os.system("git pull https://github.com/caginagirdemir/rehber")
else:
    print("Internet baglantisi bulunamadi.")
if(len(sys.argv) == 1):
    check_file("yardim")
elif(len(sys.argv) == 2):
    if (sys.argv[1].lower() == "rehber"):
        print("yardim")
        check_file("yardim")
    else:
        check_file(sys.argv[1].lower())
