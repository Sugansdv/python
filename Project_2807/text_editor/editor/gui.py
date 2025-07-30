import tkinter as tk
from tkinter import filedialog, messagebox
from editor.file_ops import FileHandler
from editor.text_ops import TextOperator

class TextEditorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Basic Text Editor")
        self.root.geometry("800x600")
        
        self.file_handler = FileHandler()
        self.text_operator = TextOperator()

        self.text_area = tk.Text(self.root, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill=tk.BOTH)

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Recent Files", command=self.show_recent_files)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Search", command=self.search_text)
        edit_menu.add_command(label="Replace", command=self.replace_text)

        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        
        self.root.config(menu=menubar)

    def open_file(self):
        path = filedialog.askopenfilename()
        if path:
            try:
                content = self.file_handler.read_file(path)
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def save_file(self):
        path = filedialog.asksaveasfilename()
        if path:
            content = self.text_area.get(1.0, tk.END)
            try:
                self.file_handler.write_file(path, content)
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def search_text(self):
        term = self.prompt("Enter text to search:")
        if term:
            self.text_operator.highlight_all(self.text_area, term)

    def replace_text(self):
        old = self.prompt("Text to replace:")
        new = self.prompt("Replace with:")
        if old and new:
            self.text_operator.replace_all(self.text_area, old, new)

    def show_recent_files(self):
        files = self.file_handler.get_recent_files()
        messagebox.showinfo("Recent Files", "\n".join(files) if files else "No recent files.")

    def prompt(self, title):
        return tk.simpledialog.askstring("Input", title)

    def run(self):
        self.root.mainloop()
