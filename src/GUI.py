import tkinter as tk   
import tkinter.ttk as ttk
from tkinter.filedialog import *
import os

class GUI:
    def __init__(self,master):

        self.master = master
        master.wm_title("AES256")
        self.fileName = "File.txt"                     
        self.mode = 0
        self.inputFormat= 0
        self.outputFormat = 0


        ################################################################################
        #Combo Boxes for selecting Mode and Input Data format
        ################################################################################

        self.lMode = tk.Label(master,text="Mode:")
        self.lMode.grid(row = 1,column = 0)

        self.comboMode = ttk.Combobox(master,values = ["ECB","CBC"])
        self.comboMode.grid(row = 1,column =1,columnspan=2)
        self.comboMode.current(0)
        self.comboMode.bind("<<ComboboxSelected>>",self.selectMode)

        self.lInput = tk.Label(master,text="Input Format")
        self.lInput.grid(row = 2,column = 0)

        self.comboInput = ttk.Combobox(master,values = ["HEX","Text"])
        self.comboInput.grid(row = 2,column =1,columnspan=2)
        self.comboInput.current(0)
        self.comboInput.bind("<<ComboboxSelected>>",self.selectFormatInput)

        self.lOutput = tk.Label(master,text="Output Format")
        self.lOutput.grid(row = 3,column = 0)

        self.comboOutput = ttk.Combobox(master,values = ["HEX","Text"])
        self.comboOutput.grid(row = 3,column =1,columnspan=2)
        self.comboOutput.current(0)
        self.comboOutput.bind("<<ComboboxSelected>>",self.selectFormatOutput)

        self.lAlgorithm = tk.Label(master,text="Algorithm")
        self.lAlgorithm.grid(row = 0, column = 0)

        self.comboAlgorithm = ttk.Combobox(master,values = ["AES256","DES"])
        self.comboAlgorithm.grid(row = 0,column=1,columnspan=2)
        self.comboAlgorithm.current(0)

        ################################################################################
        #Buttons for Encrypt and Decrypt Functions/ Input File selection
        ################################################################################

        #Encrypt Button
        self.encryptButton = tk.Button(master,text="Encrypt",command=self.encryptButton, bg="#222222", fg="#DDDDDD")
        self.encryptButton.grid(row = 4,column=1)

        #Decrypt Button
        self.decryptButton = tk.Button(master,text="Decrypt",command=self.decryptButton, bg="#222222", fg="#DDDDDD")
        self.decryptButton.grid(row = 4,column=2)

        #FileSelect Button
        self.fileSelectButton = tk.Button(master,text="Select Input File",command = self.selectFile)
        self.fileSelectButton.grid(row=4,column=0)

        #Show Current File
        self.fileDisplay = tk.Label(master, text = self.fileName[-15:],wraplength=50)
        self.fileDisplay.grid(row=5,column=0)
        


    #Cipher Mode Select and Set
    def selectMode(self,event):
        self.mode = self.comboMode.current()
       
    #Set input format variable
    def selectFormatInput(self,event):
        self.inputFormat = self.comboInput.current()

    #Set input format variable
    def selectFormatOutput(self,event):
        self.outputFormat = self.comboOutput.current()
    
    #Encrypt
    def encryptButton(self):
        print("Encrypting...\n")
        Top_Level.encrypt(self.fileName,self.mode,self.InputF,self.OutputF)
        
    
    #Decrypt
    def decryptButton(self):
        print("Decrypting...\n")
        Top_Level.decrypt(self.fileName,self.mode,self.InputF,self.OutputF)

    #Set Selected File
    def selectFile(self):
        tempdir = askopenfilename(initialdir=os.getcwd(), title='Please select a directory')
        print(tempdir)
        self.fileName = tempdir
        self.fileDisplay.configure(text=self.fileName[-15:])
        self.fileDisplay.update()

    def mainLoop(self):
        self.master.mainloop()
        




def main():
    top = tk.Tk()
    gui = GUI(top)
    gui.mainLoop()

if __name__ == '__main__':
    main()



