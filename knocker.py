#!/usr/bin/python3

import socket
import sys

try:
	def helper():
		print ("""
			Knocker v1.0 
		Created by: CR4CKB0X (Praman Kasliwal)

Knocker : A python based tool to perform port knocking.
Port Knocking: A method of reconnaissance through which a person tries to identify all the open ports of a system from 1 to 65535

Usage: knocker [-o output_file] -t ip_address
			
Example:
	knocker -t 192.168.23.158
	knocker -o open_ports.txt -t 192.168.23.158

For help: knocker -h

-o\t(Optional) Sets an output file to list out the open ports into
-t\t(Mandatory) Sets target IP Address
-h\tDisplays this help message\n
			""")

	def knock(ip, filename=None):
		print ("IP Address: "+ip, end="\n")
		#print ("Open Ports:")
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		for port in range(1,65536):
			if ~(sock.connect_ex((ip, port))):
				if (filename == None):
					print(port, end="\n")
				else:
					file = open(filename, "a+")
					print (port, file)
					file.close()
		print ("\nKnocking complete...")
		if (filename != None):
			print ("Data saved in file: ", file.name())
		exit(1)


	def main(arg):
		if len(arg) < 1:
			print ("Usage: knocker [-o output_file] -t ip_address\nExample: knocker -o open_ports.txt -t 192.168.23.158\nFor help: knocker -h\n")
			exit(1)
		#print (''.join(argv))
		if any("-h" for s in arg):
			helper()
			exit(1)
		if any("-t" for s in arg):
			ip = arg[arg.index["-t"]+1]
		else:
			print ("Error: Missing target (-t)")
			print ("Usage: knocker [-o output_file] -t ip_address\nExample: knocker -o open_ports.txt -t 192.168.23.158\n")
			exit(1)
		if any("-o" for s in arg):
			filename = arg[arg.index["-o"]+1]
		knock(ip , filename)
		exit(1)

except KeyboardInterrupt:
	print ("[*] Keyboard Interrupt detected...\nExiting the program", end="\n")
	exit(1)


if __name__ == "__main__":
	main(sys.argv[1:])