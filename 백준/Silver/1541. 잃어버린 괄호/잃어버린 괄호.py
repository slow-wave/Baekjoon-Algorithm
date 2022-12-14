import sys

p = sys.stdin.readline().rstrip()
n, prev = '', ''
ans = 0

for c in p:
    if c.isdigit():
        n += c
        continue
    else:
        if c == '-':
            if prev == '' or prev == '+':
                ans += int(n)
            else:
                ans -= int(n)
            prev = '-'
        else:
            if prev == '' or prev == '+':
                ans += int(n)
                prev = '+'
            else:
                ans -= int(n)
                prev = '-'

        n = ''

if prev == '-':
    ans -= int(n)
else:
    ans += int(n)

print(ans)