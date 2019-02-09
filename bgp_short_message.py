#!/usr/bin/env python3

import socket

BGP_IP = '127.0.0.1'

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
    sock.connect((BGP_IP, 179))
    print("Socket connected")





if __name__ == "__main__":
    main()
