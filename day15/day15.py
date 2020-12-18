def part1(xs):
    count = 0
    prev_time = dict()
    prev_turn = 0
    for x in xs:
        count += 1
        x = int(x)
        prev_time[x] = (count, 0)
        prev_turn = x
    play_game(prev_time, prev_turn, count)

def play_game(prev_dict, prev_turn, count):
    while count < 30000000:
        count += 1
        if prev_turn not in prev_dict.keys():
            prev_dict[prev_turn] = (count, 0)
            prev_turn = 0
        else:
            x, y = prev_dict[prev_turn]
            if y == 0:
                prev_turn = 0
                v, w = prev_dict[0]
                prev_dict[0] = (count, v)
            else:    
                prev_turn = x - y
                if prev_turn not in prev_dict.keys():
                    prev_dict[prev_turn] = (count, 0)
                else:
                    v, w = prev_dict[prev_turn]
                    prev_dict[prev_turn] = (count, v)
    print('count:', count, 'value:', prev_turn)

with open('input15.txt', 'r') as inputfile:
    lines = inputfile.readlines()
    string = lines[0].split(',')
    part1(string)
