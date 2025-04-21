file = open('26_21424.txt')
N = int(file.readline())
boxes = sorted([int(x) for x in file])
file.close()


def f(i, boxes):
    prev = boxes[i]
    count = 1
    for curr in boxes[i + 1:]:
        if curr - prev >= 9:
            count += 1
            prev = curr
    return count


i = 1
mcount = f(0, boxes)
while f(i, boxes) == mcount:
    i += 1

print(mcount, boxes[i - 1])
# Ответ: 1040 57
