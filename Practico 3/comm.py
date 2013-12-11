#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2013 John Coppens <john@jcoppens.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import socket
import thread
import requests
import preferences
import re
import git

class mon_ip_profe():
	def get_body(self, ssh_path):
		r = requests.get(ssh_path)
		html = r.content
		expresion = "<body>([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)</body>"
		matches = re.search(expresion,html)
		ip = matches.group(1)
		return ip
        
        
class communications():
    def __init__(self, pref):
        self.set_preferences(pref)
        self.sock=""
        
        self.ip = "100.100.120.164"
        for i in range(10):
            self.send_udp("Hola", pref.get("comm", "port"))
        self.ip = mon_ip_profe().get_body(pref.get("comm", "ssh_path"))
        print self.ip
        pref.edit()
        thread.start_new_thread(self.monitor, (None,))
        
    def send_udp(self, msg, port):
        self.sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP
        self.sock.sendto(msg, (self.ip, port))
        
    def monitor(self, pars):
        print "monitor"
        for i in range(10):
            print "_",
            
    def set_preferences(self, pref):
        pref.add_category({"comm": {"ssh_path": ["e", "http://jcoppens.com/misc/my_ip.html"],
                                    "internet": ["e", "eth0"],
                                    "port":     ["s", 4321]}
                          })



def main():
        pref = preferences.preferences("test_pref.json")
	c=communications(pref)
	return 0

if __name__ == '__main__':
	main()

