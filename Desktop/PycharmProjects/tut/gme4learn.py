# simple game pong 4 initiators


import turtle
# here the wn is window
wn = turtle.Screen()
wn.title("owais creative game intial")
wn.bgcolor("black")
wn.setup(width=800 , height= 600)
wn.tracer(0) # tracer actually stops the window for updating resulting in speeding of the game


# Paddle A
paddle_a = turtle.Turtle() # assigning the name as paddle_a whereas Turle is the object over here
paddle_a.speed(0) # this sets the speed to the max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup() # draws a line
paddle_a.goto(-350,0)

# paddle B

paddle_b = turtle.Turtle() # assigning the name as paddle_a whereas Turle is the object over here
paddle_b.speed(0) # this sets the speed to the max
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup() # draws a line
paddle_b.goto(350,0)


# ball

ball = turtle.Turtle() # assigning the name as paddle_a whereas Turle is the object over here
ball.speed(0) # this sets the speed to the max
ball.shape("square")
ball.color("white")
ball.penup() # draws a line
ball.goto(0,0)

# Functions for the moment
def paddle_a_up():
    y = paddle_a.ycor() # method in turtle module it returns the y coordinate
    y += 20
    paddle_a.sety(y) # it resets the new y

def paddle_a_down():
    y = paddle_a.ycor() # method in turtle module it returns the y coordinate
    y -= 20
    paddle_a.sety(y) # it resets the new y
def paddle_b_up():
    y = paddle_b.ycor() # method in turtle module it returns the y coordinate
    y += 20
    paddle_b.sety(y) # it resets the new y

def paddle_b_down():
    y = paddle_b.ycor() # method in turtle module it returns the y coordinate
    y -= 20
    paddle_b.sety(y) # it resets the new y

# keyboad binding
wn.listen() # it comands the wn to listen the keyboard input
wn.onkeypress(paddle_a_up,"w") # onkeypress calls the fn paddle_a _up when w is pressed
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up,"Up") # onkeypress calls the fn paddle_a _up when w is pressed
wn.onkeypress(paddle_b_down, "Down")





# as every game has this i.e. Main game loop

while True:
    wn.update() # every time the loop runs it update the screen
