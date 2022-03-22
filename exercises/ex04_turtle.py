"""Balancing act on a floatinf shelf."""

__author__ = "730482406"

from turtle import Turtle, colormode, done


def main() -> None: 
    """The entrypoint of of my scene."""
    bruno: Turtle = Turtle()
    colormode(255)
    draw_rectangle(bruno, -100, 30, 200, 40)
    bruno.circle(30)
    draw_triangle(bruno, 80, 30, 50)
    draw_rectangle(bruno, -110, 139, 10, 50)
    draw_trapezoid(bruno, 100, 73, 20, 10, 30)
    draw_pentagon(bruno, 0, 30, 20)
    done()


def draw_rectangle(a_forest: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draw a rectangle of the given width where top right corner is located at x, y."""
    a_forest.penup()
    a_forest.goto(x, y)
    a_forest.setheading(0.0)
    a_forest.pendown()
    a_forest.speed(50)
    a_forest.fillcolor(32, 67, 93)
    i: int = 0
    while i < 2:
        a_forest.forward(width)
        a_forest.right(90)
        a_forest.forward(length)
        a_forest.right(90)
        i += 1


def draw_triangle(a_triangle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a triangle where the bottom left corner is located at x, y."""
    a_triangle.penup()
    a_triangle.goto(x, y)
    a_triangle.setheading(0.0)
    a_triangle.pendown()
    a_triangle.speed(50)
    i: int = 0
    while i < 3:
        a_triangle.forward(width)
        a_triangle.left(120)
        i += 1


def draw_trapezoid(a_trap: Turtle, x: float, y: float, top: float, width: float, base: float) -> None:
    """Draw a trapezoid."""
    a_trap.penup()
    a_trap.goto(x, y)
    a_trap.setheading(0.0)
    a_trap.pendown()
    a_trap.speed(50)
    a_trap.pencolor("green")
    i: int = 0
    while i < 2:
        a_trap.forward(base)
        a_trap.left(120)
        a_trap.forward(width)
        a_trap.left(60)
        a_trap.forward(top)
        i += 1


def draw_pentagon(a_pentagon: Turtle, x: float, y: float, width: float) -> None:
    """Draw a table."""
    a_pentagon.penup()
    a_pentagon.goto(x, y)
    a_pentagon.setheading(0.0)
    a_pentagon.pendown()
    a_pentagon.speed(50)
    a_pentagon.pencolor("pink")
    i: int = 0
    while i < 5:
        a_pentagon.forward(width)
        a_pentagon.left(72)
        i += 1


if __name__ == "__main__":
    main()