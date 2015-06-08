# coding:shift-jis

import turtle
import math
import random

class Line:
	def __init__(self,slp,x0,y0):
		self.slp = float(slp)
		self.x0 = float(x0)
		self.y0 = float(y0)

	def get_y(self,x):
		return self.slp * (x-self.x0) + self.y0

	def get_x(self,y):
		return self.x0 + (y - self.y0) / self.slp

class Kame(turtle.Turtle):
	def __init__(self):
		super(Kame,self).__init__()
		self.shape('turtle')
		self.shapesize(2,2)
		self.radians()					 #角度の指定をを弧度法に変更
		#掃除機で掃除をしている感じを出すための色の変更（必須では無い）
		self.width(10)					 #軌跡の幅を10に設定
		self.getscreen().bgcolor('gray') #背景をグレイに（掃除前の感じ）
		self.pencolor('white')			 #軌跡の色を白に（掃除後の感じ）

	def hit_wall(self):
		xx = self.window_width() / 2.0	 #ウィンドウ幅の半分がx座標の最大値
		yy = self.window_height() / 2.0	 #ウィンドウ高の半分がy座標の最大値
		#今いる地点と、向いている方向から直進の軌跡を表す直線の式を表現するLineクラスの実体を作製
		line = Line(math.tan(self.heading()),self.xcor(),self.ycor())
		rand_angle = math.pi * random.random() #内側180°からランダムに（弧度法）

		if self.towards(-xx,yy) > self.heading() >= self.towards(xx,yy): #上側の壁にあたるとき
			des_x = line.get_x(yy)	 # Line型をつかって到達点のx座標を計算
			des_y = yy				 # 到達点のy座標は分かっているのでそのまま代入
			turn_angle = self.heading() + rand_angle
		elif self.towards(-xx,-yy) > self.heading() >= self.towards(-xx,yy): #左側の壁にあたるとき
			des_x = -xx
			des_y = line.get_y(-xx)
			turn_angle =  self.heading() - 0.5 * math.pi + rand_angle		 # 右へどれだけ回れば、内側を向くか計算（引き算は左回りと同じ意味）
		elif self.towards(xx,-yy) > self.heading() >= self.towards(-xx,-yy): #下側の壁にあたるとき
			des_x = line.get_x(-yy)
			des_y = -yy
			turn_angle = self.heading() - rand_angle
		else:											 #残った条件は、右側の壁にあたる角度
			des_x = xx
			des_y = line.get_y(xx)
			turn_angle = self.heading() - 0.5 * math.pi - rand_angle

		self.goto(des_x,des_y) #壁にあたる点まで移動
		self.right(turn_angle) #回転して、内側に顔を出す

	#動き回り続けるためのメソッド
	def run(self):
		while True:
			self.hit_wall()

	def click_on_move(self,x,y):
		self.goto(x,y)
