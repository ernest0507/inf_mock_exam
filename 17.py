file = open('17_21416.txt')
nums = [int(x) for x in file]
file.close()

neg_amount = sum([x for x in nums if x < 0])

ans = []
for i in range(len(nums) - 2):
    a, b, c = nums[i], nums[i + 1], nums[i + 2]
    if min(a, b, c) * max(a, b, c) > neg_amount:
        ans.append(abs(a + b + c))

print(len(ans), max(ans))
# Ответ: 10007 28854

