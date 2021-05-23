import os

def load_cmds_hadoop():
    
    hadoop_n=12
    while int(hadoop_n)!=6:
        print("""What do you want to do
    1. Setup the HDFS file
    2. Setup the core-site file
    3. Start datanode
    4. Start namenode
    5. Check DFS admin report
    0. Exit
    
    """)
        hadoop_n=input()
        if int(hadoop_n)==1:
            setup_hdfs_file()
        elif int(hadoop_n)==2:
            setup_core_file()
        elif int(hadoop_n)==3:
            start_datanode()
        elif int(hadoop_n)==4:
            start_namenode()
        elif int(hadoop_n)==5:
            get_report()
        elif int(hadoop_n)==0:
            break
        else:
            print("Incorrect input please try again")

def start_namenode():
    os.system("hadoop namenode format")
    os.system("hadoop-daemon.sh start namenode")

def start_datanode():
    os.system("hadoop datanode format")
    os.system("hadoop-daemon.sh start datanode")

def setup_core_file():
    val=input("Do you wanna configure as namenode or datanode . Press 1 for namenode or 2 for datanode\n")
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
        print("File Updated")
    if int(val)==2:
        ip_host=input("Enter the ip of the namenode ")
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
        print("File updated")

def setup_hdfs_file():
    val=input("Do you wanna configure as namenode or datanode . Press 1 for namenode or 2 for datanode\n")  
    nn = input('Enter the name of the folder')
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
        #os.system("mkdir /nn")
        print("File Updated namenode at /nn")
    
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
        os.system("mkdir /dn1")
        print("File updated datanode at /dn1")
        #os.system("hadoop namenode format")


def clear_screen_hadoop():
    os.system("clear")
    load_cmds_hadoop()

def get_report():
    os.system('hadoop dfsadmin -report')