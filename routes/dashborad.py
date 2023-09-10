from fastapi import FastAPI, APIRouter, websockets

app = FastAPI()
router = APIRouter(prefix='/dashboard')

# @Summary 所有数据统计(实时)
# @Description 所有数据统计(实时)
# @Tags 首页大盘
# @ID /dashboard/all
# @Accept  json
# @Produce  json
# @Success 200 {object} middleware.Response{data=DashboardOutput} "success"
# @Router /dashboard/all [get]
# @router.get("/all")
def DefaultDashboard():
    ws = websockets.WebSocket
    print(ws)

if __name__ == '__main__':
    DefaultDashboard()