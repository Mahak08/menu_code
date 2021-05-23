# AWS
 
import os 
import subprocess as sp
print()
os.system("tput setaf 15")
print("\t\t\t\t\t\tAWS Services Menu -- ")
os.system("tput setaf 14")
print("""
	\t\t\t\tPress 1 : Create key pairs
	\t\t\t\tPress 2 : Create Security Group 
	\t\t\t\tPress 3 : Allowing Port in Security Group
	\t\t\t\tPress 3 : Launch Instance
	\t\t\t\tPress 4 : Create  EBS Volume
	\t\t\t\tPress 5 : Attach EBS Volume To Instance
	\t\t\t\tPress 6 : Detach EBS Volume from Instance
	\t\t\t\tPress 7 : Start Instance
	\t\t\t\tPress 8 : Description of Key pair , Security Group , Volume or Instance
	\t\t\t\tPress 9 : Launch S3 Bucket
	\t\t\t\tPress 10 : Upload Static Data to S3 Bucket
	\t\t\t\tPress 11 : Create Cloudfront Distribution
	\t\t\t\tPress 12 : Stop Instance
	\t\t\t\tPress 13: Terminate Instance
	\t\t\t\tPress 14 : Delete Key pair
	\t\t\t\tPress 15 : Delete Security Group 
	\t\t\t\tPress 16 : Delete EBS Volume
	\t\t\t\tPress 17 : Exit 
	""")
input("Press Enter to continue..")
while True:
	os.system("clear")
	os.system("tput setaf 1")
	print("To exit from AWS services type quit")	

	os.system("tput setaf 15")
	print("\t\t\t\t\t\tAWS Services Menu -- ")
	os.system("tput setaf 14")
	print("""
		\t\t\t\tPress 1 : Create key pairs
		\t\t\t\tPress 2 : Create Security Group 
		\t\t\t\tPress 3 : Allowing Port in Security Group
		\t\t\t\tPress 3 : Launch Instance
		\t\t\t\tPress 4 : Create  EBS Volume
		\t\t\t\tPress 5 : Attach EBS Volume To Instance
		\t\t\t\tPress 6 : Detach EBS Volume from Instance
		\t\t\t\tPress 7 : Start Instance
		\t\t\t\tPress 8 : Description of Key pair , Security Group , Volume or Instance
		\t\t\t\tPress 9 : Launch S3 Bucket
		\t\t\t\tPress 10 : Upload Static Data to S3 Bucket
		\t\t\t\tPress 11 : Create Cloudfront Distribution
		\t\t\t\tPress 12 : Stop Instance
		\t\t\t\tPress 13: Terminate Instance
		\t\t\t\tPress 14 : Delete Key pair
		\t\t\t\tPress 15 : Delete Security Group 
		\t\t\t\tPress 16 : Delete EBS Volume
		\t\t\t\tPress 17 : Exit 
		""")
	os.system("tput setaf 10")
	print()	
	p = input ("\t\t\t\tEnter your choice : ")
	print()
	p = p.lower()

	elif ( p == 1):
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
		ssec = sp.getstatusoutput("aws ec2  create-security-group --description {0}  --group-name {1}".format(dessec, csec))
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
		sinstance = sp.getstatusoutput("aws ec2 run-instances --image-id {0} --instance-type {1} --count 1 --subnet-id {2}"
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
		sattach =sp.getstatusoutput("aws ec2 attach-volume --instance-id  {0} --volume-id {1} --device" 							"{2}".format(instanceID,volumeID,device))
		if sattach[0] == 0 :
			os.system("tput setaf 2")
			print("\t\t\t\tVolume has been Successfully attach to Instance") 
			os.system("tput setaf 15")

	elif( p == 7):
		os.system("tput setaf 10")
		volumed = input("\t\tEnter the Volume ID to detach  : ")
		instanced = input("\t\tEnter the instanceID to detach from  : ")
		deviced = input("\t\tEnter the device name of the Volume : ")
		sdetach = sp.getstatusoutput("aws ec2  detach-volume --force --device{0}  --instance-id  {1} --volume-id" 							"{2}".format(deviced,instanced,volumed))
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
		sname = input("Enter the Security Group name :")
		port = input("Enter the port no. you want to allow : ")
		pcol = input("Enter the protocol it going to use : ")
		sport = sp.getstatusoutput("aws ec2 authorize-security-group-ingress --group-name {0} --protocol "{1}" --port {2} --cidr "0.0.0.0/0" ".format(sname,pcol,port))	
		if (sport[0] == 0 ):
			os.system("tput setaf 2")
			print("Port has been allowed in Security Group")
			os.system("tput setaf 15")
	elif(p == 10 ):
		os.system("tput setaf 10")
		bucket = input("Enter the Bucket name : ")
		sbucket = sp.getstatusoutput(" aws s3 mb s3://{0}".format(bucket))
		if sbucket[0] == 0 :
			os.system("tput setaf 2")
			print("Successfully launched Bucket ")
			os.system("tput setaf 15")
		else :
			os.system("tput setaf 1")
			print("Type unique name for Bucket")

	elif(p == 11):
		os.system("tput setaf 1")
		print(" Place the static data in current directory")
		os.system("tput setaf 10")
		sthree = input("Enter the S3 Bucket name where you want to upload the data : ")
		load = sp.getstatusoutput(" aws s3 cp . s3://{0} --recursive --acl public-read".format(sthree))
		if load[0] == 0 :
			os.system("tput setaf 2")
			print("Successfully loaded the data to S3 bucket")
			os.system("tput setaf 15")
		else :
			os.system("tput setaf 1")
			print("ERROR")
			os.system("tput setaf 15")
	
	elif(p == 12):
		os.system("tput setaf 10")
		cloud = input("Enter the S3 bucket name to create cloudfront Distribution : ")
		scloud = sp.getstatusoutput("aws cloudfront create-distribution --origin-domain-name {0}.s3.amazonaws.com".format(cloud))
		if scloud[0] ==0 :
			os.system("tput setaf 2")
			print("Successfully created Cloud Front Distribution")
			os.system("tput setaf 15")

	elif ( p == 18):
		os.system("tput setaf 15")		
		break
		
	
	else:
		os.system("tput setaf 1")
		print("\t\tdon't support this service..." )
		os.system("tput setaf 15")
		print()
		
	input("Press Enter to continue ..")		
	
