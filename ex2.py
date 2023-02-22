f = open('input.txt')
distance = int(f.readline())
size = int(f.readline())
cur_size = size
n = int(f.readline())
s = f.readline().split()
stops = [int(i) for i in s]
passed_way = 0
count = 0

for i in range(n-1):
    distance_between_stops = stops[i] - passed_way
    if distance_between_stops - cur_size <= 0:
        passed_way += distance_between_stops
        cur_size = cur_size - passed_way
        if stops[i+1] - (passed_way + cur_size) > 0:
            count += 1
            cur_size = size
    else:
        count = -1
        break

if passed_way + cur_size < distance:
    if stops[-1] - (passed_way + cur_size) <= 0:
        if stops[-1] + size >= distance:
            count += 1
        else:
            count = -1
    else:
        count = -1


f = open('output.txt', 'w')
f.write(str(count))
