from string import digits, ascii_uppercase

alph = (digits + ascii_uppercase)[:21]

for x in alph:
    num1 = f'82934{x}2'
    num2 = f'2924{x}{x}7'
    num3 = f'67564{x}8'
    if (int(num1, 21) + int(num2, 21) + int(num3, 21)) % 20 == 0:
        print((int(num1, 21) + int(num2, 21) + int(num3, 21)) // 20)
# 72450445
