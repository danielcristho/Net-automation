### Repositori saya tentang belajar network automation dengan Docker, Python & GNS3

### Using Frameworks and integrate with:
* Paramiko
* Netmiko
* Telnetlib
* CSV
* SFTP

  * Netmiko, Support devices type [ssh_dispatcher.py](https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py)
### Cisco basic command:

 #### Configure IP Address & SHH
   
   ```
   configure terminal
   interface fastethernet0/0 {can be different}
   ip address 10.10.10.1 255.255.255.0 
   no shutdown
   
   ip domain name rtr.local
   crypto key generate rsa
   1024 {enter this}
   
   username admin password admin123 {can be different}
   secret cisco
   
   line vty 0 15
   login local
   
   do write {save configuration}
     
   ```
 ### For python:
   ```
   python3 -m venv netenv {create environment}
   source netenv/bin/activate
   pip3 install paramiko netmiko
   ```
   
   ![](https://github.com/danielcristho/Net-automation/blob/main/lab1.png)
   
   


 
