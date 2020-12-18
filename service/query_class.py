from dao.models import Class
from typing import *
from global_var import db


def query_all_classes_info():
    classes = Class.query.all()
    return [
        {
            'cid': _class.cid,
            'cname': _class.cname,
            'mid': _class.mid
        } for _class in classes]


def query_classes_info_by_any(data: Dict):
    sql = "select * from class"
    flag = 0
    concatenated_condition = " where "
    conditions = []
    cid = data['cid']
    cname = data['cname']
    mid = data['mid']

    if cid != '':
        conditions.append('cid=' + cid)
        flag += 1
    if cname != '':
        conditions.append('cname=' + '\"' + cname + '\"')
        flag += 1
    if mid != '':
        conditions.append('mid=' + mid)
        flag += 1

    for condition in conditions:
        if condition != conditions[len(conditions) - 1]:
            concatenated_condition = concatenated_condition + condition + " and "
        else:
            concatenated_condition = concatenated_condition + condition

    if flag != 0:
        sql += concatenated_condition
    classes = db.session.execute(sql)
    return [
        {
            'cid': _class.cid,
            'cname': _class.cname,
            'mid': _class.mid
        } for _class in classes]