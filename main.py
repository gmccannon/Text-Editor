import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog


# Function to open a file
def open_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        text.delete('1.0', tk.END)
        text.insert(tk.END, file.read())


# Function to save a file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt')
    with open(file_path, 'w') as file:
        file.write(text.get('1.0', tk.END))


# Function to find and replace
def find_and_replace():
    search_term = simpledialog.askstring("Find and Replace", "Find:")
    if search_term:
        replacement = simpledialog.askstring("Find and Replace", f"Replace '{search_term}' with:")
        if replacement:
            text.replace("1.0", tk.END, text.get("1.0", tk.END).replace(search_term, replacement))


# Main window
root = tk.Tk()
root.title("Text Editor")

# text area
text = tk.Text(root, font=("Helvetica", 22))
text.pack(fill=tk.BOTH, expand=True)

# Menu bar
menu = tk.Menu(root)
root.config(menu=menu)

# File menu
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit menu
edit_menu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Find and Replace", command=find_and_replace)

# Start the main loop
root.mainloop()
