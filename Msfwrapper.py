#Varibles/Imports
import os
from colorama import Fore, Back, Style
import subprocess

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
  global packetSearch
  os.system('cls' if os.name == 'nt' else "printf '\033c'")
  print(Fore.RED + "Payload Creation:")
  print("Welcome, to allow for easier creation of your payload we will run you through some questions limiting to what is best suited for your needs then allowing you to pick from a more directed list of packets.")
  print()
  print("   (   If unkown press enter to skip question   )")
  print()

  #OS Question 1
  print("   Question 1:  What is the targeted operating system? ")
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
 

#Main Execution Program
if userInput == "C" or userInput == "c":
    createPayload()

print(str(packetSearch))

