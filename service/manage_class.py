from typing import *
from dao.models import Class
from global_var import db


def add_class_info(data: Dict):
    cid = data['cid']
    cname = data['cname']
    mid = data['mid']
    _class = Class(cid=cid, cname=cname, mid=mid)
    db.session.add(_class)
    db.session.commit()


def update_class_info(data: Dict):
    new_cid = data['cid']
    _class = Class.query.filter(Class.cid == new_cid).first()
    _class.cname = data['cname']
    _class.mid = data['mid']
    db.session.commit()


def delete_class_info(data: Dict):
    deleted_cid = data['key']
    _class = Class.query.filter(Class.cid == deleted_cid).first()
    db.session.delete(_class)
    db.session.commit()
