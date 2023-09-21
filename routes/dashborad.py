from fastapi import FastAPI, APIRouter, Request
from starlette.websockets import WebSocket

import models
import schemas

router = APIRouter(prefix="/dashboard")
App = FastAPI()


# @Summary 所有数据统计(实时)
# @Description 所有数据统计(实时)
# @Tags 首页大盘
# @ID /dashboard/all
# @Accept  json
# @Produce  json
# @Success 200 {object} middleware.Response{data=DashboardOutput} "success"
# @Router /dashboard/all [get]
@router.get("/all")
@router.websocket("/all")
async def DefaultDashboard(websocket: WebSocket, request: Request):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        conn = True
        # 检查 websocket连接状态
        if data is None:
            conn = False
        else:
            while conn:
                out = schemas.dashborad.DashboardOutput(
                    PanelGroup=schemas.dashborad.PanelGroupData(),
                    Box1=schemas.dashborad.ChartBoxCard(
                        Title="Hardware",
                        Image="http://www.baidu.com",
                        Type="pie",
                        Series=schemas.dashborad.ChartSeries()
                    ),
                    Box2=schemas.dashborad.ChartBoxCard(
                        Title="Software",
                        Image="http://www.baidu.com",
                        Type="pie",
                        Series=schemas.dashborad.ChartSeries()
                    ),
                    Box3=schemas.dashborad.ChartBoxCard(
                        Title="SubDomain",
                        Image="http://www.baidu.com",
                        Type="pie",
                        Series=schemas.dashborad.ChartSeries()
                    ),
                    Box4=schemas.dashborad.ChartBoxCard(
                        Title="Vul Type",
                        Image="https://www.baidu.com",
                        Type="pie",
                        Series=schemas.dashborad.ChartSeries()
                    ),
                    Box5=schemas.dashborad.ChartBoxCard(
                        Title="Latest Vul",
                        Image="http://www.baidu.com",
                        Type="table",
                        Series=schemas.dashborad.Vulnerability()
                    ),
                    Box6=schemas.dashborad.ChartBoxCard(
                        Title="Web Site",
                        Image="http://www.baidu.com",
                        Type="line",
                        Series=schemas.dashborad.ChartSeries()
                    )
                )

        # 1、资产
        asset = models.assets.AssetInfo()
        assetArray, atotal = models.assets.AllRecord(request)
        vendors = []
        for asset in assetArray:
            vendors[asset.Vendor] += 1

        # 2、查域名
        domain = models.domain.DomainInfo()
        domainArray, atotal = models.domain.AllRecord(request)
        domains = []
        for domain in domainArray:
            for item in str(domain.SubDomainList).split(","):
                if item is not None:
                    domains[item] += 1

        # 3、查端口表
        srv = models.PortInfo()
        portArray, stotal = models.src.AllRecord(request)
        # 遍历端口表
        softwares = []
        for portinfo in portArray:
            software = portinfo.Product
            if software is None:
                software = portinfo.Name
            softwares[software] += 1

        # 4、Web信息
        web = models.WebInfo()
        webArray = web

    # async def checkWs():
    #     while True:
    #         data = await websocket.receive_text()
    #         print(data)
    #         print(websocket)
    #     isborke = False
