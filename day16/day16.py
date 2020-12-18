def part1(cat, myTix, nearTix):
    Ranges = getRanges(cat)
    myTix =  getTix(myTix)
    nearTix = getTix(nearTix)
    invalid = 0
    validTix = []
    possible_fields = []
    for ticket in nearTix:
        notValid = False
        ticketField = []
        for num in ticket:
            num = int(num)
            result, field = checkNum(Ranges, num)
            ticketField.append(field)
            if not result:
                invalid += num
                notValid = True
        if not notValid:
            validTix.append(ticket)
        if [] not in ticketField:
            possible_fields.append(ticketField)
    print('part1:', invalid)
    order = getOrder(possible_fields)
    part2 = 1
    for x in range(len(order)):
        for item in order[x]:
            if item <= 6:
                print(x)
                part2 *= int(myTix[0][x])
    print('part 2:', part2)


def getOrder(xss):
    order = []
    used = set()
    ones = 0
    for x in range(len(xss[0])):
        order.append(xss[0][x])
    print('before:', order)
    for ticket in xss:
        for x in range(len(ticket)):
            inter = order[x].intersection(ticket[x])
            if len(inter) > 0:
                order[x] = inter
    print('mid:', order)
    while len(used) <len(order):
        for x in range(len(order)):
            if len(order[x]) == 1:
                for item in order[x]:
                    used.add(item)
                ones +=1
            else:
                order[x] = order[x].difference(used)
    return order




def checkNum(ranges, num):
    cat = 0
    pos = set()
    valid = False
    for field in ranges:
        cat += 1
        for tup in field:
            low, high = tup
            low = int(low)
            high = int(high)
            if (num >= low and num <= high):
                valid = valid or True
                pos.add(cat)
    return (valid, pos)

def getRanges(xs):
    ranges = []
    for x in xs:
        x = x.split(': ')
        x = x[1].split(' or ')
        curr = []
        for item in x:
            item = item.split('-')
            curr.append((item[0], item[1]))
        ranges.append(curr)
    return ranges

def getTix(xs):
    xs.pop(0)
    tix = []
    for x in xs:
        x = x.split(',')
        tix.append(x)
    return tix


with open('input16.txt', 'r') as inputfile:
    lines = inputfile.readlines()
    cat = []
    myTix = []
    nearTix = []
    inputBuffer = []
    for line in lines:
        if line == '\n':
            if len(cat) == 0:
                cat = inputBuffer.copy()
            elif len(myTix) == 0:
                myTix = inputBuffer.copy()
            else:
                nearTix = inputBuffer.copy()
            inputBuffer = []
        else:
            inputBuffer.append(line.rstrip('\n'))
    nearTix = inputBuffer.copy()
    part1(cat, myTix, nearTix)
