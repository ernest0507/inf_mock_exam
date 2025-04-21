alph = 'ДГИАШЭ'

count = 0
for a1 in 'ДГШ':
    for a2 in alph:
        for a3 in alph:
            for a4 in alph:
                for a5 in 'ИАЭ':
                    count += 1

print(count)
# Ответ: 1944
