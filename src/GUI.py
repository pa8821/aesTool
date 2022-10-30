import tkinter as tk   
import tkinter.ttk as ttk
from tkinter.filedialog import *
import MainEncryptDecrypt
from FormatEnum import *
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
        self.encryptButton = tk.Button(master,text="Encrypt",command=self.encryptButton, bg="#222222", fg="#DDDDDD", activebackground="#BB0099")
        self.encryptButton.grid(row = 9,column=1)

        #Decrypt Button
        self.decryptButton = tk.Button(master,text="Decrypt",command=self.decryptButton, bg="#222222", fg="#DDDDDD")
        self.decryptButton.grid(row = 9,column=2)

        # #FileSelect Button
        # self.fileSelectButton = tk.Button(master,text="Select Input File",command = self.selectFile)
        # self.fileSelectButton.grid(row=8,column=0)

        # #Show Current File
        # self.fileDisplay = tk.Label(master, text = self.fileName[-15:],wraplength=50)
        # self.fileDisplay.grid(row=9,column=0)
        


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
    
    #Encrypt
    def encryptButton(self):
        print("Encrypting...\n")
        text = self.plainEntry.get()
        key  = self.keyEntry.get()
        iV   = self.IVEntry.get()
        instance = MainEncryptDecrypt.Encrypt_Decrypt_Class()
        output = instance.encrypt(text,key,iV, self.mode, self.inputFormat, self.outputFormat)
        self.outputDisplay.delete(0,len(self.outputDisplay.get()))
        self.outputDisplay.insert(0,output)
        
    
    #Decrypt
    def decryptButton(self):
        print("Decrypting...\n")
        MainEncryptDecrypt.decrypt()

    # #Set Selected File
    # def selectFile(self):
    #     tempdir = askopenfilename(initialdir=os.getcwd(), title='Please select a directory')
    #     print(tempdir)
    #     self.fileName = tempdir
    #     self.fileDisplay.configure(text=self.fileName[-15:])
    #     self.fileDisplay.update()

    def mainLoop(self):
        self.master.mainloop()
        




def main():
    top = tk.Tk()
    gui = GUI(top)
    gui.mainLoop()

if __name__ == '__main__':
    main()



