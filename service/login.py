from dao.models import Login
from typing import *
import hashlib


def judge_user(data: Dict):
    flag = False
    username = data['username']
    encrypted_pwd = data['pwd']
    user = Login.query.filter(Login.username == username).first()
    encode = hashlib.md5()
    encode.update(user.pwd.encode())
    user_pwd = encode.hexdigest()
    print(encrypted_pwd)
    if user is not None:
        if user_pwd == encrypted_pwd:
            flag = True
    return flag
