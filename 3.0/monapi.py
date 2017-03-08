
# coding: utf-8

# create python version -> python 3.4
# this program is monachat application program interface ver 3.0 / create by ashlee

import re
import time
import socket

class monapi(object):
	""" comment : monachat application program interface ver 3.0 / create by ashlee """
	def __init__(self) :
		self.room		=	  1
		self.name		=	  'Nameless'
		self.trip		=	  'trip'
		self.id			=	  ''
		self.type		=	  'mona'
		self.r			=	  100
		self.g			=	  100
		self.b			=	  100
		self.x			=	  0
		self.y			=	  0
		self.scl		=	  100
		self.stat		=	  '通常'
		self.__time		=	  time.time()
		self.__interval	=	  self.__time + 20.0
		self.__response =	  ''.encode('utf-8')
		self.__isfirst	=	  True
		self.__sock		=	  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		return

	def connect(self) :
		""" comment : connect to monachat """
		self.__sock.connect(('monachat.dyndns.org', 9095))
		self.__sock.send(b'MojaChat\0')
		enter = '<ENTER room="/MONA8094/%d" name="%s\" trip="%s" type="%s" r="%d" g="%d" b="%d" x="%d" y="%d" scl="%d" stat="%s" />\0' \
			% (self.room, self.name, self.trip, self.type, self.r, self.g, self.b, self.x, self.y, self.scl, self.stat)
		self.__sock.send(enter.encode('utf-8'))
		return

	def __extractid(self) :
		pattern = '<CONNECT id="(\d+)" />'
		iterator = re.finditer(pattern, self.__response.decode('utf-8'))
		for match in iterator :
			self.id = match.group(1)
		return

	def update(self) :
		""" comment : this method should always run in a loop """
		self.__time = time.time()
		if self.__time >= self.__interval :
			self.__sock.send(b'<NOP />\0')
			self.__interval = time.time() + 20.0
		return

	def reenter(self, _room) :
		""" comment : reenter -> assign int """
		self.room = _room
		comment = '<EXIT  id="%s" />\0' % self.id
		self.__sock.send(comment.encode('utf-8'))
		enter = '<ENTER room="/MONA8094/%d" name="%s\" trip="%s" type="%s" r="%d" g="%d" b="%d" x="%d" y="%d" scl="%d" stat="%s" />\0' \
			% (self.room, self.name, self.trip, self.type, self.r, self.g, self.b, self.x, self.y, self.scl, self.stat)
		self.__sock.send(enter.encode('utf-8'))
		return

	def comment(self, _comment) :
		""" comment : send comment -> assign str """
		comment = '<COM cmt="%s" />\0' % _comment
		self.__sock.send(comment.encode('utf-8'))
		return
	
	def recv(self) :
		""" comment : recv infomation """
		self.__response = self.__sock.recv(4096)
		if self.__isfirst :
			self.__extractid()
			self.__isfirst = False
		return self.__response.decode('utf-8', 'ignore')

	def setroom(self, _rooom) :
		""" comment : setting room number -> assign int """
		self.room = _rooom
		return

	def setname(self, _name) :
		""" comment : setting name -> assign str """
		self.name = _name
		return

	def settrip(self, _trip) :
		""" comment : setting trip -> assign str """
		self.trip = _trip
		return

	def settype(self, _type) :
		""" comment : setting type -> assign str """
		self.type = _type
		return

	def setcolor(self, _r, _g, _b) :
		""" comment : setting color(red, green, blue) -> assign int """
		self.r = _r
		self.g = _g
		self.b = _b
		return

	def setpos(self, _x, _y) :
		""" comment : setting x, y position -> assign int """
		self.x = _x
		self.y = _y
		return

	def setscl(self, _scl) :
		""" comment : setting direction -> assign int """
		self.scl = _scl
		return

	def setstat(self, _stat) :
		""" comment : setting status -> assign str """
		self.stat = _stat
		return