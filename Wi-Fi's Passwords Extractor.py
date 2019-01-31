#!/bin/python
# Wi-Fi's Password Extractor
# Version v1
# Coded by: Othmane Moutaouakkil [ WHOAMI2507 ]  (You don't become a coder by just changing the credits)
# Github: https://github.com/whoami2507


import subprocess

print('''
 __        ______  _____ 
 \ \      / /  _ \| ____|
  \ \ /\ / /| |_) |  _|  
   \ V  V / |  __/| |___ 
    \_/\_/  |_|   |_____|

 Written by: WHOAMI2507
''' + '\n'*2)


data=subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles=[i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results=subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results=[b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print("{:<21}| {:<}".format(i, results[0]))
    except IndexError:
        print("{:<21}| {:<}".format(i, ""))
input('')
