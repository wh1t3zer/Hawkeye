#密码加盐
from hashlib import sha256


def GenSaltPassword(password,salt):
    sh = sha256()
    sh.update(password.encode('utf-8'))
    Str = sh.hexdigest()+salt
    sh1 = sha256()
    sh1.update(Str.encode('utf-8'))
    return sh1.hexdigest()

