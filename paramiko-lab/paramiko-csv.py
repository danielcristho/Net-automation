from datetime import  datetime
import paramiko 
import time

ssh_client = paramiko.SSHClient() 
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 

#read CSV  file
data_router = open("list.csv", "r")
list_router = data_router.readlines()#baca file .csv dalam bentuk list
list_router.remove(list_router[0])# remove index pertama

file_log = open("error_log.txt", "a")

for device in list_router: 
    device = device.split(";")
    try:
        ssh_client.connect(
            hostname=device[0], # index IP 
            username=device[1], # index username
            password=device[2], # password
            port = device[3] if  device[3] else 22 
        )
        print("**********************************************")
        print(f"Success login to {device[0]}")
        conn = ssh_client.invoke_shell()

        if device[4].strip(): #hapus spasi/enter
            conn.send("enable\n")
            conn.send(f"{device[4]}\n") # send secret 
            time.sleep(1)

            
        conn.send("show ip int br | ex unas\n") #do show ip interface brief | exclude unassigned
        time.sleep(1)

        output = conn.recv(65535).decode() 
        print(output)

        ssh_client.close()  

    except paramiko.ssh_exception.AuthenticationException as message:
        print(f"{message} [{device[0]}] ")
        file_log.write(
            f"{message} [{device[0]}] {datetime.now() }\n"
        )

    except paramiko.ssh_exception.NoValidConnectionsError as message:
        print(f"{message}") 
        file_log.write(f"{message} {datetime.now() }\n")

    #buat default error exception!!!
    except Exception as message:
        print(f"error: {message} [{device[0]}]")
        file_log.write(
            f"error, message: {message}{datetime.now() }\n" 
        )

file_log.close() 