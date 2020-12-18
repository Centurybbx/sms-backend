from typing import *
from dao.models import Student
from global_var import db


def query_all_students_info():
    students: List[Student] = Student.query.all()
    return [{
        'sid': stu.sid,
        'sname': stu.sname,
        'gender': stu.gender,
        'cid': stu.cid,
        'aname': stu.aname
    } for stu in students]


def query_students_info_by_id(sid: int):
    students = Student.query.filter(Student.sid == sid).all()
    return [{
        'sid': stu.sid,
        'sname': stu.sname,
        'gender': stu.gender,
        'cid': stu.cid,
        'aname': stu.aname
    } for stu in students]


def query_students_info_by_any(data: Dict):
    sql = "select * from student"
    flag = 0;
    concatenated_condition = " where "
    conditions = []
    sid = data['sid']
    sname = data['sname']
    gender = data['gender']
    cid = data['cid']
    aname = data['aname']

    # TODO:精简 if 语句
    if sid != '':
        conditions.append('sid=' + sid)
        flag += 1
    if sname != '':
        conditions.append('sname=' + '\"' + sname + '\"')
        flag += 1
    if gender != '':
        conditions.append('gender=' + '\"' + gender + '\"')
        flag += 1
    if cid != '':
        conditions.append('cid=' + cid)
        flag += 1
    if aname != '':
        conditions.append('aname=' + aname)
        flag += 1

    # 拼接条件语句
    for condition in conditions:
        if condition != conditions[len(conditions) - 1]:
            concatenated_condition = concatenated_condition + condition + " and "
        else:
            concatenated_condition = concatenated_condition + condition
    if flag != 0:
        sql += concatenated_condition
    students = db.session.execute(sql)
    return [
        {
            'sid': student.sid,
            'sname': student.sname,
            'gender': student.gender,
            'cid': student.cid,
            'aname': student.aname
        } for student in students]
    

# print(query_students_info_by_id(1))
