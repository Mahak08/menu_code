import os
import subprocess as sp
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
		
	print()	
	os.system("tput setaf 11")
	input("Press Enter to continue..")
	print()
	os.system("tput setaf 10")
	yes = input("\t\tIncrease the LVM size ? (yes/no) : ")
	if yes == 'yes':
		print()
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


	else :
		return 







	
