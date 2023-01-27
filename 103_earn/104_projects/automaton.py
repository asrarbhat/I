"""

a python script that takes two command line arguments

first: path to file under observation => relative or absolute

second: command to be executed if the size of the file changes

ps- put both in " "

"""

import os
import time
from sys import argv, exit

if len(argv) != 3:  # as automaton.py is first argument
    print("invalid arguments!!!!")
    print("use this way: ")
    print('     python3 automaton.py "./main.c" "gcc ./main.c && ./a.out"')
    print("so if main.c changes gcc ./main.c && ./a.out will be executed")
    exit(-1)

file = argv[1]  # file whose size you want to put under observation
command = argv[2]  # command you want execute after every change
size = 0
count = 0  # how many modifications done to file since running this script
while(True):
    time.sleep(0.8)  # otherwise using resources unnessarily(potential typo)
    try:
        file_size = os.path.getsize(file)
        if size != file_size:
            os.system(
                'echo "$(tput setaf 2)[     iteration no:   '+str(count)+'  ] $(tput setaf 7)"')
            print(" ")

            # your command executes here
            os.system(command)

            print("   \n")
            os.system('echo "$(tput setaf 2)[     end     ]"')
            print("   ")
            size = file_size
            count += 1
    except (Exception, OSError, FileNotFoundError):
        pass
