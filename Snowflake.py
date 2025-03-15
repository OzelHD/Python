import turtle

def draw_koch_segment(t, length, depth):

    if depth == 0:
        t.forward(length)
    else:
        length /= 3
        draw_koch_segment(t, length, depth - 1)
        t.left(60)
        draw_koch_segment(t, length, depth - 1)
        t.right(120)
        draw_koch_segment(t, length, depth - 1)
        t.left(60)
        draw_koch_segment(t, length, depth - 1)

def draw_koch_snowflake(t, length, depth):

    for _ in range(3):
        draw_koch_segment(t, length, depth)
        t.right(120)

def main():

    screen = turtle.Screen()
    screen.title("Koch Snowflake")


    t = turtle.Turtle()
    t.speed("fastest")


    t.penup()
    t.goto(-150, 50)
    t.pendown()


    draw_koch_snowflake(t, 300, 4)


    turtle.done()

if __name__ == "__main__":
    main()
