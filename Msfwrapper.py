#Varibles/Imports
import os
from colorama import Fore, Back, Style
import subprocess

#Main Script
#Varibles
pastPackets = ()

#allowable operating systems
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
  
