# def sumTo(n):
#     result = (n * (n + 1)) // 2
#     return result
# # print(sumTo(10))
# n = int(input("Enter a number: "))
# print("sum is", sumTo(n))



# import turtle
# def drawStar(t, n, size):
#     angle = 180 - 180/n
#     for i in range(n):
#         turtle.forward(size)
#         turtle.right(angle)
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.pensize(3)
# drawStar(t,3,100)
# wn.exitonclick()



# import numbers

# def sumTo(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#     return total
# print(sumTo(10))
# n = int(input("enter a number: "))
# print("sum is", sumTo(n))



# import turtle
# def drawSprite(turtle, legs, length):
#     angle = 360 / legs
#     for i in range(legs):
#         turtle.forward(length)
#         turtle.backward(length)
#         turtle.left(angle)



# import math
# def mySqrt(x):
#     guess = x/2
#     for i in range (20):
#         guess = (1/2) * (guess+x / guess)
#     return guess
# n = int(input("Enter a positive integer : "))
# print("the result is :", mySqrt(n))
# print("the result is :", math.sqrt(n))



# import turtle
# def drawSprite(turtle, legs, length):
#     angle = 360 / legs
#     for i in range(legs):
#         turtle.forward(length)
#         turtle.backward(length)
#         turtle.left(angle)
#
# def fancySquare(t, size):
#     for i in range(4):
#         drawSprite(t, 8 ,20)
#         t.forward(size)
#         t.left(90)
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.color("red")
# t.pensize(2)
#
# fancySquare(t, 100)
#
# wn.exitonclick()



# import turtle
#
# def drawTip(t, size):
#     t.begin_fill()
#     t.left(90)
#     t.forward(size/2)
#     t.right(120)
#     t.forward(size)
#     t.right(120)
#     t.forward(size)
#     t.right(120)
#     t.forward(size/2)
#     t.right(90)
#     t.end_fill()
#
# def drawSpriteWithTips(someturtle, legs, length):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.forward(length)
#         drawTip(someturtle, 10)
#         t.backward(length)
#         someturtle.left(angle)
#
# def fancysquare(t, size):
#     for corner in range(4):
#         drawSpriteWithTips(t, 8, 20)
#         t.forward(size)
#         t.left(90)
#
# wn = turtle.Screen()
# wn.bgcolor("pink")
# t = turtle.Turtle()
# t.speed(0)
# t.pensize(3)
#
# fancysquare(t, 100)
# wn.exitonclick()



# def PositiveorNot(x):
#     if x > 0:
#         return "Positive"
#     elif x == 0:
#         return "zero"
#     else:
#         return "Negative"
#
# numbers=[-7, 5, 0]
# for i in numbers:
#     print(PositiveorNot(i))
#
# x=int(input("Enter a number: "))
# print(PositiveorNot(x))



# import turtle
#
# def drawBar(t, height,gap):
#     t.penup()
#     t.left(90)
#     t.forward(height+gap)
#     t.write(" "+str(height))
#     t.backward(height+gap)
#     t.right(90)
#     t.pendown()
#
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# def barChart(data):
#         maxheight = max(data)
#
#         num_bars = len(data)
#         border = 10
#
#         gap = (maxheight - border) / 25
#
#         wn = turtle.Screen()
#         wn.bgcolor("lightgreen")
#
#         right = 40 * num_bars + border
#         top = maxheight + 4 * border
#
#         wn.setworldcoordinates(-border, -border, right, top)
#         t = turtle.Turtle()
#         t.color("blue")
#         t.fillcolor("red")
#         t.pensize(3)
#         for height in data:
#             drawBar(t, height, gap)
#
#         wn.exitonclick()
#
# data = [48, 117, 200, 240, 160, 260, 220]
# barChart(data)