valuesVertical = []
valuesHorizontal = []
valuesMain = []
maxHorizontal = 0

def Avg(arr):
    return sum(arr) / len(arr)

def Filling(line):
    str = ''
    result = 0
    for i in range(31, 40):
        if line[i] == ' ':
            continue
        else:
            str += line[i]
    result = float(str)
    return result

with open('data.txt', 'r') as f:
    for line in f:
        if 'E   ' in line:
            if line[7] == 'Z':
                valuesVertical.append(Filling(line))
            elif line[7] == 'E':
                valuesHorizontal.append(Filling(line))
                if valuesHorizontal[len(valuesHorizontal) - 1] > valuesHorizontal[len(valuesHorizontal) - 2]:
                    maxHorizontal = valuesHorizontal[len(valuesHorizontal) - 1]
                else:
                    maxHorizontal = valuesHorizontal[len(valuesHorizontal) - 2]
                temp = max(valuesHorizontal[len(valuesHorizontal) - 1], valuesHorizontal[len(valuesHorizontal) - 2])
                valuesMain.append(valuesVertical[len(valuesVertical) - 1] / maxHorizontal)
            else:
                valuesHorizontal.append(Filling(line))
print('Average PGV: ', Avg(valuesMain))
# line[7] - определяем вертикаль или горизонталь
# можно забрать значения начиная с 28 символа, пока не наткнешься СНОВА на пустой символ, а потом пустые символы удалить
# выбираем максимальную из горизонтальных, потом вертикальную делим на горизонтальную
# массив будет состоять из элементов, каждый из которых выражен отношением вертикальной к горизонтальной