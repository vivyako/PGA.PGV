from _typeshed import Self
events = []

class Event(object):

    stations = []    
    
    def addingValues(self, line):
        Event.stations.append(Station())
        if 'E   ' in line:
            print()

class Station(object):

    valuesMain = []
    valuesVertical = []
    valuesHorizontal = []
    stationType = '' # A - ускорение, V - скорость
    stationName = ''

    def Filling(self, line):
        str = ''
        result = 0
        for i in range(31, 40):
            if line[i] == ' ':
                continue
            else:
                str += line[i]
        result = float(str)
        return result

events.append(Event())
j = len(events) - 1
with open('data.txt', 'r') as f:
    for line in f:
        if line[0] != ' ':
            print(1)
        else:
            events.append(Event())
            j += 1

#СМОТРЕТЬ СЮДА, КАК НА ПРИМЕР:
# with open('data.txt', 'r') as f:
#     for line in f:
#         events.append(Event())
#         if 'E   ' in line:
#             if line[7] == 'Z':
#                 valuesVertical.append(events.Filling(line))
#             elif line[7] == 'E':
#                 valuesHorizontal.append(events.Filling(line))
#                 if valuesHorizontal[len(valuesHorizontal) - 1] > valuesHorizontal[len(valuesHorizontal) - 2]:
#                     maxHorizontal = valuesHorizontal[len(valuesHorizontal) - 1]
#                 else:
#                     maxHorizontal = valuesHorizontal[len(valuesHorizontal) - 2]
#                 temp = max(valuesHorizontal[len(valuesHorizontal) - 1], valuesHorizontal[len(valuesHorizontal) - 2])
#                 valuesMain.append(valuesVertical[len(valuesVertical) - 1] / maxHorizontal)
#                 events.main = valuesMain[len(valuesMain) - 1]
#             else:
#                 valuesHorizontal.append(events.Filling(line))
#print('Average PGV: ', Avg(valuesMain))
# line[7] - определяем вертикаль или горизонталь
# можно забрать значения начиная с 28 символа, пока не наткнешься СНОВА на пустой символ, а потом пустые символы удалить
# выбираем максимальную из горизонтальных, потом вертикальную делим на горизонтальную
# массив будет состоять из элементов, каждый из которых выражен отношением вертикальной к горизонтальной