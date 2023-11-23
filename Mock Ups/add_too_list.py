# mock up file for what it will look like to add items to the return list in the computer application

#imports
import tkinter
from tkinter import ttk

#global vars, lists, ect
main_root = tkinter.Tk()

elements = {
    "stock_number":
    [ttk.Label(main_root, text = "Stock No#"), ttk.Entry(main_root)],
    "tag_number":
    [ttk.Label(main_root, text = "Tag No#"), ttk.Entry(main_root),
     ttk.Checkbutton(main_root, text = "No Tag No#")],
    "side":
    [ttk.Label(main_root, text = "Side of Vehicle"), ttk.Checkbutton(main_root, text = "Left/Driver"),
     ttk.Checkbutton(main_root, text = "Right/Passanger"), ttk.Checkbutton(main_root, text = "Front"),
     ttk.Checkbutton(main_root, text = "Rear"), ttk.Checkbutton(main_root, text = "Back")],
    "part_name":
    [ttk.Label(main_root,text = "Part Name"), ttk.Entry(main_root)],
    "current_location":
    [ttk.Label(main_root,text = "Current Location"), ttk.Entry(main_root),
     ttk.Radiobutton(main_root, text = "Incoming outside"), ttk.Radiobutton(main_root, text = "Incoming inside"),
     ttk.Radiobutton(main_root, text = "On dock"), ttk.Radiobutton(main_root, text = "BedBox area"),
     ttk.Radiobutton(main_root, text = "Will-Call"), ttk.Radiobutton(main_root, text = "Return Shelf")],
    "return_location":
    [ttk.Label(main_root,text = "Return To"), ttk.Entry(main_root),
     ttk.Checkbutton(main_root, text = "Warehouse")],
    "rma_number":
    [ttk.Label(main_root,text = "RMA No#"), ttk.Entry(main_root),
     ttk.Checkbutton(main_root, text = "No RMA")],
    "reason":
    [ttk.Label(main_root, text = "Reason"), ttk.Entry(main_root), ttk.Radiobutton(main_root, text = "Cancelled"),
     ttk.Radiobutton(main_root, text = "Damaged"), ttk.Radiobutton(main_root, text = "Ordered Wrong"),
     ttk.Radiobutton(main_root, text = "Parts Puller Error"), ttk.Radiobutton(main_root, text = "Pulled off Part")],
    "Notes":
    [ttk.Label(main_root,text = "Notes"), ttk.Entry(main_root)],
    "submit":
    [ttk.Button(main_root,text = "Add Part to Return List")]
}

#Funcitons 

#classes
class Part_Return:
    def __init__(self,name,relocate,location,rma,note):
        self.name = name
        self.relocate = relocate
        self.location = location
        self.rma = rma
        self.note = note

#Set up block
main_root.title("Add Part To Return List")
main_root.geometry("800x400")
main_root.grid()
#submit_button.config(command = login_func)

for row_num, line in enumerate(elements):
    for column_num, widgit in enumerate(elements[line]):
        widgit.grid(column = column_num, row = row_num)


#Run block
main_root.mainloop()
