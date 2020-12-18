from itertools import combinations

COUNT = 0
def counter(xs, end, curr):
    print('xs:', xs)
    if curr == end:
        global COUNT 
        COUNT += 1
    else:
        ys = get_list(xs, curr)
        print(ys)
        for y in ys:
            zs = xs.copy()
            zs.remove(y)
            counter(zs, end, y)

def get_list(xs, curr):
    buff = []
    for x in xs:
        if x == curr + 1 or x == curr + 2 or x == curr + 3:
            buff.append(x)
    return buff

def combs(xss):
    total = 1
    for xs in xss:
        count = 0
        n = len(xs) - 3
        if n < 0:
            n = 0
        for i in range(n + 1, len(xs)):
            for j in combinations(xs, i):
                if xs[len(xs) - 1] in j:
                    count += 1
        total = total * (count + 1)
    return total 


with open('input10.txt', 'r') as inputfile:
    lines = inputfile.readlines()
    nums = []
    count_1 = 0
    count_3 = 0
    curr = 0
    sort = []
    sort_buf = []
    sort_2 = []
    for line in lines:
        nums.append(int(line))
    nums2 = nums.copy()

    while len(nums) != 0:
        if len(nums) == 1:
            highest = nums[0]
        buff = [0, 0, 0]
        for num in nums:
            if num == curr + 1:
                buff[0] = num
            elif num == curr + 2:
                buff[1] = num
            elif num == curr + 3:
                buff[2] = num
        for x in range(3):
            if buff[x] != 0:
                nums.remove(buff[x])
                curr = buff[x]
                sort_2.append(buff[x])
                if x == 0:
                    count_1 += 1
                    sort_buf.append(buff[x])
                elif x == 2:
                    count_3 += 1
                    if len(sort_buf) > 0:
                        sort.append(sort_buf)
                    sort_buf = []
                break
    sort.append(sort_buf)
    # for the device itself
    count_3 += 1
    print('count 1:', count_1, 'count_3:', count_3)
    print('part 1:', count_1 * count_3)

    # counter(nums2, highest, 0)
    # print(COUNT)
    print('part 2:', combs(sort))