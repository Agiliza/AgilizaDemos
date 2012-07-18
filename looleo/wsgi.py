import os
import sys

from agiliza.core.handlers import WSGIHandler


sys.path.append(os.path.join(os.getcwd(), '..'))
os.environ['AGILIZA_CONFIG'] = 'looleo.config'

application = WSGIHandler()

if __name__ == "__main__":
    from wsgiref.util import setup_testing_defaults
    from wsgiref.simple_server import make_server

    httpd = make_server('', 8888, application)
    print("Serving on port 8888...")
    httpd.serve_forever()
