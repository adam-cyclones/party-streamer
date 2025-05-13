import uvicorn

def serve(dev: bool = False):
    uvicorn.run("server.app:app", host="0.0.0.0", port=9000, reload=dev)