from dao.models import Major
from typing import *
from global_var import db


def add_major_info(data: Dict):
    mid = data['mid']
    mname = data['mname']
    aname = data['aname']
    major = Major(mid=mid, mname=mname, aname=aname)
    db.session.add(major)
    db.session.commit()


def delete_major_info(data: Dict):
    mid = data['key']
    major = Major.query.filter(Major.mid == mid).first()
    db.session.delete(major)
    db.session.commit()


def update_major_info(data: Dict):
    mid = data['mid']
    major = Major.query.filter(Major.mid == mid).first()
    major.mname = data['mname']
    major.aname = data['aname']
    db.session.commit()