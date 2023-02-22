f = open('input.txt')
string = f.readline()
f.close()


def operation(op, first, second):
    if op == '+':
        return first + second
    if op == '-':
        return first - second
    if op == '*':
        return first * second


def min_and_max(i, j, mini, maxi, op):
    minimum = float("+inf")
    maximum = float("-inf")
    for k in range(i, j):
        a = operation(op[k], maxi[i][k], maxi[k+1][j])
        b = operation(op[k], maxi[i][k], mini[k+1][j])
        c = operation(op[k], mini[i][k], maxi[k+1][j])
        d = operation(op[k], mini[i][k], mini[k+1][j])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return minimum, maximum


def max_value(d, op):
    n = len(d)
    m = [[0]*n for i in range(n)]
    M = [[0]*n for i in range(n)]
    for i in range(n):
        m[i][i] = d[i]
        M[i][i] = d[i]
    for s in range(n-1):
        for i in range(n-s-1):
            j = i + s + 1
            m[i][j], M[i][j] = min_and_max(i, j, m, M, op)
    return M[0][n-1]


digits = []
operations = []
for i in string:
    if i.isdigit():
        digits.append(int(i))
    else:
        operations.append(i)


f = open('output.txt', 'w')
f.write(str(max_value(digits, operations)))
f.close()
