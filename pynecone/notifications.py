from request import Request

class Notifications(object):

    @classmethod
    def notifications(self, **kwargs):
        return Request.get("notifications", kwargs)
