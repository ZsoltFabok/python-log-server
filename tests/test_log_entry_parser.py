import unittest
from log_server.server import log_entry_parser


class LogEntryParserTestCase(unittest.TestCase):

    def test_parser(self):
        log_entry = b'pathname=C%3A%2FUsers%2Fzsolt%2FWork%2Fpython-log-server%2Flog_client.py&funcName=%3Cmodule%3E&relativeCreated=24.088144302368164&thread=13352&exc_info=None&name=localhost&msg=hello+zsolti&asctime=2017-06-23+22%3A33%3A43%2C988&stack_info=None&threadName=MainThread&exc_text=None&levelname=INFO&process=16968&args=%28%29&created=1498250023.988958&levelno=20&processName=MainProcess&lineno=24&module=log_client&message=hello+zsolti&msecs=988.9578819274902&filename=log_client.py'
        self.assertEqual(None, log_entry_parser(log_entry))