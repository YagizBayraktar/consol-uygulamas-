def mandala():    
    import turtle
    import colorsys

    t = turtle.Turtle()
    s = turtle.Screen()

    s.bgcolor("black")
    t.speed(0)

    n = 36
    h = 0

    for j in range(120):
        
        c = colorsys.hsv_to_rgb(h,1,1)
        h += 0.008
        
        t.color(c)
        
        for i in range(n):
            t.forward(150)
            t.right(170)
        
        t.right(3)

    turtle.done()