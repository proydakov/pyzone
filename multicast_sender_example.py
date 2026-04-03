import sys
import time
import socket


def sender_socket_builder(interface_ip : str = None):
    # regarding socket.IP_MULTICAST_TTL
    # ---------------------------------
    # for all packets sent, after two hops on the network the packet will not 
    # be re-sent/broadcast (see https://www.tldp.org/HOWTO/Multicast-HOWTO-6.html)
    MULTICAST_TTL = 2

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
    if interface_ip:
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.inet_aton(interface_ip))

    return sock


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Command line args should be multicast group, port and optional interface")
        print("(e.g. for SSDP, `sender 239.255.255.250 5555 [127.0.0.1]`)")
        sys.exit(1)

    mcast_grp = sys.argv[1]
    mcast_port = int(sys.argv[2])
    interface_ip = None
    if len(sys.argv) == 4:
        interface_ip = sys.argv[3]

    sock = sender_socket_builder(interface_ip)

    while True:
        tns = time.time_ns()
        data = str(tns).encode("utf-8")
        sock.sendto(data, (mcast_grp, mcast_port))
        time.sleep(500.0 / 1_000_000)
