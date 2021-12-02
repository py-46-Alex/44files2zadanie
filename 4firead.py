import os
from pprint import pprint

def writer():
    second_dict = listo_creator()
    collection = start_progr()
    for name_of_file in second_dict.keys():
        with open('4fil.txt', 'a') as f:
            f.write(f'{name_of_file}\n')
            f.write(f'{second_dict[name_of_file]}\n')
            f.write(f'{collection[name_of_file]}\n')
    print("Запись в 4-ый файл в папке готов")

def listo_creator():
    first_dict = {}
    for files in os.listdir():
        if files.endswith(('.txt')):
            counterr = 0
            with open(files, encoding='utf-8') as data:
                for strokes in data:
                    counterr += 1
                    first_dict[files] = counterr
    second_dict = {}
    sorted_vales = sorted(first_dict.values())
    for w in sorted_vales:
        for k in first_dict.keys():
            if first_dict[k] == w:
                second_dict[k] = first_dict[k]
   
    return second_dict

def start_progr(): 
    collection = {}
    for files in os.listdir():
        if files.endswith(('.txt')):
            with open(files, encoding='utf-8') as data:
                for strokes in data:
                    collection[files] = data.read()
    return collection

writer()
