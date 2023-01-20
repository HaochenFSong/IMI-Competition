from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import numpy as np
import csv

"https://github.com/seatgeek/thefuzz  name match package"

# Read in all the target data
name_map = {}
# Create target list
for c in map(chr, range(97, 123)):
    name_map[c] = []

for c in map(chr, range(97, 123)):
    with open(c+".csv", newline='', encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name_map[c].append(row['NameBirth'])

# Read in the node name file

node_name_arr = []
with open("nodes_name.csv", newline='', encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        node_name_arr.append(row['NameBirth'])

# Create a csv file
header = ['NameBirth', 'matchnum']

with open('match.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    
threshold = 10
# Max name 1000000
max_num = 1000000

for i in range(0, int(max_num / 4)):
    extracted_name = node_name_arr[i]
    val = process.extractOne(extracted_name, name_map[extracted_name[0]])
    name = val[0]
    match_num = val[1]
    
    with open('match.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writerow({'NameBirth': name, 'matchnum': match_num})

print(len(node_name_arr))