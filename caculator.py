import socket, sys, subprocess, os

def CustomIP():
    global input2
    global IP
    global Loopback
    global prefix
    global ClassNum
    global Subnetmask
    global SubnetmaskList
    global NOH
    global Subnet
    global Slist
    global IPlist
    global Broadcast
    global x
    input2 = (input('Insert IP address: '))# user needs to insert a custom ip address 
    IP = input2.split('/')[0]
    Loopback = IP.split(".")[0]
    prefix = int(input2.split('/')[-1])
    ClassNum = ["A", "B", "C", "D", "E"] # A list over the classes that are in use in IPv4 
    SubnetmaskList = ["0.0.0.0","128.0.0.0","192.0.0.0","224.0.0.0","240.0.0.0","248.0.0.0","252.0.0.0","254.0.0.0","255.0.0.0",
    "255.128.0.0","255.192.0.0","255.224.0.0","255.240.0.0","255.248.0.0","255.252.0.0","255.254.0.0","255.255.0.0",
    "255.255.128.0","255.255.192.0","255.255.224.0","255.255.240.0","255.255.248.0","255.255.252.0","255.255.254.0","255.255.255.0",
    "255.255.255.128","255.255.255.192","255.255.255.224","255.255.255.240","255.255.255.248","255.255.255.252","255.255.255.254","255.255.255.255"]
    Subnetmask = SubnetmaskList[prefix]
    os.system("cls")
    print('================================')
    print('IP: ' + IP)
    print('Subnetmask:', Subnetmask)
    print('Prefix:',prefix)
    if prefix not in range(0, 5): # checks which class the input are in
        if prefix not in range(5, 8):
            if prefix not in range(8, 16) or Loopback == "127":
                if not Loopback == "127" and prefix != "8":
                    if prefix not in range(16, 24):
                        if prefix not in range (24, 33):
                            x = "not valid"
                        else:
                            x = ClassNum[2]
                    else:
                        x = ClassNum[1]
                else:        
                    x = ClassNum[0]
                    print("Loopback Address")
            else:
                x = ClassNum[0]
        else:
            x = 'Undefind'
    else:
        x = ClassNum[3]
    print('Class:', x)

    NOH=[32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
    print("Number of IP's:","{:,}".format(2**NOH[prefix]))
    print("Number of Hosts:","{:,}".format(2**NOH[prefix]-2))
    Subnet = ".".join(map(str, [i & m for i,m in zip(map(int, IP.split(".")), map(int, Subnetmask.split(".")))]))
    Slist = Subnetmask.split(".")
    IPlist = IP.split(".")
    for i in range(0, len(IPlist)):IPlist[i] = int(IPlist[i])
    for i in range(0, len(Slist)):Slist[i] = int(Slist[i])
    Broadcast = [(IPlist[i] & Slist[i]) | (255^Slist[i]) for i in range(4)]
    print("Subnet ID:",Subnet)
    print("Broadcast address: {0}".format('.'.join(map(str, Broadcast))))
    print('================================')
    SaveToServer()

def SaveToServer():
    SaveInput = input('Do you wanna save this?: ')
    if SaveInput == 'y':
        my_file = open("IPOutput.txt","w+")
        my_file.write('================================\n')
        my_file.write('IP: ' + IP+'\n')
        my_file.write('Subnetmask: '+Subnetmask+'\n')
        my_file.write('Prefix: '+str(prefix)+'\n')
        my_file.write('Class: '+x+'\n')
        my_file.write("Number of IP's: "+"{:,}".format(2**NOH[prefix])+'\n')
        my_file.write("Number of Hosts: "+"{:,}".format(2**NOH[prefix]-2)+'\n')
        my_file.write("Subnet ID: "+Subnet+'\n')
        my_file.write("Broadcast address: {0}".format('.'.join(map(str, Broadcast)))+'\n')
        my_file.write('================================')
    else:
        return()

def DefaultIP():
    hName = socket.gethostname()
    IPaddress = socket.gethostbyname(hName)
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