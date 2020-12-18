from dao.models import Academy, Teacher, Course
from typing import *
from global_var import db


def query_all_academies_info():
    academies = Academy.query.filter().all()
    return [
        {
            'aid': academy.aid,
            'aname': academy.aname,
            'number': academy.number
        } for academy in academies]


def query_academies_info_by_any(data: Dict):
    sql = "select * from academy"
    flag = 0
    concatenated_condition = " where "
    conditions = []
    aid = data['aid']
    aname = data['aname']

    if aid != '':
        conditions.append('aid=' + aid)
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
    academies = db.session.execute(sql)
    return [
        {
            'aid': academy.aid,
            'aname': academy.aname,
            'number': academy.number
        } for academy in academies]


# def query_teachers_info_by_title_and_aname(data: Dict):
#     aname = data['aname']
#     title = data['title']
#     teachers = Academy.query.filter(Academy.aname == aname).first().teachers
#     teachers_info = []
#     for t in teachers:
#         if t.title == title:
#             teachers_info.append(t)
#     return [
#         {
#             'tid': teacher.tid,
#             'tname': teacher.tname,
#             'gender': teacher.gender,
#             'title': teacher.title,
#             'aname': teacher.aname
#         } for teacher in teachers_info]

def query_teachers_info_by_title_and_aname(data: Dict):
    aname = data['aname']
    title = data['title']
    sql = 'call getTeachersInfoByAnameAndTitle(\"' +aname+'\",\"'+title+'\")'
    teachers_info = db.session.execute(sql)
    return [
        {
            'tid': teacher.tid,
            'tname': teacher.tname,
            'gender': teacher.gender,
            'title': teacher.title,
            'aname': teacher.aname
        } for teacher in teachers_info]


# def query_course_info_by_academy(data: Dict):
#     aname = data['aname']
#     courses = Course.query.filter(Course.aname == aname)
#     return [
#         {
#             'cid': course.cid,
#             'cname': course.cname,
#             'credit': course.credit,
#             'period': course.period,
#             'aname': course.aname
#         } for course in courses]

def query_course_info_by_academy(data: Dict):
    aname = data['aname']
    sql = 'call getCoursesInfoByAcademy'+'("'+aname+'")'
    courses = db.session.execute(sql)
    return [
        {
            'cid': course.cid,
            'cname': course.cname,
            'credit': course.credit,
            'period': course.period,
            'aname': course.aname
        } for course in courses]

# print(query_course_info_by_academy('计算机科学与技术'))
# print(query_teachers_amount_by_title('计算机科学与技术', '教授'))
