from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import yaml
import collections


class Server():
    class MyHandler(BaseHTTPRequestHandler):
        # FIXME: server should log to somewhere else, not to stdout
        def do_POST(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            content_len = int(self.headers.get('content-length', 0))
            log_entry = log_entry_parser(self.rfile.read(content_len))
            # FIXME this should go to a file
            print(' - '.join(log_entry.values()))

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


def log_entry_parser(log_entry_raw):
    log_entry = parse.unquote(log_entry_raw.decode())
    log_data = dict([(x.split('=')[0],x.split('=')[1]) for x in log_entry.split('&')])

    return collections.OrderedDict({
        'datetime':    log_data['asctime'].replace('+', ' '),
        'logger_name': log_data['name'],
        'level_name':  log_data['levelname'],
        'message':     log_data['message'].replace('+', ' ')
    })
