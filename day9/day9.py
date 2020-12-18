def part1check(xs, buf, n):
    num = int(xs[n].rstrip('\n'))
    for x in buf:
        x = int(x)
        for y in buf:
            y = int(y)
            if x != y and x + y == num:
                buf.append(num)
                buf.pop(0)
                return part1check(xs, buf, n + 1)
    print('Part 1:', num)
    return num

def part2(xs, num):
    def helper(start, curr, sum_so_far, count):
        sum_so_far += int(xs[curr])
        print(sum_so_far)
        count.append(int(xs[curr]))
        if sum_so_far == num:
            return count
        elif sum_so_far > num:
            return helper(start + 1, start + 1, 0, [])
        else:
            return helper(start, curr + 1, sum_so_far, count)
    return helper(0, 0, 0, [])

def part2v2(xs, num):
    length = len(xs)
    for x in range(length):
        numx = int(xs[x])
        sum_so_far = numx
        count = 1
        ys = [numx]
        for y in range(x + 1, length):
            numy = int(xs[y])
            sum_so_far += numy
            ys.append(numy)
            count += 1
            print(sum_so_far)
            if sum_so_far == num and count >= 2:
                return ys
            elif sum_so_far > num:
                break

def small(xs):
    smallest = xs[0]
    for i in range(len(xs)):
        if xs[i] < smallest:
            smallest = xs[i]
    return smallest

def large(xs):
    largest = xs[0]
    for i in range(len(xs)):
        if xs[i] > largest:
            largest = xs[i]
    return largest


with open('input9.txt', 'r') as inputfile:
    lines = inputfile.readlines()
    num_buffer = []
    for x in range(25):
        num_buffer.append(lines[x])
    invalid = part1check(lines, num_buffer, 25)
    ys = part2v2(lines, invalid)
    print(small(ys) + large(ys))
