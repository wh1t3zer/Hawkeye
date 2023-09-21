import time
from typing import List

import schemas.public
from utils.database import Base
from sqlalchemy import Column, Integer, and_, or_, func
from sqlalchemy.orm import Session


class AssetInfo(Base):
    __tablename__ = "hawkeye_asset"
    id = Column(Integer, primary_key=True, index=True, nullable=False)  # 自增主键
    task_id = Column(Integer, nullable=False)  # 任务ID
    ip = Column(Integer, nullable=False)  # IP
    gps = Column(Integer, nullable=False)  # GPS
    area = Column(Integer, nullable=False)  # 区域
    isp = Column(Integer, nullable=False)  # 运营商
    os = Column(Integer, nullable=False)  # 操作系统
    vendor = Column(Integer, nullable=False)  # 设备
    create_at: time.time()  # 添加时间
    is_delete = Column(Integer, nullable=False)  # 是否已删除；0：否；1：是

    def Find(self, db: Session):
        result = db.query(AssetInfo).all()
        return result

    def Save(self, db: Session):
        db.commit()
        db.add()

    def Delete(self, db: Session, id):
        query = db.query(AssetInfo)
        query = query.filter_by(id=id).delete()
        db.commit()
        return query

    def PageList(self, db: Session, param: schemas.public.PublicListInput):
        pageNo = param.Page
        pageSize = param.Limit

        # limit offset pagesize
        offset = (pageNo - 1) * pageSize
        query = db.query(AssetInfo)
        query = query.filter_by(is_delete='0')
        if param.Info is not None:
            query = query.where(

                or_(AssetInfo.ip.like("%" + param.Info + "%"), AssetInfo.vendor.like("%" + param.Info + "%"))).all()
        # recordList = db.query(AssetInfo).order_by(AssetInfo.id.desc()).limit(pageSize).offset(offset).all()
        # 切片，判断有无数据
        recordList = db.query(AssetInfo).order_by(AssetInfo.id.desc()).all()[offset:pageSize]
        count = len(query)
        if recordList is None:
            return None, 0
        if count == 0:
            return None, 0
        return query, count

    def AllRecord(self, db: Session, taskID):
        query = db.query(AssetInfo)
        query = query.filter_by(is_delete='0')
        count: int
        if taskID > 0:
            query = query.where("task_id" == taskID).all()
            result = db.query(AssetInfo).order_by(AssetInfo.id.desc()).all()

            if result is None:
                return None, 0
            if count == 0:
                return None, 0
        else:
            query = query.all()
            return query, count
