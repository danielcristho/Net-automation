from datetime import  datetime
import paramiko 
import time


ssh_client = paramiko.SSHClient() 
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 

#Dictionary
list_router = [
        {
            "ip": "10.10.10.1",
            "username": "cisco",
            "password": "cisco"
        },

        {
            "ip": "10.10.10.2",
            "username": "cisco2",
            "password": "cisco2"
        },

        {
            "ip": "10.10.10.3",
            "username": "cisco3",
            "password": "cisco3"
        },

        {
            "ip": "10.10.10.4",
            "username": "cisco",
            "password": "cisco",
            "port": "2221"
        },

        {
            "ip": "10.10.10.5",
            "username": "cisco5",
            "password": "cisco5"
        },
    ]

file_log = open("error_log.txt", "a")

for device in list_router: 

    try:
        ssh_client.connect(
            hostname=device["ip"], 
            username=device["username"], 
            password=device["password"],
            port = device["port"] if "port" in device else 22 
        )
        print("**********************************************")
        print(f"Success login to {device['ip']} ")
        conn = ssh_client.invoke_shell()

            
        conn.send("show ip int br | ex unas\n") #do show ip interface brief | exclude unassigned
        time.sleep(1)

        output = conn.recv(65535).decode() 
        print(output)

        ssh_client.close()  

    except paramiko.ssh_exception.AuthenticationException as message:
        print(f"{message} [{device['ip']}] ")
        file_log.write(
            f"{message} [{device['ip']}] {datetime.now() }\n"
        )

    except paramiko.ssh_exception.NoValidConnectionsError as message:
        print(f"{message}") 
        file_log.write(f"{message} {datetime.now() }\n")

    #buat default error exception!!!
    except Exception as message:
        print(f"error: {message} [{device['ip']}]")
        file_log.write(
            f"error, message: {message}{datetime.now() }\n" 
        )

file_log.close()         