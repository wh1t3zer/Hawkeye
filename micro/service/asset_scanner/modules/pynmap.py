import json

import nmap


class NmapScanner:
    def __init__(self):
        self.target = ""

    # 运行程序
    def _run(self, target, ports, args):
        self.target = target
        np = nmap.PortScanner()
        try:
            if ports:
                return np.scan(hosts=target, ports=ports, arguments=args)
            else:
                return np.scan(hosts=target, arguments=args)
        except Exception as e:
            print(self.target, e)
            return False

    # 转换扫描结果
    def parse_scanresult(self, scan_result):
        result = {}
        portinfo_list = []
        data = scan_result['scan'][self.target]
        print(data)
        # 1、设备信息
        if "vendor" in data.keys():
            if len(data['vendor'].values()):
                result['vendor'] = list(data['vendor'].values())[0]
            else:
                "Unknow"

        # 2、获取系统消息
        if "osmatch" in data.keys():
            os_list = []
            for item in data['osmatch']:
                for os in item['osclass']:
                    os_list.append(os['osclass'])
            if len(os_list) == 0:
                result['os'] = 'Unknow'
            else:
                result['os'] = max(os_list, key=os_list.count)
                if result['vendor'] == 'Unknow':
                    result['vendor'] = result['os']
                else:
                    result['vendor']

        # 获取服务列表
        for key, val in data['tcp'].items():
            if val['state'] == 'closed':
                continue
            portinfo_list.append({
                'port': key, 'name': val['name'], 'state': val['state'], 'product': val['product'],
                'version': val['version'], 'extrainfo': val['extrainfo'], 'conf': val['conf'], 'cpe': val['cpe']
            })
        result['portinfo_list'] = portinfo_list
        return result

    # 返回扫描结果详情
    def get_detail(self, ip, ports='22-65535', args='-sV -O') -> dict:
        print("[+] Nmap get_detail Running....")
        scan_result = self._run(ip, ports, args)
        if not scan_result:
            return False
        print("[+] Nmap get_detail Finished....")
        return self.parse_scanresult(scan_result)

    # 返回存活主机列表
    def get_alive(self, net, args="-sn") -> list:
        print("[+] Nmap get_alive Running....")
        scan_result = self._run(net, ports='', args=args)
        if not scan_result:
            return False
        data = scan_result['scan']
        print("[+] Nmap get_alive Finished....")
        return list(data.keys())


if __name__ == '__main__':
    scanner = NmapScanner()
    ports_val = '22,25,53,80,111,631,3306,3389,5900,5901,7001,9200'
    data = scanner.get_detail('127.0.0.1', ports_val, '-sV -O')
    print(json.dumps(data))
