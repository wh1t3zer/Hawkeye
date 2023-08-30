import hashlib
from hashlib import sha256

#密码加盐
def GenSaltPassword(password,salt):
    sh = sha256()
    sh.update(password.encode('utf-8'))
    Str = sh.hexdigest()+salt
    sh1 = sha256()
    sh1.update(Str.encode('utf-8'))
    return sh1.hexdigest()

#md5
def MD5(crypt: str):
    md5 = hashlib.md5()
    md5.update(crypt.encode('utf-8'))
    result = md5.hexdigest()
    return result
