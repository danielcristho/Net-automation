import paramiko  #ssh ke device
import time
import getpass # hide password when input

uname = input("Username: ") or "cisco" # input username
passwd = getpass.getpass() or "cisco"

ssh_client = paramiko.SSHClient() 
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 

for x in range(1, 6):
    ssh_client.connect(
        hostname=f"10.10.10.{x}", 
        username=uname, 
        password=passwd
    )
    print("**********************************************")
    print(f"Success login to 10.10.10.{x}")
    conn = ssh_client.invoke_shell() 

    #config di shell cisco
    conn.send("configure terminal\n")
    conn.send("interface lo1\n")
    conn.send(f"ip address 11.11.14.{x} 255.255.255.255\n")
    time.sleep(5) 

    conn.send("do write\n") # save configuration
    time.sleep(2)
    conn.send("do show ip int br | ex unas\n")
    time.sleep(1)

    output = conn.recv(65535).decode() 
    print(output)

    ssh_client.close() 
