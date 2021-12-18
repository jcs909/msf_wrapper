#!/usr/bin/env python3                # specify the interpreter


### IMPORT STATEMENTS ###
import sys  # import the sys library
import subprocess


### HELPER FUNCTIONS ###
def is_even(file):  # define our line printing function

    for line in file:  # loop through every line in the file

        line = line.rstrip()  # remove the trailing newlines

        for nums in line:  # loop through each line

            print(nums)  # print each word


### MAIN FUNCTION ###
def main():  # define a main function

    file_to_open = sys.argv[1]  # get the file name from the cmd line

    opened_file = open(file_to_open)  # open the file

    is_even(opened_file)  # call our print words function with the open file

    opened_file.close()  # close the file when done


### DUNDER CHECK ###
if __name__ == '__main__':  # dunder check
    main()  # call the main function
