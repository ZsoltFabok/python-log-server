from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import yaml
import logging
from logging.handlers import TimedRotatingFileHandler


class Server():
    class MyHandler(BaseHTTPRequestHandler):
        def do_POST(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            content_len = int(self.headers.get('content-length', 0))
            log_entry = log_entry_parser(self.rfile.read(content_len))

            self.server.logger.info(' - '.join(log_entry))
            return

        def log_message(self, format, *args):
            # FIXME: not safe, because ignores all kinds of issues
            return

    def init_logger(self, filename):
        handler = TimedRotatingFileHandler(filename=filename, when='midnight', backupCount=5)
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        logger = logging.getLogger("server")
        logger.setLevel(logging.INFO)
        logger.propagate = False
        logger.handlers = []
        logger.addHandler(handler)
        return logger

    def start(self, config_file):
        try:
            # FIXME would be nice to load the configuration every minute so
            # that I don't have to restart the server every time there is a change
            with open(config_file, 'r') as file:
                self.config = yaml.load(file)

            print('Server started to listen on port {}'.format(self.config['port']))
            server = HTTPServer((self.config['host'], self.config['port']), self.MyHandler)
            server.logger = self.init_logger(self.config['log_file'])
            server.serve_forever()
        except Exception as e:
            # FIXME this not nice
            print(e)


def log_entry_parser(log_entry_raw):
    log_entry = parse.unquote(log_entry_raw.decode())
    log_data = dict([(x.split('=')[0], x.split('=')[1]) for x in log_entry.split('&')])
    return [log_data['asctime'].replace('+', ' '), log_data['name'].replace('+', ' '), log_data['levelname'], log_data['message'].replace('+', ' ')]
