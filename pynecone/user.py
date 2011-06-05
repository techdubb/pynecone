from request import Request

class User(object):
    
    @classmethod
    def auth(self, **kwargs):
        return Request.post("users/auth", kwargs)

    @classmethod
    def info(self, **kwargs):
        return Request.get("users/info", kwargs)

    @classmethod
    def posts(self, **kwargs):
        return Request.get("user/posts", kwargs)
