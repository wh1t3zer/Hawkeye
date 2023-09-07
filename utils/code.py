import hashlib
from hashlib import sha256

# 密码加盐
import jsonmarshal

# 加盐 源密码sha256->二次密码+盐 sha256
def GenSaltPassword(password, salt):
    sh = sha256()
    sh.update(password.encode('utf-8'))
    Str = sh.hexdigest() + salt
    sh1 = sha256()
    sh1.update(Str.encode('utf-8'))
    return sh1.hexdigest()


# md5
def MD5(crypt: str):
    md5 = hashlib.md5()
    md5.update(crypt.encode('utf-8'))
    result = md5.hexdigest()
    return result


# 判断切片是否存在该字符串
def InStringSlice(Slice: list, s: str):
    for item in range(Slice):
        if item == s:
            return True
    return False


# Obj转JSON 结构体对象转JSON
def Obj2Json(s: object):
    jsonmarshal.marshal(s)
    return str(s)
