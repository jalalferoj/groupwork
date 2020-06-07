#! /usr/bin/python3

# bannergrabber.py - IWarboys - June 2020

# import socket module for network functionality
import socket

# import re module to use regular expressions for validating user input
import re


# function to obtain and validate ipv4 address from user
def get_address():
    
    # prompt user for ipv4 address and store string in variable called address
    address = input("Please enter the IPv4 address of the target host: ")
    print()
    
    # test if input string matches a regular expression which represents the format of a valid ipv4 address
    # if no match, the body of the while loop executes to prompt the user until a correctly formatted address is provided
    while not re.match("^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$", address):    
        address = input("Please enter a valid IPv4 address (example: 192.168.0.10): ")
        print()
        
    # return the validated address (string)
    return address

# function to obtain and validate list of ports from user
def get_ports():
    
    # initialise an empty list to hold the requested port numbers
    req_ports = []
    
    # initialise a variable to an arbitrary string value, will use this for user input
    port = "x"
    
    print("Please enter requested TCP port numbers one by one.")
    print("Port numbers can be in the range 0 - 65535.")
    print("Enter blank or single space to finish.")
    
    # check if the port variable contains one of the escape values, if not the body of while loop executes
    # the while loop will execute at least once because of the initial value of the variable: port
    while port not in ["", " "]:
        
        # prompt user for input, store string in variable: port
        port = input("Port number: ")
        
        # test if variable: port is not set to an escape value before continuing
        # if port contains an escape value the program returns to while loop, which will not execute
        if port not in ["", " "]:
            
            try:
                # attempt to cast the variable: port as an integer
                port = int(port)
            
            except:
                # if port cannot be cast as an integer print error message, returns to while loop
                print(port, "is not a valid port number: not an integer")
            
            else:
                # port cast successfully as integer, first check if it is out of range
                if port < 0 or port > 65535:
                    
                    # print error message if port is out of range, returns to while loop
                    print(port, "is not a valid port number: not in range 0 - 65535")              
                
                else:
                    # if port is in range, check if value is already in the list to prevent duplicates
                    if port not in req_ports:
                        
                        #if port is in range and not already in list - append port to list, return to while loop
                        req_ports.append(port)
    
    # return the validated list of ports  (list of integers)            
    return req_ports

# function to perform scanning, takes arguments ip_address (string) and port_list (list of integers)
def scan_ports(ip_address, port_list):
    
    # output host address and seleceted port numbers
    print()
    print("*" * 65)
    print()
    print("Scanning host:", ip_address)
    print("Ports:", port_list)
    print()
    print("*" * 65)
    print()
    
    #loop through each port number in the list
    for port in port_list:

        # create a new socket and store in variable: s
        s = socket.socket()

        try:
            #attempt to make a connection to the supplied ip address and current port number
            s.connect((ip_address,  port))
        
        except:
            # if attempt to connect fails - output error message, continue with for loop
            print("Port", port, ": Could not connect.\n")
        
        else:
            # if connection is successful: use recv method to read 1024 bytes of data from socket,
            # use the decode method to convert bytes to utf-8 character set, store in variable: banner. 
            banner = (s.recv(1024)).decode("utf-8")
            
            # output the banner information
            print("Port", port, ":", banner)
            
            # close the connection
            s.close
            
    print("Scanning complete.")
    print()
    return
      

# Output welcome notice and description for users

print()
print("*"*65)
print()
print("                    Welcome to BannerGrabber")
print()
print()
print("   This program uses 'banner grabbing' to obtain information on ")
print(" applications or services running on TCP ports on a network host.")
print()
print()
print("      Tip: to test on local machine use IP address 127.0.0.1")
print()
print("      Useful ports to try: 20, 21 (FTP)" )
print("                           22 (SSH)")
print("                           23 (Telnet)")
print("                           25 (SMTP)")
print("                           80 (HTTP)")
print("                          110 (POP3)")
print()
print()
print("         Please only scan ports on a network host if you ")
print("                    are authorised to do so!")
print()
print("*"*65)
print()

# Program flow:

# call get_address to obtain ip address from user and assign to variable ip_address
ip_address = get_address() 

# call get_ports to obtain list of ports from user and assign to variable port_list
port_list = get_ports()

# call scan_ports with ip_address and port_list obtained from user
scan_ports(ip_address, port_list)

# End of program
     

