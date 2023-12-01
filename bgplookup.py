from netmiko import ConnectHandler
from netmiko import ConnectHandler, SSHDetect, NetmikoTimeoutException, NetmikoAuthenticationException
import getpass

#Obtain Username
username = input("Please enter your Username: ")

# Obtain Password
password=getpass.getpass(prompt="Please enter your Password: ")

# Obtain Prefix
prefix = input("Enter IP Prefix to lookup: ")

# Define the netmiko parameters for SSH connection
netmiko_params = {
    "device_type": "cisco_ios",
    "ip": "X.X.X.X",
    "username": username,
    "password": password,
    "global_delay_factor": 2,
}


net_connect = ConnectHandler(**netmiko_params)

output = net_connect.send_command('show ip route ' + prefix)
print (output)

output = net_connect.send_command('show ip bgp ' + prefix)
print (output)
