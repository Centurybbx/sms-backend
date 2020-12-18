from typing import *
from dao.models import Student, Course, Elective
from global_var import db


def add_course_info(data: Dict):
    course = Course(cid=data['cid'],
                    cname=data['cname'],
                    credit=data['credit'],
                    term=data['term'],
                    period=data['period'],
                    tid=data['tid'],
                    aname=data['aname'])
    db.session.add(course)
    db.session.commit()


def delete_course_info(data: Dict):
    course = Course.query.filter(Course.cid == data['key']).first()
    db.session.delete(course)
    db.session.commit()


def update_course_info(data: Dict):
    new_cid = data['cid']
    course = Course.query.filter(Course.cid == new_cid).first()
    course.cname = data['cname']
    course.credit = data['credit']
    course.term = data['term']
    course.period = data['period']
    course.tid = data['tid']
    course.aname = data['aname']
    db.session.commit()


def add_elective_info(data: Dict):
    elective = Elective(eid=data['eid'],
                        sid=data['sid'],
                        cid=data['cid'],
                        grade=data['grade'])
    db.session.add(elective)
    db.session.commit()


def delete_elective_info(data: Dict):
    elective = Elective.query.filter(Elective.eid == data['key']).first()
    db.session.delete(elective)
    db.session.commit()


def update_elective_info(data: Dict):
    new_eid = data['eid']
    elective = Elective.query.filter(Elective.eid == new_eid).first()
    elective.sid = data['sid']
    elective.cid = data['cid']
    elective.grade = data['grade']
    db.session.commit()