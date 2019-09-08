# Knocker v1.0

## Basic Information
<strong>Knocker</strong>: A python based tool to perform <b>port knocking</b>.<br>
<strong>Port Knocking</strong>: A method through which a person tries to identify all the open ports of a system from 1 to 65535.<br>

## Usage
  `$ python3 knocker [-o output_file] -t ip_address`
			
  Example:<br>
		`$ python3 knocker -t 192.168.23.158`<br>
		`$ python3 knocker -o open_ports.txt -t 192.168.23.158`<br>
		`$ python3 knocker -d example.com`<br>

  For help: knocker -h<br>
  -o --> (Optional) Sets an output file to list out the open ports into<br>
  -t --> (Mandatory if -d not used) Sets target IP Address<br>
  -d --> (Mandatory if -t not used) Sets target from domain name instead of IP Address <br>
  -h --> Displays this help message<br>

## Credits
	Created by: CR4CKB0X (Praman Kasliwal)
