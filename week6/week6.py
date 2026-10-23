import turtle

#---setup---

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()

#---functions---
def drawPoly(someturtle, somesides, somdesize):
    angle = 360 / somesides
    for i in range(somesides):
        someturtle.fd(somdesize)
        someturtle.left(angle)

def drawSpiral(someturtle, angle):
    size = 1
    for i in range(100):
        someturtle.fd(size)
        someturtle.right(angle)
        size = size + 2

def drawEquitriangle(someturtle, somesize):
    drawPoly(someturtle, 3, somesize)

def drawStar(someturtle, size):
    for i in range(5):
        someturtle.fd(size)
        someturtle.right(144)

def drawSprite(someturtle, legs, length):
    angle = 360 / legs
    for i in range(legs):
        someturtle.fd(length)
        someturtle.backward(length)
        someturtle.left(angle)

#-----EXERCİSES-----

#---exersice01---
# tess.color('hotpink')
# tess.pensize(3)
# drawPoly(tess, 8, 50)


#---exercise02---
# tess.color("blue")
# tess.pensize(3)
# for i in range(20):
#     drawPoly(tess, 4, 80)
#     tess.left(18)


#---exercise03---
# tess.color("blue")
# tess.pensize(2)
# tess.penup()
# tess.goto(-150, 0)
# tess.pendown()
# drawSpiral(tess, 90)
# tess.penup()
# tess.goto(150, 0)
# tess.pendown()
# drawSpiral(tess, 89)


#---exercise04---
# drawEquitriangle(tess, 100)


#---exercise05---
# tess.color("hotpink")
# tess.pensize(3)
# tess.penup()
# tess.goto(-200, 150)
# tess.pendown()
# for i in range(5):
#     drawStar(tess,100)
#     tess.penup()
#     tess.forward(350)
#     tess.right(144)
#     tess.pendown()


#---exercise06---
# drawSprite(tess, 15, 120)

#---finish---
wn.exitonclick()

