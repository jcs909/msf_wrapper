#Varibles/Imports
import os
from colorama import Fore, Back, Style
import subprocess
import socket

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
  #Find Local Host Automation
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("8.8.8.8", 80))
  ip_address = s.getsockname()[0]
  print(Fore.RED + "   Question 3: Is the IP below your current IP if yes please press enter if not please retype your LHOST in the command line? ")
  print("   IP: " + str(ip_address))
  print()
  OS = input(Fore.WHITE + "Command Line: ")

  #If Lhost wrong
  operatingSystem = ""
  while OS not in operatingSystem:
   os.system('cls' if os.name == 'nt' else "printf '\033c'")
   print(Fore.RED + " What is your LHost that you want?")
   print()
   OS = input(Fore.WHITE + "Command Line: ")
   ip_address = OS

  #Lport finder !!!
  print(Fore.RED + "   Question 4: What is your current local port? ")
  print("   IP: " + str(ip_address))
  print()
  OS = input(Fore.WHITE + "Command Line: ")
  lPort = OS

  #Is script for linux or windows?
  print(Fore.RED + "   Question 5: What format is the targeted machine? ")
  print("   Options: windows, linux")
  print()
  OS = input(Fore.WHITE + "Command Line: ")
  typeOfMachine = OS


def finlization():
  #Type of payload and naming payload
  print(Fore.RED + "   Question 6: Lastly what would you like to name your packet? ")
  print()
  OS = input(Fore.WHITE + "Command Line: ")
  namePacket = OS

 

#Main Execution Program
if userInput == "C" or userInput == "c":
    createPayload()

print()
print("Final Output")
print(str(packetFinal))
#Pick a Packet ( Grep first 10 command for later grep -m 10)

Lportnhost()
finlization()



