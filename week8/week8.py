# def gradeMark(mark):
#     if mark >= 90:
#         return "A"
#     elif mark >= 80:
#         return "B"
#     elif mark >= 70:
#         return "C"
#     elif mark >= 60:
#         return "D"
#     else:
#         return "F"
#
# marks = [90, 85, 9, 80, 73, 54, 45]
# for marks in marks:
#     print("Grade is", gradeMark(marks))
#
# mark = float(input("Enter your mark: "))
# print("Grade is", gradeMark(mark))



# import turtle
# t = turtle.Turtle()
# wn = turtle.Screen()
# def chooseColor(height):
#     if height >= 200:
#         return "red"
#     elif height >= 100:
#         return "yellow"
#     else:
#         return "green"
#
# def drawBar(t, height, gap):
#     t.penup()
#     t.left(90)
#     t.forward(height + gap)
#     t.write(" " + str(height))
#     t.backward(height + gap)
#     t.right(90)
#     t.pendown()
#
#     t.fillcolor(chooseColor(height))
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(350)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# def barChart(data):
#     max_height = max(data)
#     num_bars = len(data)
#     border = 10
#     gap = (max_height + border) / 25
#
#     wn.bgcolor("lightgreen")
#     right = 40 * num_bars * border
#     top = max_height + 4 * border
#     wn.setworldcoordinates(-border, -border, right, top)
#
#     t.color("blue")
#     t.pensize(3)
#
#     for height in data:
#         drawBar(t, height, gap)
#
#
# data = [48, 117, 200, 240, 160, 260, 220]
# barChart(data)
# wn.exitonclick()


# import turtle
# t = turtle.Turtle()
# wn = turtle.Screen()
# def chooseColor(height):
#     if height >= 200:
#         return "red"
#     elif height >= 100:
#         return "yellow"
#     else:
#         return "green"
#
# def drawBar(t, height, gap):
#     if(height >= 0):
#         labelY = height + gap
#     else:
#         labelY = gap
#     t.penup()
#     t.left(90)
#     t.forward(labelY)
#     t.write(" " + str(height))
#     t.backward(labelY)
#     t.right(90)
#     t.pendown()
#
#     t.fillcolor(chooseColor(height))
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(350)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# def barChart(data):
#     max_height = max(data)
#     min_height = min(data)
#     num_bars = len(data)
#     border = 10
#     gap = (max_height + border) / 25
#
#     wn.bgcolor("lightgreen")
#     right = 40 * num_bars * border
#     top = max_height + 4 * border
#     bottom = min(min_height, 0) - border
#     wn.setworldcoordinates(-border, bottom, right, top)
#
#     t.color("blue")
#     t.pensize(3)
#
#     for height in data:
#         drawBar(t, height, gap)
#
#
# data = [48, 117, -60, 240, 160, -110, 220]
# barChart(data)
# wn.exitonclick()



# def findHypote(x, y):
#     hypot = (x ** 2 + y ** 2) ** 0.5
#     return hypot
# print(findHypote(3, 4))