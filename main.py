import tkinter as tk
from tkinter import filedialog


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


def change_text():
    pass


# Main window
root = tk.Tk()
root.title("Text Editor")

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

# Style Menu
style_menu = tk.Menu(menu)
menu.add_cascade(label="Style", menu=style_menu)
style_menu.add_command(label="Text", command=change_text)

# text area
text = tk.Text(root, font=("Helvetica", 22))
text.pack(fill=tk.BOTH, expand=True)

# Start the main loop
root.mainloop()

