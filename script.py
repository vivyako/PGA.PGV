import matplotlib.pyplot as plt
import math

valuesVerticalA = []
valuesHorizontalA = []
valuesMainA = []
valuesVerticalV = []
valuesHorizontalV = []
valuesMainV = []
maxHorizontal = 0
eventLines = 0
stationA = []
stationV = []
x = []
y = []
lastLength = 0

def GetCoords(lastLength): 
    for i in range(lastLength, len(stationV), 1):
        for j in range(lastLength, len(stationA), 1):
            if stationV[i] == stationA[j]:
                x.append(math.log10(valuesMainV[i]))
                y.append(math.log10(valuesMainA[j]))

def GetStation(station):
    str = ''
    for i in range(0, 5, 1):
        str += line[i]
    station.append(str)

def Avg(valuesMain):
    return sum(valuesMain) / len(valuesMain)

def GetValues(line, valuesVertical, valuesHorizontal, valuesMain, station):
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
            GetStation(station)
    else:
        valuesHorizontal.append(Filling(line))

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
    lines = f.readlines()
    for line in lines:
        if line[1] != ' ':
            eventLines += 1
            if 'E   ' in line:
                GetValues(line, valuesVerticalV, valuesHorizontalV, valuesMainV, stationV)
            if 'APGA' in line:
                GetValues(line, valuesVerticalA, valuesHorizontalA, valuesMainA, stationA)
        elif eventLines > 6: 
            eventLines = 0
            GetCoords(lastLength)
            lastLength = len(stationV)
        else: 
            eventLines = 0

fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set(title='PGA.PGV')
ax.set_ylabel('PGA (нм/с^2)')
ax.set_xlabel('PGV (нм/с)')
plt.show()