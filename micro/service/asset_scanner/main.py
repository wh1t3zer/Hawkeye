# 分布式节点
import argparse
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
    description = "\033[32mProvide Service of Airth by GRPC.\033[0m"
    example = "\n\nexample:\n\t[-] 向注册中心(127.0.0.1:8848)注册主机(192.168.1.11:50051)服务:\n\t" \
              "python3 agent.py agent --registry_host IP --registry_port 8848 --server_name asset_scanner " \
              "--server_addr IP\n\t" \
              "\n\nexample:\n\t[-] 离线扫描脚本:\n\t" \
              "python3 agent.py  --registry_host IP --registry_port 8848 --server_name asset_scanner " \
              "--server_addr IP\n\t "
    description += example
    parser = argparse.ArgumentParser(description=description, prog='python3 main.py',
                                     formatter_class=RawTextHelpFormatter)
    subparsers = parser.add_subparsers(help='sub-command help')
    # 子命令 agent
    parser_a = subparsers.add_parser('agent', help='agent help')
    parser_a.add_argument('--registry_host', required=True, help='\t输入注册中心IP（必填）')
    parser_a.add_argument('--registry_port', required=True, help='\t输入注册中心端口（必填）')
    parser_a.add_argument('--server_name', required=True, help='\t输入服务名（必填）')
    parser_a.add_argument('--server_addr', required=True, help='\t输入本机出口IP，不为127.0.0.1')
    parser_a.add_argument('--server_port', required=True, help='\t输入服务端口，默认随机端口')

    # 默认函数 agent
    parser_a.set_defaults(function=agent)
    # 子命令 script
    parser_s = subparsers.add_parser('script', help='script help')
    parser_s.add_argument('--domain', required=False, help='\t目标域名（选填）IP和域名选其一')
    parser_s.add_argument('--ip', required=False, help='\t目标IP（选填）IP和域名选其一')
    parser_s.add_argument('--net', required=False, help='\t目标网段192.168.4.0/24')
    parser_s.add_argument('--webscan', type=bool, required=False, help='\t是否开启web扫描（选填），默认False')
    parser_s.add_argument('--verify', type=bool, required=False, help='\t是否开启POC（选填），默认False')
    parser_s.add_argument('--exploit', type=bool, required=False, help='\t是否使用EXP（选填）,默认False')
    parser_s.add_argument('--honeypot', type=bool, required=False, help='\t输入蜜罐识别(选填), 默认False')
    parser_s.add_argument('--conf', required=False, help='\t指定数据源(选填), 默认./data.json')
    parser_s.add_argument('--output', required=False, help='\t存储扫描结果的本地目录(选填), 默认./output/')

    # 默认函数script
    parser_s.set_defaults(func=script)
    args = parser.parse_args()
    # 执行函数
    args.func(args)


if __name__ == '__main__':
    main()
