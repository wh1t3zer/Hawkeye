import nmap
class NmapScanner:
    def __init__(self):
        self.target = ""

    #运行程序
    def run(self,target,port,args):
        self.target = target
        np = nmap.PortScanner()