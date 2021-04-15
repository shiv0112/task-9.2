#!/usr/bin/python3
import subprocess as sb
import cgi
print("Content-Type: text/html")
sb.getoutput("dnf install httpd -y")
sb.getoutput("systemctl enable httpd")
a=sb.getoutput("systemctl start httpd")
print(a)

