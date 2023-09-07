# PanelGroupData 头顶四个数据统计box
class PanelGroupData:
    VulCount: int
    AssetCount: int
    ServiceCount: int
    ResourceCount: int


# ChartSeries chart数据源
class ChartSeries:
    Name: str
    Value: int


# TableSeries 表格数据源
class TableSeries:
    VulID: str
    VulName: str
    VulType: str


# TimeLineSeries 时间线数据源
class TimeLineSeries:
    Content: str
    Timestamp: str
    Icon: str
    Type: str


# ChartBoxCard 卡片内容
class ChartBoxCard:
    Title: str
    Image: str
    Type: str
    Series: list


# TableBoxCard 卡片内容
class TableBoxCard:
    Title: str
    Image: str
    Type: str
    Series: list


# TimeLineBoxCard 卡片内容
class TimeLineBoxCard:
    Title: str
    Image: str
    Type: str
    Series: list


# Vulnerability 漏洞信息
class Vulnerability:
    VulID: str
    VulName: str
    VulType: str


# DashboardOutput 全局
class DashboardOutput:
    PanelGroup: PanelGroupData
    Box1: ChartBoxCard
    Box2: ChartBoxCard
    Box3: ChartBoxCard
    Box4: ChartBoxCard
    Box5: ChartBoxCard
    Box6: ChartBoxCard


# TaskDashboardOutput 任务视图
class TaskDashboardOutput:
    PanelGroup: PanelGroupData
    Box1: ChartBoxCard
    Box2: ChartBoxCard
    Box3: ChartBoxCard
    Box4: ChartBoxCard
    Box5: ChartBoxCard
    Box6: ChartBoxCard
    Status: str
    Percent: int
