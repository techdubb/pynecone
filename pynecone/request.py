from urllib import urlencode
from urllib2 import Request, urlopen
from simplejson import loads
from settings import Settings

class Request(object):

    # Handle GET requests
    @classmethod
    def get(self, path, parameters = {}):
        path = "%s%s?%s" % (Settings.host, path, urlencode(parameters))

        return self.request(path)

    # Handle POST requests  
    @classmethod
    def post(self, path, parameters={}):
        path = "%s%s" % (Settings.host, path,)

        return self.request(path, parameters)

    @classmethod
    def request(self, path, parameters = {}):

        if len(parameters) == 0:
            f = urlopen(path)
        else:
            f = urlopen(path, urlencode(parameters))

        return loads(f.read())
