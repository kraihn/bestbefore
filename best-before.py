#! /usr/bin/env python
import sys
import datetime
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
			if year < 1000:
				year += 2000
			dates.append(date(year,int(input[1]),int(input[2])))
		except: 
			pass

		try:
			year = int(input[0])
			if year < 1000:
				year += 2000
			dates.append(date(year,int(input[2]),int(input[1])))
		except: 
			pass

		try:
			year = int(input[1])
			if year < 1000:
				year += 2000
			dates.append(date(year,int(input[0]),int(input[2])))
		except: 
			pass

		try:
			year = int(input[1])
			if year < 1000:
				year += 2000
			dates.append(date(year,int(input[2]),int(input[0])))
		except: 
			pass

		try:
			year = int(input[2])
			if year < 1000:
				year += 2000
			dates.append(date(year,int(input[0]),int(input[1])))
		except: 
			pass

		try:
			year = int(input[2])
			if year < 1000:
				year += 2000
			dates.append(date(year,int(input[1]),int(input[0])))
		except:
			pass
            
		
		if len(dates) > 0:
			now = date.today()
			
			best = dates[0];
			count = (dates[0] - now).days
			
			for bdate in dates[1:]:
				days = (bdate - now).days
				if days < count:
					best = bdate
					count = days
			
			print best
				
		else:
			print arg + ' is illegal'


if __name__ == '__main__':
	main()
