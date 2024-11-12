# Version 4.5
Cơ bản đã hoàn thành xong tất cả mọi thứ.
Đây là danh sách cần demo:
1. Inter-vlan routing: Sử dụng tính năng Simple PDU cho nhanh.
	1.1. PC pings each other
	1.2. PC pings to Smartphone and vice versa
	1.3. PC pings to Webcam and vice versa
2. Inter-site routing (between vlans): Sử dụng tính năng ping.
	2.1. PC pings to server
	2.2. Server pings to PC
3. ACL on L3 switch: Camera - Server - PC system
   Surveillance room: VLAN 60 (192.168.60.0/25)
	3.1. PC and Server cannot access Vlan 60 and vice versaa
   3.2. Webcam from each department can access Vlan 60 and vice versa.
4. WAN routing and Site-to-site IPSec VPN
	4.1. Demo PC pinging from main site to aux site 1 and vice versa; main site to aux site 2 and vice versa.
	4.2. IPSec VPN:
      4.2.1. From the main router, show crypto isakmp sa. State=QM_IDLE.
      4.2.2. From the main router, show crypto ipsec sa, giải thích # packets encaps and # packets decaps. Demo khi sử dụng dịch vụ HTTP thì sẽ chỉ có # packets decaps.
6. Servers
	5.1. DHCP server provides IP addresses to departments. IP addresses of servers and webcams are static.
	5.3. Web server and DNS server:
		+ Main site: ccc-hospital.main.in
		+ Aux site 1: ccc-hospital.aux1.in
		+ Aux site 2: ccc-hospital.aux2.in
		+ Public: ccc-hospital.com
		Note: Devices from main site can connect to servers on aux site 1 and 2.
7. Services
   Used: DMZ, DNS server, Web server, File server, Email server, NAT overload.
	6.1. External DNS server and web server for customers. Customers should access the hospital’s official website.
      6.1.1. show ip nat trans
	6.2. Email server (192.168.250.4).
		6.2.1. Create usernames and passwords in Email Server. Configure Mail in client's PC.
		6.2.2. Demo sending emails and receiving emails.
		6.2.3. Demo rejecting unauthorized users (SMTP authentication failed) since the email server cannot recognize the user.
		6.2.4. Demo sending emails to unregistered/unauthorized users (Send Successful but a Send Notification Failure is automatically sent)
      6.2.5. show ip nat trans
	6.3. File server (can only work with built-in files)
		6.3.1. Create user account in File server. Then authenticate user in client's PC (command: ftp 192.168.250.3)
		6.3.2. Download a file from the File server (get <file_name>). To list all files from File Server, use command 'dir' within ftp.
      6.3.3. Create a txt file from text editor.
      6.3.4. Put the file into the File server (put <file_name>).
      6.3.5. Verify the new file in the File server.
      6.3.6. Log in as another user, verify the new file from the File server. Download it.
      6.3.7. show ip nat trans
8. Verify and disqualify connection between internal and external network.
   Used: DMZ, Firewall; NAT overload
	7.1. INSIDE to DMZ (ccc-hospital.com); INSIDE to OUTSIDE1/2 (google.com)
	7.2. DMZ to OUTSIDE1/2
	7.3. OUTSIDE1/2 to DMZ, chỉ cho phép sử dụng dịch vụ HTTP và DNS của 192.168.250.2 (ccc-hospital.com)
   7.4. DMZ to INSIDE, chỉ cho phép ping và tracert tới DNS-Web server 200.0.0.2 của Main site.
	7.5. show ip nat trans ở main router. Project này dùng NAT overload. Giải thích ý nghĩa của inside local, inside global, outside global/local.
9. Client-to-site VPN (Remote access VPN)
   8.1. Create a VPN client. usergroup=remoteccc, userkey=vpnremote, hostserver = 192.168.11.2, username=admin, password=admin
   8.2. ipconfig /all
   8.3. From the main site router, ping to 192.180.0.x (x is the IP address the VPN gets from the VPNCLIENT pool: 192.180.0.0 -> 192.180.0.50)
   8.4. From the remote PC, ping to the main site router (192.168.11.2); tracert to Vlan 10, Vlan 60 (Surveillance - Fail), Vlan 200.
   8.5. From the main site router, verify VPN connection:
      8.5.1. sh crypto isakmp sa. State=QM_IDLE
      8.5.2. sh crypto ipsec sa. Verify 'crypto map staticmap'
   



-- Version 3 --
Done:
- Main router, Aux1 router, aux2 router: NAT overload, ACL. IPSec VPN to Main <-> Aux1 and Main <-> Aux2.
- Firewall: Setup Static route and OSPF routing; Created Object network, enable NAT; configure policy (ACL).

Next step:
- Change the design of the Internet (v4)


-- Version 2 --

Trong project 7 co cac configure step nhu sau:

Config step:

1 Network Design and beautification.

﻿﻿﻿2 Basic settings to all devices plus ssh on the routers and L3 switches.
   
﻿﻿﻿3 VLANs assignment plus all access and trunk ports on L2 and L3 switches.
   
﻿﻿﻿4 Switchport security to server-side site department.
   
﻿﻿﻿5 Subnetting and IP addressing
   
﻿﻿﻿6 OSPF on the routers and L3 switches.
   
7 Static IP address to serverRoom devices.

﻿﻿﻿8 DHCP server device configurations.
   
﻿﻿﻿9 Inter-VLAN routing on the L3 switches plus ip dhcp helper addresses. Default static route.
   
﻿﻿﻿10 Wireless network configurations.
   
﻿11﻿﻿﻿ PAT + Access Control List
 
﻿﻿12 Site-to-site IPSec VPN
  
13 Verifying and testing configurations.

Version 2 da lam xong cac buoc tu 1-10.
