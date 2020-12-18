def checker(xs):
    questions = set()
    for x in xs:
        x = x.rstrip('\n')
        for elem in x:
            questions.add(elem)
    return len(questions)

def checker2(xs):
    #TODO fix empty set intersection anything will be empty set
    questions = set()
    count = 0
    for x in xs:
        curr = set()
        for elem in x.rstrip('\n'):
            curr.add(elem)
        if count == 0:
            questions = curr
            count += 1
        else:
            questions = questions.intersection(curr)
    return len(questions)

# part 1
with open('input6.txt', 'r') as inputfile:
    lines = inputfile.readlines()
    inputbuffer = []
    count = 0
    count2 = 0
    #print(lines)
    for line in lines:
        if line == '\n':
            #check inputbuffer
            #print(inputbuffer)
            num = checker(inputbuffer)
            count += num
            num2 = checker2(inputbuffer)
            count2 += num2
            inputbuffer = []
        else:
            inputbuffer.append(line)
    count += checker(inputbuffer)
    count2 += checker2(inputbuffer)
    print('part 1:', count)
    print('part 2:', count2)
