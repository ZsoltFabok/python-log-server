from log_server.server import Server
import sys


if __name__ == "__main__":
    config_file = sys.argv[1]
    Server().start(config_file)
