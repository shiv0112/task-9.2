#!/usr/bin/python3
import subprocess as sb
import cgi
print("Content-Type: text/html")
form=cgi.FieldStorage()
n=form.getvalue("dn")
a=sb.getoutput("mkfs.ext4 /dev/"+n)
print(a)
