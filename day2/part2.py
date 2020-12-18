import csv
import string

unfiltered = []
filtered = []
valid = 0
with open('input.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    for x in reader:
        unfiltered.append(x)

unfiltered.pop(0)

for x in range(len(unfiltered)):
    filtered.append(unfiltered[x][0].split(":"))

for x in filtered:
    policy = x[0]
    password = x[1]
    letter = policy.split(' ')[1]
    window = policy.split(' ')[0]
    minimum = int(window.split('-')[0])
    maximum = int(window.split('-')[1])
    count = 0
    present = 0
    for element in password:
        if count == minimum or count == maximum:
            if element == letter:
                present += 1
        count += 1

    if present == 1:
        valid += 1

print(valid)