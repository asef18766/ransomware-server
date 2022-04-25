#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socketserver, sys, threading
from time import ctime
import keystore

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        cur = threading.current_thread()
        print('[%s] Client connected from %s and [%s] is handling with him.' % (ctime(), self.request.getpeername(), cur.name))
        while True:
            try:
                indata:str = self.request.recv(1024).decode()
                print('recv: ' + indata)
                
                iv, key = indata.split("|")
                keystore.save_key(bytes.fromhex(iv), bytes.fromhex(key))
                
                outdata = 'echo ' + indata
                self.request.send(outdata.encode())
            except ConnectionResetError:
                print(f'client {self.request.getpeername()} closed connection.')
                break

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

if __name__ == '__main__':
    HOST, PORT = '0.0.0.0', 7000
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address
    print('server start at: %s:%s' % (HOST, PORT))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)