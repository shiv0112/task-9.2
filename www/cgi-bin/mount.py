#!/usr/bin/python3
import subprocess as sb
import cgi
print("Content-Type: text/html")
form=cgi.FieldStorage()
f=form.getvalue("dn")
p=form.getvalue("pn")
sb.getoutput("mkdir /"+f)
sb.getoutput("lsblk")
p=input("Enter a partition name")
a=sb.getoutput("mount /dev/"+p+" "+"/"+f)
sb.getoutput("cd /"+f)
print(a)
