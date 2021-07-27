import paramiko  #ssh ke device
import time
import getpass # hide password when input

from paramiko.client import SSHClient

ip_address = input("IP Address: ") or "10.10.10.1" #input ip addr 
username = input("Username: ") or "cisco" # input username
password = getpass.getpass() or "cisco"

ssh_client = paramiko.SSHClient() 
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
ssh_client.connect(hostname=ip_address, username=username, password=password) 

print(f"Success login to:{ip_address}")
conn = ssh_client.invoke_shell() 

#config di shell cisco
conn.send("configure terminal\n")

#add interface using looping
# for n in range(0,4):
#     conn.send(f"interface lo{n}\n")
#     conn.send(f"ip address 11.11.11.{n+1} 255.255.255.255\n")
#     time.sleep(1) 

#delete interface using looping
for n in range(4):
    conn.send(f"no interface lo{n}\n")
    time.sleep(0.5)

output = conn.recv(65535).decode() 
print(output)

ssh_client.close() 