#!/usr/bin/env python

import subprocess as sp
import re
import time
import os.path as osp
import os
import requests


ssh_path = "http://jcoppens.com/misc/my_ip.html"
internet = "eth0"
ip_file  = osp.expanduser("~/.mon_ip.txt")
ip_file2  = osp.expanduser("~/profe_html.txt")

def prev_ip():
	try:
		with open(ip_file2, "r") as f:
			ip = f.read()
			return ip
	except:
		return None

def guardar(ip):
	with open(ip_file2, "a") as f:
		f.write("\n"+ip)
		

		

def get_body():
	#~ from pyquery import PyQuery
	#~ d = PyQuery("http://jcoppens.com/misc/my_ip.html")
	#~ d=d("body").html()
	#~ print d
	#~ profe_ip=d
	
	r=requests.get(ssh_path)
	html=r.content
	expresion="<body>([0-9]+.[0-9]+.[0-9]+.[0-9]+)</body>"
	matches =re.search(expresion,html)
	ip= matches.group(1)
	print "Ip profe: "+ip
	guardar(ip)
	
	#~ a=prev_ip()
	#~ print a


while True:
	print "cargando..."
	get_body()
	time.sleep(1) 

def main():
	return 0

if __name__ == '__main__':
	main()
