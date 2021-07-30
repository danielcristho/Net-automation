from os import close, write
from datetime import  datetime
import paramiko 
import time
import getpass

from paramiko import file

uname = input("Username: ") or "cisco" 
passwd = getpass.getpass() or "cisco"

ssh_client = paramiko.SSHClient() 
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
#NESTED LIST
list_ip = [
        "10.10.10.1",
        "10.10.10.2",
        "10.10.10.3", #type 'str'
        "10.10.10.4",
        "10.10.10.5"
    ]

file_log = open("error_log.txt", "a")

for ip in list_ip:
    router_split = ip.split(".")[-1]

    try:
        ssh_client.connect(
            hostname=ip, 
            username=uname, 
            password=passwd
        )
        print("**********************************************")
        print(f"Success login to {ip}")
        conn = ssh_client.invoke_shell()

            
        conn.send("show ip int br | ex unas\n") #do show ip interface brief | exclude unassigned
        time.sleep(1)

        output = conn.recv(65535).decode() 
        print(output)

        ssh_client.close()  

    except paramiko.ssh_exception.AuthenticationException as message:
        print(f"{message} [{ip}] ")
        file_log.write(
            f"{message} [{ip}] {datetime.now() }\n"
        )
    except paramiko.ssh_exception.NoValidConnectionsError as message:
        print(f"{message}") 
        file_log.write(f"{message} {datetime.now() }\n")
    #buat default error exception!!!
    except Exception as message:
        print(f"error: {message} [{ip}]")
        file_log.write(
            f"error, message: {message}{datetime.now() }\n" 
        )

file_log.close()         