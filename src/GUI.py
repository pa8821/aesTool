from tkinter import *   
from tkinter.ttk import *
import Top_Level
from tkinter.filedialog import *
import os

class GUI:
    def __init__(self,master):

        self.fileName = "TextFile1.txt"                     
        self.Mode = 0
        self.InputF= 0
        self.OutputF = 0


        ################################################################################
        #Combo Boxes for selecting Mode and Input Data format
        ################################################################################

        self.l1 = Label(master,text="Mode:")
        self.l1.grid(row = 1,column = 0)

        self.combo = Combobox(master,values = ["ECB","CBC","OFB","CFB"])
        self.combo.grid(row = 1,column =1,columnspan=2)
        self.combo.current(0)
        self.combo.bind("<<ComboboxSelected>>",self.selectMode)

        self.l2 = Label(master,text="Input Format")
        self.l2.grid(row = 2,column = 0)

        self.combo2 = Combobox(master,values = ["HEX","Text"])
        self.combo2.grid(row = 2,column =1,columnspan=2)
        self.combo2.current(0)
        self.combo2.bind("<<ComboboxSelected>>",self.selectFormat)

        self.l3 = Label(master,text="Output Format")
        self.l3.grid(row = 3,column = 0)

        self.combo3 = Combobox(master,values = ["HEX","Text"])
        self.combo3.grid(row = 3,column =1,columnspan=2)
        self.combo3.current(0)
        self.combo3.bind("<<ComboboxSelected>>",self.selectFormatOutput)

        self.l4 = Label(master,text="Algorithm")
        self.l4.grid(row = 0, column = 0)

        self.combo4 = Combobox(master,values = ["AES256","DES","..."])
        self.combo4.grid(row = 0,column=1,columnspan=2)
        self.combo4.current(0)

        ################################################################################
        #Buttons for Encrypt and Decrypt Functions/ Input File selection
        ################################################################################

        #Encrypt Button
        self.enbutton = Button(master,text="Encrypt",command=self.encryptButton,bg='green')
        self.enbutton.grid(row = 4,column=1)

        #Decrypt Button
        self.debutton = Button(master,text="Decrypt",command=self.decryptButton,bg='red')
        self.debutton.grid(row = 4,column=2)

        #FileSelect Button
        self.fFileSelect = Button(master,text="Select Input File",command = self.selectFile)
        self.fFileSelect.grid(row=4,column=0)

        #Show Current File
        self.filedisplay = Label(master, text = self.fileName[-15:],wraplength=50)
        self.filedisplay.grid(row=5,column=0)
        


    #Cipher Mode Select and Set
    def selectMode(self,event):
        self.Mode = self.combo.current()
       
    #Set input format variable
    def selectFormat(self,event):
        self.InputF = self.combo2.current()

    #Set input format variable
    def selectFormatOutput(self,event):
        self.OutputF = self.combo3.current()
    
    #Encrypt
    def encryptButton(self):
        print("Encrypting...\n")
        Top_Level.encrypt(self.fileName,self.Mode,self.InputF,self.OutputF)
        
    
    #Decrypt
    def decryptButton(self):
        print("Decrypting...\n")
        Top_Level.decrypt(self.fileName,self.Mode,self.InputF,self.OutputF)

    #Set Selected File
    def selectFile(self):
        tempdir = askopenfilename(initialdir=os.getcwd(), title='Please select a directory')
        print(tempdir)
        self.fileName = tempdir
        self.filedisplay.configure(text=self.fileName[-15:])
        self.filedisplay.update()
        




def main():
    top = Tk()
    e = GUI(top)
    top.wm_title ("Crypto Check")
    top.mainloop()

    
    

if __name__ == '__main__':
    main()



