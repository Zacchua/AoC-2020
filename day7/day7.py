def dict_entry(xs):
    key = xs[0]
    values = xs[1]
    new_val = []
    if "no other bags" in values:
        new_val = None
    else:
        for entry in values:
            entry = entry[2:]
            if entry[-1] == 's':
                entry = entry[:-1]
            new_val.append(entry)
    return (key[:-1], new_val)

def dict_entry_2(xs):
    key = xs[0]
    values = xs[1]
    new_vals = []
    if 'no other bags' in values:
        new_vals= None
    else:
        for entry in values:
            num = entry[0]
            bag = entry[2:]
            if bag[-1] == 's':
                bag = bag[:-1]
            new_vals.append((num, bag))
    return (key[:-1], new_vals)

def checker(tup, dict1):
    bag, contained = tup
    if contained == None:
        return False
    elif 'shiny gold bag' in contained:
        return True
    elif len(contained) > 1:
        #TODO this only checks the first item in each list
        return checker((contained[0], dict1[contained[0]]), dict1) or checker((bag, contained[1:]), dict1)
    else:
        return checker((contained[0], dict1[contained[0]]), dict1)

def no_of_bags(xs, dict2):
    if xs is None:
        return 1
    elif len(xs) == 0:
        return 0
    else:
        no, bag = xs[0]
        if dict2[bag] is None:
            return (int(no) * no_of_bags(dict2[bag], dict2)) + no_of_bags(xs[1:], dict2)
        else:
            return (int(no) * no_of_bags(dict2[bag], dict2)) + no_of_bags(xs[1:], dict2) + int(no) 

with open('input7.txt', 'r') as inputfile:
    lines = inputfile.readlines()
    bags = {}
    part2 = {}
    count = 0
    for line in lines:
        line = line.rstrip(".\n")
        line = line.split(" contain ")
        line[1] = line[1].split(", ")
        key, values = dict_entry(line)
        key2, values2 = dict_entry_2(line)
        bags[key] = values
        part2[key2] = values2
    list_of_bags = bags.items()
    for x in list_of_bags:
        if checker(x, bags):
            count += 1
    
    print('part 1:', count)
    print('home:', no_of_bags(part2['shiny gold bag'], part2))