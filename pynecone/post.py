from request import Request

class Post(object):
    
    @classmethod
    def show(self, **kwargs):
        return Request.get("posts/show", kwargs)

    @classmethod
    def all(self, **kwargs):
        return Request.get("posts/all", kwargs)

    @classmethod
    def list(self, **kwargs):
        return Request.get("posts/list", kwargs)

    @classmethod
    def comments(self, **kwargs):
        return Request.get("post/comments", kwargs)
