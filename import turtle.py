import turtle 

control = turtle.Screen()
car = turtle.Turtle()


car.color("green")
car.shape("turtle")
car.setposition(0,0)

def turn_left():
	car.heading(90)
def turn_right():
	car.heading(180)





control.onkey(turn_left, "Right")
control.onkey(turn_right, "Left")
control.listen()

turtle.mainloop()