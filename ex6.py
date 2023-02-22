def largest_number(digits):
    answer = ''
    while digits:
        max_digit = '0'
        for digit in digits:
            if max_digit.startswith(digit) and digit[0] > max_digit[len(digit)]:
                max_digit = digit
            elif digit.startswith(max_digit) and max_digit[0] <= digit[len(max_digit)]:
                max_digit = digit
            elif digit > max_digit and not digit.startswith(max_digit):
                max_digit = digit
        answer += max_digit
        digits.remove(max_digit)
    return answer


f = open('input.txt')
n = int(f.readline())
Digits = f.readline().split()
f.close()

f = open('output.txt', 'w')
f.write(largest_number(Digits))
f.close()
