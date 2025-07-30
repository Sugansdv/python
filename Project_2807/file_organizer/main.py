from core.organizer import organize

if __name__ == "__main__":
    import os

    #  Change this path to the folder you want to organize
    folder_to_organize = os.path.abspath("test_folder")  # <- Create and test here
    organize(folder_to_organize, dry=False)  # dry=True to preview, dry=False to apply
