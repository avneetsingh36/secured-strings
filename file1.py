# This program is intended to collect a user password and keep it safely in another file --> this will resemble a mini computer network
# This network will attempt to use the OSI reference model layered architecture

import math, sys
from file2 import receptionOfInfo

#Important Variables
user_password = ''
manipulated_Pass = ''
more_encrypted_pass = ''

def toBinary(a):
    l,m = [], []
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m

#LAYER 1: Application Layer

def collectPassword(): 
    global user_password
    user_password = input("\nEnter the password (preferably one that uses numbers, letters and chars) that you would like to use: ")

#LAYER 2: Presentation Layer

def hidePassword(password):
    global manipulated_Pass
    passes = 0
    passes5x = 0
    for i in password:
        passes += 1
        passes5x += 5
        if i.isnumeric():
            i = int(i) 
            manipulated_Pass = manipulated_Pass + str(round(pow(i,(5/3))))
        elif i.isalpha():
            i = int(ord(i)) + round(pow((passes-1),3/2))
            if i > 122:
                i = i - 26
            manipulated_Pass = manipulated_Pass + chr(i) 
        else:
            i = int(ord(i)) + round(math.gamma(math.asinh(passes5x)))
            if i > 47:
                i = i - 15
            manipulated_Pass = manipulated_Pass + chr(i)
    return manipulated_Pass

#LAYER 3: Session Layer
#This is a simplex system in which the computer will interact with the intermediary node to establish a conctection

def establishCommunication():
    with open('/path/to/intermediaryNode.txt', mode='w', encoding= 'utf-8') as f:
        f.write("Connection Established")
        print("\nWrote to file.")
    with open('/path/to/intermediaryNode.txt', encoding= 'utf-8') as f:
        print("Connection status:")
        print(f.read())
    with open('/path/to/intermediaryNode.txt', 'r+') as f:
        f.truncate(0)
        print("\nConnection Testing was cleared from the file.\n")

#LAYER 4: Transport Layer

def checkSize():
    global manipulated_Pass, more_encrypted_pass
    more_encrypted_pass = toBinary(manipulated_Pass)
    pass_size = sys.getsizeof(more_encrypted_pass)
    if  pass_size > 10000:
        print("Your file does meet the size requirement to break up the information and then send it!")
    else:
        print("Your file does not meet the size requirement to break up the information and then send it!")

#LAYER 5: Network Layer

def checkRouting():
    print("This Computer Network only has one logical path, so we will transmit the data via this path!")

#LAYER 6: Data Link Layer

def info():
    print("You are in luck - we are working in the constraints of a wired connnected network system, so we will be sending the data now efficiently!\n")

def transmissionToNode():
    global more_encrypted_pass
    with open('/path/to/intermediaryNode.txt', mode='w', encoding= 'utf-8') as m:
        m.write(f'Encrypted pass in Binary: {more_encrypted_pass}')
        print("\nEncryped password has been sent to the intermediary node.")

#LAYER 7: Physical Layer
def mediaAspect():
    print("\nThe type of media used was text media.")
    print("The synchronization of bits and data was a success!")
    print("The information was computed using a line structure of communcation using a simplex mode.\n")
    
def destinationNodeAccessesInfo(): 
    receptionOfInfo()
    #recap of what is happening here is in file2.py if you would like to see the final transmission of bits over the medium we have established


#THIS IS THE DATA EXECUTION LAYER

collectPassword()
hidePassword(user_password)
establishCommunication()
checkSize()
checkRouting()
info()
transmissionToNode()
mediaAspect()
destinationNodeAccessesInfo()







#DATA SENT TO FILE: Prolly would use SQL to create a DB rather than trying to make a DB from scratch in python - thoughts?