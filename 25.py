def dividers(n):
    divs = set()
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            divs.add(d)
            divs.add(n // d)
    return sorted([x for x in divs if x % 10 == 7 and x != 7])


num = 1_125_000 + 1
count = 0
while count < 5:
    res = dividers(num)
    if len(res) > 0:
        count += 1
        print(num, min(res))
    num += 1
# Ответ:
# 1125003 467
# 1125006 97
# 1125009 17
# 1125011 3187
# 1125012 177