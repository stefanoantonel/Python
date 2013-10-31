#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Clase para leer el contenido de una pagina web.

Los valores que contiene son:
	self.status		contiene el estado de la conexion (200, 404, 408, ...)
	self.reason		valor en texto del status
	self.headers	una lista con el resultado de la comunicacion con el servidor
	self.read1		contiene la pagina html

Las funciones que contiene son:
	self.html_connect(self,url)	realiza la conexion con el servidor
	self.html_showStatus(self)	devuelve una tupla con self.status y self.reason
	self.html_read(self)			lee el contenido de la pagina
	self.html_showHTML(self)		devuelve el codigo HTML leido en la funcion html_read
	self.html_close(self)		cierra la conexion
"""

import httplib
from urlparse import urlparse
import os,sys
import socket
import re

class html(object):
	
	def __init__(self):
		pass

	"""
	Funcion que realiza la conexion.
	Tiene que recibir: la url
	"""
	def html_connect(self,url):
		socket.setdefaulttimeout(20)
		try:
			parse=urlparse(url)
			if parse.scheme=="http":
				#self.conn=httplib.HTTPConnection(parse.netloc,timeout=60)
				self.conn=httplib.HTTPConnection(parse.netloc)
			else:
				#self.conn=httplib.HTTPSConnection(parse.netloc,timeout=60)
				self.conn=httplib.HTTPSConnection(parse.netloc)
			if parse.path=="":
				# Si no disponemos de path le ponemos la barra
				path="/"
			elif parse.query:
				# Si disponemos de path y query, realizamos el montaje
				path="%s?%s" % (parse.path,parse.query)
			else:
				# Si solo disponemos de path
				path=parse.path
			self.conn.request("GET",path)
			self.response1=self.conn.getresponse()
			self.status=self.response1.status
			self.reason=self.response1.reason
			self.headers=self.response1.getheaders()
		except socket.error:
			#errno, errstr = sys.exc_info()[:2]
			#if errno == socket.timeout:
				#print "There was a timeout"
			#else:
				#print "There was some other socket error"
			self.status=408
		except:
			self.status=404

	"""Muestra el estado"""
	def html_showStatus(self):
		try:
			return self.status, self.reason
		except:
			return ""

	"""Lee el contenido"""
	def html_read(self):
		self.read1=self.response1.read()

	"""Muestra el contenido"""
	def html_showHTML(self):
		if self.read1:
			return self.read1
		return ""

	"""Cierra la conexion"""
	def html_close(self):
		try:
			self.conn.close()
		except:
			pass
	
	def get_body(self):
		from pyquery 
		import PyQuery
		d = PyQuery("http://jcoppens.com/misc/my_ip.html")
		d=d("body").html()

if __name__=="__main__":
	obj=html()
	print("Loading... " )
	obj.html_connect("http://jcoppens.com/misc/my_ip.html")
	#~ print obj.html_showStatus()
	#~ print obj.status
	#~ print obj.headers
	
	if obj.status==200:
		obj.html_read()
		result=obj.html_showHTML()
		result=re.search(".*?", result);
		#~ print result
		
	obj.html_close()
