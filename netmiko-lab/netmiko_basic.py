from netmiko import ConnectHandler
rtr1 = {
    "device_type": "mikrotik_routeros", 
    "host": "10.10.10.1",
    "username": "router1",
    "password": "1234",
}

rtr2 = {
    "device_type": "cisco_ios",
    "host": "10.10.10.2" ,
    "username": "router2" ,
    "password": "cisco",
}

conn = ConnectHandler(**rtr1)
output = conn.send_config_set("ip address print")

conn = ConnectHandler(**rtr2)
output = conn.send_config_set("ip interface brief | exclude unassigned")

print("------------------------------------")
print(f"Interface on {rtr1['host']}")
print(output)