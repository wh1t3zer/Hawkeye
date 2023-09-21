from fastapi import FastAPI, APIRouter, Request, Depends
from sqlalchemy.orm import Session

import schemas.asset
from models.assets import AssetInfo
from schemas import public
from utils.database import get_db

app = FastAPI()
router = APIRouter(prefix="/asset")


@router.post("/list")
def AssetList(parms: schemas.public.PublicListInput, db: Session = Depends(get_db)):
    info = AssetInfo()
    # list = info.PageList(db, parms)
    #info.Delete(db)
   # List = Find(db)
    #list = info.AllRecord(db, 1)
    list = info.AllRecord(db,3)
    return list
   # return List
