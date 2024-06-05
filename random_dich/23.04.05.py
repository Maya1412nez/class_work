# 1
def maximum(array, col):
    lst = []
    for i in range(col):
        lst.append(max(array))
        array.remove(max(array))
    return lst

def minimum(array, col=0, max_val=0):
    print(111)
    print(array)
    lst = []
    if max_val:
        while max_val >= sum(lst):
            lst.append(min(array))
            array.remove(min(array))
        lst.remove(max(lst))
        print(sum(lst), max(lst))
    elif col:
        for i in range(col):
            lst.append(min(array))
            array.remove(min(array))
        lst.remove(max(lst))
        print(sum(lst), max(lst))
    return lst

# print(maximum([10, 9, 8, 4, 3, 2], 3))

def first():
    from pathlib import Path
    import math
    import numpy as np
    data = open('data.txt', 'r', encoding='utf-8')
    Gfats, Gprotein, Gcarbohydrates, Gkkal = [],[],[],[]
    k = 0
    for row in data:
        if 'Жиры' not in row:
            name, fats, protein, carbohydrates, kkal = row.split('\t')
            # print(name, fats, protein, carbohydrates, kkal)
            fats, protein, carbohydrates, kkal = float(fats.replace(',', '.')), float(protein.replace(',', '.')), float(carbohydrates.replace(',', '.')), float(kkal.replace(',', '.'))
            Gfats.append(float(fats))
            Gprotein.append(float(protein))
            Gcarbohydrates.append(float(carbohydrates))
            Gkkal.append(float(kkal))
            k += 1
    Gfats, Gprotein, Gcarbohydrates, Gkkal = np.array(Gfats),np.array(Gprotein),np.array(Gcarbohydrates),np.array(Gkkal)
    sr_fats, sr_protein, sr_carbohydrates, sr_kkal = sum(Gfats) / k, sum(Gprotein) / k, sum(Gcarbohydrates) / k, sum(Gkkal) / k
    sr_sqr_fats = Gfats.std(ddof=1)
    sr_sqr_protein = Gprotein.std(ddof=1)
    sr_sqr_carbohydrates = Gcarbohydrates.std(ddof=1)
    sr_sqr_kkal = Gkkal.std(ddof=1)

# print(f'''
# Answer:
# {sr_fats, sr_protein, sr_carbohydrates, sr_kkal}
# ''')
# print(sr_sqr_fats, sr_sqr_protein, sr_sqr_carbohydrates, sr_sqr_kkal)
# data.close()

# 2

# data = Path('23.04.05.txt').read_text(encoding='utf-8').splitlines()
# print(data)

def three():
    data = open('data.txt', 'r', encoding='utf-8')
    matrix = [[],
            [],
            [],
            []]
    for row in data:
        if 'Жиры' not in row:
            name, fats, protein, carbohydrates, kkal = row.split('\t')
            matrix[0].append(float(fats.replace(',', '.'))); matrix[1].append(float(protein.replace(',', '.'))); matrix[2].append(float(carbohydrates.replace(',', '.'))); matrix[3].append(float(kkal.replace(',', '.')))
    matrix = np.array(matrix)
    # print(matrix)
    print(matrix.mean(axis=1))
    print(matrix.std(ddof=1, axis=1))
    max_kkal = max(matrix[3])
    print(max_kkal)
    data = open('data.txt', 'r', encoding='utf-8')
    for row in data:
        if 'Жиры' not in row:

            name, fats, protein, carbohydrates, kkal = row.split('\t')
            if max_kkal == float(kkal.replace(',', '.')):
                print(name)


# 4
def four():
    data = open('data.txt', 'r', encoding='utf-8')
    matrix = [[],
            [],
            [],
            []]
    for row in data:
        if 'Жиры' not in row:
            name, fats, protein, carbohydrates, kkal = row.split('\t')
            matrix[0].append(float(fats.replace(',', '.'))); matrix[1].append(float(protein.replace(',', '.'))); matrix[2].append(float(carbohydrates.replace(',', '.'))); matrix[3].append(float(kkal.replace(',', '.')))
    matrix = np.array(matrix)
    # print(matrix)
    print(matrix.mean(axis=1))
    print(matrix.std(ddof=1, axis=1))
    lst = list(matrix[3])
    max_kkal = (maximum(lst, 10))
    print(max_kkal)
    data = open('data.txt', 'r', encoding='utf-8')
    for row in data:
        if 'Жиры' not in row:

            name, fats, protein, carbohydrates, kkal = row.split('\t')
            if float(kkal.replace(',', '.')) in max_kkal:
                print(name, kkal)



# ЕГЭ СyandexКААААААААА
def EGE():
    file = open('class_work/demo.txt', 'r', encoding='utf-8')
    values = []
    max_val, col = 0, 0
    for row in file:
        if len(row.split()) == 2:
            max_val, col = row.split()
            max_val, col = int(max_val), int(col)
        else:
            values.append(int(''.join(row.split())))

    # print(max_val, col)
    # print(values)

    lst = minimum(values, max_val=max_val)
    # print(lst)
    print(max(lst), len(lst))
    lst2 = []
    while (len(lst2) == len(lst)) or (len(lst2) == 0):
        print((len(lst2) == len(lst)) or (len(lst2) == 0))
        print(len(lst), len(lst2))
        values.remove(min(values))
        print(values)
        lst2 = minimum(values, col=len(lst))


    print(lst2)
    print('''
    
    
    
    
    
    
    
    
    ''')
    print(len(lst2), max(lst2))


def main():
    EGE()

main()