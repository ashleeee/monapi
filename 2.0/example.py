
# coding: utf-8

import monapi

mona = monapi.monapi()

def init() :
	mona.setroom(30)
	mona.setpos(200, 200)
	return

def main() :
	init()
	mona.connect()
	while(1) :
		mona.update()
		print(mona.recv())
	return

if __name__ == '__main__' : main()