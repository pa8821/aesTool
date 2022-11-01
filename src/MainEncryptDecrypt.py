import enum
import EncryptionModes
import numpy as np
from FormatEnum import *


class Encrypt_Decrypt_Class:
    def __init__(self):
        pass

    def encrypt(self,inputData, inputKey, inputIV, Mode=CipherMode.ECB,InputFormat=Format.hexadecimal,OutputFormat=Format.hexadecimal):

        Data = self.stringToList(inputData, InputFormat)
        Key  = self.stringToList(inputKey, InputFormat)
        IV   = self.stringToList(inputIV, InputFormat)

        if(Mode==CipherMode.ECB):
            CT = EncryptionModes.ECBencrypt(Data,Key)
        elif(Mode==CipherMode.CBC):
            CT = EncryptionModes.CBCencrypt(Data,Key,IV)        
                                                                            
        txt = self.formatOutput(OutputFormat, CT)                                        #Format Cipher into Hex or Text based on OutputFormat. 
        Cipher = ''.join(txt)
        print(Cipher)
        return Cipher

    def decrypt(self,inputData, inputKey, inputIV, Mode=CipherMode.ECB,InputFormat=Format.hexadecimal,OutputFormat=Format.hexadecimal):
        Data = self.stringToList(inputData, InputFormat)
        Key  = self.stringToList(inputKey, InputFormat)
        IV   = self.stringToList(inputIV, InputFormat)

        if(Mode==CipherMode.ECB):
            PT = EncryptionModes.ECBdecrypt(Data,Key)
        elif(Mode==CipherMode.CBC):
            PT = EncryptionModes.CBCdecrypt(Data,Key,IV)        
                                                                            
        txt = self.formatOutput(OutputFormat, PT)                                        #Format Cipher into Hex or Text based on OutputFormat. 
        plaintext = ''.join(txt)
        print(plaintext)
        return plaintext


    #Take a string of input data and return a list of the bytes in that input data either in hex or ascii as indicated by inputFormat.
    def stringToList(self, string, inputFormat):
        if(inputFormat == Format.ascii):
            data = ''.join(string.encode('utf-8'))                                  #Data stored on 1st line of txt file, Key stored on 2nd Line, IV stored on 3rd Line
            d = list(data)
            d.pop()

        elif(inputFormat == Format.hexadecimal):
            d = []
            for i in range(0,len(string),2):
                temp = int(string[i:i+2],16)
                d.append(temp)

        #If data is not a multiple of  the 128 bit block size, then pad with zeroes. 
        while(len(d)%16!=0):                                                        
            d.append(0)

        return d

    #Format Output data as Hex or ASCII. 
    def formatOutput(self, OutputFormat, CT):
        txt = []
        if OutputFormat==Format.hexadecimal:                                            #Format output as string of HEX
            for i in CT:                                                     
                for j in i:
                    temp = hex(int(j))[2:]                                              #Cut off "0x" from the returned hex value
                    if len(temp)<2: 
                        temp = '0'+ temp                                                #If the hex value is a single digit, add a leading 0. 
                    txt.append(temp)

        else:                                                                           #
            for i in CT:
                for j in i:
                    temp = chr(int(j)).encode('utf-8').decode('utf-8')
                    txt.append(temp)
        return txt
        
        

