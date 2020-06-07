#! /usr/bin/python3


# portscanner.py - IWarboys - June 2020

# import socket module for network functionality
import socket

# import re module to use regular expressions for validating user input
import re

# import sys module to provide exit method for error handling
import sys


# function to obtain and validate ipv4 address from user
def get_address():
    
    # prompt user for ipv4 address and store string in variable called address
    address = input("Please enter the IPv4 address of the target host: ")
    print()
    
    # test if input string matches a regular expression which represents the format of a valid ipv4 address
    # if no match, the body of while loop executes to prompt the user until a correctly formatted address is provided
    while not re.match("^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$", address):    
        address = input("Please enter a valid IPv4 address (example: 192.168.0.10): ")
        print()
        
    # return the validated address(string)
    return address


# function to let user decide whether to scan all ports or only well-known ports
def get_ports():
    print("Enter w to scan only well-known ports: 0 - 1023 (default)")
    print("Enter a to scan all ports: 0 - 65535")
    print()
    
    # initialise variable: max_port to default value for last port to be scanned
    max_port = 1023
    
    # prompt user for input choice
    port_choice = input("Enter w or a: ")
    
    # check if user chose to scan all ports
    if port_choice in ["a","A"]:
        
        # if so store last port number in max_port
        max_port = 65535
        
    # return the required value for the last port (integer)
    return max_port


# function to perform port scan, takes 2 arguments:
# ip_address (string) and last_port (integer)
def scan_ports(ip_address, last_port):    
    print()
    print("*" * 65)
    print()
    print("Scanning host:", ip_address)
    print("TCP Ports: 0 -", last_port)
    print()
    print("*" * 65)
    print()
    
    # use try to handle connection errors
    try:
        # Loop through required port range, add 1 to last_port so it is included
        for port in range(0, last_port + 1):
            
                # create a stream socket and store in variable: s
                # socket family: AF_INET for IPv4 addresses
                # soket type: SOCK_STREAM for TCP connections
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
                # connect to ip address:port combination and store result in variable: result
                result = s.connect_ex((ip_address, port))
                
                # test if result = 0 which would indicate that port is open
                if result == 0:
                    
                    # if port is open: output to indicate that port is open
                    print("Port", port, "is open")
                
                # close connection
                s.close()
        print()
        print("Scan completed.")
        print()
    
    # on address related error: output message and exit    
    except socket.gaierror:
        print("\nHostname could not be resolved.")
        sys.exit()
     
    # on socket connection error: output message and exit    
    except socket.error:
        print("\nCould  not connect to server")
        sys.exit()
    
    # if user presses ctrl-c: output message and exit    
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
        sys.exit()


# Output welcome notice and description for users

print()
print("*"*65)
print()
print("                    Welcome to PortScanner")
print()
print()
print()
print("      This program scans for open TCP ports on a network host. ")
print()
print()
print("      Tip: to test on local machine use IP address 127.0.0.1")
print()
print()
print()
print("         Please only scan ports on a network host if you ")
print("                    are authorised to do so!")
print()
print("*"*65)
print()

# Program flow:

# call get_address to obtain ip address from user and store in string variable: ip_address
ip_address = get_address() 

# call get_ports to obtain choice of last port from user and store in integer variable: last_port
last_port = get_ports()

# call scan_ports, with arguments ip_address and last_port obtained from user, to perform the port scan
scan_ports(ip_address, last_port)

# End of program