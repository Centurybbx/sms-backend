from typing import *
from dao.models import Student, Course, Elective, Teacher
from global_var import db
import simplejson as json


def query_all_courses_info():
    courses: List[Course] = Course.query.all()
    return [
        {
            "cid": course.cid,
            "cname": course.cname,
            "credit": course.credit,
            "term": course.term,
            "period": course.period,
            "tid": course.tid,
            "aname": course.aname
        } for course in courses]


def query_courses_info_by_any(data: Dict):
    sql = "select * from course"
    flag = 0
    concatenated_condition = " where "
    conditions = []
    cid = data['cid']
    cname = data['cname']
    term = data['term']
    credit = data['credit']
    period = data['period']
    tid = data['tid']
    aname = data['aname']

    if cid != '':
        conditions.append('cid=' + cid)
        flag += 1
    if cname != '':
        conditions.append('cname=' + '\"' + cname + '\"')
        flag += 1
    if credit != '':
        conditions.append('credit=' + credit)
        flag += 1
    if term != '':
        conditions.append('term=' + '\"' + term + '\"')
        flag += 1
    if period != '':
        conditions.append('period=' + '\"' + period + '\"')
        flag += 1
    if tid != '':
        conditions.append('tid=' + tid)
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
    courses = db.session.execute(sql)
    return [
        {
            'cid': course.cid,
            'cname': course.cname,
            'credit': course.credit,
            'term': course.term,
            'period': course.period,
            'tid': course.tid,
            'aname': course.aname
        } for course in courses]


def query_courses_info_by_term_and_sid(data: Dict):
    sid = data['sid']
    term = data['term']
    sql = "SELECT e.`eid`, s.sid, s.`sname`, c.cid, c.`cname`, c.credit, c.`term`,c.`period`, e.`grade`" \
          "FROM student s, course c, elective e WHERE s.`sid` = e.`sid` " \
          "AND c.`cid` = e.`cid`" \
          "AND s.sid = " + sid + " AND c.`term` = \'" + term + "\'"
    all_info = db.session.execute(sql)
    return [
        {
            'eid': info.eid,
            'sid': info.sid,
            'sname': info.sname,
            'cid': info.cid,
            'cname': info.cname,
            'credit': info.credit,
            'term': info.term,
            'period': info.period,
            'grade': info.grade
        } for info in all_info]


def query_all_elective_info():
    sql = "SELECT e.`eid`, s.sid, s.`sname`, c.cid, c.`cname`, c.credit, c.`term`,c.`period`, e.`grade`" \
          "FROM student s, course c, elective e WHERE s.`sid` = e.`sid` " \
          "AND c.`cid` = e.`cid`"
    all_info = db.session.execute(sql)
    return [
        {
            'eid': info.eid,
            'sid': info.sid,
            'sname': info.sname,
            'cid': info.cid,
            'cname': info.cname,
            'credit': info.credit,
            'term': info.term,
            'period': info.period,
            'grade': info.grade
        } for info in all_info]


def query_students_grades_by_class_and_term(data: Dict):
    cid = data['cid']
    term = data['term']
    term = '\"' + term + '\"'
    sql = "SELECT s.`sid`, s.sname, SUM(e.`grade`)/COUNT(*) AS average_grade " \
          "FROM student s, course c, elective e " \
          "WHERE s.`sid`  = e.`sid` " \
          "AND  c.`cid` = e.`cid` " \
          "AND c.`term` = " + term + \
          " AND s.`cid` = " + cid + \
          " GROUP BY s.`sid` " \
          " ORDER BY average_grade DESC"
    all_info = db.session.execute(sql)
    return [
        {
            'sid': info.sid,
            'sname': info.sname,
            'average_grade': info.average_grade
        } for info in all_info]


def query_all_elective_grade_info():
    sql = "SELECT s.`sid`, s.sname, SUM(e.`grade`)/COUNT(*) AS average_grade " \
          "FROM student s, course c, elective e " \
          "WHERE s.`sid`  = e.`sid` " \
          "AND  c.`cid` = e.`cid` " \
          "GROUP BY s.`sid` " \
          "ORDER BY average_grade DESC"
    all_info = db.session.execute(sql)
    return [
        {
            'sid': info.sid,
            'sname': info.sname,
            'average_grade': info.average_grade
        } for info in all_info]


def query_elective_table_info():
    elective = Elective.query.all()
    return [
        {
            'eid': e.eid,
            'sid': e.sid,
            'cid': e.cid,
            'grade': e.grade
        } for e in elective]


def query_elective_info_by_any(data: Dict):
    sql = "select * from elective"
    flag = 0
    concatenated_condition = " where "
    conditions = []
    eid = data['eid']
    sid = data['sid']
    cid = data['cid']
    grade = data['grade']

    if eid != '':
        conditions.append('eid=' + eid)
        flag += 1
    if sid != '':
        conditions.append('sid=' + '\"' + sid + '\"')
        flag += 1
    if cid != '':
        conditions.append('cid=' + '\"' + cid + '\"')
        flag += 1
    if grade != '':
        conditions.append('grade=' + '\"' + grade + '\"')
        flag += 1

    for condition in conditions:
        if condition != conditions[len(conditions) - 1]:
            concatenated_condition = concatenated_condition + condition + " and "
        else:
            concatenated_condition = concatenated_condition + condition

    if flag != 0:
        sql += concatenated_condition
    elective_info = db.session.execute(sql)
    return [
        {
            'eid': elective.eid,
            'sid': elective.sid,
            'cid': elective.cid,
            'grade': elective.grade,
        } for elective in elective_info]

# query_all_elective_info()
# print(query_students_grades_by_class_and_term(cid=1, term='2019-2020下'))
# print(query_courses_info_by_term_and_id(sid=1, term='2019-2020下'))
