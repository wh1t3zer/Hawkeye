import os


# 路径是否存在
def PathExist(path):
    if os.path.exists(path):
        return True
    else:
        return False
