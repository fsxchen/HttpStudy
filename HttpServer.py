#!/usr/bin/python
#coding:utf-8

"""
study the http protocol
the base http server
"""
import socket, sys

returnData = "HTTP/1.1 200 OK\r\n"
returnData += "Server: PythonServer\r\n"
returnData += "Content-Type: text/html; charset=UTF-8\r\n"
# returnData += "Line-based text data: text/html"
returnData = """
<!DOCTYPE html>\n
<head>
<title>My frist Server</title>
</head>
<h1>aaa</h1>
<li>bbb</li>
</hmtl>\n
"""

# returnData += "hahahh"

class HttpServer():
    def __init__(self, host="127.0.0.1", port=8888):
        self.host = host
        self.port = port
        try:
            self.HttpSerSock = socket.socket()
        except Exception, e:
            print e
            sys.exit(-1)
    def run(self):
        self.HttpSerSock.bind((self.host, self.port))
        self.HttpSerSock.listen(5)
        while 1:
            connection, address = self.HttpSerSock.accept()
            data = connection.recv(2046)
            connection.send(returnData)
            print address, data

hs = HttpServer()
hs.run()