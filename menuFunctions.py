from tkinter import filedialog, simpledialog

def open_file(text_widget):
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        text_widget.delete('1.0', 'end')
        text_widget.insert('end', file.read())

def save_file(text_widget):
    file_path = filedialog.asksaveasfilename(defaultextension='.txt')
    with open(file_path, 'w') as file:
        file.write(text_widget.get('1.0', 'end'))

def find_and_replace(text_widget):
    search_term = simpledialog.askstring("Find and Replace", "Find:")
    if search_term:
        replacement = simpledialog.askstring("Find and Replace", f"Replace '{search_term}' with:")
        if replacement:
            text_widget.replace("1.0", 'end', text_widget.get("1.0", 'end').replace(search_term, replacement))
