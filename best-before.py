#! /usr/bin/env python
import sys

def main():
	for arg in sys.argv[1:]:
		if len(arg) > 4:
			interpret(arg)
		else:
			print arg + ' is illegal'


def interpret(arg):
	print arg + ' ' + str(len(arg))


if __name__ == '__main__':
	main()
