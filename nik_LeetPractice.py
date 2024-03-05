#Leetcode Practice
import src.Library.datastructures as struct
import src.Library.linked_list_prob as llprob
import src.Library.misc_prob as mprob
import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("nikLeet")
top_label = tk.Label(root, text="LeetCode Problem Types:")
top_label.pack(pady=10, padx=200)
# Create a Listbox
listbox = tk.Listbox(root, selectmode=tk.SINGLE)  # Use tk.MULTIPLE for multiple selections
listbox.pack(pady=10)

# Insert items into the Listbox along with corresponding functions
item_function_mapping = {
    "Miscellaneous": mprob.miscProbSelect,
    "Linked List": llprob.linkedListProbSelect
}

for item in item_function_mapping:
    listbox.insert(tk.END, item)

# Create a button to execute the selected item's function
def on_button_click():
    selected_index = listbox.curselection()
    if selected_index:
        selected_item = listbox.get(selected_index)
        selected_function = item_function_mapping.get(selected_item)
        if selected_function:
            selected_function(result_label)
            top_label.pack_forget()
            listbox.pack_forget()
            button.pack_forget()
            back_Button.pack(pady=10)

    else:
        result_label.config(text="No item selected")

def on_backbutton_click():
    top_label.pack(pady=10, padx=200)       
    listbox.pack(pady=10)       
    button.pack(pady=10)
    back_Button.forget()
    result_label.config(text="",pady=10)



button = tk.Button(root, text="Select Library", command=on_button_click)
button.pack(pady=10)

back_Button = tk.Button(root, text="Back", command=on_backbutton_click)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()