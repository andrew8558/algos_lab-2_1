def check1(price, j, cur, coupons):
    x = price[j:]
    x.sort()
    count = len(x) - x.index(cur) - 1
    if coupons <= count:
        return False
    else:
        return True


def check2(price, j, cur, coupons):
    count = 0
    for i in range(j+1, len(price)):
        if price[i] > cur:
            count += 1
        if 100 < price[i] <= cur and count < coupons:
            return True
    if count < coupons:
        return True
    else:
        return False


f = open('input.txt')
n = int(f.readline())
price = []
for i in range(n):
    price.append(int(f.readline()))
f.close()

coupons = 0
spent_money = 0
days_left = n
spent_coupons = 0
coupon_days = []

for i in price:
    if coupons == 0:
        if i > 100:
            coupons += 1
        spent_money += i
    elif coupons >= days_left:
        coupon_days.append(n - days_left + 1)
        coupons -= 1
        spent_coupons += 1
    elif coupons < days_left:
        if i <= 100:
            if check1(price, n - days_left, i, coupons):
                coupon_days.append(n - days_left + 1)
                coupons -= 1
                spent_coupons += 1
            else:
                spent_money += i
        else:
            if check2(price, n - days_left, i, coupons):
                coupon_days.append(n - days_left + 1)
                coupons -= 1
                spent_coupons += 1
            else:
                spent_money += i
                coupons += 1
    days_left -= 1

f = open('output.txt', 'w')
f.write(f'{spent_money}\n')
f.write(f'{coupons} {spent_coupons}\n')
for i in coupon_days:
    f.write(f'{i}\n')
f.close()
