import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from menuFunctions import open_file, save_file, find_and_replace

# Main window
root = tk.Tk()
root.title("Text Editor")

# Text area
text = tk.Text(root, font=("Helvetica", 22))
text.pack(fill=tk.BOTH, expand=True)

# Menu bar
menu = tk.Menu(root)
root.config(menu=menu)

# File menu
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=lambda: open_file(text))
file_menu.add_command(label="Save", command=lambda: save_file(text))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit menu
edit_menu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Find and Replace", command=lambda: find_and_replace(text))

# Start the main loop
root.mainloop()
