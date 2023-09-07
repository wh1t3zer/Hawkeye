import yaml
import os


# 查看配置文件
def read_config(filename):
    # 获取yaml文件路径
    yamlPath = os.path.join(os.path.dirname(__file__), '../conf/' + filename).replace("\\", "/")

    with open(yamlPath, 'rb') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config
