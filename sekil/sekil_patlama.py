def patlama():
    import turtle
    import colorsys

    t = turtle.Turtle()
    screen = turtle.Screen()

    screen.bgcolor("black")
    t.speed(0)
    t.width(2)

    h = 0

    for i in range(500):

        c = colorsys.hsv_to_rgb(h, 1, 1)
        h += 0.004
        t.color(c)

        t.forward(i)
        t.left(91)

        t.circle(i * 0.3)
        t.right(45)

    turtle.done()