# takes in a list of equations
def part1(xs): 
    count = 0
    for statement in xs:
        count += equate(statement)
    print('part 1:', count)

def equate(string):
    stack = []
    op = 'null'
    openParen = 0
    closeParen = 0
    inParen = False
    paren = ""
    for x in range(len(string)):
        if inParen:
            if string[x] != ')' and string[x] != '(':
                paren = paren + string[x]
            elif string[x] == '(':
                openParen += 1
                paren = paren + string[x]
            else:
                closeParen += 1
                if closeParen == openParen:
                    inParen = False
                    res = equate(paren)
                    paren = ""
                    if len(stack) == 0:
                        stack.append(res)
                    else:
                        num = stack.pop()
                        if op == '+':
                            stack.append(res + num)
                        else:
                            stack.append(res * num)
                        op = 'null'
                else:
                    paren = paren + string[x]
        elif string[x] == '+':
            op = '+'
        elif string[x] == '*':
            op = '*'
        elif string[x] == " ":
            continue
        elif string[x] == '(':
            openParen += 1
            inParen = True
        else:
            if op == 'null':
                stack.append(int(string[x]))
            else:
                num = stack.pop(-1)
                if op == '+':
                    stack.append(num + int(string[x]))
                else:
                    stack.append(num * int(string[x]))
                op = 'null'
    return stack[0]

def part2(xs):
    count = 0
    for line in xs:
        # print(evaluate(line))
        count += evaluate(line)
    print('part 2:', count)

def evaluate(string):
    stack = []
    op = 'null'
    openParen = 0
    closeParen = 0
    inParen = False
    paren = ""
    ret = 1
    for x in range(len(string)):
        if inParen:
            if string[x] != ')' and string[x] != '(':
                paren = paren + string[x]
            elif string[x] == '(':
                openParen += 1
                paren = paren + string[x]
            else:
                closeParen += 1
                if closeParen == openParen:
                    inParen = False
                    res = evaluate(paren)
                    paren = ""
                    if len(stack) == 0 or op == '*':
                        stack.append(res)
                    else:
                        num = stack.pop()
                        stack.append(res + num)
                        op = 'null'
                else:
                    paren = paren + string[x]
        elif string[x] == '+':
            op = '+'
        elif string[x] == '*':
            op = '*'
        elif string[x] == " ":
            continue
        elif string[x] == '(':
            openParen += 1
            inParen = True
        else:
            if op == 'null' or op == '*':
                stack.append(int(string[x]))
            else:
                num = stack.pop(-1)
                stack.append(num + int(string[x]))
                op = 'null'
    for item in stack:
        ret *= item
    return ret

with open('input18.txt', 'r') as inputfile:
    lines = inputfile.readlines()
    statements = []
    for line in lines:
        statements.append(line.rstrip('\n'))
    part1(statements)
    part2(statements)
