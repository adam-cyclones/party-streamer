from .server import serve

def prod():
    serve()
    pass


def dev():
    serve(dev=True)
    pass