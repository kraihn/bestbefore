#! /usr/bin/env python
import sys
from datetime import date


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
		dates = []

		try:
			year = int(input[0])
			if year < 2000:
				year += 2000
			dates.append(date(year,int(input[1]),int(input[2])))
		except: 
			pass

		try:
			year = int(input[0])
			if year < 2000:
				year += 2000
			dates.append(date(year,int(input[2]),int(input[1])))
		except: 
			pass

		try:
			year = int(input[1])
			if year < 2000:
				year += 2000
			dates.append(date(year,int(input[0]),int(input[2])))
		except: 
			pass

		try:
			year = int(input[1])
			if year < 2000:
				year += 2000
			dates.append(date(year,int(input[2]),int(input[0])))
		except: 
			pass

		try:
			year = int(input[2])
			if year < 2000:
				year += 2000
			dates.append(date(year,int(input[0]),int(input[1])))
		except: 
			pass

		try:
			year = int(input[2])
			if year < 2000:
				year += 2000
			dates.append(date(year,int(input[1]),int(input[0])))
		except:
			pass
            
            
            
		print dates
		
		if len(dates) > 0:
			print dates[0]
		else:
			print arg + ' is illegal'


if __name__ == '__main__':
	main()
