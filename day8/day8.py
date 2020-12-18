def execute(string, pointer, ACC):
    if string[0] == 'nop':
        return (pointer + 1, ACC)
    elif string[0] == 'acc':
        op = string[1][0]
        num = int(string[1][1:])
        if op == '+':
            ACC += num
        elif op == '-':
            ACC -= num
        return (pointer + 1, ACC)
    elif string[0] == 'jmp':
        op = string[1][0]
        num = int(string[1][1:])
        if op == '+':
            return (pointer + num, ACC)
        elif op == '-':
            return (pointer - num, ACC)

def checker(n, lines):
    done = []
    ACC = 0
    pointer = 0
    print('new try')
    for i in range(n + 1):
        done.append(False)
    while done[pointer] == False:
        if pointer == n:
            print('part 2:', ACC)
            return True
        else:
            done[pointer] = True 
            num = execute(lines[pointer], pointer, ACC)
            pointer, ACC = num
            if pointer > (n):
                return False
    return False


with open('input8.txt', 'r') as inputfile:
    lines = inputfile.readlines()
    pointer = 0
    done = []
    ACC = 0
    n = len(lines)
    print(n)

    # initialises the done array to False
    for i in range(n):
        lines[i] = lines[i].rstrip('\n')
        done.append(False)
        lines[i] = lines[i].split(' ')

    while done[pointer] == False:
        done[pointer] = True
        num = execute(lines[pointer], pointer, ACC)
        pointer, ACC = num
    print('part 1:', ACC)
    
    for i in range(n):
        if lines[i][0] == 'nop':
            lines[i][0] = 'jmp'
            if checker(n, lines):
                break 
            else:
                lines[i][0] = 'nop'
        elif lines[i][0] == 'jmp':
            lines[i][0] = 'nop'
            if checker(n, lines):
                break
            else:
                lines[i][0] = 'jmp'
    # print(lines)
