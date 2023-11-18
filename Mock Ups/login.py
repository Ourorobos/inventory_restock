# mock up file for the login window for the computer application

#imports
import tkinter
from tkinter import ttk

#global vars, lists, ect
memory_users = [["admin","tkinter","admin"], #this will be found on the server but in the form of user obj/class
                ["shipping","ship","editor"]]

login_root = tkinter.Tk()
name_label = ttk.Label(login_root,text = "User Name")
password_label = ttk.Label(login_root,text = "Password")
name_entry = ttk.Entry(login_root)
password_entry = ttk.Entry(login_root)
submit_button = ttk.Button(login_root,text = "Login")

#Funcitons
def login_func():
    user_name = name_entry.get()
    user_password = password_entry.get()
    for user in memory_users:
        if user[0] == user_name and user[1] == user_password:
            print("Wellcome")

#classes

#Set up block
login_root.title("Login")
login_root.geometry("300x150")
submit_button.config(command = login_func)

name_label.pack()
name_entry.pack()
password_label.pack()
password_entry.pack()
submit_button.pack()


#Run block
login_root.mainloop()
