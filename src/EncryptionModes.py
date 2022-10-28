#from XOR import *
from Key import *
import numpy as np
from Block import *


def CBCdecrypt(CT,Key,IV):
    F = Factory()
    Key = Keyh(Key)
    IVBlock = BlockAES(IV)
    for i in range(0,int(len(CT)/16)):
        B = F.getObject('AES',CT[16*i:16*i+16])
        IVn = BlockAES(B.ListData())
        B.decrypt(Key)
        B.XOR(IVBlock.getData())
        IVBlock = IVn
        yield B.ListData()


def ECBdecrypt(CT,Key):
    F = Factory()
    Key = Keyh(Key)
    for i in range(0,int(len(CT)/16)):
        B = F.getObject('AES',(CT[16*i:16*i+16])) 
        B.decrypt(Key)
        yield B.ListData()


def CBCencrypt(Data,Key,IV):                           #This is higher level than encrypt as it uses cipher block chaining
    F = Factory()
    Key = Keyh(Key)
    IVBlock = F.getObject('AES',IV)
    for i in range(0,int(len(Data)/16)):
        B = F.getObject('AES',(Data[16*i:16*i+16]))                                  
        B.XOR(IVBlock.getData())                                     
        B.encrypt(Key)                                      
        IVBlock = B                                    #Bad as IVBlock refers to the object 'B', saved by creating a new object B at the next loop iteration
        yield B.ListData()                        



def ECBencrypt(Data,Key):
    F = Factory()
    Key = Keyh(Key)
    for i in range(0,int(len(Data)/16)):
        B = F.getObject('AES',(Data[16*i:16*i+16]))
        B.encrypt(Key)
        yield B.ListData()



#def OFBEncrypt(Data,Key,IV):
#    IVBlock = BlockAES(IV)
#    Key = Keyh(Key)
#    for i in range(0,int(len(Data)/16)):
#        B = BlockAES(Data[16*i:16*i+16])
#        IVBlock.encrypt(Key)
#        B.XOR(IVBlock.getData())
#        yield B.ListData()


#def CFBEncrypt(Data,Key,IV):
#    IVBlock = BlockAES(IV)
#
#    Key = Keyh(Key)
#    for i in range(0,int(len(Data)/16)):
#        B = BlockAES(Data[16*i:16*i+16])
#        IVBlock.encrypt(Key)
#        B.XOR(IVBlock.getData())
#        IVBlock = B
#        yield B.ListData()
