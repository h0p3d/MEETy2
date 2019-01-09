#agario hoped Start 12pm 12/29/18 end 3:30pm
import turtle
import random
from ball import *
import time
#constants
turtle.tracer(1,0)
turtle.ht()
canvas = turtle.getcanvas()
RUNNING = True
SLEEP = .0077
SCREEN_WIDTH = int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height()/2)
NUMBER_OF_BALLS = 5
MIN_BALL_RADIUS = 10
MAX_BALL_RADIUS = 100
MIN_BALL_DX = -5
MAX_BALL_DX = 5
MIN_BALL_DY = -5
MAX_BALL_DY = 5
BALLS = []
MY_BALL = Ball(0,0,5,5,20,"blue")
MY_BALL.ball.st()

def move_all_balls():
	for ball in BALLS:
		ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def collide(ball_a, ball_b):
	if ball_a == ball_b:
		return False
	xa,ya = ball_a.ball.pos()
	xb,yb = ball_b.ball.pos()
	dist = ((abs(xa-xb))**2 + (abs(ya-yb))**2)**.5
	return dist+10 <= ball_a.r+ball_b.r

def check_all_balls_collision():
	for a in  range(len(BALLS)):
		for b in range(len(BALLS)):
			if collide(BALLS[a],BALLS[b]):
				eater = a if BALLS[a].r > BALLS[b].r else b
				eaten = b if eater == a else a 
				if BALLS[eater].r <= MAX_BALL_RADIUS:
					BALLS[eater].r += 1
					BALLS[eater].ball.turtlesize(BALLS[eater].r/10)
				BALLS[eaten].ball.ht()
				BALLS[eaten] = make_ball()

def check_myball_collision():
	for b in range(len(BALLS)):
		if collide(MY_BALL, BALLS[b]):
			if MY_BALL.r < BALLS[b].r:
				return False
			else:
				MY_BALL.r += 1
				MY_BALL.ball.turtlesize(MY_BALL.r/10)
				BALLS[b].ball.ht()
				BALLS[b] = make_ball()
	return True

def myball_eat():
	for ball in BALLS:
		if ball.r < MY_BALL.r:
			return True
	return False

def collides_with_others(ball):
	if collide(ball, MY_BALL):
		return True
	for b in BALLS:
		if collide(ball, b):
			return True
	return False

def make_ball():
	invalid = True
	while invalid:
		can_ball_eat = myball_eat()
		x = random.randint(-SCREEN_WIDTH+MAX_BALL_RADIUS, SCREEN_WIDTH-MAX_BALL_RADIUS)
		y = random.randint(-SCREEN_HEIGHT+MAX_BALL_RADIUS, SCREEN_HEIGHT-MAX_BALL_RADIUS)
		rand = random.randint(MIN_BALL_DX, MAX_BALL_DX)
		while rand == 0:
			rand = random.randint(MIN_BALL_DX, MAX_BALL_DX)
		dx = rand
		rand = random.randint(MIN_BALL_DX, MAX_BALL_DX)
		while rand == 0:
			rand = random.randint(MIN_BALL_DX, MAX_BALL_DX)
		dy = rand
		radius = random.randint(MIN_BALL_RADIUS, MAX_BALL_RADIUS) if can_ball_eat else 10
		color = (random.random(), random.random(), random.random())
		ball = Ball(x,y,dx,dy,radius,color)
		invalid = collides_with_others(ball)
	ball.ball.st()
	return ball

#init balls
for i in range(NUMBER_OF_BALLS):
	BALLS.append(make_ball())

def movearound(event):
	x = event.x-SCREEN_WIDTH
	y = SCREEN_HEIGHT-event.y
	MY_BALL.ball.setpos(x,y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()
time.sleep(1.5)
while RUNNING:
	SCREEN_WIDTH = int(turtle.getcanvas().winfo_width()/2)
	SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height()/2)
	move_all_balls()
	check_all_balls_collision()
	RUNNING = check_myball_collision()
	time.sleep(SLEEP)