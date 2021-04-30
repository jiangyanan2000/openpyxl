import ipaddress
import time
from hack.scapy_arp_one import scapy_arp_request
from multiprocessing import Process, Queue


def scapy_arp_scan(network):
    qyt_queue = Queue()
    net = ipaddress.ip_network(network)
    for ip in net:
        ip_addr = str(ip)
        arp_one = Process(target=scapy_arp_request, args=(ip_addr, qyt_queue))
        arp_one.start()
    time.sleep(1)

    ip_mac_list = []
    while True:
        if qyt_queue.empty():
            break
        else:
            ip, mac = qyt_queue.get()
            ip_mac_list.append((ip, mac))
    return ip_mac_list


if __name__ == "__main__":

    active_ip_mac = scapy_arp_scan('192.168.2.0/24')
    print("活动的Ip与MAC地址如下：")
    # print(active_ip_mac)
    for ip, mac in active_ip_mac:
        # print(11111)
        print(ip, mac)
