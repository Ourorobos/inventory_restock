# mock up file for what it will look like to add items to the return list in the computer application

#imports
import tkinter
from tkinter import ttk

#global vars, lists, ect
memory = []

main_root = tkinter.Tk()

name_label = ttk.Label(main_root,text = "Part Name")
relocate_label = ttk.Label(main_root,text = "Return To")
location_label = ttk.Label(main_root,text = "Current Location")
rma_label = ttk.Label(main_root,text = "RMA No#")
note_label = ttk.Label(main_root,text = "Notes")

name_entry = ttk.Entry(main_root)
relocate_entry = ttk.Entry(main_root)
location_entry = ttk.Entry(main_root)
rma_entry = ttk.Entry(main_root)
note_entry = ttk.Entry(main_root)

submit_button = ttk.Button(main_root,text = "Add Part to Return List")

#Funcitons
def add_to_memory():
    memory.append(
        Part_Return(
            name_entry.get(),relocate_entry.get(),location_entry.get(),rma_entry.get(),note_entry.get()
        )
    )    

#classes
class Part_Return:
    def __init__(self,name,relocate,location,rma,note):
        self.name = name
        self.relocate = relocate
        self.location = location
        self.rma = rma
        self.note = note

#Set up block
main_root.title("Login")
main_root.geometry("300x300")
#submit_button.config(command = login_func)

name_label.pack()
name_entry.pack()
relocate_label.pack()
relocate_entry.pack()
location_label.pack()
location_entry.pack()
rma_label.pack()
rma_entry.pack()
note_label.pack()
note_entry.pack()
submit_button.pack()


#Run block
main_root.mainloop()
