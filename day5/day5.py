import math

#part 1 finding the highest seat id: row * 8 + column

def checkrow(row_string, range_of_row):
        low, high = range_of_row
        if len(row_string) == 1:
                if row_string[0] == 'F':
                        return low
                elif row_string[0] == 'B': 
                        return high
        else:
                if row_string[0] == 'F':
                        mid = math.floor((high + low) / 2)
                        return checkrow(row_string[1:], (low, mid))
                elif row_string[0] == 'B':
                        mid = math.ceil((high + low) / 2)
                        return checkrow(row_string[1:], (mid, high))

def checkcol(col_string, range_of_cols):
        low, high = range_of_cols
        if len(col_string) == 2:
                if col_string[0] == 'L':
                        return low
                elif col_string[0] == 'R':
                        return high
        else:
                if col_string[0] == 'L':
                        mid = math.floor((high + low) / 2)
                        return checkcol(col_string[1:], (low, mid))
                elif col_string[0] == 'R':
                        mid = math.ceil((high + low) / 2)
                        return checkcol(col_string[1:], (mid, high))

with open("input.txt", "r") as inputfile:
        lines = inputfile.readlines()
        seat_id = 0
        seat_ids = []
        for line in lines:
                line.rstrip("\n")
                row_num = checkrow(line[:7], (0, 127))
                col_num = checkcol(line[7:], (0, 7))
                new_seat = (row_num * 8) + col_num
                seat_ids.append(new_seat)
                if new_seat > seat_id:
                        seat_id = new_seat
        print("part 1:", seat_id)

        for x in range(seat_id):
                if x not in seat_ids:
                        if (x + 1) in seat_ids:
                                if (x - 1) in seat_ids:
                                        print('part 2:', x)
