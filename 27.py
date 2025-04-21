# from math import dist
# file = open('27_A_21425.txt')
# def centroid(c):
#     n = len(c)
#     min_s_dist, ind = float('inf'), 0
#     for i in range(n):
#         s = 0
#         for j in range(n):
#             s += dist(c[i], c[j])
#         if s < min_s_dist:
#             min_s_dist = s
#             ind = i
#
#     return c[ind]
#
# c1, c2 = [], []
# for line in file:
#     x, y = [float(i.replace(',', '.')) for i in line.split()]
#     if x > 15:
#         c1.append([x, y])
#     else:
#         c2.append([x, y])
#
#
# x1, y1 = centroid(c1)
# x2, y2 = centroid(c2)
#
# print((x1 + x2) / 2 * 10_000, (y1 + y2) / 2 * 10_000)
# Ответ: 167990 73043

# from math import dist
# file = open('27_B_21425.txt')
# def centroid(c):
#     n = len(c)
#     min_s_dist, ind = float('inf'), 0
#     for i in range(n):
#         s = 0
#         for j in range(n):
#             s += dist(c[i], c[j])
#         if s < min_s_dist:
#             min_s_dist = s
#             ind = i
#
#     return c[ind]
#
# c1, c2, c3 = [], [], []
# for line in file:
#     x, y = [float(i.replace(',', '.')) for i in line.split()]
#     if x < 0:
#         c1.append([x, y])
#     elif x > 0 and y > 0:
#         c2.append([x, y])
#     else:
#         c3.append([x, y])
#
#
# x1, y1 = centroid(c1)
# x2, y2 = centroid(c2)
# x3, y3 = centroid(c3)
#
# print((x1 + x2 + x3) / 3 * 10_000, (y1 + y2 + y3) / 3 * 10_000)
# Ответ: 122627 29105

