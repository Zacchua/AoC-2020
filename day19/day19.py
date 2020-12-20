def part1(xs):
    rules = []
    messages = []
    inputbuffer = []
    count = 0
    for x in xs:
        if x == '\n':
            rules = inputbuffer
            inputbuffer= []
        else:
            inputbuffer.append(x.rstrip('\n'))
    messages = inputbuffer
    # print(rules, messages)
    valid= find_valids(rules)
    for message in messages:
        if message in valid:
            count += 1
    print(count)

def find_valids(rules):
    rule_dict = {}
    for rule in rules:
        rule = rule.split(':')
        rule_dict[int(rule[0])] = rule[1].lstrip()
    valids = recurse(rule_dict, 0, [])
    return valids

def recurse(rules_dict, num, to_add):
    if rules_dict[num] == '"a"':
        new_add = []
        if len(to_add) > 0:
            for item in to_add:
                new_item = item + 'a'
                new_add.append(new_item)
        else:
            new_add.append('a')
        return new_add
    elif rules_dict[num] == '"b"':
        new_add = []
        if len(to_add) > 0:
            for item in to_add:
                new_item = item + 'b'
                new_add.append(new_item)
        else:
            new_add.append('b')
        return new_add
    else:
        afterBar = False
        before = to_add
        after = to_add.copy()
        next_num = ''
        for elem in rules_dict[num]:
            if elem == '|':
                afterBar = True
            elif elem == ' ':
                if next_num != '':
                    next_num = int(next_num)
                    if afterBar:
                        after = recurse(rules_dict, next_num, after)
                    else:
                        before = recurse(rules_dict, next_num, before)
                    next_num = ''
            else:
                next_num = next_num + elem
        if next_num != '' and afterBar:
            after = recurse(rules_dict, int(next_num), after)
        elif next_num != '':
            before = recurse(rules_dict, int(next_num), before)
        return before + after
        



with open('input19.txt', 'r') as inputfile:
    lines = inputfile.readlines()
    part1(lines)