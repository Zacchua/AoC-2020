def part1(pocket, count, num):
    if count == 6:
        print('part 1:', num)
    else:
        # creates the new arrays
        before = []
        after = []
        for x in range(len(pocket[count]) + 2):
            before.append([])
            after.append([])
            for y in range(len(pocket[count]) + 2):
                before[x].append('.')
                after[x].append('.')
        pocket[count + 1] = after
        pocket[-(count + 1)] = before
        # extends previous arrays
        for x in range(-count, count + 1):
            pocket[x] = extendArray(pocket[x])
        newPocket = {}
        total_num = 0
        for z in range(-(count + 1), count + 2):
            newPocket[z] = []
            for x in range(len(pocket[count])):
                newPocket[z].append([])
                for y in range(len(pocket[count])):
                    new_sym = checker(x, y, z, pocket, count)
                    if new_sym == '#':
                        total_num += 1
                    newPocket[z][x].append(new_sym)
        count += 1
        return part1(newPocket, count, total_num)

def part2(pocket, count, num):
    if count == 6:
       print('part 2:',  num) 
    else:
        before = []
        for x in range(len(pocket[count][count]) + 2):
            before.append([])
            for y in range(len(pocket[count][count]) + 2):
                before[x].append('.')
        pocket[count + 1] = {}
        pocket[-(count + 1)] = {}
        for w in range(-(count + 1), count + 2):
            pocket[count + 1][w] = before.copy()
            pocket[-(count + 1)][w] = before.copy()
            pocket[w][count + 1] = before.copy()
            pocket[w][-(count + 1)] = before.copy()
        for x in range(-count, count + 1):
            for y in range(-count, count + 1):
                pocket[x][y] = extendArray(pocket[x][y])
        newPocket = {}
        total_num = 0
        for z in range(-(count + 1), count + 2):
            newPocket[z] = {}
            for w in range(-(count + 1), count + 2):
                newPocket[z][w] = []
                for x in range(len(pocket[count][count])):
                    newPocket[z][w].append([])
                    for y in range(len(pocket[count][count])):
                        new_sym = checker2(x, y, z, w, pocket, count)
                        if new_sym == '#':
                            total_num += 1
                        newPocket[z][w][x].append(new_sym)
        count += 1
        return part2(newPocket, count, total_num)
        

def checker2(x, y, z, w, pocket, count):
    counter = 0
    for new_x in range(x - 1, x + 2):
        for new_y in range(y - 1, y + 2):
            for new_z in range(z - 1, z + 2):
                for new_w in range(w - 1, w + 2):
                    if new_x >= 0 and new_x < len(pocket[z][w]):
                        if new_y >= 0 and new_y < len(pocket[z][w][x]):
                            if new_z >= -(count + 1) and new_z < (count + 1):
                                if new_w >= -(count + 1) and new_w < (count + 1):
                                    if pocket[new_z][new_w][new_x][new_y] == '#':
                                        counter += 1
    if pocket[z][w][x][y] == "." :
        if counter == 3:
            return '#'
        else:
            return '.'
    else:
        if counter == 4 or counter == 3:
            return '#'
        else:
            return '.' 

def checker(x, y, z, pocket, count):
    counter = 0
    for new_x in range(x - 1, x + 2):
        for new_y in range(y - 1, y + 2):
            for new_z in range(z - 1, z + 2):
                if new_x >= 0 and new_x < len(pocket[z]):
                    if new_y >= 0 and new_y < len(pocket[z][x]):
                        if new_z >= -(count + 1) and new_z < (count + 1):
                            if pocket[new_z][new_x][new_y] == '#':
                                counter += 1
    if pocket[z][x][y] == "." :
        if counter == 3:
            return '#'
        else:
            return '.'
    else:
        if counter == 4 or counter == 3:
            return '#'
        else:
            return '.'
        


def extendArray(xss):
    toReturn = []
    for x in range(len(xss) + 2):
        toReturn.append([])
        for y in range(len(xss[0]) + 2):
            if x == 0 or x == len(xss) + 1:
                toReturn[x].append('.')
            elif y == 0 or y >len(xss[0]):
                toReturn[x].append('.')
            else:
                toReturn[x].append(xss[x - 1][y - 1])
    return toReturn


def make2dArray(xs):
    array = []
    pocket = {}
    for line in xs:
        lineArray = []
        for elem in line.rstrip('\n'):
            lineArray.append(elem)
        array.append(lineArray)
    pocket[0] = array
    return pocket

def make3dArray(xs):
    array = []
    pocket = {}
    for line in xs:
        lineArray = []
        for elem in line.rstrip('\n'):
            lineArray.append(elem)
        array.append(lineArray)
    pocket[0] = {}
    pocket[0][0] = array
    return pocket 


with open('input17.txt', 'r') as inputfile:
    lines = inputfile.readlines()
    part1(make2dArray(lines), 0, 0)
    part2(make3dArray(lines), 0, 0)
