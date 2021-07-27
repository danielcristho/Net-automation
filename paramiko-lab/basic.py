import paramiko  #ssh ke device
import time
import getpass # hide password when input

from paramiko.client import SSHClient

ip_address = input("IP Address: ") #input ip addr
username = input("Username: ") # input username
password = getpass.getpass()

ssh_client = paramiko.SSHClient() # membuat variabel utk function paramiko
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # menambahkan key dari router ke host
ssh_client.connect(hostname=ip_address, username=username, password=password) # connect melalui parameter yg sudah di inputkan pada variabel

print(f"Success login to:{ip_address}")
conn = ssh_client.invoke_shell() #masuk ke shell device dan bisa config

#config di shell cisco
conn.send("configure terminal\n")
conn.send("interface lo0\n")
conn.send("ip address 11.11.11.1 255.255.255.0\n")
time.sleep(1) # sleep utk menunggu konffgurasi di eksekuski

output = conn.recv(65535).decode() #mengcapture jumlah karakter yg di inputkan kemudian ubah ke decode
print(output)

ssh_client.close() #close