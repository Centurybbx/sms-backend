from typing import *
from dao.models import Academy
from global_var import db


def add_academy_info(data: Dict):
    aid = data['aid']
    aname = data['aname']
    academy = Academy(aid=aid, aname=aname)
    try:
        db.session.add(academy)
        db.session.commit()
    except:
        print("插入失败！")


def delete_academy_info(data: Dict):
    aid = data['key']
    academy = Academy.query.filter(Academy.aid == aid).first()
    db.session.delete(academy)
    db.session.commit()


def update_academy_info(data: Dict):
    aname = data['aname']
    aid = data['aid']
    academy = Academy.query.filter(Academy.aname == aname).first()
    academy.aid = aid
    db.session.commit()