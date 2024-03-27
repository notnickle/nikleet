import tkinter as tk
from tkinter import messagebox
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys #Allows Control of Browser Keystrokes
from selenium.webdriver.support.select import Select 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrapeProb(url):

    problem = ''
    #Import Firefox Driver
    driver = webdriver.Firefox()  
    driver.get(url)

    descript_div = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
            "//div[@class='elfjS']")))
    problem = descript_div.text
    driver.close()
    return problem


def open_prob(root, paragraph_text):
    # Create new window for problem
    new_window = tk.Toplevel(root)
    new_window.title("New Window")

    # Create a label and text box for display
    output_label = tk.Label(new_window, text=paragraph_text, justify="left")
    output_label.grid(row=0, column=0, padx=5, pady=5)

    output_text = tk.Text(new_window, height=25, width=30)
    output_text.grid(row=0, column=1, padx=5, pady=5)


def twoSum2(top_label, root, name):
    top_label.config(text="Function for the miscellaneous problem 'Two Sum 2' executed.",pady=10, padx=200)

    paragraph_text = scrapeProb(grab_problem_url_by_name(name))

    open_prob(root, paragraph_text)

    return


def twoSum(top_label, root, name):
    top_label.config(text="Function for the miscellaneous problem 'Two Sum' executed.",pady=10, padx=200)

    # Grab Problem Text
    file_path = f"src/Library/misc.txt" 
    paragraph_text = open_paragraph_by_name(file_path, name)

    open_prob(root, paragraph_text)

    return

def open_paragraph_by_name(file_path, name):
    with open(file_path, "r") as file:
        content = file.read()

    # Split the corntent into paragaphs based on the delimiter ":"
    paragraphs = content.split("\n\n")  # Assuming double newline as delimiter

    # Iterate through the paragraphs to find the one with the matching name
    for paragraph in paragraphs:
        lines = paragraph.split("\n")
        paragraph_name = lines[0].strip()[:-1]  # Remove the colon at the end
        if paragraph_name == name:
            # Return the paragraph text without the name
            return "\n".join(lines[1:]).strip()

    # If the name is not found, return None or raise an exception
    return None

def grab_problem_url_by_name(name):

    with open("src/Library/prob_urls.txt", "r") as file:
        content = file.read()

    # Split the corntent into paragaphs based on the delimiter ":"
    paragraphs = content.split("\n\n")  # Assuming double newline as delimiter

    # Iterate through the paragraphs to find the one with the matching name
    for paragraph in paragraphs:
        lines = paragraph.split("\n")
        paragraph_name = lines[0].strip()[:-1]  # Remove the colon at the end
        if paragraph_name == name:
            # Return the paragraph text without the name
            return "\n".join(lines[1:]).strip()

    # If the name is not found, return None or raise an exception
    return None


def probSelect(listbox, top_label):
    top_label.config(text="Choose a misc. problem")
    # Insert problems into the Listbox along with corresponding functions
    listbox.delete(0,tk.END)
    for item in problem_mapping:
        listbox.insert(tk.END, item)




problem_mapping = {
    "Two Sum": twoSum,
    "Two Sum 2":twoSum2
    }    