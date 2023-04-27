# apr/27/2023 11:34:59 by RouterOS 7.8
# software id = WE38-MTWZ
#
# model = RB2011UiAS-2HnD
# serial number = 7A6608DB8F36
/interface bridge
add name=bridge1
/interface ethernet
set [ find default-name=ether6 ] disabled=yes
set [ find default-name=ether7 ] disabled=yes
set [ find default-name=ether8 ] disabled=yes
set [ find default-name=ether10 ] disabled=yes
set [ find default-name=sfp1 ] disabled=yes
/interface wireless
set [ find default-name=wlan1 ] ssid=MikroTik
/interface ethernet switch port
set 2 default-vlan-id=200 vlan-header=always-strip vlan-mode=secure
set 3 default-vlan-id=300 vlan-header=always-strip vlan-mode=secure
set 4 default-vlan-id=400 vlan-header=always-strip vlan-mode=secure
set 5 default-vlan-id=500 vlan-header=always-strip vlan-mode=secure
/interface list
add name=PERMITE-WINBOX
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/port
set 0 name=serial0
/interface bridge port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4
add bridge=bridge1 interface=ether5
/ip neighbor discovery-settings
set discover-interface-list=PERMITE-WINBOX
/interface ethernet switch vlan
add independent-learning=yes ports=ether1,ether2 switch=switch1 vlan-id=200
add independent-learning=yes ports=ether1,ether3 switch=switch1 vlan-id=300
add independent-learning=yes ports=ether1,ether4 switch=switch1 vlan-id=400
add independent-learning=yes ports=ether1,ether5 switch=switch1 vlan-id=500
/interface list member
add interface=ether9 list=PERMITE-WINBOX
/ip cloud
set update-time=no
/ip dhcp-client
add interface=ether9
/ip service
set telnet disabled=yes
set ftp disabled=yes
set www disabled=yes
set api disabled=yes
set api-ssl disabled=yes
/ip ssh
set allow-none-crypto=yes always-allow-password-login=yes
/system clock
set time-zone-autodetect=no
/tool mac-server
set allowed-interface-list=PERMITE-WINBOX
/tool mac-server mac-winbox
set allowed-interface-list=PERMITE-WINBOX
/tool mac-server ping
set enabled=no
