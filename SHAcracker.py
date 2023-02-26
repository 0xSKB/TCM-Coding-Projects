#!/bin/python3

from pwn import *
import sys

# This function actually does all the heavy lifting
#################################################
def crack_this(p_hash, pass_list):
    # initialize a variable to keep track of the attempts
    attempts = 0
    # This will log the pregress as process p
    with log.progress(f"Attempting to reverse password: {p_hash}!") as p:
        # This will loop through the list created from from word_list_open as pass_list
        for passwrd in pass_list:
            # This strips any spaces and encodes the in latin-1
            passwrd = passwrd.strip('\n').encode('latin-1')
            # Hashes the passwrd in sha256 hex then stores it in the variable hasher
            hasher = sha256sumhex(passwrd)
            p.status(f"[{attempts}] {passwrd.decode('latin-1')} == {hasher}")
            # if the condition is met then it will print a success message along with the hashed password in clear text. Then exit the program
            if hasher == p_hash:
                p.success(f"Password hash found after {attempts} attempts! {p_hash} hashes to {passwrd.decode('latin-1')}!")
                exit()
            attempts += 1
        # If there is not success then a failure message will be printed
        p.failure("Password hash not found!")
##################################################


# This opens the text file and runs a loop to strip
# the \n off the password in the list and then returns a new list to iterate over.
#################################################
def word_list_open(list):
    p_list = []
    with open(f'{list}', 'r') as n_list:
        for item in n_list:
            item = item.strip('\n')
            p_list.append(item)
    n_list.close()
    return p_list
#################################################

# Gets text file input from user then pumps it into the word list function.
#################################################
text_file = input("Text file please: ")
password_list = word_list_open(text_file.strip())
#################################################
hash_this_please = input("Please input a hash to crack: ")
hash_this_please = hash_this_please.strip()
################################################

crack_this(hash_this_please, password_list)
