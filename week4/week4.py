# for i in range(100):
#     print("We like Python's turtles(!)")



# months = ["Jenuary", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# for month in months:
#     print("One of the months of the year is", month)



# numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# for newLine in numbers:
#     print(newLine)
# for square in numbers:
#     print(square**2)



# import turtle
# screen = turtle.Screen()
# dali = turtle.Turtle()
#
# dali.penup()
# dali.goto(-200,0)
# dali.pendown()
# for i in range(4):
#     dali.forward(75)
#     dali.left(90)
#
# dali.penup()
# dali.goto(-100,0)
# dali.pendown()
# for i in range(3):
#     dali.forward(75)
#     dali.left(120)
#
# dali.penup()
# dali.goto(0,0)
# dali.pendown()
# for i in range(6):
#     dali.forward(75*1/2)
#     dali.left(60)
#
# dali.penup()
# dali.goto(100,0)
# dali.pendown()
# for i in range(8):
#     dali.forward(60*1/2)
#     dali.left(45)
# screen.exitonclick()



# import turtle
# screen = turtle.Screen()
# sabri = turtle.Turtle()
#
# screen.bgcolor("lightgreen")
# sabri.shape("turtle")
# sabri.color("blue")
# sabri.pensize(3)
# sabri.stamp()
# sabri.penup()
# for i in range(12):
#     sabri.forward(125)
#     sabri.pendown()
#     sabri.forward(25)
#
#     sabri.penup()
#     sabri.forward(25)
#     sabri.stamp()
#     sabri.backward(175)
#     sabri.left(30)
#
# screen.exitonclick()



# import turtle
# screen = turtle.Screen()
# pirate = turtle.Turtle()
# turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]
#
# for angle in turns:
#     pirate.left(angle)
#     pirate.forward(100)
# print("Pirate final heading:", pirate.heading())
# screen.exitonclick()



# import turtle
#
# sides = int(input("Enter the number of sides: "))
# length = int(input("Enter the length: "))
# penColor = input("Enter the pen color: ")
# fillColor = input("Enter the fill color: ")
#
# angle = 360/sides
#
# screen = turtle.Screen()
# oklid = turtle.Turtle()
# oklid.pencolor(penColor)
# oklid.fillcolor(fillColor)
# oklid.pensize(5)
# oklid.begin_fill()
#
# for i in range(sides):
#     oklid.forward(length)
#     oklid.left(angle)
#
# oklid.end_fill()
#
# screen.exitonclick()



# import turtle
# screen = turtle.Screen()
# jewish = turtle.Turtle()
# jewish.pensize(3)
# jewish.left(36) #to obtain the exact same shape as the one in the question
#
# for i in range(5):
#     jewish.forward(100)
#     jewish.left(144)
#
# screen.exitonclick()



# import turtle
#
# leg = int(input("Enter the number of legs: "))
# angle1 = 360 / leg
#
# screen = turtle.Screen()
# spider = turtle.Turtle()
#
# spider.penup()
# spider.goto(0, -10)
# spider.pendown()
# spider.fillcolor("black")
# spider.begin_fill()
# spider.circle(10)
# spider.end_fill()
#
# spider.penup()
# spider.goto(0, 0)
#
# for i in range(leg):
#     spider.left(angle1)
#     spider.forward(10)
#     spider.pendown()
#     spider.forward(100)
#     spider.penup()
#     spider.backward(110)
#
# screen.exitonclick()