from paramiko import SSHClient
from scp import SCPClient
import getpass
import os
import sys
from os import listdir
from os.path import isfile, join

def isFile():
	filename = raw_input("Please enter the name or path of the file you would like to upload (plus extension): ")
	return filename


server = raw_input("Server: ")
port = int(raw_input("Port Number: "))
print "Please enter your login..."
username = raw_input("Username: ")
password = getpass.getpass("Password: ")

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect(server, port, username, password)

# SCPCLient takes a paramiko transport as its only argument
scp = SCPClient(ssh.get_transport())

filename = isFile()

while True:
	if filename != "quit":
		scp.put("ftp/" + filename)
	else:
		print "File does not exist"
	test = raw_input("Would you like to upload another file? (yes to continue, anything else to quit): ")
	if test != "yes":
		sys.exit()
	filename = isFile()