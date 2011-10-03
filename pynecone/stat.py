from request import Request

class Stat(object):

    @classmethod
    def stats(self, **kwargs):
        return Request.get("stats", kwargs)
