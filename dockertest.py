import os
name = "test"
name1= "centos"
tag = "latest"
os.system("docker run -it --name {0} {1}:{2}".format(name,name1,tag))
