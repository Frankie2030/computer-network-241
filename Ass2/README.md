# Version 4.5.1

**Cơ bản đã hoàn thành xong tất cả mọi thứ. Dưới đây là danh sách cần demo:**

## 1. Inter-VLAN Routing
- Sử dụng tính năng Simple PDU để kiểm tra nhanh.
  - **1.1**: PC pings each other.
  - **1.2**: PC pings Smartphone và ngược lại.
  - **1.3**: PC pings Webcam và ngược lại.

## 2. Inter-Site Routing (Between VLANs)
- Sử dụng tính năng ping.
  - **2.1**: PC pings to server.
  - **2.2**: Server pings to PC.

## 3. ACL on L3 Switch: Camera - Server - PC System
- Surveillance room: VLAN 60 (192.168.60.0/25).
  - **3.1**: PC và Server không thể truy cập VLAN 60 và ngược lại.
  - **3.2**: Webcam từ mỗi department có thể truy cập VLAN 60 và ngược lại.

## 4. WAN Routing and Site-to-Site IPSec VPN
- **4.1**: Demo PC pinging từ main site đến aux site 1 và 2, và ngược lại.
- **4.2**: IPSec VPN:
  - **4.2.1**: Từ main router, `show crypto isakmp sa`. State=QM_IDLE.
  - **4.2.2**: Từ main router, `show crypto ipsec sa`, giải thích số packets encaps và decaps. Demo khi sử dụng dịch vụ HTTP thì chỉ có số packets decaps.

## 5. Servers
- **5.1**: DHCP server cung cấp IP cho các department. IP của servers và webcams là static.
- **5.2**: Web server và DNS server:
  - Main site: `ccc-hospital.main.in`.
  - Aux site 1: `ccc-hospital.aux1.in`.
  - Aux site 2: `ccc-hospital.aux2.in`.
  - Public: `ccc-hospital.com`.
  - **Note**: Các thiết bị từ main site có thể kết nối đến servers trên aux site 1 và 2.

## 6. Services
- **Sử dụng**: DMZ, DNS server, Web server, File server, Email server, NAT overload.
  - **6.1**: External DNS và Web server cho khách hàng. Khách hàng truy cập website chính thức của bệnh viện.
    - **6.1.1**: `show ip nat trans`.
  - **6.2**: Email server (192.168.250.4).
    - **6.2.1**: Tạo usernames và passwords trong Email Server. Cấu hình Mail trên PC client.
    - **6.2.2**: Demo gửi và nhận email.
    - **6.2.3**: Demo từ chối user không hợp lệ (SMTP authentication failed).
    - **6.2.4**: Demo gửi email đến user không đăng ký (Send Successful nhưng có Send Notification Failure).
    - **6.2.5**: `show ip nat trans`.
  - **6.3**: File server (chỉ làm việc với file có sẵn).
    - **6.3.1**: Tạo tài khoản trên File server. Xác thực từ PC client (`ftp 192.168.250.3`).
    - **6.3.2**: Download file từ File server (`get <file_name>`).
    - **6.3.3**: Tạo file txt từ text editor.
    - **6.3.4**: Upload file lên File server (`put <file_name>`).
    - **6.3.5**: Kiểm tra file mới trên File server.
    - **6.3.6**: Đăng nhập bằng user khác và kiểm tra file mới. Download file đó.
    - **6.3.7**: `show ip nat trans`.

## 7. Verify and Disqualify Connection Between Internal and External Network
- **Sử dụng**: DMZ, Firewall, NAT overload.
  - **7.1**: INSIDE to DMZ (`ccc-hospital.com`); INSIDE to OUTSIDE1/2 (`google.com`).
  - **7.2**: DMZ to OUTSIDE1/2.
  - **7.3**: OUTSIDE1/2 to DMZ, chỉ cho phép HTTP và DNS từ 192.168.250.2 (`ccc-hospital.com`).
  - **7.4**: DMZ to INSIDE, chỉ cho phép ping và tracert đến DNS-Web server 200.0.0.2 của Main site.
  - **7.5**: `show ip nat trans` ở main router (sử dụng NAT overload). Giải thích inside local, inside global, outside global/local.

## 8. Client-to-Site VPN (Remote Access VPN)
- **8.1**: Tạo VPN client: `usergroup=remoteccc`, `userkey=vpnremote`, `hostserver=192.168.11.2`, `username=admin`, `password=admin`.
- **8.2**: `ipconfig /all`.
- **8.3**: Từ main site router, ping đến `192.180.0.x` (IP từ VPNCLIENT pool: `192.180.0.0 -> 192.180.0.50`).
- **8.4**: Từ remote PC, ping đến main site router (`192.168.11.2`); tracert đến VLAN 10, VLAN 60 (Surveillance - Fail), VLAN 200.
- **8.5**: Từ main site router, xác minh kết nối VPN:
  - **8.5.1**: `show crypto isakmp sa`. State=QM_IDLE.
  - **8.5.2**: `show crypto ipsec sa`. Kiểm tra `crypto map staticmap`.






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
