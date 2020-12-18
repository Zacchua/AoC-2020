    
total = 1
for n in range(1, 8, 2):
     count = 0
     x = 0
     with open ('inputday3.txt', 'r') as mapfile:
         for line in mapfile:
            line = line.rstrip()
            if line[x % len(line)] == '#':
                count += 1
            x += n
     total = total * count
        

with open ('inputday3.txt', 'r') as mapfile:
    row_count = 0
    x = 0
    lastcount = 0
    for line in mapfile:
        line = line.rstrip()
        if row_count % 2 == 0:
            if line[x % len(line)] == '#':
                lastcount += 1
            x += 1
        row_count += 1
    total = total * lastcount

print(total)
