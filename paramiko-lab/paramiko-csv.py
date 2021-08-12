from datetime import  datetime
import paramiko 
import time
import csv

ssh_client = paramiko.SSHClient() 
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 

file_log = open("error_log.txt", "a")

#read CSV  file
data_router = open("list.csv", "r")
list_router = csv.DictReader(data_router, delimiter=",") #read using dictionary


for device in list_router: 
    try:
        ssh_client.connect(
            hostname=device['ip'], # index IP 
            username=device['username'], # index username
            password=device['password'], # password
            port = device['port'] if  device['port'] else 22 
        )
        print("**********************************************")
        print(f"Success login to {device['ip']}")
        conn = ssh_client.invoke_shell()

        if device['enable']:
            conn.send("enable\n")
            conn.send(f"{device['enable']}\n") # send secret 
            time.sleep(2)


        conn.send("terminal length 0\n") # hapus more di shell pada saat show run
        conn.send("show running-config\n") #do show ip interface brief | exclude unassigned
        time.sleep(5)

        output = conn.recv(65535).decode() 
        file_backup = open (f"backup_config/{device['ip']}.cfg", "w") #save backup file to folder backup_config/
        file_backup.write(output)
        file_backup.close()

        ssh_client.close()  

    except paramiko.ssh_exception.AuthenticationException as message:
        print(f"{message} [{device['ip']}] ")
        file_log.write(
            f"{message} [{device['ip']}] {datetime.now()}\n"
        )

    except paramiko.ssh_exception.NoValidConnectionsError as message:
        print(f"{message}") 
        file_log.write(f"{message} {datetime.now()}\n")

    #buat default error exception!!!
    except Exception as message:
        print(f"error: {message} [{device['ip']}]")
        file_log.write(
            f"error, message: {message}{datetime.now()}\n" 
        )

file_log.close() 