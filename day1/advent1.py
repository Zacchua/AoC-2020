import csv

nums = []
with open('input2.csv') as csv_file:
    reader = csv.DictReader(csv_file, delimiter = ",")
    for x in reader:
        nums.append(int(x['\ufeffnum']))

for x in range(len(nums)):
    for y in range(1, len(nums)):
        for z in range(2, len(nums)):
            if nums[x] + nums[y] + nums[z]== 2020:
                print (nums[x] * nums[y] * nums[z])