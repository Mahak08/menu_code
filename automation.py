import os
import subprocess as sp
import getpass



password = 'menu'
flag = 'false'
while flag != 'True':
	passwd = getpass.getpass("\t\t\t\tEnter the password : ")
	if password !=  passwd :
		print("Password incorrect ...")
	else:
		flag = 'True'

def vm():
	os.system("date")


def load_cmds_hadoop():
    


	def install_hadoop(): 
		os.system("rpm -q hadoop")

	def start_namenode():
		os.system("hadoop-daemon.sh start namenode")
		os.sytem("jps")

	def start_datanode():
		os.system("hadoop-daemon.sh start datanode")
		os.system("jps")
	def setup_core_file():
		os.system("tput setaf 10")
		val=input("\t\tDo you wanna configure as namenode or datanode . Press 1 for namenode or 2 for datanode\n")
		if int(val)==1:
			with open("/etc/hadoop/core-site.xml",'w+') as f:
				f.write("<?xml version='1.0'?>\n")
				f.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n")
				f.write("<!-- Put site-specific property overrides in this file. -->\n\n")
				f.write("<configuration>\n")
				f.write("<property>\n")
				f.write("<name>fs.default.name</name>\n")
				f.write("<value>hdfs://0.0.0.0:9001</value>\n")
				f.write("</property>\n")
				f.write("</configuration>\n")
			os.system("tput setaf 2")
			print("\t\t\t\tSuccessfully configured core file of hadoop")
			os.system("tput setaf 15")
		elif int(val)==2:
			os.system("tput setaf 10")
			ip_host=input("\t\tEnter the ip of the namenode : ")
			os.system("tput setaf 15")
			with open("/etc/hadoop/core-site.xml",'w+') as f:
				f.write("<?xml version='1.0'?>\n")
				f.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n")
				f.write("<!-- Put site-specific property overrides in this file. -->\n\n")
				f.write("<configuration>\n")
				f.write("<property>\n")
				f.write("<name>fs.default.name</name>\n")
				f.write(f"<value>hdfs://{ip_host}:9001</value>")
				f.write("</property>\n")
				f.write("</configuration>\n")
			os.system("tput setaf 2")
			print("\t\t\t\tSuccessfully configured core file of hadoop")
			os.system("tput setaf 15")

	def setup_hdfs_file():
		os.system("tput setaf 10")
		val=input("\t\tDo you wanna configure as namenode or datanode . Press 1 for namenode or 2 for datanode\n")  
		nn = input('\t\tEnter the name of the folder')
		os.system("tput setaf 15")
		if int(val)==1:
			with open("/etc/hadoop/hdfs-site.xml",'w+') as f:
				f.write("<?xml version='1.0'?>\n")
				f.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n")
				f.write("<!-- Put site-specific property overrides in this file. -->\n\n")
				f.write("<configuration>\n")
				f.write("<property>\n")
				f.write("<name>dfs.name.dir</name>\n")
				f.write("<value>/{nn}</value>\n")
				f.write("</property>\n")
				f.write("</configuration>\n")
			os.system("sudo mkdir /nn")
			os.system("hadoop namenode format")
			os.system("tput setaf 2")
			print("\t\t\t\tSuccessfully configured the HDFS file of Hadoop")
			os.system("tput setaf 15")
    
		if int(val)==2:
			with open("/etc/hadoop/hdfs-site.xml",'w+') as f:
				f.write("<?xml version='1.0'?>\n")
				f.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n")
				f.write("<!-- Put site-specific property overrides in this file. -->\n\n")
				f.write("<configuration>\n")
				f.write("<property>\n")
				f.write("<name>dfs.data.dir</name>\n")
				f.write("<value>/dn1</value>\n")
				f.write("</property>")
				f.write("</configuration>\n")
			os.system("sudo mkdir /dn1")
			os.system("tput setaf 2")
			print("\t\t\t\tSuccessfully configured the HDFS file of Hadoop")
			os.system("tput setaf 15")
			


	def clear_screen_hadoop():
		os.system("clear")
		load_cmds_hadoop()

	def get_report():
		os.system('hadoop dfsadmin -report')

			
	while True:
		os.system("clear")
		os.system("tput setaf 15")
		print("\t\t\t\t\t\t\tMENU FOR HADDOP SERVICE")
		os.system("tput setaf 14")
		print("""
			\t\t\t============================================
			\t\t\t|| Press 1 : Hadoop Installes or not	||
			\t\t\t|| Press 2 : Setup the hdfs-site file	||
			\t\t\t|| Press 3 : Setup the core-site file     ||
			\t\t\t|| Press 4 : Start datanode               ||
			\t\t\t|| Press 5 : Start namenode               ||
			\t\t\t|| Press 6 : Check DFS admin report       ||
			\t\t\t|| Press 0 : Exit                         ||
			\t\t\t============================================
			""")
		print()
		os.system("tput setaf 10")
		hadoop_n=input("\t\t\t\t\t\tEnter the choice : ")
		os.system("tput setaf 15")
		print()
		if int(hadoop_n) ==1:
			install_hadoop()
		if int(hadoop_n)==2:
			setup_hdfs_file()
		elif int(hadoop_n)==3:
			setup_core_file()
		elif int(hadoop_n)==4:
			start_datanode()
		elif int(hadoop_n)==5:
			start_namenode()
		elif int(hadoop_n)==6:
			get_report()
		elif int(hadoop_n)==0:
			break
		else:
			os.system("tput setaf 1")
			print("Incorrect input please try again")
			os.system("tput setaf 15")



def LVM_partition():
	
	os.system("tput setaf 1")
	print("\t\t\t\t\t\tinstalling the lvm2")
	status = sp.getstatusoutput("yum install lvm2")
	if status[0] == 0:
		os.system("tput setaf 2")
		print("\t\t\t\t\t\tSuccessfully installed lvm2")
		os.system("tput setaf 10")
		device = input("\t\tEnter the storage HD name : ")
		pv = sp.getstatusoutput("pvcreate {}".format(device))
		if(pv[0] == 0):
			os.system("tput setaf 2")
			print("\t\tsuccessfully created pv")
			os.system("tput setaf 15")
			out  = sp.getoutput("pvdisplay {0}".format(device))
			print(out)
			print()
			os.system("tput setaf 11")
		input("Press Enter to continue..")
		print()
		os.system("tput setaf 10")
		volume = input("\t\tEnter the volume group name : ")
		vg = sp.getstatusoutput("vgcreate {0} {1}".format(volume,device))
		if (vg[0] == 0):
			os.system("tput setaf 2")
			print("successfully created {0} volume group".format(volume))
			os.system("tput setaf 15")
			out1 = sp.getoutput("vgdisplay {0}".format(volume))
			print(out1)
	
		print()
		os.system("tput setaf 11")
		input("Press Enter to continue..")
		print()
		os.system("tput setaf 10")
		logical = input("\t\tEnter the logical volume name : ")
		size = input("\t\tEnter size of logical volume : ")
		lv=sp.getstatusoutput("lvcreate --name {0} --size {1} {2}".format(logical,size,volume))	
		if(lv[0] == 0):
			os.system("tput setaf 2")
			print("\t\tSuccessfully created logical volume {0}".format(logical))
			os.system("tput setaf 15")
			out2 = sp.getoutput("lvdisplay /dev/{0}/{1}".format(volume,logical))
			print(out2)
		print()	
		os.system("tput setaf 11")
		input("Press Enter to continue..")
		print()
	
		ext = sp.getstatusoutput("mkfs.ext4 /dev/{0}/{1}".format(volume,logical))
		if(ext[0] == 0):
			os.system("tput setaf 2")
			print("\t\tSuccessfully formated LVM")
		print()	
		os.system("tput setaf 11")
		input("Press Enter to continue")	
		print()

		os.system("tput setaf 10")
		mountfile = input("\t\tEnter the folder name on which you want to mount : ")
		mount = sp.getstatusoutput("mount /dev/{0}/{1} {2}".format(volume,logical,mountfile))
		if mount[0] == 0 :
			os.system("tput setaf 2")
			print("Successfully mounted the LVM on {0}".format(mountfile))
			os.system("tput setaf 15") 
			out3 = sp.getoutput("df -Th")
			print(out3)		
			
def extend_LVM():
	print()
	os.system("tput setaf 10")
	extendv = input("\t\tEnter the volume group name : ")		
	extendl = input("\t\tEnter the logical volume name you want to extend : ")
	extends = input("\t\tEnter size of logical volume : ")
	extendlv = sp.getstatusoutput("lvextend --size +{0} /dev/{1}/{2}".format(extends,extendv,extendl))
	if (extendlv[0] == 0):
		os.system("tput setaf 2")
		print("Successfully extended the LV {0}".format(extendl))
			
	print()
	os.system("tput setaf 10")
	print("\t\tFormating the extended LVM partition ..")
	extendext = sp.getstatusoutput("resize2fs /dev/{0}/{1}".format(extendv,extendl))
	if (extendext[0] == 0):
		os.system("tput setaf 2")
		print("\t\tSuccessfully formated the extended LVM partition")
		os.system("tput setaf 15")
		out4 = sp.getoutput("df -Th")
		print(out4)
		print("\t\t\t------------------------------------------------------")
			
def docker():

	def docker_configure():
		with open("/etc/yum.repos.d/docker-ce.repo",'w+') as f:
				f.write("[docker]\n")
				f.write("baseurl = http://download.docker.com/linux/centos/7/x86_64/stable\n")
				f.write("gpgcheck = 0")			
		os.system("yum list docker-ce ")
		os.system("tput setaf 2")
		print("\t\t\t\tSuccessfully Configured the Docker Repo File")
		os.system("tput setaf 15")
	def docker_install():
		installd = sp.getstatusoutput("yum install docker-ce --nobest -y")
		if installd[0] == 0 :
			os.system("tput setaf 2")
			print("\t\t\t\tSuceessfully installed the docker-ce")
			os.system("tput setaf 15")
	def docker_service():
		startd = sp.getstatusoutput("systemctl start docker")
		os.system("systemctl enable docker")
		if start[0] == 0:
			os.system("tput setaf 2")
			print("\t\t\t\tSUccessfully Started the docker service")
			os.system("tput setaf 15")
	def docker_info():
		os.system("docker info")
	def docker_search():
		os.system("tput setaf 10")
		docker_hub = input("\t\tEnter the image name for searching : ")
		os.system("tput setaf 15")
		os.system("docker search {}".format(docker_hub))

	def docker_pull():
		os.system("tput setaf 10")
		docker_image = input("\t\tEnter the OS image name  e.g. ubuntu:14.04 : ")
		docker_tag = input("\t\tEnter the tag for OS image e.g.(latest) : ")
		pulls = sp.getstatusoutput("docker pull {0}:{1}".format(docker_image,docker_tag))
		if pulls[0] == 0 :
			os.system("tput setaf 2")
			print("\t\t\t\tSuccessfully Pulled the image")
			os.system("tput setaf 15")
			os.system("docker images")	
	def dokcer_launch_container():
		os.system("tput setaf 10")
		container_name = input("\t\tEnter the container name : ")
		docker_name = input("\t\tEnter the OS name you want to launch e.g (ubuntu:14.04) : ")
		container_tag = input("\t\tEnter the OS tag for container : ")
		os = sp.getstatusoutput("docker run -itd --name {0} {1}:{2}".format(container_name,docker_name,container_name))
		if os[0] == 0 :
			os.system("tput setaf 2")
			print("\t\t\t\tSuccessfully launced the container {0}".format(conatiner_name))
			os.system("tput setaf 15")	
			
	def docker_images():
		os.system("docker images")
	def docker_container():
		os.system("tput setaf 10")
		run = input("\t\tView running container or all container : ")
		if ("running" in run):
			os.system("tput setaf 2")
			print("\t\t\t\tShowing only running Containers")
			os.system("tput setaf 15")					
			os.system("docker ps")
		else :
			os.system("tput setaf 2")
			print("\t\t\t\tShowing all the Containers")
			os.system("tput setaf 15")				
			os.system("docker ps -a")
	def docker_start():
		os.system("tput setaf 10")
		start = input("\t\tEnter the Container name or Container ID : ")
		os.system("tput setaf 15")
		os.system("docker start {}".format(start))
	def docker_stop():
		os.system("tput setaf 10")
		stop = input("\t\tEnter the Container name or Container ID : ")
		os.system("tput setaf 15")
		os.system("docker stop {}".format(stop))
	def docker_attach():
		os.system("tput setaf 1")
		print("\t\tTo exit from the attach container press ctrl+p+q")
		os.system("tput setaf 10")			
		attachd = input("\t\tEnter the Container name or Container ID : ")
		os.system("tput setaf 15")			
		os.system("docker attach {}".format(attachd))
	def docker_del_image():
		os.system("tput setaf 10")
		allimage = input("\t\tDo You want to delete all images ? (Y/N) : ")
		os.system("tput setaf 15")
		if allimages == 'Y':
			os.system("docker rmi -f $(docker images -q)")
		else :
			os.system("tput setaf 10")
			delimage = input("\t\tEnter the image ID for deletion : ")
			os.system("tput setaf 15")
			os.system("docker rmi -f {}".format(delimage))
	def docker_del_container():
		os.system("tput setaf 10")
		allcontainer = input("\t\tDo you want to delete all container ? (Y/N) : ")
		os.system("tput setaf 15")
		if allcontainer == 'Y':
			os.system("docker rm -f $(docker ps -aq)")
		else:
			os.system("tput setaf 10")
			delcontainer = input("\t\tEnter the container name or ID for deletion : ")
			os.system("tput setaf 15")				
			os.system("docker rm -f {}".format(delcontainer))

	while True :
		os.system("clear")
		os.system("tput setaf 15")
		print("\t\t\t\t\t\t\tMENU FOR DOCKER SERVICE ")
		os.system("tput setaf 14")
		print("""
			\t\t\t==================================================
			\t\t\t|| Press 1 : Configure Docker repo file		||
			\t\t\t|| Press 2 : Install Docker community edition	||
			\t\t\t|| Press 3 : Start Docker services		||
			\t\t\t|| Press 4 : Docker infomation			||
			\t\t\t|| Press 5 : Search image from Docker hub	||
			\t\t\t|| Press 6 : Pull OS Image 			||
			\t\t\t|| Press 7 : Launch Container			||
			\t\t\t|| Press 8 : Start Container Service		||
			\t\t\t|| Press 9 : Stop Container Service		||
			\t\t\t|| Press 10: List of Docker Images  		||
			\t\t\t|| Press 11: List of Docker Conatiner 		||	
			\t\t\t|| Press 12: Attach to Docker Container		||
			\t\t\t|| Press 13: Remove Images			||
			\t\t\t|| Press 14: Remove Container			||
			\t\t\t|| Press 0 EXIT					||
			\t\t\t==================================================
			""")
		print()
		dockeri = int(input("\t\t\t\tEnter your choice for Docker Services : "))
		if dockeri == 1 :
			docker_configure()
		elif dockeri == 2 :
			docker_install()
		elif dockeri == 3 :
			docker_service()
		elif dockeri == 4 :
			docker_info()
		elif dockeri == 5 :
			docker_search()
		elif dockeri == 6 :
			docker_pull()
		elif dockeri == 7 :
			docker_launch_container()
		elif dockeri == 8 :
			docker_start()
		elif dockeri == 9 :
			docker_stop()
		elif dockeri == 10 :
			dokcer_images()
		elif dockeri == 11 :
			docker_container()
		elif dockeri == 12:
			docker_attach()
		elif dockeri == 13 :
			docker_del_image()
		elif dockeri ==14 :
			docker_del_container()
		elif dockeri == 0 :
			break
		else :
			os.system("tput setaf 1")
			print("\t\t\t\tTHIS SERVICE IS NOT SUPPORTED")
			os.system("tput setaf 15")
		input("Press Enter to continue..")



			
def AWS_automation():
	
	while True:
		os.system("clear")
		os.system("tput setaf 1")
		print("To exit from AWS services Press 17")	
		os.system("tput setaf 15")
		print("\t\t\t\t\t\t\tMENU FOR AWS SERVICE -- ")
		os.system("tput setaf 14")
		print("""
		\t\t\t==========================================================
		\t\t\t|| Press 1 : Create key pairs				||
		\t\t\t|| Press 2 : Create Security Group 			||
		\t\t\t|| Press 3 : Allowing Port in Security Group		||
		\t\t\t|| Press 4 : Launch Instance				||
		\t\t\t|| Press 5 : Create  EBS Volume				||
		\t\t\t|| Press 7 : Detach EBS Volume from Instance		||
		\t\t\t|| Press 8 : Start Instance				||
		\t\t\t|| Press 9 : Description of Key pair , Security Group 	||
		\t\t\t||		 ,Volume or Instance			||	
		\t\t\t|| Press 10 : Launch S3 Bucket				||
		\t\t\t|| Press 11 : Upload Static Data to S3 Bucket		||
		\t\t\t|| Press 12 : Create Cloudfront Distribution		||
		\t\t\t|| Press 13 : Stop Instance				||
		\t\t\t|| Press 14: Terminate Instance				||
		\t\t\t|| Press 15 : Delete Key pair				||
		\t\t\t|| Press 16 : Delete Security Group 			||
		\t\t\t|| Press 17 : Delete EBS Volume				||
		\t\t\t|| Press 0 : Exit 					||
		\t\t\t==========================================================
		""")
		os.system("tput setaf 10")
		print()	
		p = int(input("\t\t\t\tEnter your choice : "))
		print()
		
		if( p == 1):
			os.system("tput setaf 10")
			ckey = input("\t\tEnter the Key Pair name : ")
			skey = sp.getstatusoutput("aws ec2 create-key-pair --key-name {}".format(ckey))
			if skey[0] == 0 :
				os.system("tput setaf 2")
				print("\t\t\t\tSuccessfully created the key pair")
				os.system("tput setaf 15 ")
				print(skey[1])
	
		elif( p == 15):
			os.system("tput setaf 10")
			dkey = input("\t\tEnter the key pair name you want to delete : ")
			skey1  = sp.getstatusoutput("aws ec2  delete-key-pair --key-name {}".format(dkey))
			if skey1[0] == 0 :
				os.system("tput setaf 2")
				print("\t\t\t\tSuccessfully deleted the key-pair")	
				os.system("tput setaf 15")

		elif ( p == 9):
			os.system("tput setaf 10")
			q = input("\t\tEnter the Service name for Description : ")
			os.system("tput setaf 15")
			if ( "security" in q) : 
				os.system("aws ec2 describe-security-groups | grep GroupName")
			elif ("key" in q) :
				os.system("aws ec2 describe-key-pairs")
			elif  ( "instance" in q)  :
				namei = input("\t\tEnter the Instance ID")
				os.system("aws ec2 describe-instances --instance-ids {0}".format(namei))
			elif  ("volume" in p)  :	
				namev = input("\t\tEnter the Volume ID")	
				os.system("aws ec2 describe-volumes --volume-ids {0}".format(namev))

		elif( p == 2):
			os.system("tput setaf 10")
			csec = input("\t\tEnter the security group name : ")
			dessec = input("\t\tEnter the description for user security group : ") 
			ssec = sp.getstatusoutput("aws ec2  create-security-group --description {0}  --group-name" 						"{1}".format(dessec,csec))
			if ssec[0] == 0 :
				os.system("tput setaf 2")
				print("\t\t\t\tsuccessfully created security group")
				os.system("tput setaf 15")
				print(ssec[1])
		elif( p == 16):
			os.system("tput setaf 10")
			dsec = input("\t\tEnter  Security group name to delete : ")
			ssec1 =sp.getstatusoutput("aws ec2  delete-security-group   --group-name {0}".format(dsec))
			if ssec == 0:
				os.system("tput setaf 2")
				print("\t\t\t\tSuccessfully deleted the Security group {}".format(dsec))
				os.system("tput setaf 15")
			
		elif ( p == 4):
			os.system("tput setaf 10")
			image = input("\t\tEnter the image ID of the instance : ")
			itype = input("\t\tEnter the instance type : ")
			subnet = input("\t\tEnter the subnet ID : ")
			secur = input("\t\tEnter the security group ID you want to attach : ")
			key = input("\t\tEnter key pair name to attach : ")
			sinstance = sp.getstatusoutput("aws ec2 run-instances --image-id {0} --instance-type {1} --count 1" 								"--subnet-id {2}"
					" --security-group-ids {3} --key-name {4}".format(image,itype,subnet,secur,key))	
			if sinstance[0] == 0 :
				os.system("tput setaf 2")
				print("\t\t\t\tSuccessfully launched the instance")
				os.system("tput setaf 15")
		

		elif ( p == 5) :
			os.system("tput setaf 10")
			cvolume = input("\t\tEnter availability Zone  e.g. ap-south-1a : ")
			size = input("\t\tEnter the size of the Volume group : ")		
			svolume = sp.getstatusoutput("aws ec2 create-volume --availability-zone {0} --size {1} "
						" --volume-type gp2".format(cvolume,size))
			if svolume[0] == 0 :
				os.system("tput setaf 2")
				print("\t\t\t\tSuccessfully created EBS volume")
				os.system("tput setaf 15")
			else :	
				print("volume is not been created")
		elif( p == 17): 
			dvolume = input("\t\tEnter the Volume group id for deletion e.g. vol-0e7f6209670a2795a : ")
			svolume1 = sp.getstatusoutput("aws ec2  delete-volume  --volume-id {}".format(dvolume))		
			if svolume1[0] == 0 :
				os.system("tput setaf 2")
				print("\t\t\t\tSuccessfully deleted the volume")
				os.system("tput setaf 15")
		
		elif( p == 6) :
			os.system("tput setaf 10")
			volumeID = input("\t\tEnter the Volume  ID : ")
			instanceID = input("\t\tEnter the instance ID to which you want to attach Volume : ")
			device = input("\t\tEnter the device name (e.g. /dev/sdb) of the volume : ")				
			sattach =sp.getstatusoutput("aws ec2 attach-volume --instance-id  {0} --volume-id {1} --device" 						"{2}".format(instanceID,volumeID,device))
			if sattach[0] == 0 :
				os.system("tput setaf 2")
				print("\t\t\t\tVolume has been Successfully attach to Instance") 
				os.system("tput setaf 15")

		elif( p == 7):
			os.system("tput setaf 10")
			volumed = input("\t\tEnter the Volume ID to detach  : ")
			instanced = input("\t\tEnter the instanceID to detach from  : ")
			deviced = input("\t\tEnter the device name of the Volume : ")
			sdetach = sp.getstatusoutput("aws ec2  detach-volume --force --device{0}  --instance-id  {1} --volume-id" 								"{2}".format(deviced,instanced,volumed))
			if sdetach[0] == 0 :
				os.system("tput setaf 2")
				print("\t\t\t\tVolume has been Successfully detach from instance") 
				os.system("tput setaf 15")
	
		elif ( p == 13):
			os.system("tput setaf 10")
			stop = input ("\t\tEnter the instance ID of instance you want to stop : ")
			os.system("tput setaf 15")
			os.system("aws ec2  stop-instances --instance-ids {0}".format(stop))
			
		elif ( p == 8):
			os.system("tput setaf 10")
			start = input("\t\tEnter the instance ID to start the instance : ")
			os.system("tput setaf 15")		
			os.system("aws ec2  start-instances --instance-ids {0}".format(start))
		
		elif ( p == 14):
			os.system("tput setaf 10")
			terminate = input("\t\tEnter the instance ID to terminate the instance : ")
			os.system("tput setaf 15")		
			os.system("aws ec2  terminate-instances --instance-ids {0}".format(terminate))
	
		elif(p == 3 ):
			os.system("tput setaf 10")
			sname = input("\t\tEnter the Security Group name :")
			port = input("\t\tEnter the port no. you want to allow : ")
			pcol = input("\t\tEnter the protocol it going to use : ")
			sport = sp.getstatusoutput("aws ec2 authorize-security-group-ingress --group-name {0} --cidr 0.0.0.0/0 "
			"--protocol {1} --port {2}  ".format(sname,pcol,port))	
			if (sport[0] == 0 ):
				os.system("tput setaf 2")
				print("\t\tPort has been allowed in Security Group")
				os.system("tput setaf 15")
		elif(p == 10 ):
			os.system("tput setaf 10")
			bucket = input("\t\tEnter the Bucket name : ")
			sbucket = sp.getstatusoutput(" aws s3 mb s3://{0}".format(bucket))
			if sbucket[0] == 0 :
				os.system("tput setaf 2")
				print("\t\tSuccessfully launched Bucket ")
				os.system("tput setaf 15")
			else :
				os.system("tput setaf 1")
				print("Type unique name for Bucket")
	
		elif(p == 11):
			os.system("tput setaf 1")
			print(" Place the static data in current directory")
			os.system("tput setaf 10")
			sthree = input("\t\tEnter the S3 Bucket name to upload the data : ")
			imagename = input("\t\tEnter the name of Static data :")
			load = sp.getstatusoutput(" aws s3 cp {0} . s3://{1} --recursive --acl public-read".format(imagename,sthree))
			if load[0] == 0 :
				os.system("tput setaf 2")
				print("\t\tSuccessfully loaded the data to S3 bucket")
				os.system("tput setaf 15")
			else :
				os.system("tput setaf 1")
				print("\t\t\t\tERROR")
				os.system("tput setaf 15")
		elif(p == 12):
			os.system("tput setaf 10")
			cloud = input("\t\tEnter the S3 bucket name to create cloudfront Distribution : ")
			scloud = sp.getstatusoutput("aws cloudfront create-distribution --origin-domain-name" 							"{0}.s3.amazonaws.com".format(cloud))
			if scloud[0] ==0 :
				os.system("tput setaf 2")
				print("\t\tSuccessfully created Cloud Front Distribution")
				os.system("tput setaf 15")
		elif ( p == 0):
			os.system("tput setaf 15")		
			break
	

		else:
			os.system("tput setaf 1")
			print("\t\tdon't support this service..." )
			os.system("tput setaf 15")
			print()
	
		input("Press Enter to continue ..")		
	
while True :
	os.system("clear")
	os.system("tput setaf 15")
	print("\t\t\t\t\t\tWELCOME TO MY MENU!!")
	os.system("tput setaf 3")	
	print("""
	\t\t\t\t==========================================
	\t\t\t\t|| Press 1 : To run date		||
	\t\t\t\t|| Press 2 : LVM PARTITION		||
	\t\t\t\t|| Press 3 : EXTEND LVM PARTITION	||
	\t\t\t\t|| Press 4 : HADOOP SERVICE		||
	\t\t\t\t|| Press 5 : DOCKER SERVICE 		||
	\t\t\t\t|| Press 6 : AWS SERVICE 		||
	\t\t\t\t|| Press 0 : EXIT 			||
	\t\t\t\t==========================================
	""")
	os.system("tput setaf 10")
	print()
	ch = int(input("\t\t\t\t\t\tEnter your choice : "))
	os.system("tput setaf 15")
	ch = int(ch)
	if int(ch) == 1 :
		vm()
	elif int(ch) == 2 : 
		LVM_partition()
	elif ch == 3 :
		extend_LVM()
	elif ch == 4 :
		load_cmds_hadoop()
	elif ch == 5 :
		docker()
	elif ch == 6 :
		AWS_automation()
	elif ch == 0 :
		exit()
	else :
		os.system("tput setaf 1")
		print("DOES NOT SUPPORT THIS SERVICE ")
		os.system("tput setaf 15")
	
	input("Press Enter to continue..")


