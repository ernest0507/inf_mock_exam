from turtle import *

screensize(1500, 1500)
tracer(0)
k = 15
lt(90)
down()

rt(30)
for _ in range(3):
    rt(150)
    fd(6 * k)
    rt(30)
    fd(12 * k)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, 'red')

exitonclick()
# Ответ: 29
