import math

def apply(mask, num):
    num = str(num)
    num = num[2:]
    length = len(mask)
    while len(num) < length:
        num = '0' + num
    num = list(num)
    for x in range(length):
        if mask[x] != 'X':
            num[x] = mask[x]
    return listbin_toint(num)

def listbin_toint(xs):
    num = 0
    length = len(xs)
    for x in range(length):
        num += int(xs[length - 1 - x]) * int(math.pow(2, x))
    return num
        
def part1(xs):
    mask = ''
    num = 0
    mem = dict()
    count = 0
    for line in xs:
        if line[1] == 'a':
            line = line[7:]
            mask = line.rstrip('\n')
        else:
            line = line[4:]
            line = line.split(']')
            pos = int(line[0])
            num = line[1][3:].rstrip('\n')
            num = int(num)
            new_num = apply(mask, bin(num))
            mem[pos] = int(new_num)
    for value in mem.values():
        count += value
    print('part 1:', count)

def part2(xs):
    mask = ''
    num = 0
    mem2 = dict()
    count = 0
    for line in xs:
        if line[1] == 'a':
            line = line[7:]
            mask = line.rstrip('\n')
        else:
            line = line[4:]
            line = line.split(']')
            mem = int(line[0])
            num = line[1][3:].rstrip('\n')
            num = int(num)
            mem = str(bin(mem))
            mem = mem[2:]
            length = len(mask)
            while len(mem) < length:
                mem = '0' + mem
            memlist = apply_v2(mask, list(mem), 0)
            for location in memlist:
                location = listbin_toint(location)
                print(location)
                mem2[location] = num
    for value in mem2.values():
        count += value
    print('part 2:', count)

# returns a list of mems
def apply_v2(mask, mem, n):
    length = len(mask)
    memlist = []
    mem = list(mem)
    for x in range(n, length):
        if mask[x] == '1':
            mem[x] = mask[x]
        elif mask[x] == 'X':
            mem1 = mem.copy()
            mem1[x] = 0
            mem[x] = 1
            new_mem = apply_v2(mask, mem1, x + 1)
            memlist = memlist + new_mem
    memlist.append(mem)
    return memlist
           

with open('input14.txt', 'r') as inputfile:
    lines = inputfile.readlines()
    part2(lines)
