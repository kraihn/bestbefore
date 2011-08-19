#! /usr/bin/env python
import sys

def main():
	for arg in sys.argv[1:]:
		if len(arg) > 4:
			interpret(arg)
		else:
			print arg + ' is illegal'


def interpret(arg):
	input = arg.split('/')
	if len(input) != 3:
		print arg + ' is illegal'
	
	else:
		print input[0]
		print input[1]
		print input[2]
		print arg + ' ' + str(len(arg))
	

if __name__ == '__main__':
	main()
