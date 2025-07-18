import shutil
def copy_file(src, dest):
    shutil.copy(src, dest)
    print(f"Copied from {src} to {dest}")
