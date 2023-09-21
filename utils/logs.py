from datetime import timedelta
from loguru import logger


# 清除默认日志记录器
logger.remove()

# def _filter(record, request: Request):
#     record["extra"] = {"traceid": request.state.context.request_id}
#     return True
# 创建新日志记录器
# 命名格式“年-月-日”形式
# request.app.state.logger.info("xxxx") 使用Request类传全局变量
logger.add(
    sink="./logs/hawkeye.{time:YYYY_MM_DD}.log",
    format=("{time:YYYY-MM-DD HH:mm:ss} | {level} | {message} "),
    level="INFO",
    rotation="1 days",
    retention=timedelta(days=7),
    # filter=_filter
)
