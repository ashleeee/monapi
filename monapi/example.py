
# coding: utf-8

import time
import monapi

mona	=	monapi.monapi()

def init() :
	mona.setroom(0)
	mona.setpos(200, 200)
	return

def main() :
	init()
	mona.connect()
	while(1) :
		print(mona.recv())
	return

if __name__ == '__main__' : main()