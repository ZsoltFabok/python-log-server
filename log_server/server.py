from http.server import BaseHTTPRequestHandler, HTTPServer
import yaml


class Server():
    class MyHandler(BaseHTTPRequestHandler):
        def do_POST(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            content_len = int(self.headers.get('content-length', 0))
            print(self.rfile.read(content_len))
            return

    def start(self, config_file):
        try:
            # FIXME would be nice to load the configuration every minute so
            # that I don't have to restart the server every time there is a change
            with open(config_file, 'r') as file:
                self.config = yaml.load(file)

            print('Server started to listen on port {}'.format(self.config['port']))
            server = HTTPServer((self.config['host'], self.config['port']), self.MyHandler)
            server.serve_forever()
        except Exception as e:
            # FIXME this not nice
            print(e)


def log_entry_parser(log_entry):
    return log_entry