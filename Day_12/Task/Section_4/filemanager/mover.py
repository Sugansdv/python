import shutil
def move_file(src, dest):
    shutil.move(src, dest)
    print(f"Moved from {src} to {dest}")
