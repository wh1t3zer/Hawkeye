import re

from micro.service.asset_scanner.modules.pynmap import NmapScanner


class AssetScanner:
    """
    example
    127.0.0.1 / test.com
    """

    def __init__(
            self, domain="", ip="", scan_port="22,25,53,80,3306,5900,6379,7001,8080,8081,9000,27017"
            , domain_dict=['www', 'main', 'smtp'],
            webscan=False, verify=False, exploit=False, honeypot=False
    ):
        self.domain = self._format_domain(domain)
        self.ip = self._format_ip(ip)
        self.host = self._format_host()
        self.scan_port = scan_port
        self.honeypot = honeypot
        self.webscan = webscan
        self.verify = verify
        self.exploit = exploit
        self.domain_dict = domain_dict

    def _format_domain(self, domain):
        # 正则匹配域名是否正确
        pattern = re.compile(
            r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|'
            r'([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|'
            r'([a-zA-Z0-9][-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9]))\.'
            r'([a-zA-Z]{2,13}|[a-zA-Z0-9-]{2,30}.[a-zA-Z]{2,3})$'
        )
        if pattern.match(domain):
            return domain
        else:
            return False

    def _format_ip(self, ip):
        # 判断输入是否正确IP
        pattern = re.compile(
            '^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$'
        )
        if pattern.match(ip):
            return ip
        else:
            return False

    def _format_host(self):
        if not self.domain and not self.ip:
            print("Failed Scan asset,Invalid IP or Domain")
            return False
        else:
            if self.domain:
                return self.domain
            else:
                return self.ip

    # 主机扫描,主程序
    def hostinfo_scan(self):
        """
        一、域名解析，查询，IP信息，子域名爆破
        二、主机信息、端口
        """
        # 使用nmap模块
        result = NmapScanner().get_detail(self.host, ports=self.scan_port)

