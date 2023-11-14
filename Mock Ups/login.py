# mock up file for the login window for the computer application

#imports
import tkinter

#global vars, lists, ect
memory_users = [["admin","tkinter","admin"], #this will be found on the server
                ["shipping","ship","editor"]]

#classes
class user:

    def __init__(self,name,password,type):
        self.name = name
        self.password = password
        self.type = type

# !!!! main code block !!!!
