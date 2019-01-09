#agario hoped Start 12pm 12/29/18
import turtle
class Ball:
	def __init__(self,x,y,dx, dy, r, color):
		self.ball = turtle.clone()
		turtle.ht()
		self.ball.pu()
		self.ball.setpos(x,y)
		self.dx = dx
		self.dy = dy
		self.r = r
		self.ball.shape("circle")
		self.ball.color(color)
		self.ball.turtlesize(r/10)
		self.ball.ht()

	def move(self, width, height):
		current_x, current_y = self.ball.pos()
		new_x = current_x + self.dx
		new_y = current_y + self.dy
		right_side_ball = new_x + self.r
		left_side_ball = new_x-self.r
		top_side_ball = new_y+self.r
		bottom_side_ball = new_y-self.r
		if top_side_ball > height or bottom_side_ball< -height:
			new_y = current_y-self.dy
			self.dy = -self.dy
		if right_side_ball > width or left_side_ball < -width:
			new_x = current_x-self.dx
			self.dx = -self.dx
		self.ball.setpos(new_x, new_y)