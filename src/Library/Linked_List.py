import tkinter as tk
from tkinter import messagebox



#Add two numbers problem
def addTwoNumbers(top_label):
    top_label.config(text="Function for the Linked_List problem 'Add Two Numbers' executed.",pady=10, padx=200)    
    return


def mergeTwoLists(top_label):
    top_label.config(text="Function for the Linked_List problem 'Merge Two Lists' executed.",pady=10, padx=200)    
    return





def probSelect(listbox, top_label):
    top_label.config(text="Choose a linked list problem")
    # Insert problems into the Listbox along with corresponding functions
    listbox.delete(0,tk.END)
    for item in problem_mapping:
        listbox.insert(tk.END, item)





problem_mapping = {
    "Add Two Numbers": addTwoNumbers,
    "Merge Two Lists": mergeTwoLists
    }    
