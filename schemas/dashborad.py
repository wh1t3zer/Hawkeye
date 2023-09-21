from pydantic import BaseModel

from schemas.vul import VulInfoOutput


# PanelGroupData 头顶四个数据统计box
class PanelGroupData(BaseModel):
    VulCount: int
    AssetCount: int
    ServiceCount: int
    ResourceCount: int

    class Config:
        orm_mode = True


# ChartSeries chart数据源
class ChartSeries(BaseModel):
    Name: str
    Value: int

    class Config:
        orm_mode = True


# TableSeries 表格数据源
class TableSeries(BaseModel):
    VulID: str
    VulName: str
    VulType: str

    class Config:
        orm_mode = True


# TimeLineSeries 时间线数据源
class TimeLineSeries(BaseModel):
    Content: str
    Timestamp: str
    Icon: str
    Type: str

    class Config:
        orm_mode = True


# 基础内容模型
class BaseBoxCard(BaseModel):
    Title: str
    Image: str
    Type: str

    class Config:
        orm_mode = True


# ChartBoxCard 卡片内容
class ChartBoxCard(BaseBoxCard):
    Series: ChartSeries

    class Config:
        orm_mode = True


# TableBoxCard 卡片内容
class TableBoxCard(BaseBoxCard):
    Series: VulInfoOutput

    class Config:
        orm_mode = True


# TimeLineBoxCard 卡片内容
class TimeLineBoxCard(BaseBoxCard):
    Series: TimeLineSeries

    class Config:
        orm_mode = True


# Vulnerability 漏洞信息
class Vulnerability(BaseModel):
    VulID: str
    VulName: str
    VulType: str

    class Config:
        orm_mode = True


# DashboardOutput 全局
class DashboardOutput(BaseModel):
    PanelGroup: PanelGroupData
    Box1: ChartBoxCard
    Box2: ChartBoxCard
    Box3: ChartBoxCard
    Box4: ChartBoxCard
    Box5: ChartBoxCard
    Box6: ChartBoxCard

    class Config:
        orm_mode = True

    # def __init__(self, PanelGroup, Box1, Box2, Box3, Box4, Box5, Box6):
    #     self.PanelGroup = PanelGroup
    #     self.Box1 = Box1
    #     self.Box2 = Box2
    #     self.Box3 = Box3
    #     self.Box4 = Box4
    #     self.Box5 = Box5
    #     self.Box6 = Box6


# TaskDashboardOutput 任务视图
class TaskDashboardOutput(DashboardOutput):
    Status: str
    Percent: int

    class Config:
        orm_mode = True
