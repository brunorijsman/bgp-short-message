#!/usr/bin/env python3

import socket
impor struct

BGP_IP = '172.31.31.121'

SHORT_MSG = (b'\xff\xff\xff\xff\xff\xff\xff\xff'     # First 8 bytes of marker
             b'\xff\xff\xff\xff\xff\xff\xff\xff'     # Last 8 bytes of marker
             b'\x00\x10'                             # Length 16
             b'\x01')                                # Open

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
    sock.connect((BGP_IP, 179))
    print("Socket connected")
    sock.send(SHORT_MSG)
    # Trick TCP into sending a RST when the socket is closed
    on_off = 1
    linger = 0
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', on_off, linger))
    print("Socket linger time set to 0")
    # Close the socket
    sock.close()
    print("Socket closed")
    # Terminate without reading the response NOTIFICATION

if __name__ == "__main__":
    main()
