import os
from pprint import pprint


opa ={}
xxx = {}
collection = {}
for files in os.listdir():
   if files.endswith(('.txt')):
       with open(files, encoding='utf-8') as data:
            for strokes in data:
                collection[files] = data.read()

for files in os.listdir():
    if files.endswith(('.txt')):
        counterr = 0
        with open(files, encoding='utf-8') as data:
            for strokes in data:
                counterr += 1
            opa[files] = counterr

sorted_vales = sorted(opa.values())

for w in sorted_vales:
    for k in opa.keys():
        if opa[k] == w:
            xxx[k] = opa[k]

for name_of_file in xxx.keys():
    with open('4fil.txt', 'a') as f:
        f.write(f'{name_of_file}\n')
        f.write(f'{xxx[name_of_file]}\n')
        f.write(f'{collection[name_of_file]}\n')
