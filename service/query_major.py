from dao.models import Major
from typing import *
from global_var import db


def query_all_majors_info():
    majors = Major.query.all()
    return [
        {
            'mid': major.mid,
            'mname': major.mname,
            'aname': major.aname
        } for major in majors]


def query_majors_info_by_any(data: Dict):
    sql = "select * from major"
    flag = 0
    concatenated_condition = " where "
    conditions = []
    mid = data['mid']
    mname = data['mname']
    aname = data['aname']

    if mid != '':
        conditions.append('mid=' + mid)
        flag += 1
    if mname != '':
        conditions.append('mname=' + '\"' + mname + '\"')
        flag += 1
    if aname != '':
        conditions.append('aname=' + '\"' + aname + '\"')
        flag += 1

    for condition in conditions:
        if condition != conditions[len(conditions) - 1]:
            concatenated_condition = concatenated_condition + condition + " and "
        else:
            concatenated_condition = concatenated_condition + condition

    if flag != 0:
        sql += concatenated_condition
    majors = db.session.execute(sql)
    return [
        {
            'mid': major.mid,
            'mname': major.mname,
            'aname': major.aname
        } for major in majors]