from fastapi import FastAPI
from app.routers import user, workspace, node, qa

app = FastAPI()

app.include_router(user.router)
app.include_router(workspace.router)
app.include_router(node.router)
app.include_router(qa.router)
