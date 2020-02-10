#!/usr/bin/python3

import socket
import sys

try:
	def helper():
		print ("""
			Knocker v1.0 
		Created by: CR4CKB0X (Praman Kasliwal)

  Knocker : A python based tool to perform port knocking.
  Port Knocking: A method through which a person tries to identify all the open ports of a system from 1 to 65535

  Usage: knocker [-o output_file] -t ip_address
			
  Example:
		knocker -t 192.168.23.158
		knocker -o open_ports.txt -t 192.168.23.158

  For help: knocker -h

  -o\t(Optional) Sets an output file to list out the open ports into
  -t\t(Mandatory) Sets target IP Address
  -d\t(Optional) Set target using domain name
  -h\tDisplays this help message\n
			""")

	def knock(ip, filename=None):
		print ("IP Address: "+ip, end="\n")
		#print ("Open Ports:")
		try:
			for port in range(1,65536):
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				if not(sock.connect_ex((ip, port))):
					if (filename == None):
						print(port, end="\n")
					else:
						file = open(filename, "a+")
						print (port, file)
						file.close()
				sock.close()			
		except:
			sys.exit("[!] Error in Socket Establishment...")
		print ("\nKnocking complete...")
		if (filename != None):
			print ("Data saved in file: ", file.name())
		exit()


	def main(arg):
		if len(arg) < 1:
			sys.exit ("Usage: knocker [-o output_file] -t ip_address\nExample: knocker -o open_ports.txt -t 192.168.23.158\nFor help: knocker -h\n")
		#print (''.join(argv))
		filename = None
		ip = None
		flag = 0
		for i in range(len(arg)):
			if (arg[i] == "-t"):
				flag += 1
				ip = arg[i+1]
			elif (arg[i] == "-d"):
				flag += 1
				ip = socket.gethostbyname(arg[i+1])
			elif (arg[i] == "-o"):
				filename = arg[i+1]
			elif arg[i] == "-h":
				helper()
				exit(1)
		if flag == 0:
			print ("Error: Missing target (-t)")
			sys.exit ("Usage: knocker [-o output_file] -t ip_address\nExample: knocker -o open_ports.txt -t 192.168.23.158\n")
		elif flag == 2:
			sys.exit ("Error: Enter either '-t' or '-d', both must not be given. \n")
		knock (ip, filename)

		exit()

except KeyboardInterrupt:
	sys.exit ("[*] Keyboard Interrupt detected...\nExiting the program")
	#exit(1)


if __name__ == "__main__":
	try:
		main(sys.argv[1:])
	except KeyboardInterrupt:
		sys.exit ("[*] Keyboard Interrupt detected...\nExiting the program")
