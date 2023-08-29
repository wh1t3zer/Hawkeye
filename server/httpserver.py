import json

import uvicorn
from fastapi import FastAPI,Request
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from middleware.response import response
from routes.user import router as user_router
from routes.admin import router as admin_router
from utils.const import AdminSessionInfoKey
from utils.file import read_config
from micro.Nacos import init

config = read_config('base.yaml')
PORT = config['http']['port']
app = FastAPI()
app.include_router(user_router)
app.include_router(admin_router)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=config['http']['allow_ip'])


#注册到nacos
# @app.on_event("startup")
# async def startup():
#     print('register for nacos')
#     init()


def runserver():
    uvicorn.run(app, host="0.0.0.0", port=PORT)
