import tkinter as tk

class TextOperator:
    def highlight_all(self, text_widget, term):
        text_widget.tag_remove('highlight', '1.0', tk.END)
        idx = '1.0'
        while True:
            idx = text_widget.search(term, idx, nocase=1, stopindex=tk.END)
            if not idx:
                break
            end_idx = f"{idx}+{len(term)}c"
            text_widget.tag_add('highlight', idx, end_idx)
            idx = end_idx
        text_widget.tag_config('highlight', background='yellow')

    def replace_all(self, text_widget, old, new):
        content = text_widget.get("1.0", tk.END)
        new_content = content.replace(old, new)
        text_widget.delete("1.0", tk.END)
        text_widget.insert("1.0", new_content)
