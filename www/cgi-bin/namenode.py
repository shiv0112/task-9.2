#!/usr/bin/python3
import subprocess as sb
import cgi
print("Content-Type: text/html")
form=cgi.FieldStorage()
k=form.getvalue("ip")
m=open("/etc/hadoop/hdfs-site.xml", "w")
m.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/name</value>
</property>
</configuration>""")
m.close()
sb.getoutput("mkdir /name")
m=open("/etc/hadoop/core-site.xml", "w")
m.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://"""+str(k)+"""</value>
</property>
</configuration>""")
m.close()
sb.getoutput("systemctl stop firewalld")
sb.getoutput("echo 'Y' | hadoop namenode -format")
sb.getoutput("hadoop-daemon.sh start namenode")
a=sb.getoutput("jps")
b=sb.getoutput("hadoop dfsadmin -report") 
print(a)
print(b)
