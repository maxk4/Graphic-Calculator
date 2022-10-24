# COURSE: CPSC 231 FALL 2021
# INSTRUCTOR: Jonathan Hudson
# Tutorial: Zack Hassan
# ID: 30151219
# Name: Maximilian Kaczmarek
# Date: Oct,19,2021
# Description: Making a graphic calculator

from math import *
import turtle

# Constants
BACKGROUND_COLOR = "white"
WIDTH = 800
HEIGHT = 600
AXIS_COLOR = "black"

#function to get color
def get_color(equation_counter):
    """
    Get color for an equation based on counter of how many equations have been drawn (this is the xth equation)
    :param equation_counter: Number x, for xth equation being drawn
    :return: A string color for turtle to use
    """
    #modulating colors
    calculation = equation_counter % 3
    if calculation == 0:
        return "red"
    if calculation == 1:
        return "green"
    if calculation == 2:
        return "blue"


#converts the x and y value to a pixel value
def calc_to_screen_coord(x, y, x_origin, y_origin, ratio):
    """
    Convert a calculator (x,y) to a pixel (screen_x, screen_y) based on origin location and ratio
    :param x: Calculator x
    :param y: Calculator y
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (screen_x, screen_y) pixel version of calculator (x,y)
    """

    screen_x = x_origin + (ratio * x)
    screen_y = y_origin + (ratio * y)

    return screen_x, screen_y


#calculates the minmax of x
def calc_minmax_x(x_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER x value to draw for a 0->WIDTH of screen
    Smallest: Convert a pixel x=0 to a calculator value and return integer floor
    Largest : Convert a pixel x=WIDTH to a calculator value and return integer ceiling
    :param x_origin: Pixel x origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) x value to draw for a 0->WIDTH of screen
    """

    screen_x_min = 0
    x_min_solver = (screen_x_min - x_origin)/ratio
    min_x = int(floor(x_min_solver))

    screen_x_max = WIDTH
    x_max_solver = (screen_x_max - x_origin)/ratio
    max_x = int(ceil(x_max_solver))

    return min_x, max_x


#calculates the minmax of y
def calc_minmax_y(y_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER y value to draw for a 0->HEIGHT of screen
    Smallest: Convert a pixel y=0 to a calculator value and return integer floor
    Largest : Convert a pixel y=HEIGHT to a calculator value and return integer ceiling
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) y value to draw for a 0->HEIGHT of screen
    """

    screen_y_min = 0
    y_min_solver = (screen_y_min - y_origin)/ratio
    min_y = int(floor(y_min_solver))

    screen_y_max = HEIGHT
    y_max_solver = (screen_y_max - y_origin)/ratio
    max_y = int(ceil(y_max_solver))

    return min_y, max_y


#draws a line in between 2 points
def draw_line(pointer, screen_x1, screen_y1, screen_x2, screen_y2):
    """
    Draw a line between two pixel coordinates (screen_x_1, screen_y_1) to (screen_x_2, screen_y_2)
    :param pointer: Turtle pointer to draw with
    :param screen_x1: The pixel x of line start
    :param screen_y1: The pixel y of line start
    :param screen_x2: The pixel x of line end
    :param screen_y2: The pixel y of line end
    :return: None (just draws in turtle)
    """

    pointer.penup()
    pointer.setposition(screen_x1, screen_y1)
    pointer.pendown()
    pointer.setposition(screen_x2, screen_y2)


#draws the ticks on the x-axis
def draw_x_axis_tick(pointer, screen_x, screen_y):
    """
    Draw an x-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """
    tick_length_xaxis = 5
    pointer.penup()
    pointer.setposition(screen_x, screen_y + tick_length_xaxis)
    pointer.pendown()
    pointer.setposition(screen_x, screen_y - tick_length_xaxis)


#numbers on the x axis
def draw_x_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw an x-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    """

    pointer.penup()
    pointer.setposition(screen_x, screen_y - 20)
    pointer.pendown()
    turtle.write(label_text)


#draws ticks on the y axis
def draw_y_axis_tick(pointer, screen_x, screen_y):
    """
    Draw an y-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """

    tick_length_yaxis = 5
    pointer.penup()
    pointer.setposition(screen_x + tick_length_yaxis, screen_y)
    pointer.pendown()
    pointer.setposition(screen_x - tick_length_yaxis, screen_y)


#lables the y axis with numbers
def draw_y_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw an y-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    """

    pointer.penup()
    pointer.setposition(screen_x - 20, screen_y)
    pointer.pendown()
    turtle.write(label_text)


#draws the x axis
def draw_x_axis(pointer, x_origin, y_origin, ratio):
    """
    Draw an x-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    smallestvalueofx, largestvalueofx = calc_minmax_x(x_origin, ratio)
    pointer.penup()
    pointer.setposition(0, y_origin)
    pointer.pendown()
    pointer.setposition(WIDTH, y_origin)

#creates the x-axis ticks and labels
    x_spacing = 1
    for i in range(smallestvalueofx, largestvalueofx + x_spacing, x_spacing):
        screencordx1, screencordy1 = calc_to_screen_coord(i, 0, x_origin, y_origin, ratio)
        draw_x_axis_tick(pointer, screencordx1, screencordy1)
        draw_x_axis_label(pointer, screencordx1, screencordy1, str(i))


def draw_y_axis(pointer, x_origin, y_origin, ratio):
    """
    Draw an y-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    smallestvalueofy, largestvalueofy = calc_minmax_y(y_origin, ratio)
    pointer.penup()
    pointer.setposition(x_origin, 0)
    pointer.pendown()
    pointer.setposition(x_origin, HEIGHT)

#creates the y-axis for the ticks and lables
    y_spacing = 1
    for i in range(smallestvalueofy, largestvalueofy + y_spacing, y_spacing):
        screencordx1, screencordy1 = calc_to_screen_coord(0, i, x_origin, y_origin, ratio)
        draw_y_axis_tick(pointer, screencordx1, screencordy1)
        draw_y_axis_label(pointer, screencordx1, screencordy1, str(i))


#draws the functions
def draw_expression(pointer, expr, colour, x_origin, y_origin, ratio):
    """
    Draw expression centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param expr: The string expression to draw
    :param colour: The colour to draw the expression
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """

    pointer.color(colour)
    delta = 0.1
    min_x, max_x = calc_minmax_x(x_origin, ratio)
    min_y, max_y = calc_minmax_y(y_origin, ratio)
    x = min_x

#draws the line in small sections
    while x <= max_x:
        x1 = x
        x2 = x + delta
        y1 = calc(expr, x1)
        y2 = calc(expr, x2)

        screenx1, screeny1 = calc_to_screen_coord(x1, y1, x_origin, y_origin, ratio)
        screenx2, screeny2 = calc_to_screen_coord(x2, y2, x_origin, y_origin, ratio)

        draw_line(pointer, screenx1, screeny1, screenx2, screeny2)
        x += 0.01




# YOU SHOULD NOT NEED TO CHANGE ANYTHING BELOW THIS LINE UNLESS YOU ARE DOING THE BONUS


def calc(expr, x):
    """
    Return y for y = expr(x)
    Example if x = 10, and expr = x**2, then y = 10**2 = 100.
    :param expr: The string expression to evaluate where x is the only variable
    :param x: The value to evaluate the expression at
    :return: y = expr(x)
    """
    return eval(expr)


def setup():
    """
    Sets the window up in turtle
    :return: None
    """
    turtle.bgcolor(BACKGROUND_COLOR)
    turtle.setup(WIDTH, HEIGHT, 0, 0)
    screen = turtle.getscreen()
    screen.screensize(WIDTH, HEIGHT)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    screen.delay(delay=0)
    pointer = turtle
    pointer.hideturtle()
    pointer.speed(0)
    pointer.up()
    return pointer


def main():
    """
    Main loop of calculator
    Gets the pixel origin location in the window and a ratio
    Loops a prompt getting expressions from user and drawing them
    :return: None
    """
    # Setup
    pointer = setup()
    # turtle.tracer(0)
    # Get configuration
    x_origin, y_origin = eval(input("Enter pixel coordinates of chart origin (x,y): "))
    ratio = int(input("Enter ratio of pixels per step: "))
    # Draw axis
    pointer.color(AXIS_COLOR)
    draw_x_axis(pointer, x_origin, y_origin, ratio)
    draw_y_axis(pointer, x_origin, y_origin, ratio)
    # turtle.update()
    # Get expressions
    expr = input("Enter an arithmetic expression: ")
    equation_counter = 0
    while expr != "":
        # Get colour and draw expression
        colour = get_color(equation_counter)
        draw_expression(pointer, expr, colour, x_origin, y_origin, ratio)
        # turtle.update()
        expr = input("Enter an arithmetic expression: ")
        equation_counter += 1


main()
turtle.exitonclick()
