import turtle

# Function to move turtle forward and push coordinates to stack

def move_forward_and_push(t, stack):
    x, y = t.position()
    stack.append((x, y))
    t.forward(100)
    t.left(90)


# Function to move turtle backward and pop coordinates from stack
def move_backward_and_pop(t, stack):
    x, y = stack.pop()
    t.pencolor("white")
    t.goto(x, y)


# Function to make a square path and backtrack
def make_square_and_backtrack():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.title("Square Path with Backtracking")

    t = turtle.Turtle()
    t.speed(1)

    stack = []

    for _ in range(4):
        move_forward_and_push(t, stack)

    # Backtrack
    for _ in range(4):
        move_backward_and_pop(t, stack)

    turtle.done()


make_square_and_backtrack()
