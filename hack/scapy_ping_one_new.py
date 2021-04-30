import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import scapy
from scapy.all import *
from random import randint


def scapy_ping_one(host):
    id_ip = randint(1, 65535)
    id_ping = randint(1, 65535)
    seq_ping = randint(1, 65535)
    packet = IP(dst=host, ttl=1, id=id_ip) / ICMP(id=id_ping, seq=seq_ping) / b'welcometchina'
    ping = sr1(packet, timeout=2, verbose=False)
    # ping.show()
    if ping:
        return ping
        os._exit(3)


if __name__ == '__main__':
    scapy_ping_one("192.168.2.151")


