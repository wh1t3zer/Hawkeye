# 分布式节点
import json

from micro.service.asset_scanner.handler.script import AssetScanner


def agent(args):
    pass


# 离线脚本扫描
def script(args):
    if not args.domain and not args.ip:
        print("error missing arguments --domain or --ip")
        return
    domain_dict = None
    scan_ports = None
    conf_path = args.conf
    if not conf_path:
        conf_path = DOMAIN_BRUTE_DICT
    try:
        with open(conf_path, "r") as f:
            conf_data = json.loads(f.read())
            domain_dict = conf_data['domain_dict']
            scan_ports = ','.join(conf_data['domain_dict'])
    except Exception as e:
        print("Failed loading conf_data,Info: ", e)
        return
    print("scan_ports", scan_ports, domain_dict, args.webscan)
    if args.domain:
        as_scanner = AssetScanner(
            # 域名、端口、漏扫、poc、exp、蜜罐
            domain=args.domain,
            scan_port=scan_ports,
            domain_dict=domain_dict,
            webscan=args.webscan,
            verify=args.verify,
            exploit=args.exploit,
            honeypot=args.honeypot
        )
    elif args.ip:
        as_scanner = AssetScanner(
            # ip、端口、漏扫、poc、exp、蜜罐
            ip=args.ip,
            scan_port=scan_ports,
            webscan=args.webscan,
            verify=args.verify,
            exploit=args.exploit,
            honeypot=args.honeypot
        )
    else:
        print("[*]Unknown Error")
        return
    resp = as_scanner.Run()
    if not resp:
        print("[*]Response data nothing")
        return
    filename = as_scanner.save_result(resp, dirs=args.output)
    if filename:
        print("[*]Save Result data at ", filename)


def main():
    print("\033[33m\t\t---------- Asset Scanner ----------\033[0m")
