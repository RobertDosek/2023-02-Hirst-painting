import turtle as tm
from random import choice

'''Colors extraction'''
# import colorgram
# number_of_colors = 38
# colors = colorgram.extract('hirst.jpg', number_of_colors)
# print(colors)
# list_of_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     list_of_colors.append(color_tuple)
# print(list_of_colors)
tm.colormode(255)
final_list = [ (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
               (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157),
               (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166),
               (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188),
               (34, 151, 210), (65, 66, 56)]

# 10 x 10 rows of spots
# radius 20, space depart 50
tim = tm.Turtle()

tim.penup()
tim.speed(0)
tim.hideturtle()
level = 0
number_of_rows = 10
number_of_columns = 10


for jump in range(number_of_rows):
    tim.goto(-250,-250+level)
    for step in range(number_of_columns):
        tim.dot(20,choice(final_list))
        tim.forward(50)
    level += 50


screen = tm.Screen()
screen.exitonclick()