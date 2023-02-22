f = open('INPUT.txt')
x = f.readline().split()
k = int(x[1])
s = f.readline().strip()
draw = ''
for i in s:
    draw += i
    draw += '-'
string = draw[:-1]
length = len(string)
f.close()


count = 0
for i in range(length):
    if string[i] != '-':
        count += 1
    remainder = k
    for j in range(1, length+1):
        if i-j >= 0 and i+j <= length-1:
            if string[i-j] != '-':
                if string[i-j] == string[i+j]:
                    count += 1
                else:
                    if remainder > 0:
                        count += 1
                    remainder -= 1
                    if remainder == -1:
                        break
        else:
            break
f = open('OUTPUT.txt', 'w')
f.write(str(count))
f.close()
