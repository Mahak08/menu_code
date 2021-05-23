import os
import time as t
while True:
os.system("clear")
os.system("tput setaf 3")
print("\t\t\t\t\tWELCOME TO THE WORLD OF AUTOMATION")
os.system("tputsetaf 7")
        insert = int(input("\n\nPRESS 1 FOR LOCAL AND 2 FOR REMOTE SIDE : "))
        if insert == 1:
os.system("clear")
os.system("tput setaf 3")
print("\t\t\t\t\WELCOME TO LOCAL-SIDE")
os.system("tputsetaf 7")
print("""
                        1) Press 1 DOCKER WORLD
                        """)
                x = int(input("ENTER YOUR CHOICE:"))
				if x==1:
                        def docker():
os.system("clear")
os.system("tputsetaf 5")
print("\t\t\t\tWELCOME TO WORLD OF DOCKER")
os.system("tputsetaf 7")
print("""
                                                 A) Press 1 For Starting Docker Service
                                                 B) Press 2 For Launch Container
                                                 C) Press 3 For Start Container
                                                 D) Press 4 For Stop Container
                                                 E) Press 5 For Status Of Containers
                                                 F) PRESS 6 FOR DELETE CONTAINERS""")
                                y=int(input("ENTER YOUR CHOICE : "))
                                if y==1:
os.system("tputsetaf 3;cd /etc/yum.repos.d/;wget https://download.docker.com/linux/centos/docker-ce.repo;yum install docker-ce --nobest;systemctl start docker;systemctl status docker")
print("\n\-------------------docker has been installed---------------")
elif y==2:
                                        image = input("GIVE THE IMAGE NAME : ")
                                        version = input("ENTER VERSION : ")
os_name = input("ENTER YOUR OS NAME : ")
os.system(f"docker pull {image}:{version};docker run -it --name {os_name} {image}:{version} ")
elif y==3:
os_name = input("ENTER YOUR OS NAME TO START: ")
os.system(f"docker start {os_name}")
elif y==4:
os_name = input("ENTER YOUR OS NAME TO STOP: ")
os.system(f"docker stop {os_name}")
elif y==5:
os.system("docker ps -a")
elif y==6:
os_name = input("ENTER YOUR OS NAME TO DELETE: ")
os.system(f"docker rm {os_name}")
elif y==7:
image_name = input("ENTER YOUR IMAGE NAME TO DELETE: ")
                                        version = int(input("ENTER VERSION : "))
os.system(f"dockerrmi {image_name}:{version}")
docker()
os.system("tputsetaf 7")
input("\n\nDO YOU WANT TO CONTINUE :")
