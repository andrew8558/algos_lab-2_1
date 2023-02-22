f = open('input.txt')
x = f.readline().split()
n = int(x[0])
height = int(x[1])
apples = {}
for i in range(n):
    apples[i+1] = [i for i in map(int, f.readline().split())]
f.close()


order = []
while apples:
    maximum = float("-inf")
    apple_for_eat = None
    for i in apples.keys():
        if height - apples[i][0] > 0:
            if apples[i][1] - apples[i][0] > maximum:
                maximum = apples[i][1] - apples[i][0]
                apple_for_eat = i
    if apple_for_eat:
        height += maximum
        order.append(apple_for_eat)
        apples.pop(apple_for_eat)
    else:
        break

f = open('output.txt', 'w')
if apples:
    f.write(str(-1))
else:
    s = ''
    for i in order:
        s += str(i) + ' '
    f.write(s)
f.close()
