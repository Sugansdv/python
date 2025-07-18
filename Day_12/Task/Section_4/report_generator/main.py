from reader import read_csv
from analyzer import summarize

data = read_csv("data.csv")
summary = summarize(data, "score")
print("Summary:", summary)
