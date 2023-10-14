import turtle

turtle_screen =turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("black")
turtle.speed(0)

turtle_colors = ["red","yellow","black","blue","brown","pink"]

for i in range(30):
    turtle_instance.color(turtle_colors[i % 6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(20)

turtle.mainloop()
#turtle.done()