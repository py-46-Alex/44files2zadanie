import os
from pprint import pprint

with open('fi1.txt', encoding='utf-8') as fale1:
    filename1 = 'fi1.txt'
    counter1 = 0
    for strokes1 in fale1:
        counter1 += 1

with open('fi2.txt', encoding='utf-8') as fale2:
    filename2 = 'fi2.txt'
    counter2 = 0
    for strokes2 in fale2:
        counter2 += 1

with open('fi3.txt', encoding='utf-8') as fale3:
    filename3 = 'fi3.txt'
    counter3 = 0
    for strokes3 in fale3:
        counter3 += 1

def comparison(com1, com2, com3):
    with open('fi1.txt', encoding='utf-8') as fale1:
        data1 = fale1.read()
    with open('fi2.txt', encoding='utf-8') as fale2:
        data2 = fale2.read()
    with open('fi3.txt', encoding='utf-8') as fale3:
        data3 = fale3.read()

    if com1 < com2 and com1 < com3:
        with open('fi4.txt', 'w') as f:
            f.write(f'{filename1}\n')
            f.write(f'{counter1}\n')
            f.write(f'{data1}\n')
        if com2 < com3:
            with open('fi4.txt', 'a') as f:
                f.write(f'{filename2}\n')
                f.write(f'{counter2}\n')
                f.write(f'{data2}\n')
                f.write(f'{filename3}\n')
                f.write(f'{counter3}\n')
                f.write(f'{data3}\n')
        elif com3 < com2:
            with open('fi4.txt', 'a') as f:
                f.write(f'{filename3}\n')
                f.write(f'{counter3}\n')
                f.write(f'{data3}\n')
                f.write(f'{filename2}\n')
                f.write(f'{counter2}\n')
                f.write(f'{data2}\n')
    elif com2 < com1 and com2 < com3:
        with open('fi4.txt', 'w') as f:
            f.write(f'{filename2}\n')
            f.write(f'{counter2}\n')
            f.write(f'{data2}\n')
        if com1 < com3:
            with open('fi4.txt', 'a') as f:
                f.write(f'{filename1}\n')
                f.write(f'{counter1}\n')
                f.write(f'{data1}\n')
                f.write(f'{filename3}\n')
                f.write(f'{counter3}\n')
                f.write(f'{data3}\n')
        elif com3 < com1:
            with open('fi4.txt', 'a') as f:
                f.write(f'{filename3}\n')
                f.write(f'{counter3}\n')
                f.write(f'{data3}\n')
                f.write(f'{filename1}\n')
                f.write(f'{counter1}\n')
                f.write(f'{data1}\n')
    elif com3 < com1 and com3 < com2:
        with open('fi4.txt', 'w') as f:
            f.write(f'{filename3}\n')
            f.write(f'{counter3}\n')
            f.write(f'{data3}\n')
        if com1 < com2:
            with open('fi4.txt', 'a') as f:
                f.write(f'{filename1}\n')
                f.write(f'{counter1}\n')
                f.write(f'{data1}\n')
                f.write(f'{filename2}\n')
                f.write(f'{counter2}\n')
                f.write(f'{data2}\n')
        elif com2 < com1:
            with open('fi4.txt', 'a') as f:
                f.write(f'{filename2}\n')
                f.write(f'{counter2}\n')
                f.write(f'{data2}\n')
                f.write(f'{filename1}\n')
                f.write(f'{counter1}\n')
                f.write(f'{data1}\n')
    else:
        print('Одинаковое количество строк в файлах . Слияние в файл 4 не выполнено')

comparison(counter1, counter2, counter3)


    # for dinner in fale:
    #     dish_name = dinner.strip()
    #     counter = int(fale.readline().strip())
    #     cook_box = []
    #     for ingr in range(counter):
    #         ingredient_name, quantity, measure = fale.readline().split('|')
    #         cook_box.append({'ingredient_name':ingredient_name.strip(), 'quantity':int(quantity.strip()), 'measure':measure.strip()})
    #     cook_book[dish_name] = cook_box
    #     fale.readline()
