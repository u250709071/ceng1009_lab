# import random
#
# for i in range(10):
#     print(random.random())



# import random
#
# for i in range(10):
#     print(random.randint(25,35))



# import math
# from math import hypot
# a = int(input("Enter the first side: "))
# b = int(input("Enter the second side: "))
#
# hypotenuse2 = math.sqrt(a**2 + b**2)
# print("The hypotenuse is ", hypotenuse2)
#
# hypotenuse1 = math.hypot(3, 4)
# print(hypotenuse1)




# import math
# from math import radians
#
# radius = float(input("Enter the radius of the circle: "))
# def areaOfCircle(r):
#     return math.pi * r**2
# print(areaOfCircle(radius))



# import turtle
#
# def drawStar(t, side):
#     for i in range(5):
#         t.fd(side)
#         t.right(144)
#
# screen = turtle.Screen()
# tess = turtle.Turtle()
# drawStar(tess, 100)
#
# screen.exitonclick()



# import turtle
#
# def drawSquare(t, side):
#     for i in range(4):
#         t.fd(side)
#         t.left(90)

# screen = turtle.Screen()
# leonardo = turtle.Turtle()
# screen.bgcolor("lightgreen")
# leonardo.color("pink")
# leonardo.pensize(4)
#
# for i in range(5):
#     drawSquare(leonardo, 20)
#     leonardo.penup()
#     leonardo.fd(40)
#     leonardo.pendown()
#
# screen.exitonclick()

# import turtle
# screen = turtle.Screen()
# mahmut = turtle.Turtle()
# screen.bgcolor("lightgreen")
# mahmut.color("red")
# mahmut.pensize(3)
#
# for i in range(20, 120, 20):
#     drawSquare(mahmut, i)
#     mahmut.penup()
#     mahmut.backward(10)
#     mahmut.right(90)
#     mahmut.fd(10)
#     mahmut.left(90)
#     mahmut.pendown()
#
# screen.exitonclick()

