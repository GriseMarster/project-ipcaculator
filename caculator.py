import socket, sys, subprocess
from typing import ContextManager



while True:
    ipa = input('\n' 'Wanna see the computers IP(1)\nSet a custom IP(2)\nQuit(3): ')

    # takes the output of "ipa" and if it's 1 it finds the computers details like it's name and ip address.
    # needs to add more later
    if ipa == '1':
        hName = socket.gethostname()
        IPaddress = socket.gethostbyname(hName)
        print('\n''Host Name is: ' + hName)
        print('Computer IP Address is: ' + IPaddress)
        print()
        break

    # takes the output of "ipa" and if it's 2 it tries to show the subnet, subnet mask, brodcast ip, id address, classes. 
    elif ipa == '2':
        # user enters the ip address here, and if there is added a subnet it needs to take that in consiterration
        input2 = (input('Insert IP address: '))# user needs to insert a custom ip address
        
        class IPCaculator(object):
            def
        
    elif ipa == 'secret word':
        x = input('what do you wanna do?: ')
        subprocess.run(x)
    
    elif ipa == '3':
        print('Quitting...')
        break

    else:
        # if the user doesn't chosses between 1 or 2 they will get and error that they have to chosse between 1 and 2
        print('\n' 'incorrect number, you need to chosse between 1 to 3.')







    


#Ip class A
#1 to 126 1.0.0.0 to 126.255.255.255
#subnet mask 255.0.0.0


#Loopback class
#127.0.0.1 - 127.255.255.255
#subnet mask 255.0.0.0

#Ip class B
#128 to 191 128.0.0.0 to 191.255.255.255
#subnet mask 255.255.0.0

#ip class C
#192 to 223 192.0.0.0 to 223.255.255.255
#subnet mask 255.255.255.0