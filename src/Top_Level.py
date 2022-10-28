import EncryptionModes
from Files import *
import numpy as np

#This is a comment

def main():                                                 #Main not used by GUI
    F = FileHandler("TextFile1.txt")
    Data = F.getData()
    Key = F.getKey()

    CT = EncryptionModes.ECBencrypt(Data,Key)          #Encrypt returns list of CT values for each block of data.
    Ciphertext = []
    txt = []
    for i in CT:                                            #Format output as string of HEX 
        print(i)
        for j in i:
            Ciphertext.append(j)
            


    PT = CBC.CBCdecrypt(Ciphertext,DK[1],DK[2])
    txt = [] 
    for i in PT:
        for j in i:
            temp = chr(int(j)).encode('utf-8').decode('utf-8')
            txt.append(temp)
        
        
    Plaintext = ''.join(txt)
    print(Plaintext)

   
def encrypt(FileName="TextFile1.txt",Mode=0,InputF=0,OutputF=0):
    F = FileHandler(FileName,InputF)
    Data = F.getData()
    Key = F.getKey()
    IV = F.getIV()

    if(Mode==0):
        CT = EncryptionModes.ECBencrypt(Data,Key)
    elif(Mode==1):
        CT = EncryptionModes.CBCencrypt(Data,Key,IV)
    elif(Mode==2):
        CT = EncryptionModes.OFBEncrypt(Data,Key,IV)
    elif(Mode==3):
        CT = EncryptionModes.CFBEncrypt(Data,Key,IV)
        
                                                                        #Encrypt returns list of CT values for each block of data.
    Ciphertext = []
    txt = []
    
    if OutputF==0:
        for i in CT:                                                    #Format output as string of HEX 
            for j in i:
                temp = hex(int(j))[2:]
                if len(temp)<2:
                    temp = '0'+ temp
                txt.append(temp)

    else:
        for i in CT:
            for j in i:
                temp = chr(int(j)).encode('utf-8').decode('utf-8')
                txt.append(temp)

    Cipher = ''.join(txt)
    print(Cipher)





def decrypt(FileName = "TextFile1.txt",Mode = 0, InputF = 0,OutputF=1):
    F = FileHandler(FileName,InputF)
    Data = F.getData()
    Key = F.getKey()
    IV = F.getIV()
    
    if(Mode==0):
        PT = EncryptionModes.ECBdecrypt(Data, Key)
    elif(Mode==1):
        PT = EncryptionModes.CBCdecrypt(Data,Key)
    else:
        print("OFB Mode")

    txt = [] 
    if OutputF==1:
        for i in PT:
            for j in i:
                temp = chr(int(j)).encode('utf-8').decode('utf-8')
                txt.append(temp)
    else:
        for i in PT:
            for j in i:
                temp = hex(int(j))[2:]
                if len(temp)<2:
                    temp = '0'+ temp
                txt.append(temp)


        
        
    Plaintext = ''.join(txt)
    print(Plaintext)
        


    

    
if __name__ == '__main__':
    main()
