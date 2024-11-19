import turtle

def draw_circle(x, y, radius, color):
    """Draw a filled circle."""
    turtle.penup()
    turtle.goto(x, y - radius)  # Move to the starting position
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(x, y, width, height, color):
    """Draw a filled rectangle."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_m_cutout(x, y, width, height, color):
    """Draw the 'M' cutout at the bottom of the rectangle."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()

    # Draw the M cutout
    turtle.goto(x + width * 0.2, y - height * 0.4)  # First diagonal
    turtle.goto(x + width * 0.5, y)  # Middle point
    turtle.goto(x + width * 0.8, y - height * 0.4)  # Second diagonal
    turtle.goto(x + width, y)  # End of the M
    turtle.goto(x, y)  # Back to start
    turtle.end_fill()

def draw_ironman_logo():
    """Draw the full Ironman logo."""
    turtle.speed(5)
    turtle.bgcolor("white")



    # Draw the red circle (head)
    draw_circle(0, 150, 75, "blue")

    # Draw the red rectangle (body)
    draw_rectangle(-150, -150, 300, 220, "blue")

    # Draw the white 'M' cutout
    draw_m_cutout(-100, -150, 200, -125, "white")

    # Hide turtle and finish
    turtle.hideturtle()
    turtle.done()

# Run the function
draw_ironman_logo()