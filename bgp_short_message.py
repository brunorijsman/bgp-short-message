#!/usr/bin/env python3

import socket

BGP_IP = '127.0.0.1'

SHORT_MSG = (b'\xff\xff\xff\xff\xff\xff\xff\xff'     # First 8 bytes of marker
             b'\xff\xff\xff\xff\xff\xff\xff\xff'     # Last 8 bytes of marker
             b'\x00\x10')                            # Length 16

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
    sock.connect((BGP_IP, 179))
    print("Socket connected")
    sock.send(SHORT_MSG)
    print("Short message sent")

if __name__ == "__main__":
    main()