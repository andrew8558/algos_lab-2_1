f = open('INPUT.txt')
s = f.readline().split()
n = int(s[0])
m = int(s[1])
r = s[2]
deck = f.readline().split()
board_cards = f.readline().split()
f.close()

rang = {'6': 1, '7': 2, '8': 3, '9': 4, 'T': 5, 'J': 6, 'Q': 7, 'K': 8, 'A': 9, 'X': 10}

flag = 0
for i in board_cards:
    card = 'X' + r
    for j in deck:
        if (rang[j[0]] > rang[i[0]] and i[1] == j[1]) or (j[1] == r and i[1] != r):
            if card[1] == r and j[1] != r:
                card = j
            elif rang[j[0]] < rang[card[0]] and card[1] == j[1]:
                card = j
    if card == ('X'+r):
        flag = 1
        break
    else:
        deck.remove(card)

f = open('OUTPUT.txt', 'w')
if flag == 0:
    f.write('YES')
else:
    f.write('NO')
f.close()
