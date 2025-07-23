def merge_files(file1, file2, output_file):
    with open(output_file, "w") as outfile:
        for fname in [file1, file2]:
            with open(fname, "r") as infile:
                outfile.write(infile.read() + "\n")
    print(f"Merged into {output_file}")

# Example
merge_files("file1.txt", "file2.txt", "merged.txt")
