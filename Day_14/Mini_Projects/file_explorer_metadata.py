import os
from datetime import datetime

def get_metadata(file_path):
    try:
        size = os.path.getsize(file_path)
        created = datetime.fromtimestamp(os.path.getctime(file_path)).strftime("%Y-%m-%d %H:%M:%S")
        modified = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y-%m-%d %H:%M:%S")
        return size, created, modified
    except Exception as e:
        return "Error", "Error", "Error"

def explore_folder(folder_path):
    if not os.path.exists(folder_path):
        print(" Folder not found.")
        return

    files = os.listdir(folder_path)
    report_lines = []
    report_lines.append(f"{'Filename':<40} {'Size (bytes)':<15} {'Created':<20} {'Last Modified':<20}")
    report_lines.append("-" * 100)

    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            size, created, modified = get_metadata(file_path)
            report_lines.append(f"{file:<40} {size:<15} {created:<20} {modified:<20}")

    report = "\n".join(report_lines)

    # Display on console
    print("\n File Metadata Report:\n")
    print(report)

    # Save to file
    output_file = "metadata_report.txt"
    try:
        with open(output_file, "w") as f:
            f.write(report)
        print(f"\n Metadata saved to '{output_file}'")
    except Exception as e:
        print(" Error writing report:", e)

def main():
    print("=== File Explorer with Metadata Viewer ===")
    folder = input("Enter folder path to explore: ").strip()
    explore_folder(folder)

if __name__ == "__main__":
    main()
