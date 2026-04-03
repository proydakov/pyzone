import sys
import time
import struct
import socket


def listener_socket_builder(mcast_grp : str, mcast_port : int, interface_ip : str = None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # on this port, listen ONLY to MCAST_GRP
    sock.bind((mcast_grp, mcast_port))

    if interface_ip:
        mreq = struct.pack('4s4s', socket.inet_aton(mcast_grp), socket.inet_aton(interface_ip))
    else:
        mreq = struct.pack('4sl', socket.inet_aton(mcast_grp), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    return sock


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Command line args should be multicast group, port and optional interface")
        print("(e.g. for SSDP, `listener 239.255.255.250 5555 [127.0.0.1]`)")
        sys.exit(1)

    mcast_grp = sys.argv[1]
    mcast_port = int(sys.argv[2])
    interface_ip = None
    if len(sys.argv) == 4:
        interface_ip = sys.argv[3]

    sock = listener_socket_builder(mcast_grp, mcast_port, interface_ip)

    while True:
        data, address = sock.recvfrom(1500)

        tns = time.time_ns()
        rtns = int(data.decode("utf-8"))
        delta = tns - rtns
        print(delta)
