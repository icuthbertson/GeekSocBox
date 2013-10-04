from paramiko import SSHClient
from scp import SCPClient

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('shell.geeksoc.org', 22, 'icuthbertson', 'Dexter0502')

# SCPCLient takes a paramiko transport as its only argument
scp = SCPClient(ssh.get_transport())

scp.put('test.txt', 'test2.txt')
scp.get('test2.txt')