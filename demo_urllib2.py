
from urllib2 import Request
from urllib2 import urlopen

import json


rq = Request("http://locahost:8888/")
rq.add_header("accept", "application/json")

response = urlopen(rq)

# devuelve el contenido
text = response.readlines()[0]

ob = json.loads(text)
#ob es un listado de diccionarios que representan books


