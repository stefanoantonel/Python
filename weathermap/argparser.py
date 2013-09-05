#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  argparser.py



class ArgsParser():
	def get_city(self,args):
		for i in args:
			if("--city" in i):
				return i[7:] #cuando lo encuentra, contando desde el 7 para adelante dentro del arreglo
		return 'London'
	def get_unit(self,args):
		for i in args:
			if("--unit" in i):
				return i[7:] #cuando lo encuentra, contando desde el 7 para adelante
		return 'Celsius'
		
def main():
	
	return 0

if __name__ == '__main__':
	main()

