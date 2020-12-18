def check(xs):
    true = True
    for x in xs:
        x = x.rstrip("\n")
        y = x.split(" ")
        for z in y:
            if z[0 : 3] == "byr":
                if int(z[4:]) < 1920 or int(z[4:]) > 2002: 
                    true = False
            elif z[0: 3] == "iyr":
                if int(z[4:]) < 2010 or int(z[4:]) > 2020:
                    true = False
            elif z[0 : 3] == "eyr":
                if int(z[4:]) < 2020 or int(z[4:]) > 2030:
                    true = False
            elif z[0 : 3] == "hgt":
                if z[-2:] == "cm":
                    if int(z[4:-2]) < 150 or int(z[4:-2]) > 193:
                        true = False
                elif z[-2:] == "in":
                    if int(z[4:-2]) < 59 or int(z[4: -2]) > 76:
                        true = False
                else:       
                    true = False
            elif z[0:3] == 'hcl':
                if z[4] == '#':
                    if not checkhcl(z[5:]):
                        true = False
                else:
                    true = False
            elif z[0 : 3] == 'ecl':
                ecl = z[4:]
                if not (ecl == 'amb' or ecl == 'blu' or ecl == 'brn' or ecl == 'gry' or ecl == 'grn' or ecl == 'hzl' or ecl =='oth'):
                    true = False
            elif z[0 : 3] == 'pid':
                if not len(z[4:]) == 9:
                        true = False                    
    return true

def checkhcl(string):
    if len(string) == 6:
        for x in range(6):
            y = string[x]
            if y == '0' or y == '1' or y =='2' or y == '3' or y == '4' or y == '5' or y == '6' or y == '7' or y == '8' or y == '9' or y == 'a' or y == 'b' or y =='c' or y == 'd' or y == 'e' or y == 'f':
                return True
            else:
                return False
    else:
        return False

#part 1
with open ("input.txt", "r") as inputfile:
    inputbuffer = []
    count = 0
    lines = inputfile.readlines()
    for line in lines:
        if line == '\n':
            curr = 0
            present = False
            for x in inputbuffer:
                splitted = x.split(" ")
                for y in splitted:
                    if y[0 : 3] == 'cid':
                        present = True
                curr += len(splitted)
            if curr == 7 and not present:
                count += 1
            elif curr == 8:
                count += 1
            inputbuffer = []
        else:
            inputbuffer.append(line)
    print('part 1', count)

#part 2
with open('input.txt' ,'r') as inputs:   
    inputbuffer = []
    count2 = 0
    lines = inputs.readlines()
    for line in lines:
        if line == '\n':
            curr = 0
            present = False
            for x in inputbuffer:
                splitted = x.split(" ")
                for y in splitted:
                    if y[0: 3] == "cid":
                        present = True
                curr += len(splitted)
            if curr == 7 and not present:
                if check(inputbuffer):
                    count2 += 1
            elif curr == 8:
                if check(inputbuffer):
                    count2 += 1
            inputbuffer = []
        else:
            inputbuffer.append(line)
    print("part 2", count2)







