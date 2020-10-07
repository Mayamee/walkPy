def update(sym, curPoint):
    if sym == "n":
        curPoint[1] += 1
    elif sym == "s":
        curPoint[1] -= 1
    elif sym == "w":
        curPoint[0] += 1
    elif sym == "e":
        curPoint[0] -= 1
    else:
        pass
    return curPoint


def read(pointWL, point):
    pointWL.append(point)  # readFunction


def linker(pointWL):
    # должен вернуть словарь
    li = []
    point = {}
    indexPoint = "point"
    indexLink = "link"
    for item in pointWL:
        if (not hasFound(item, li, indexPoint)):
            point[indexPoint] = item
            point[indexLink] = search(item, pointWL)
            li.append(point.copy())
    return li


def hasFound(point, arr, indexP):
    flag = False
    for item in arr:
        flag = flag or item[indexP] == point
        if(flag):
            break
    return flag


def search(value, array):
    index = 0
    for i in range(len(array)):
        if(array[i] == value):
            index += 1
    return index


def addPoints(way):
    allPoints = []
    start = [0, 0]
    allPoints.append(start.copy())
    for step in way:
        allPoints.append(update(step, start).copy())
    return allPoints


def is_valid_walk(way):
    allPoints = addPoints(way)
    if((allPoints[len(allPoints)-1] != [0, 0]) and len(allPoints) != 11):
        return False
    linkedArr = linker(allPoints)
    if(linkedArr[0]["link"] != 2):
        return False
    del linkedArr[0]
    for currentPoint in linkedArr:
        if(currentPoint["link"] != 1):
            return False
    return True


wayArr = ['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']
print(is_valid_walk(wayArr))
