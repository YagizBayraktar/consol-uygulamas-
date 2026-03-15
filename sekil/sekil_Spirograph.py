def spirograph():
    import turtle
    import colorsys
    import math

    t = turtle.Turtle()
    screen = turtle.Screen()

    screen.bgcolor("black")
    t.speed(0)
    t.width(2)

    h = 0

    for i in range(720):

        c = colorsys.hsv_to_rgb(h, 1, 1)
        h += 0.002
        t.color(c)

        x = 200 * math.sin(math.radians(i))
        y = 200 * math.cos(math.radians(i))

        t.penup()
        t.goto(x, y)
        t.pendown()

        for j in range(36):
            t.forward(120)
            t.left(170)

    turtle.done()