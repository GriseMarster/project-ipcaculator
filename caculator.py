import socket, sys, subprocess
from turtle import clear
from typing import ContextManager



while True:
    ipAdressing = input('\n' 'Wanna see the computers IP(1)\nSet a custom IP(2)\nQuit(3): ')

    # takes the output of "ipa" and if it's 1 it finds the computers details like it's name and ip address.
    # needs to add more later
    if ipAdressing == '1':
        hName = socket.gethostname()
        IPaddress = socket.gethostbyname(hName)
        Class_conveter = (IPaddress[:3])
        BClass = int(Class_conveter)

        print('\n''Host Name is: ' + hName)
        print('Computer IP Address is: ' + IPaddress)
        
        if BClass in range(1, 126, 1):
            print('Class is: A')
        
        elif BClass in range(128, 191, 1):
            print('Class is: B')

        elif BClass in range(192, 223, 1):
            print('Class is: C')
        
        elif BClass in range(224, 239, 1):
            print('Class is: D')

        elif BClass in range(240, 255, 1):
            print('Class is: E')
        
        else:
          print("Not at correct ip")
          continue


    # takes the output of "ipa" and if it's 2 it tries to show the subnet, subnet mask, brodcast ip, id address, classes. 
    elif ipAdressing == '2':
        # user enters the ip address here, and if there is added a subnet it needs to take that in consiterration
        
        input2 = (input('Insert IP address: '))# user needs to insert a custom ip address
        Class_conveter = (input2[:3])
        BClass = int(Class_conveter)
        IPB = input2.split('.')
        
        # Checks the users input to see what class the ip-address is under.
        print('Your IP is: ' + input2)
        if BClass in range(1, 126, 1):
            print('Class is: A')
            print(IPB)

        elif BClass in range(128, 191, 1):
            print('Class is: B')
            print(IPB)
            
        elif BClass in range(192, 223, 1):
            print('Class is: C')
            print(IPB)

        elif BClass in range(224, 239, 1):
            print('Class is: D')
            print(IPB)

        elif BClass in range(240, 255, 1):
            print('Class is: E')
            print(IPB)

        else:
          print("Not an correct ip")
          continue

    elif ipAdressing == 'secret word':
        x = input('what do you wanna do?: ')
        subprocess.run(x)
    
    elif ipAdressing == '3':
        print('Quitting...')
        break

    else:
        # if the user doesn't chosses between 1, 2 or 3 they will get and error that they have to chosse a correct number
        print('\n' 'incorrect number, you need to chosse between 1 to 3.')
        continue






    


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