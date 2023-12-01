# BGP-Prefix-Lookup

I am often asked by people to check on the status of a Subnet/prefix in our routing table
I wrote this handy little script to SSH into one of my WAN Routers and do a "Sh ip route" as well as a "show ip BGP"  and display the output.

- To deploy this in your network, you need to change the "ip" under the netmiko_params section of the script to a device in your network running BGP
- The script will prompt you for your username and password however you can specify a username and password in the netmiko_params section (I do not advise this unless this is being executed in a secure or LAB Environment)

