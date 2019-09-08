#!/usr/bin/python3

import os
import sys

def main():
	if not os.geteuid() == 0:
    	sys.exit("""\033[1;91m\n[!] Knocker installer must be run as root. ¯\_(ツ)_/¯\n\033[1;m""")
    else:
    	print ("Welcome to Knocker! Please be patient while knocker installs... It will hardly take a moment to install...", end="\n")
    	install = os.system("""sudo chmod +x knocker.py && sudo mkdir /usr/bin/knocker && sudo cp knocker.py /usr/bin/knocker/knocker && tput setaf 34; echo "Knocker has been sucessfuly installed. Execute 'knocker -h' to understand the working." """)

if __name__ == "__main__":
	main()