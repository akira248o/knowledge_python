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
		self.radians()					 #�p�x�̎w������ʓx�@�ɕύX
		#�|���@�ő|�������Ă��銴�����o�����߂̐F�̕ύX�i�K�{�ł͖����j
		self.width(10)					 #�O�Ղ̕���10�ɐݒ�
		self.getscreen().bgcolor('gray') #�w�i���O���C�Ɂi�|���O�̊����j
		self.pencolor('white')			 #�O�Ղ̐F�𔒂Ɂi�|����̊����j

	def hit_wall(self):
		xx = self.window_width() / 2.0	 #�E�B���h�E���̔�����x���W�̍ő�l
		yy = self.window_height() / 2.0	 #�E�B���h�E���̔�����y���W�̍ő�l
		#������n�_�ƁA�����Ă���������璼�i�̋O�Ղ�\�������̎���\������Line�N���X�̎��̂��쐻
		line = Line(math.tan(self.heading()),self.xcor(),self.ycor())
		rand_angle = math.pi * random.random() #����180�����烉���_���Ɂi�ʓx�@�j

		if self.towards(-xx,yy) > self.heading() >= self.towards(xx,yy): #�㑤�̕ǂɂ�����Ƃ�
			des_x = line.get_x(yy)	 # Line�^�������ē��B�_��x���W���v�Z
			des_y = yy				 # ���B�_��y���W�͕������Ă���̂ł��̂܂ܑ��
			turn_angle = self.heading() + rand_angle
		elif self.towards(-xx,-yy) > self.heading() >= self.towards(-xx,yy): #�����̕ǂɂ�����Ƃ�
			des_x = -xx
			des_y = line.get_y(-xx)
			turn_angle =  self.heading() - 0.5 * math.pi + rand_angle		 # �E�ւǂꂾ�����΁A�������������v�Z�i�����Z�͍����Ɠ����Ӗ��j
		elif self.towards(xx,-yy) > self.heading() >= self.towards(-xx,-yy): #�����̕ǂɂ�����Ƃ�
			des_x = line.get_x(-yy)
			des_y = -yy
			turn_angle = self.heading() - rand_angle
		else:											 #�c���������́A�E���̕ǂɂ�����p�x
			des_x = xx
			des_y = line.get_y(xx)
			turn_angle = self.heading() - 0.5 * math.pi - rand_angle

		self.goto(des_x,des_y) #�ǂɂ�����_�܂ňړ�
		self.right(turn_angle) #��]���āA�����Ɋ���o��

	#������葱���邽�߂̃��\�b�h
	def run(self):
		while True:
			self.hit_wall()

	def click_on_move(self,x,y):
		self.goto(x,y)
