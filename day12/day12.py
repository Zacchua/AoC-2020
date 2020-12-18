import math 

def execute(xs, x_coord, y_coord, head):
    for step in xs:
        if step[0] == 'F':
            new_x, new_y = move(x_coord, y_coord, step[1:], head)
            x_coord = new_x
            y_coord = new_y
        elif step[0] == 'N':
            new_x, new_y = move(x_coord, y_coord, step[1:], '+y')
            x_coord = new_x
            y_coord = new_y
        elif step[0] == 'S':
            new_x, new_y = move(x_coord, y_coord, step[1:], '-y')
            x_coord = new_x
            y_coord = new_y
        elif step[0] == 'E':
            new_x, new_y = move(x_coord, y_coord, step[1:], '+x')
            x_coord = new_x
            y_coord = new_y
        elif step[0] == 'W':
            new_x, new_y = move(x_coord, y_coord, step[1:], '-x')
            x_coord = new_x
            y_coord = new_y
        elif step[0] == 'R':
            new_head = rotate_right(head, step[1:])
            head = new_head
        elif step[0] == 'L':
            amt = int(step[1:])
            new_head = rotate_right(head, (360 - (amt % 360)))
            head = new_head
    return (x_coord, y_coord)


def move(x, y, amt, head):
    amt = int(amt)
    if head == '+x':
        return (x + amt, y)
    elif head =='-x':
        return (x - amt, y)
    elif head =='-y':
        return (x, y - amt)
    elif head =='+y':
        return (x, y + amt)

def rotate_right(head, amt):
    amt = int(amt)
    num = math.floor((amt / 90) % 4)
    direction = convert(head)
    direction += num
    return convert_back(direction % 4)

def convert(head):
    if head == '+x':
        return 1
    elif head == '-y':
        return 2
    elif head == '-x':
        return 3
    elif head == '+y':
        return 4

def convert_back(num):
    if num == 1:
        return '+x'
    elif num == 2:
        return '-y'
    elif num == 3:
        return '-x'
    elif num == 0:
        return '+y'

def manhatten(x, y):
    return abs(x) + abs(y)

def execute_v2(xs, x_coord, y_coord, wp):
    for step in xs:
        if step[0] == 'F':
            new_x, new_y = move2(x_coord, y_coord, step[1:], wp)
            x_coord = new_x
            y_coord = new_y
        elif step[0] == 'N' or step[0] == 'S' or step[0] == 'E' or step[0] == 'W':
            wp = shift_wp(step[0], step[1:], wp)
        elif step[0] == 'R':
            new_wp = rotate_wp(step[1:], wp)
            wp = new_wp
        elif step[0] == 'L':
            amt = int(step[1:])
            new_wp = rotate_wp(360 - amt, wp)
            wp = new_wp
    return (x_coord, y_coord)

def move2(x, y, amt, wp):
    amt = int(amt)
    x_amt, y_amt = wp
    return (x + (x_amt * amt), y + (y_amt * amt))

def shift_wp(letter, amt, wp):
    amt = int(amt)
    x, y = wp 
    if letter == 'N':
        return (x, y + amt)
    elif letter == 'S':
        return (x, y - amt)
    elif letter == 'E':
        return (x + amt, y)
    elif letter == 'W':
        return (x - amt, y)

def rotate_wp(amt, wp):
    amt = int(amt)
    x, y = wp 
    if amt == 90:
        return (y, -x)
    elif amt == 180:
        return (-x, -y)
    elif amt == 270:
        return (-y, x)
    elif amt == 360 or amt == 0:
        return (x, y)


with open('input12.txt', 'r') as inputfile:
    lines = inputfile.readlines()
    steps = []
    for line in lines:
        steps.append(line.rstrip('\n'))
    x, y  = execute(steps, 0, 0, '+x')
    print('part 1:', manhatten(x, y))
    new_x, new_y = execute_v2(steps, 0, 0, (10, 1))
    print('part 2:', manhatten(new_x, new_y))
