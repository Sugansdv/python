import csv

def read_csv(file):
    with open(file, newline='') as f:
        return list(csv.DictReader(f))
