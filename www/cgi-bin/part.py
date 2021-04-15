#!/usr/bin/python3
import subprocess as sb
import cgi
print("Content-Type: text/html")
form=cgi.FieldStorage()
n=form.getvalue("dn")
p=form.getvalue("ps")
i="(echo 'n' ; echo 'p'; echo -ne '\n'; echo -ne '\n'; echo '+"+str(p)+"G'; echo 'w')| fdisk /dev/"+str(n)
sb.getoutput(i)
a=sb.getoutput("udevadm settle")
b=sb.getoutput("lsblk")
print(a)
print(b)
