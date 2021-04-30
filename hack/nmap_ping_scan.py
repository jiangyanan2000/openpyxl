import  nmap
import sys
def nmap_ping_scan(network_perfix):
    nm = nmap.PortScanner()
    ping_scan_raw_result = nm.scan(hosts=network_perfix,arguments="-v -n -sn")
    host_list = []
    # print(ping_scan_raw_result)
    # print(ping_scan_raw_result["scan"])
    for Result in ping_scan_raw_result["scan"].values():
        if Result["status"]["state"] == "up":
            host_list.append(Result["addresses"]["ipv4"])
        return host_list

if __name__ == "__main__":
    ip_list = []
    ip_addr = "192.16.2."
    for i in range(0,226):
        ip_addrs = ip_addr+str(i)
        ip_list.append(ip_addrs)
    for ip in ip_list:
        for host in nmap_ping_scan(ip):
                print("%-20s %5s" % (host,"is up!"))
