import sys, requests
from os import system, name

# Python script that prints out all comments in HTML source code. 
# Primary use: OSINT Gathering if the web devs have forgotten to remove critical comments
# Written By Aksel Troan
# GitHub: https://github.com/AkselTroan
#
# Usage: htmlCommentChecker.py websites.txt

def clear():  # Clearing terminal

    # For Windows
    if name == 'nt':
        _ = system('cls')

    # For MacOS and Linux
    else:
        _ = system('clear')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    welcome = """    __  __________  _____       ______                                     __     ________              __
   / / / /_  __/  |/  / /      / ____/___  ____ ___  ____ ___  ___  ____  / /_   / ____/ /_  ___  _____/ /_____  _____
  / /_/ / / / / /|_/ / /      / /   / __ \/ __ `__ \/ __ `__ \/ _ \/ __ \/ __/  / /   / __ \/ _ \/ ___/ //_/ _ \/ ___/
 / __  / / / / /  / / /___   / /___/ /_/ / / / / / / / / / / /  __/ / / / /_   / /___/ / / /  __/ /__/ ,< /  __/ /
/_/ /_/ /_/ /_/  /_/_____/   \____/\____/_/ /_/ /_/_/ /_/ /_/\___/_/ /_/\__/   \____/_/ /_/\___/\___/_/|_|\___/_/     


	Written by Aksel Troan
	Github: https://github.com/AkselTroan"""

def main():
    if len(sys.argv) != 2:
        print(bcolors.FAIL + 'Usage: htmlCommentChecker.py websites.txt' + bcolors.ENDC)
        exit()

    f = open(sys.argv[1], "r")
    web_page = f.readlines()
    clear()
    print(bcolors.OKGREEN + bcolors.welcome + bcolors.ENDC)
    for page in web_page:
        print("")
        
        print(bcolors.HEADER + f"Checking {page}" + bcolors.ENDC)
        r = requests.get(page.replace("\n", ""))
        text = r.text.splitlines()
        for line in text:
            if line.__contains__('<!--') or line.__contains__('-->'):
                print(line)
        print("")

if __name__ == "__main__":
    main()