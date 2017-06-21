#!/usr/bin/env python

import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8001


class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write("Hello World !")
        return


try:
    server = HTTPServer(('localhost', PORT), MyHandler)
    print("serving at port", PORT)
    server.serve_forever()
except Exception as e:
    print(e)
