import paramiko  #ssh ke device
import time
import getpass # hide password when input

uname = input("Username: ") or "cisco" # input username
passwd = getpass.getpass() or "cisco"

ssh_client = paramiko.SSHClient() 
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 

list_ip = [
        "10.10.10.1",
        "10.10.10.2",
        "10.10.10.3", #type 'str'
        "10.10.10.4",
        "10.10.10.5"
    ]

for ip in list_ip:
    router_split = ip.split(".")[-1]# buat variabel split utk memecah str mjd list 
                                   #[-1]:index terakhir dri list IP
    ssh_client.connect(
        hostname=ip, 
        username=uname, 
        password=passwd
    )
    print("**********************************************")
    print(f"Success login to {ip}")
    conn = ssh_client.invoke_shell()

    
    #config di shell cisco
    conn.send("configure terminal\n")

    #NESTED LIST
    for x in range(6, 9): #buat looping utk banyak interface sesuai range
        conn.send(f"interface lo{x}\n")
        conn.send(f"ip address 11.{x+1}.1.{router_split} 255.255.255.255\n") #IP Addr=interface + 1
        time.sleep(2) 

    conn.send("do write\n") # save configuration
    time.sleep(2)
    conn.send("do show ip int br | ex unas\n") #do show ip interface brief | exclude unassigned
    time.sleep(1)

    output = conn.recv(65535).decode() 
    print(output)

    ssh_client.close() 
