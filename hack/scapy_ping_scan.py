import multiprocessing
import ipaddress
from hack.scapy_ping_one import scapy_ping_one

def scapy_ping_scan(network):
    net = ipaddress.ip_network(network)
    ip_address = {}
    for ip in net:
        ip_addr = str(ip)
        ping_one = multiprocessing.Process(target=scapy_ping_one,args=(ip_addr,))
        ping_one.start()
        ip_address[ip_addr] = ping_one
    ip_list = []
    for ip ,process in ip_address.items():
        if process.exitcode == 3:
            ip_list.append(ip)
        else:
            process.terminate()
    return sorted(ip_list)

if __name__ == '__main__':
    import time
    t1 = time.time()
    active_ip = scapy_ping_scan('192.168.2.0/24')
    print("活动Ip地址如下：")
    for ip in active_ip:
        print(ip)
    t2 = time.time()
    print("总共运行的时间为：",t2-t1)


