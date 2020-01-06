'''
Created on 10 Aug 2019

@author: apple
'''
from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

class Window(Frame):

    
    def __init__(self, master=None):
        self.initFile()
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()
        
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        selectedItem = tk.Label(self,text = 'Sound Setting:')
        selectedItem.grid(column=0, row=1)
        # placing the button on my window
        global number
        number =tk.StringVar()
        global numberChosen
        numberChosen = ttk.Combobox(self, width=12, textvariable=number)
        #numberChosen.config(command = self.loadButton)
        settingKey = list(settingList.keys())
        numberChosen['values'] = settingKey   
        numberChosen.grid(column=1, row=1)      
        numberChosen.bind("<<ComboboxSelected>>", self.loadButton)

        newName = tk.Label(self,text = 'New Name:')
        newName.grid(column=0, row=2)
        global entryVar
        entryVar = tk.StringVar()
        global e1
        e1=Entry(self,textvariable = entryVar)
        e1.grid(column=1,row=2)
        e1.config(state='disabled')
        
        global labelVar
        labelVar = tk.StringVar
        l1 = Label(self)
        
        global music1S
        music1S = tk.StringVar()
        global music1
        music1 = ttk.Combobox(self,width=12,textvariable=music1S)
        music1["value"]=soundList
        music1.grid(column=1,row=3)
        music1.bind("<<ComboboxSelected>>", self.chooseMusic)
        
        global music2S
        music2S = tk.StringVar()
        global music2
        music2 = ttk.Combobox(self,width=12,textvariable=music2S)
        music2["value"]=soundList
        music2.grid(column=1,row=4)
        music2.bind("<<ComboboxSelected>>", self.chooseMusic)
       

        numberChosen.current(settingKey.index(lastUsed))
        music1.current(settingList[lastUsed][0])
        music2.current(settingList[lastUsed][1])
        

        # button that save the setting 
        global saveButton
        saveButton = Button(self, text="Save")
        saveButton.config(command=self.saveButton)
        saveButton.grid(column=2,row=1)
        saveButton.config(state='disabled')

        #button that apply the setting
        # button that save the setting 
        applyButton = Button(self, text="Apply&Close")
        applyButton.config(command=self.save)
        applyButton.grid(column=3,row=1)
        
         
    def saveButton(self):
        #checkname
        a = entryVar.get()
        if number.get() == 'new':
            if a == '':
                tkinter.messagebox.showinfo("Title", "please Input Title")
            if a in soundList:
                tkinter.messagebox.showinfo("Title", "Title name already exist, please get a new one")
            else:
                b=int(soundList.index(music1S.get()))
                c=int(soundList.index(music2S.get()))
                settingList[a] = (b,c)
                numberChosen['values'] = list(settingList.keys())    
                numberChosen.current(list(settingList.keys()).index(a))
                #write it to file
                writeStr = "\n"+a+" "+str(b)+" "+str(c) 
                print(writeStr)
                #print(settingList.items())
                outFile = open("save","a")
                outFile.write(writeStr)
                outFile.close()
                tkinter.messagebox.showinfo("Title", "Setting is saved.")
                e1.delete(0,END)
        else:
            pass

    #when selected, the combobox should show as new/(empty) and play music
    #new should can be save in memory
    def chooseMusic(self,self2):
        numberChosen.current(list(settingList.keys()).index("new"))
        settingList["new"] = (int(soundList.index(music1S.get())),int(soundList.index(music2S.get())))
    
    #save the whole system and exit
    def save(self):
        self.saveButton()
        settingList["new"] = (0,0)
        #first line is a list of music can choose
        lastUsed = number.get()
        writeString = ''
        for item in range(len(soundList)):
            writeString = writeString + soundList[item] + " "
        writeString += "\n"
          
        #second line is the last choice
        writeString += lastUsed 
        #print writeString
        #others are the mode arraylist
        for items in settingList:
            writeString +=  "\n"+ items + " "
            for y in range(len(settingList[items])):
                writeString += str(settingList[items][y]) + " "
            
        print(writeString)
        
        outFile = open("save","w")
        outFile.write(writeString)
        outFile.close()
        
        exit()
        
    def labelforNew(self):
        numberChosen.current(list(settingList.keys()).index("new"))
        

    def loadButton(event,event2):
        a = number.get()
        print((settingList[a]))
        music1.current(settingList[a][0])
        music2.current(settingList[a][1])
        if a == "new":
             e1.config(state='normal')
             saveButton.config(state='normal')
        else:
             e1.config(state= 'disable')
             saveButton.config(state='disable')
        
        
    def initFile(self):
        infile = open("save","r")
        #first line of file is choices of sound track  
        global soundList
        global settingList
        global lastUsed
        settingList = {}
        #read sound for selection
        soundList = infile.readline().split()
        for word in soundList:
            print(word)
        #read LastUsed sound
        lastUsed = infile.readline().rstrip()
        print(lastUsed)
        #read setting that is saved
        for line in infile:
            line=line.rstrip()
            word = line.split()
            settingList[word[0]] = (int(word[1]),int(word[2]))
            
            
        print(settingList)
        infile.close()
        
        #set the current to last used
        
            
root = tk.Tk()
root.geometry("400x300")

app = Window(root)
root.mainloop()
