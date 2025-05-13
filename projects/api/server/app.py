from fastapi import FastAPI
from server.routers.logs import logs_router

app = FastAPI()

app.include_router(
    # Include the routers from the scene_graph module
    # This is a placeholder, replace with actual routers
    logs_router
    # scene_graph.routers.another_router,
)