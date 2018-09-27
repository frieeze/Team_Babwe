import os
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

nfc = "/home/alexis/isen/Team_Babwe/test.txt"

nbs = os.path.getmtime(nfc)

print(nbs)
print(time.time())

if time.time()-15 < nbs :
    print(bcolors.OKGREEN,"Je vous pisse au cul")