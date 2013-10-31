#!/usr/bin/env python

import subprocess as sp
import re
import time
import os.path as osp
import os


ssh_dest = "jcoppens@jcoppens.com"
ssh_path = "jcoppens.com/misc/my_ip.html"
internet = "eth0"
ip_file  = osp.expanduser("~/.mon_ip.txt")

def prev_ip():
    try:
        with open(ip_file, "r") as f:
            #~ ip = read(f)
            ip = f.read()
            return ip
    except:
        return None

def get_body():
	#~ import PyQuery
	#~ from pyquery
	from pyquery import PyQuery
	d = PyQuery("http://jcoppens.com/misc/my_ip.html")
	d=d("body").html()
	print d
	profe_ip=d

def save_and_upload(ip):
	#~ print os.system("echo ")
	#~ print "Updating IP to %s" % ip
	with open(ip_file, "w") as f:
		f.write(ip)
	html = "<html><head><title>IP echo</title></head><body>" + ip + "</body></html>"
	#~ command = "ssh " + ssh_dest + " \"echo \\\"%s\\\" > %s\"" % (html, ssh_path)
	command = "ssh " + ssh_dest + " \"echo \\\"%s\\\" > %s\"" % (html, ssh_path)
	os.system(command)

while True:
    res = sp.check_output(["ifconfig", internet])
    r = re.search("addr:([0-9]+.[0-9]+.[0-9]+.[0-9]+)", res);
    ip_now = r.group(1)
    print ip_now, prev_ip()
    get_body()
    if ip_now != prev_ip():
        save_and_upload(ip_now)
        get_body()
    time.sleep(2)
    


def main():
	return 0

if __name__ == '__main__':
	main()

