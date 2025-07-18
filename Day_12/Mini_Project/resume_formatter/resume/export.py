import os

def export_resume(content, filename, format="txt"):
    ext = ".md" if format == "md" else ".txt"
    full_path = filename + ext
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f" Resume saved to: {os.path.abspath(full_path)}")
