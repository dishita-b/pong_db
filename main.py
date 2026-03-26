#getting started with python
#ping pong game

import turtle #turtle imported module
# import winsound

wn=turtle.Screen() #window for the game
wn.title("pong by @Dishita") #title for the game
wn.bgcolor("black")
wn.setup(width=800, height=600) #size of the window
wn.tracer(0) #stops the window from updating, updating manually/speeds up the game

# Score
score_a=0
score_b=0

# Paddle A
paddle_a= turtle.Turtle() 
paddle_a.speed(0) #speed of animation-->max speed and not the speed of the paddle that moves
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #stretchs width by 5 times(100) of the given default(20x20) pixels
paddle_a.penup() #turtles draw lines when they move..this blocks that drawing of lines
paddle_a.goto(-350,0) #(x-coord-left,centre=0 vertical-y axis)

# Paddle B
paddle_b= turtle.Turtle() #turtle object-->t=module name,T-->class name
paddle_b.speed(0) #speed of animation-->max speed and not the speed of the paddle that moves
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #stretchs width by 5 times(100) of the given default(20x20) pixels
paddle_b.penup() #turtles draw lines when they move..this blocks that drawing of lines
paddle_b.goto(350,0) #(x-coord-right,centre=0 vertical-y axis)

#ball
ball= turtle.Turtle() #turtle object-->t=module name,T-->class name
ball.speed(0) #speed of animation-->max speed and not the speed of the paddle that moves
ball.shape("square")
ball.color("white")
ball.penup() #turtles draw lines when they move..this blocks that drawing of lines
ball.goto(0,0) #(centre,centre=0)
ball.dx = 0.1
ball.dy = -0.1 #change or delta change in x and y direction

# Pen
pen = turtle.Turtle() #module and class names
pen.speed(0) # animation speed and not the movement speed
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align= "center", font=("Courier", 24, "normal"))


#function
def paddle_a_up(): #defining a function for movement 
    y = paddle_a.ycor() #current y coordinate// get the y coor
    if y < 250: #add 20 pixles to y
        paddle_a.sety(y + 20) #set the new value to y

def paddle_a_down(): #defining a function for movement 
    y = paddle_a.ycor() #current y coordinate// get the y coor
    if y > -250: #subtract 20 pixles to y
        paddle_a.sety(y - 20) #set the new value to y

def paddle_b_up(): #defining a function for movement 
    y = paddle_b.ycor() #current y coordinate// get the y coor
    if y < 250:
        paddle_b.sety(y + 20) #set the new value to y

def paddle_b_down(): #defining a function for movement 
    y = paddle_b.ycor() #current y coordinate// get the y coor
    if y > -250:
        paddle_b.sety(y - 20) #set the new value to y
    
# Keyboard binding
wn.listen() #to listen to the keyboard input
wn.onkeypress(paddle_a_up, "w") #when the user presses w it calles the func paddle-up// W will not work
wn.onkeypress(paddle_a_down, "s") #when the user presses s it calles the func paddle-up// S will not work
wn.onkeypress(paddle_b_up, "Up") #when the user presses w it calles the func paddle-up// W will not work
wn.onkeypress(paddle_b_down, "Down") #when the user presses s it calles the func paddle-up// S will not work
wn.onkeypress(quit, "q")

# Main game loop
try:
    while True:
        wn.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border check
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        # Win condition
        if score_a == 10 or score_b == 10:
            pen.clear()
            pen.goto(0, 0)
            winner = "Player A" if score_a == 10 else "Player B"
            pen.write("{} Wins!".format(winner), align="center", font=("Courier", 36, "normal"))
            break

        # Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1

except Exception:
    pass

wn.mainloop()

