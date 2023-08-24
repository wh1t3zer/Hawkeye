from fastapi import FastAPI
import uvicorn
from micro.Nacos import init
from routes.user import router as user_router
from util.file import read_config
from fastapi.middleware.trustedhost import TrustedHostMiddleware

config = read_config('base.yaml')
PORT = config['port']
app = FastAPI()
app.include_router(user_router)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=config['allow_ip'])

@app.on_event("startup")
async def startup():
    print('run application')
    init()

@app.get("/")
def index():
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1",port=PORT)
