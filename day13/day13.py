import math

def bus_time(bus, time):
    bus = int(bus)
    time = int(time)
    if time % bus == 0:
        return time
    else:
        return bus_time(bus, time + 1)

def check_time(bus, time):
    if bus == 'x':
        return True
    else:
        bus = int(bus)
        time = int(time)
        if time % bus == 0:
            return True
        else: 
            return False

with open('input13.txt', 'r') as inputfile:
    lines = inputfile.readlines()
    time = lines[0].rstrip('\n')
    schedule = lines[1].split(',')
    busses = []
    for bus in schedule:
        if bus != 'x':
            busses.append(bus)
    
    shortest = (busses[0], bus_time(busses[0], time))
    for bus in busses:
        prev_bus, prev_time = shortest
        curr_time = bus_time(bus, time)
        if curr_time < prev_time:
            shortest = (bus, curr_time)


    print(shortest)
    x, y = shortest
    print('part 1:', int(x) * (y - int(time)))
    
    
    num = 0
    mult = 1
    offset = 0
    for bus in schedule:
        if bus == 'x':
            offset += 1
            continue
        else:
            print(num, mult, bus, offset)
            bus = int(bus)
            count = 0
            while ((num + offset + count) % bus != 0):
                count = count + mult
            num = num + count
            mult = math.lcm(mult, bus)
            offset += 1
    print('part 2:', num)

