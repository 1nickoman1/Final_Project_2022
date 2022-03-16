'''
Created on Mar 15, 2022

@author: 1526331
'''
#imports
from tkinter import *
from tkinter.ttk import *


# functions


if __name__ == '__main__':
    win = Tk()    
    win.title("Application")
    win.iconwindow('')
    win.geometry('500x500')
    win.config(bg='gray')
    win.minsize(200, 100)
    Username = StringVar()
    Password = StringVar()

    
    
    #frame
    frame_personal = Frame(win)
    frame_personal1 = Frame(win)
    
    
    
    
    #labels
    len_Username = Label(frame_personal,
                           text = "Username")
    len_Password = Label(frame_personal,
                           text = "Password")

    
    
    len_Username = Entry(frame_personal)
    len_Password = Entry(frame_personal)
    
    
    #buttons
    len_Login = Button(frame_personal,
                        text = "Login",
                        width = 8)
    
    #Textvarible
    len_Username_entry = Label(frame_personal,
                   textvariable = Username)
    len_Password_entry = Label(frame_personal,
                   textvariable = Password)

    #Buttons
    
    
    
    
    #grids
    len_Username.grid(row=1, column = 1)
    len_Username_entry.grid(row=2, column = 1)
    
    len_Password.grid(row=2, column = 0)
    len_Password_entry.grid(row=2, column = 1)
    
    
    len_Username.grid(row=0, column=0)
    len_Password.grid(row=0, column=2)
    #len_km.grid(row=2, column=0)

    frame_personal.grid(row=0, column= 0)
    frame_personal1.grid(row=1, column= 0)
    
    
    
    win.mainloop()