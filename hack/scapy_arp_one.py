import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
def scapy_arp_request(ip_address,queue=None):
    result_raw = srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(op=1,hwdst="00:00:00:00:00:00",pdst=ip_address),timeout= 1,verbose=False)
    # print(result_raw)
    # print(type(result_raw[0].res))
    # print(result_raw[0].res)
    try:
        result_list = result_raw[0].res
        # print(result_list[0][1].getlayer(ARP).fields["hwsrc"])

        # print("___________________")
        # print(result_list)
        if queue == None:
            return result_list[0][1].getlayer(ARP).fields["hwsrc"]
            # print(type(queue))
        else:
            # print(queue)
            queue.put((ip_address,result_list[0][1].getlayer(ARP).fields["hwsrc"]))
            # print(type(queue))

    except:
        return

if __name__ == "__main__":
    import sys
    print(scapy_arp_request("192.168.2.151"))