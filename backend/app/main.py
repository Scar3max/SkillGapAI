from fastapi import FastAPI
from backend.app.api import auth,analysis
from backend.app.events import registry

app=FastAPI()

app.include_router(auth.router,prefix='/auth',tags=['auth'])

app.include_router(analysis.router,prefix='/analysis',tags=['analysis'])