import math

def check_empty(seats, row, column):
    occupied = 0
    unoccupied = 0
    top = row - 1
    bottom = row + 2
    right = column + 2
    left = column - 1
    global BOTTOM
    global RIGHT

    if top < 0:
        top = 0

    if bottom > BOTTOM:
        bottom = BOTTOM 

    if left < 0:
        left = 0

    if right > RIGHT:
        right = RIGHT 

    for x in range(top, bottom):
        for y in range(left, right):
            if seats[x][y] == '#':
                occupied += 1

    if seats[row][column] == 'L':
        if occupied >= 1:
            return 'L'
        else: 
            return '#'
    elif seats[row][column] == '#':
        if occupied >= 5:
            return 'L'
        else: 
            return '#'
    elif seats[row][column] == '.':
        return '.'

    
def check_v2(seats, row, column):
    
    occupied = 0
    global BOTTOM
    global RIGHT

    #print('row:', row, 'col:', column)

    
    # check vertical before
    x = row - 1
    while x >= 0: 
        if seats[x][column] == '#':
            occupied += 1
            break
        elif seats[x][column] == 'L':
            break
        x -= 1
    
    for x in range(row + 1, BOTTOM):
        if seats[x][column] == '#':
            occupied += 1
            break
        elif seats[x][column] == 'L':
            break

    # check horizontal
    y = column - 1
    while y >= 0:
        if seats[row][y] == '#':
            occupied += 1
            break
        elif seats[row][y] == 'L':
            break
        y -= 1
    
    for y in range(column + 1, RIGHT):
        if seats[row][y] == '#':
            occupied += 1
            break
        elif seats[row][y] == 'L':
            break

    i = row - 1
    j = column - 1
    while i >= 0 and j >= 0:
        if seats[i][j] == '#':
            occupied += 1
            break
        elif seats[i][j] == 'L':
            break
        i -= 1
        j -=1

    up_extreme_x = row + 1
    up_extreme_y = column + 1
    # check backslash diagonalafter 
    while up_extreme_x < BOTTOM and up_extreme_y < RIGHT:
        if seats[up_extreme_x][up_extreme_y] == '#' and up_extreme_x != row and up_extreme_y != column:
            occupied += 1
            break
        elif seats[up_extreme_x][up_extreme_y] == 'L':
            break
        up_extreme_x += 1
        up_extreme_y += 1

    i = row + 1
    j = column - 1
    while i < BOTTOM and j >= 0:
        if seats[i][j] == '#':
            occupied += 1
            break
        elif seats[i][j] == 'L':
            break
        i += 1
        j -= 1

    low_extreme_x = row - 1
    low_extreme_y = column + 1
    # check forwardslash diagonal
    while low_extreme_x >= 0 and low_extreme_y < RIGHT:
        if seats[low_extreme_x][low_extreme_y] == '#' and low_extreme_x != row and low_extreme_y != column:
            occupied += 1
            break
        elif seats[low_extreme_x][low_extreme_y] == 'L':
            break
        low_extreme_x -= 1
        low_extreme_y += 1


    if seats[row][column] == 'L':
        if occupied >= 1:
            return 'L'
        else:
            return '#'
    elif seats[row][column] == '#':
        if occupied >= 5:
            return 'L'
        else:
            return '#'
    elif seats[row][column] == '.':
        return '.'




def checker(seat_map, prev, count):
    print('prev:', prev)
    copy = []
    for line in seat_map:
        copy.append(line.copy())
    new = 0
    global BOTTOM
    BOTTOM = len(copy)
    global RIGHT
    RIGHT = len(copy[0])
    print('bot:', BOTTOM, 'right:', RIGHT)
    for row in range(BOTTOM):
        for col in range(RIGHT):
            new_elem = check_v2(seat_map, row, col)
            if new_elem == '#':
                new += 1
            copy[row][col] = new_elem
    if new == prev:
        print(new) 

    else:
        for line in copy:
            print('count:', count, line)
        checker(copy, new, count + 1)

with open('input11.txt', 'r') as inputfile:
    lines = inputfile.readlines()
    seat= []
    for line in lines:
        line = line.rstrip('\n')
        seat_line = []
        for elem in line:
            seat_line.append(elem)
        seat.append(seat_line)
    checker(seat, 0, 1)
   
