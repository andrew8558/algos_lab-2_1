f = open('input.txt')
n = int(f.readline())
A = []
for i in range(n):
    A.append(f.readline())
f.close()

lessons = [i.split() for i in A]
for i in range(n):
    A = lessons[i]
    lessons[i] = [int(A[0]), int(A[1])]
last_lesson = 0
count = 0
lessons.sort()

for i in lessons:
    if i[0] >= last_lesson:
        last_lesson = i[1]
        count += 1
    elif i[1] < last_lesson:
        last_lesson = i[1]

f = open('output.txt', 'w')
f.write(str(count))
f.close()
