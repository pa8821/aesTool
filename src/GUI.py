from distutils.log import error
import tkinter as tk   
import tkinter.ttk as ttk
from tkinter.filedialog import *
from tkinter import messagebox
import MainEncryptDecrypt
from FormatEnum import *
from functools import partial
import os

class GUI:
    def __init__(self,master):

        self.master = master
        master.wm_title("AES256")                   
        self.mode = CipherMode.ECB
        self.inputFormat= Format.hexadecimal
        self.outputFormat = Format.hexadecimal

        ################################################################################
        #Combo Boxes for selecting Mode and Input Data format
        ################################################################################

        self.lMode = tk.Label(master,text="Mode:", anchor= "w")
        self.lMode.grid(row = 1,column = 0)

        self.comboMode = ttk.Combobox(master,values = ["ECB","CBC"])
        self.comboMode.grid(row = 1,column =1,columnspan=2)
        self.comboMode.current(0)
        self.comboMode.bind("<<ComboboxSelected>>",self.selectMode)

        self.lInput = tk.Label(master,text="Input Format:")
        self.lInput.grid(row = 2,column = 0)

        self.comboInput = ttk.Combobox(master,values = ["HEX","Text"])
        self.comboInput.grid(row = 2,column =1,columnspan=2)
        self.comboInput.current(0)
        self.comboInput.bind("<<ComboboxSelected>>",self.selectFormatInput)

        self.lOutput = tk.Label(master,text="Output Format:")
        self.lOutput.grid(row = 3,column = 0)

        self.comboOutput = ttk.Combobox(master,values = ["HEX","Text"])
        self.comboOutput.grid(row = 3,column =1,columnspan=2, pady=(0,12))
        self.comboOutput.current(0)
        self.comboOutput.bind("<<ComboboxSelected>>",self.selectFormatOutput)

        self.lAlgorithm = tk.Label(master,text="Algorithm:")
        self.lAlgorithm.grid(row = 0, column = 0)

        self.comboAlgorithm = ttk.Combobox(master,values = ["AES256","DES"])
        self.comboAlgorithm.grid(row = 0,column=1,columnspan=2)
        self.comboAlgorithm.current(0)

        self.lEntry = tk.Label(master,text="Input:")
        self.lEntry.grid(row = 7, column = 0)
        self.plainEntry = tk.Entry(master, width=50)
        self.plainEntry.grid(row=7, column = 1, columnspan=2)

        self.lOutputLabel = tk.Label(master,text="Output:")
        self.lOutputLabel.grid(row = 8, column = 0)
        self.outputDisplay = tk.Entry(master, width=50)
        self.outputDisplay.grid(row=8, column = 1, columnspan=2)

        self.lKey = tk.Label(master,text="Key:")
        self.lKey.grid(row = 5, column = 0)
        self.keyEntry = tk.Entry(master, width=50)
        self.keyEntry.grid(row=5, column = 1, columnspan=2)

        self.lIV = tk.Label(master,text="IV:")
        self.lIV.grid(row = 6, column = 0)
        self.IVEntry = tk.Entry(master, width=50)
        self.IVEntry.grid(row=6, column = 1, columnspan=2)

        ################################################################################
        #Buttons for Encrypt and Decrypt Functions/ Input File selection
        ################################################################################

        #Encrypt Button
        self.encryptButton = tk.Button(master,text="Encrypt",width = 20, command=partial(self.encryptDecryptCommon, True), bg="#22EE80", fg="#000000", activebackground="#BB0099")
        self.encryptButton.grid(row = 9,column=1)

        #Decrypt Button
        self.decryptButton = tk.Button(master,text="Decrypt",width = 20, command=partial(self.encryptDecryptCommon, False), bg="#E80E80", fg="#DDDDDD")
        self.decryptButton.grid(row = 9,column=2)
        


    #Cipher Mode Select and Set
    def selectMode(self,event):
        mode = self.comboMode.current()
        self.mode = CipherMode.ECB if mode == 0 else CipherMode.CBC
       
    #Set input format variable
    def selectFormatInput(self,event):
        selectedFormat = self.comboInput.current()
        self.inputFormat = Format.hexadecimal if selectedFormat == 0 else Format.ascii

    #Set input format variable
    def selectFormatOutput(self,event):
        selectedFormat = self.comboOutput.current()
        self.outputFormat = Format.hexadecimal if selectedFormat == 0 else Format.ascii

    def encryptDecryptCommon(self, encrypt=True):
        text = self.plainEntry.get()
        key  = self.keyEntry.get()
        iV   = self.IVEntry.get()

        if((self.inputFormat == Format.hexadecimal and len(key) != 64) or (self.inputFormat == Format.ascii and len(key) != 32)):
            messagebox.showerror("Error", "Incorrect Key length. Key must be 32 Bytes")

        if(len(text)==0):
            messagebox.showerror("Error", "Input length must be at least 1 byte")

        else:
            instance = MainEncryptDecrypt.Encrypt_Decrypt_Class()
            output = instance.encrypt(text,key,iV, self.mode, self.inputFormat, self.outputFormat) if encrypt else instance.decrypt(text,key,iV, self.mode, self.inputFormat, self.outputFormat)
            self.outputDisplay.delete(0,len(self.outputDisplay.get()))
            self.outputDisplay.insert(0,output)



    def mainLoop(self):
        self.master.mainloop()
        




def main():
    top = tk.Tk()
    gui = GUI(top)
    gui.mainLoop()

if __name__ == '__main__':
    main()



