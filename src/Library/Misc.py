import tkinter as tk
from tkinter import messagebox



def twoSum(result_label):
    result_label.config(text="Function for the miscellaneous problem 'Two Sum' executed.",pady=10, padx=200)
    return()




def probSelect(listbox, top_label, result_label):
    result_label.config(text="Function for miscellaneous problems executed.",pady=10, padx=200)
    top_label.config(text="Choose a misc. problem")
    # Insert problems into the Listbox along with corresponding functions
    listbox.delete(0,tk.END)
    for item in problem_mapping:
        listbox.insert(tk.END, item)




problem_mapping = {
    "Two Sum": twoSum
    }    