import paramiko  #ssh ke device
import time
import getpass # hide password when input

username = input("Username: ") or "cisco" # input username
password = getpass.getpass() or "cisco"

ssh_client = paramiko.SSHClient() 
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 

for x in range(1, 5):
    ssh_client.connect(hostname=f"10.10.10.{x}", username=username, password=password)

print(f"Success login to 10.10.10.{x}")
conn = ssh_client.invoke_shell() 

#config di shell cisco
conn.send("configure terminal\n")
conn.send("interface lo0\n")
conn.send(f"ip address 11.11.11.{x} 255.255.255.0\n")
time.sleep(1) 

output = conn.recv(65535).decode() 
print(output)

ssh_client.close() 