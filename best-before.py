#! /usr/bin/env python
import sys

def main():
	for arg in sys.argv[1:]:
		interpret(arg);


def interpret(arg):
	print arg


if __name__ == '__main__':
	main()
