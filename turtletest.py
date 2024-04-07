import turtle

def draw_square_path(t, side_length):
    for _ in range(4):
        t.forward(side_length)
        t.right(90)

def return_to_start(t, side_length):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(180)  # Turn 180 degrees
    draw_square_path(t, side_length)

def main():
    t = turtle.Turtle()
    t.speed("slow")
    side_length = 100

    # Draw a square path
    draw_square_path(t, side_length)

    # Return to the starting point
    return_to_start(t, side_length)

    # Hide the turtle and display the result
    t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
