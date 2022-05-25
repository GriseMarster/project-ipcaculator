from msilib.schema import Class
import socket, sys, subprocess, os


hName = socket.gethostname()
IPaddress = socket.gethostbyname(hName)

def CustomIP():
    input2 = (input('Insert IP address: '))# user needs to insert a custom ip address 
    IP = input2.split('/')[0]
    Loopback = IP.split(".")[0]
    prefix = int(input2.split('/')[-1])
    ClassNum = ["A", "B", "C", "D", "E"] # A list over the classes that are in use in IPv4 
    SubnetmaskList = ["0.0.0.0","128.0.0.0","192.0.0.0","224.0.0.0","240.0.0.0","248.0.0.0","252.0.0.0","254.0.0.0","255.0.0.0",
    "255.128.0.0","255.192.0.0","255.224.0.0","255.240.0.0","255.248.0.0","255.252.0.0","255.254.0.0","255.255.0.0",
    "255.255.128.0","255.255.192.0","255.255.224.0","255.255.240.0","255.255.248.0","255.255.252.0","255.255.254.0","255.255.255.0",
    "255.255.255.128","255.255.255.192","255.255.255.224","255.255.255.240","255.255.255.248","255.255.255.252","255.255.255.254","255.255.255.255"]
    
    os.system("cls")
    print('================================')
    print('IP: ' + IP)
    print('Subnetmask:', SubnetmaskList[prefix])
    print('Prefix:',prefix)
    if prefix not in range(0, 4): # checks which class the input are in
        if prefix not in range(5, 7):
            if prefix not in range(8, 15) or Loopback == "127":
                if Loopback != "127" and prefix != "8":
                    if prefix not in range(16, 23):
                        if prefix not in range (24, 32):
                            print("Class: not valid")
                        else:
                            print('Class:',ClassNum[2])
                    else:
                        print("Class:",ClassNum[1])
                else:        
                    print("Class:",ClassNum[0])
                    print("Loopback Address")
            else:
                print("Class:",ClassNum[0])
        else:
            print("Class: Undefind")
    else:
        print("Class:",ClassNum[3])
    NOH=[32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
    print("Number of IP's:","{:,}".format(2**NOH[prefix]))
    print("Number of Hosts:","{:,}".format(2**NOH[prefix]-2))
    print('================================')
    


def DefaultIP():
    Class_conveter = (IPaddress[:3])
    BClass = int(Class_conveter)

    print('\n''Host Name is: ' + hName)
    print('Computer IP Address is: ' + IPaddress)
        
    if BClass in range(1, 126, 1):
        print('Class is: A')
        return()

    elif BClass in range(128, 191, 1):
        print('Class is: B')
        return()

    elif BClass in range(192, 223, 1):
        print('Class is: C')
        return()

    elif BClass in range(224, 239, 1):
        print('Class is: D')
        return()

    elif BClass in range(240, 255, 1):
        print('Class is: E')
        return()
        
    else:
        print("Not at correct ip")
        return()


def Startup():
    ipAdressing = input('\n' 'Wanna see the computers IP(1)\nSet a custom IP(2)\nQuit(3): ')

    if ipAdressing == '1':
        DefaultIP()

    # takes the output of "IPAddressing" and if it's 2 it tries to show the subnet, subnet mask, brodcast ip, id address, classes. 
    elif ipAdressing == '2':
        CustomIP()
        # user enters the ip address here, and if there is added a subnet, it needs to take that in consiterration
        
    elif ipAdressing == 'secret word':
        x = input('what do you wanna do?: ')
        subprocess.run(x)
    
    elif ipAdressing == '3':
        print('Quitting...')
        return()

    else:
        # if the user doesn't chosses between 1, 2 or 3 they will get and error that they have to chosse a correct number
        print('\n' 'incorrect number, you need to chosse between 1 to 3.')
        return()
Startup()


    


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