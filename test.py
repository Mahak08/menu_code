import os

with open("/etc/yum.repos.d/docker-ce1.repo",'w+') as f:
	f.write("[docker]\n")
	f.write("baseurl = http://download.docker.com/linux/centos/7/x86_64/stable\n")
	f.write("gpgcheck = 0")			
os.system("yum list docker-ce")
