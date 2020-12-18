from typing import *
from dao.models import Teacher, Course
from global_var import db


def query_all_teachers_info():
    teachers: List[Teacher] = Teacher.query.all()
    return [
        {
            'tid': t.tid,
            'tname': t.tname,
            'gender': t.gender,
            'office': t.office,
            'title': t.title,
            'aname': t.aname
        }for t in teachers
    ]


def query_teacher_courses_info_by_tid(data: Dict):
    tid = data['tid']
    infomation = db.session.query(Course, Teacher).filter(Teacher.tid == tid,
                                                          Course.tid == tid)
    course_list = []
    for info in infomation:
        for i in info:
            if type(i) == Course:
                course_list.append(i)
    return [
        {
            'cid': course_info.cid,
            'tid': course_info.tid,
            'cname': course_info.cname,
            'credit': course_info.credit,
            'term': course_info.term,
            'period': course_info.period
        }for course_info in course_list
    ]


def query_teachers_info_by_any(data: Dict):
    sql = "select * from teacher"
    flag = 0
    concatenated_condition = " where "
    conditions = []
    tid = data['tid']
    tname = data['tname']
    gender = data['gender']
    office = data['office']
    title = data['title']
    aname = data['aname']

    if tid != '':
        conditions.append('tid=' + tid)
        flag += 1
    if tname != '':
        conditions.append('tname=' + '\"' + tname + '\"')
        flag += 1
    if gender != '':
        conditions.append('gender=' + '\"' + gender + '\"')
        flag += 1
    if office != '':
        conditions.append('office=' + '\"' + office + '\"')
        flag += 1
    if title != '':
        conditions.append('title=' + '\"' + title + '\"')
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
    teachers = db.session.execute(sql)
    return [
        {
            'tid': teacher.tid,
            'tname': teacher.tname,
            'gender': teacher.gender,
            'office': teacher.office,
            'title': teacher.title,
            'aname': teacher.aname
        } for teacher in teachers]

# print(query_teacher_courses_info(2))
# objs = db.session.query(Course, Teacher).filter(Teacher.tid==2).all()
# for obj in objs:
#     for o in obj:
#         print(type(o) == Course)


# print(query_all_teachers_info())