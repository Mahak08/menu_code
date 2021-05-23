import os
import getpass
from pyfiglet import Figlet
t=Figlet('big')

print(t.renderText("\t\t HEY ! WELCOME TO THE WORLD OF DOCKER "))
os.system("tputsetaf 3")
print("***********************************************************************************")
os.system("tputsetaf 7")
print("***********************************************************************************")
os.system("tputsetaf 4")
passwd = getpass.getpass("Enter Your Password :")

apass = "redhat"

if passwd != apass:
print("Authentication Incorrect")
exit()

os.system("tputsetaf 7")
print("PLEASE SELECT THE LOGIN TYPE (local/remote) :" , end='')
location = input()
print(location)

if location == "remote":
remoteIP = input("Enter Your IP :")
os.system("tputsetaf 3")
print(t.renderText("\t\t DOCKER WORLD"))
os.system("tputsetaf 9")
print("IMPORTANT : TO PERFORM ANY TASK YOU HAVE TO START THE DOCKER USING PRESS 3:")
os.system("tputsetaf 1")
while True:

print("""
            Press 1: To Install Docker community edition.                                                                                                                                                                                                                                                                        
            Press 2: TO open gedit file and see repo list                                                                                                                                     
            Press 3: To start/stop/restart of  docker/httpd/firewall/ etc.                                                                                                                   
            Press 4: To check docker version/running container/repository/images etc. using example just you have to type the name like(version/ps/images).                                                
            Press 5: To create a new container with any name of your wish eg.(webOS etc.) ,only you have to give image name (ubuntu:14.04/mycentos etc.)                                                                                                                     
            Press 6: To install the net-tools/wgetetc.using yum.                                                                                                                                                                                                                                                          
            Press 7: To inspect anything eg.(web,containerimage,IPAddress,MacAddress etc)                                                                                          
            Press 8: To check free space in memory.                                                                                                                                                                                                                                          
            Press 9: To check the Gateway of the container                                                                                                                             
            Press 10: To create a new volume inside docker                                                                                                                             
            press 11: To start docker-compose file (for stopping the docker-compose use "ctrl+c")
            Press 12: Exit
            """)
print("PRESS ANY NUMBER TO AQUIRE SERVICES :" , end='')
ch = input()
        print(ch)
	
        if location == "local":
os.system("tputsetaf 3")
print(t.renderText("\t\t YOU HAVE SELECTED LOCAL"))

                if int(ch) == 1:
os.system("tputsetaf 7")
os.system("yum install docker-ce --nobest")
elif int(ch) == 2:
os.system("tputsetaf 7")
os.system("geditdocker.repo")
elif int(ch) == 3:
print("Enter what you want to do start/stop/restart :" ,end ='')
create_name = input()
os.system("systemctl {} ".format(create_name))
print("Enter your choice docker/httpd/firewall etc. :" , end ='')
create_name = input()
os.system("tputsetaf 7")   
os.system("systemctl start {} ".format(create_name))
elif int(ch) == 4:
print("Enter what you want to check :" ,end ='')
check_name = input(ch)
os.system("tputsetaf 6")
os.system("docker {} ".format(check_name))
elif int(ch) == 5:
print("Give name to the container :",end = '')
                        name = input()
os.system("docker container run -it  --name {}".format(name))
print("Enter image name to create container :" ,end ='')
image_name = input()
os.system("docker run -it {}".format(image_name))
print("Press :0 To exit")
os.system("exit")
elif int(ch) == 6:
print("Enter what yo install :",end='')
install_name = input()
os.system("tputsetaf 6")
os.system("yum install {}".format(install_name))
elif int(ch) == 7:
print("what you want to inspect :",end='')
inspect_name = input()
os.system("tputsetaf 6")
os.system("docker inspect {}".format(inspect_name))
elif int(ch) == 8:
os.system("tputsetaf 5")
os.system("free -m") 
elif int(ch) == 9:
os.system("tputsetaf 5")
os.system("route -n")
elif int(ch) == 10:
print("Enter volume name :",end='')
volume_name = input()
os.system("tputsetaf 5")
os.system("docker volume create {}".format(volume_name))
elif int(ch) == 11:
os.system("tputsetaf 4")
os.system("docker-compose up")
elif int(ch) == 12:
os.system("tputsetaf 2")
os.system("exit")
os.system("figlet -f block \t\t THANK YOU !")
	
                else:
print("Option Not Supported")
input("Enter To Continue......")
os.system("clear")



elif location == "remote":
os.system("tputsetaf 3")
print(t.renderText("\t\t REMOTELY SELECTED"))
os.system("tputsetaf 3")
                if int(ch) == 1:
os.system("tputsetaf 7")
os.system("ssh {0} yum install docker-ce --nobest")   
elif int(ch) == 2:
os.system("tputsetaf 7")
os.system("ssh {0} geditdocker.repo")
elif int(ch) == 3:
print("Enter what you want to do start/stop/restart :" ,end ='')
create_name = input()
os.system("ssh {0} systemctl {1} ".format(create_name))
print("Enter your choice docker/httpd/firewall etc. :" , end ='')
create_name = input()
os.system("tputsetaf 7")   
os.system("ssh {0} systemctl start {1} ".format(create_name))
elif int(ch) == 4:
print("Enter what you want to check :" ,end ='')
check_name = input(ch)
os.system("tputsetaf 6")
os.system("ssh {0} docker {1} ".format(check_name)) 
elif int(ch) == 5:
print("Give name to the container :",end = '')
                    name = input()
os.system("ssh {0} docker container run -it  --name {1}".format(name))
print("Enter image name to create container :" ,end ='')
image_name = input()
os.system("docker run -it {2}".format(image_name))
print("Press :0 To exit")
elif int(ch) == 6:
print("Enter what yo install :",end='')
install_name = input()
os.system("tputsetaf 6")
os.system("ssh {0} yum install {1}".format(install_name))  
elif int(ch) == 7:
print("what you want to inspect :",end='')
inspect_name = input()
os.system("tputsetaf 6")
os.system("ssh {0} docker inspect {1}".format(inspect_name))
elif int(ch) == 8:
os.system("tputsetaf 5")
os.system("free -m")
elif int(ch) == 9:
os.system("tputsetaf 5")
os.system("ssh {0} route -n")
elif int(ch) == 10:
print("Enter volume name :",end='')
volume_name = input()
os.system("tputsetaf 5")
os.system("ssh {0} docker volume create {1}".format(volume_name))
elif int(ch) == 11:
os.system("tputsetaf 4")
os.system("ssh {0} docker-compose up")

elif int(ch) == 12:
os.system("tputsetaf 2")
os.system("ssh {0} exit")
os.system("figlet -f banner \t\t THANK YOU !")
                else:
print("Location doesn't exist")

	
