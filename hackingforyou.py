from getpass import getpass
import os
from os import system
import time
from time import sleep
LR = '\033[0;31m'
LL = '\033[0;37m'
L = "\033[0;94m"
print (L +'Hello c-4150')
A = input (LL +'UesrName: ')
B = getpass(LL +'Password: ')
if A == 'c-4150' and B == '******':
   print (LL +'Welcome back mister '+A)

else:
   system('clear')
   exit()

C = input (LL +'Do you want to enter the secure network now: ')
def mice():
    print (' ______________________________________________________________________________')
    print ('|                                                                              |')
    print ('|                          Enter uesr and Password                             |')
    print ('|______________________________________________________________________________|')
    print ('|                                                                              |')
    print ('|                                                                              |')
    print ('|                                                                              |')
    print ('|                 UserName:           [ C-4150 ]                               |')
    print ('|                                                                              |')
    print ('|                 Password:           [ ****** ]                               |')
    print ('|                                                                              |')
    print ('|                                                                              |')
    print ('|                                                                              |')
    print ('|                                   [ OK ]                                     |')
    print ('|______________________________________________________________________________|')
    print ('|                                                                              |')
    print ('|                                                                              |')
    print ('|______________________________________________________________________________|')
mice()

if C == 'y':
   print (mice)

else:
   system('clear')
   exit()

print (LL +'You have been logged into the secure network Please wait for the download')
H = input (LR +'y/n: ')

def U():
    print ('10%')
    time.sleep(4)
    print ('20%')
    time.sleep(9)
    print ('30%')
    time.sleep(5)
    print ('44%')
    time.sleep(8)
    print ('60%')
    time.sleep(7)
    print ('87%')
    time.sleep(6)
    print ('99%')
    time.sleep(4)
    print ('100%')
    print ('Done..')
U()

if H == 'y':
   print (U)

else:
   system('clear')
   exit()


