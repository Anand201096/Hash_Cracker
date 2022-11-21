import hashlib
import pyfiglet

from cfonts import render
from termcolor import colored

banner = render("Hash_Cracker", colors=['blue', 'yellow'], align='center')
print(banner)

print(colored('[!] Warning: Enter valid hash algorithm', 'red'))

print("======================================================")

cred='Coded by:--> @AnandGurav'
print(colored(cred,'red'))
lang='GitHub:--> Anand201096'
print(colored(lang,'red'))
print("======================================================")


wordlist_location = str(input(colored('[+] Enter wordlist file location: ', 'green')))
hash_input = str(input(colored('[+] Enter hash to be cracked: ', 'green')))

input1 = str(input(colored('[+] Enter hash type: ', 'green'))) 

if "md5" in input1:
    hash_o = hashlib.md5
elif "sha512" in input1:
    hash_o = hashlib.sha512
else:
    print('\n')
    print(colored('[*] Enter Valid Hash Algorithm....', 'red'))
    exit()

with open(wordlist_location, 'r') as file:
    for line in file.readlines():
        hash_ob = hash_o(line.strip().encode())
        hashed_pass = hash_ob.hexdigest()
        if hashed_pass == hash_input:
            print(colored('\n [+] Found cleartext password: ', 'green') + line.strip())
            exit(0)
        else:
            print(colored('\n [-] Invalid cleartext password: ', 'red') + line.strip())


