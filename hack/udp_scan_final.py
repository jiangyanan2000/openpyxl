from scapy.all import *
from scapy_ping_one_new import scapy_ping_one
def udp_scan_final(hostname,lport,hport):
    ping_result = scapy_ping_one(hostname)
    if ping_result[1] == 2:
        print("设备"+hostname+"不可达！！！")
    else:
        result_raw = sr(IP(dst=hostname)/UDP(dport=(int(lport),int(hport))),
                        timeout=1,
                        verbose=False)
        scan_prot = []
        for x in range(int(lport),int(hport)):
            scan_prot.append(x)

        port_not_open = []
        result_list = result_raw[0].res
        for i in range(len(result_list)):
            if result_list[i][1].haslayer(ICMP):
                port_not_open.append(result_list[i][1][3].fields["dport"])
        return list(set(scan_prot).difference(set(port_not_open)))



if __name__ == "__main__":
    host = input("请输入你要扫描主机的IP:")
    port_low = input("请输入扫描端口号最低端口：")
    port_high = input("请输入扫描端口号最高端口：")
    # print(udp_scan_final())
    print("开放的端口号如下：")
    for port in udp_scan_final(host,port_low,port_high):
        print(port)



