# Knocker
A port knocking code, written in python3
# Information
        ***Knocker v1.0***
		Created by: CR4CKB0X (Praman Kasliwal)

  Knocker : A python based tool to perform port knocking.
  Port Knocking: A method through which a person tries to identify all the open ports of a system from 1 to 65535
# Usage
  `$ knocker [-o output_file] -t ip_address`
			
  Example:
		`$ knocker -t 192.168.23.158`
		`$ knocker -o open_ports.txt -t 192.168.23.158`

  For help: knocker -h

  -o  (Optional) Sets an output file to list out the open ports into
  -t  (Mandatory) Sets target IP Address
  -h  Displays this help message\n
