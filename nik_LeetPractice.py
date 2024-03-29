#Leetcode Practice
import src.Library.datastructures as struct
import src.Library.Linked_List as linked_list
import src.Library.Misc as misc
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font


# Create the main window
root = tk.Tk()
root.title("nikLeet")
icon = tk.PhotoImage(file = "nikleet.png")
root.iconphoto(False, icon)
custom_font = font.Font(family="Comic Sans MS", size = 18, weight="bold")
mode = ''


# Create a button to execute the selected item's function
def on_m1button_click():
    global mode
    selected_index = listbox.curselection()
    if selected_index:
        selected_item = listbox.get(selected_index)
        mode = str(selected_item)
        selected_library = main_item_function_mapping.get(selected_item)
        if selected_library:
            back_Button.pack(side=tk.LEFT, pady=5)
            selected_library(listbox, top_label)
            forget_m1()   
            m2_button.pack(pady=10)

    else:
        result_label.config(text="No item selected")

# Create a button to execute the selected item's function
def on_m2button_click():
    global mode
    if mode.lower() == 'misc':
        selected_index = listbox.curselection()
        if selected_index:
            selected_item = listbox.get(selected_index)
            selected_library = misc.problem_mapping.get(selected_item)
            if selected_library:
                forget_m2()
                selected_library(top_label, root, selected_item)

    elif mode.lower() == 'linked_list':
        selected_index = listbox.curselection()
        if selected_index:
            selected_item = listbox.get(selected_index)
            selected_library = linked_list.problem_mapping.get(selected_item)
            if selected_library:
                forget_m2() 
                selected_library(top_label)
    else:
        result_label.config(text="No item selected")

# Create a button to execute back_Button's desired function
def on_backbutton_click():
    back_Button.forget()
    m2_button.forget()
    result_label.forget()
    listbox.forget()
    top_label.pack(pady=10, padx=200)       
    listbox.pack(pady=10)       
    result_label.pack(pady=10)
    m1_button.pack(pady=10)

    top_label.config(text="LeetCode Problem Types:")
    result_label.config(text="")

    listbox.delete(0,tk.END)
    for item in main_item_function_mapping:
        listbox.insert(tk.END, item)

def forget_m1():
    m1_button.forget()
    
def forget_m2():
    m2_button.forget()
    listbox.forget()
    result_label.forget()


# Create Top Text
top_label = tk.Label(root, text="LeetCode Problem Types:", font=custom_font)
top_label.pack(pady=10, padx=200)

# Create a Listbox
listbox = tk.Listbox(root, selectmode=tk.SINGLE)  # Use tk.MULTIPLE for multiple selections
listbox.pack(pady=10)

# Insert items into the Listbox along with corresponding functions
main_item_function_mapping = {
    "Misc": misc.probSelect,
    "Linked_List": linked_list.probSelect
}
for item in main_item_function_mapping:
    listbox.insert(tk.END, item)



# Main Menu Button
m1_button = tk.Button(root, text="Select Library", command=on_m1button_click)
m1_button.pack(pady=10)

m2_button = tk.Button(root, text="Select Problem", command=on_m2button_click)

# Label to display the result
result_label = tk.Label(root, text="")

# Widgets that appear after selecting a Library appear below
back_Button = tk.Button(root, text="Back", command=on_backbutton_click)

#Text Box for Problems
prob_textwidget = tk.Text(root, height=10, width=30)

# Start the GUI event loop
root.mainloop()