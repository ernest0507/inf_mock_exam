from string import digits, ascii_uppercase

alph = (digits + ascii_uppercase)[:12]

file = open('24_21421.txt')
a = file.readline()
file.close()

n = ''
countm = 0
for x in a:
    if x in alph:
        if len(n) == 0 and x != '0':
            n += x
        elif len(n) > 0:
            n += x
        if int(n, 12) % 2 == 0:
            countm = max(countm, len(n))
    else:
        n = ''
print(countm)


