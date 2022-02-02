def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)
        
choose = input("Binary converter(1)\nDecimal converter(2)")

if choose == '1':
    input1 = input('binary here: ')
    binaryToDecimal(input1)
    


elif choose == '2':
    input2 = (input('Decimal here: '))
    deciconvert = int(input2)
    print(bin(deciconvert)[2:])
    