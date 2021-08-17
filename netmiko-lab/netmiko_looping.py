from netmiko import ConnectHandler

for n in range(1, 6):
    rtr1 = {
        "device_type": "cisco_ios", 
        "host": f"10.10.10.{n}",
        "username": "cisco",
        "password": "cisco",
    }

    conn = ConnectHandler(**rtr1)

    list_config = []
    for x in range(2,6):
       list_config.append(f"interface lo{x}")
       list_config.append(f"ip address 10.{x+1}.{x+1}.{n} 255.255.255.0")
        
      

    print("-----------------------------------------------")
    print(f"Interface on Router {rtr1['host']}")

    output = conn.send_config_set(list_config)
    print(output)

    output = conn.send_command("show ip int brief | exclude unassigned")
    print(output)