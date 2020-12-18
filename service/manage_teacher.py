from typing import *
from dao.models import Teacher
from global_var import db


def add_teacher_info(data: Dict):
    teacher = Teacher(tid=data['tid'],
                      tname=data['tname'],
                      gender=data['gender'],
                      office=data['office'],
                      title=data['title'],
                      aname=data['aname'])
    db.session.add(teacher)
    db.session.commit()


def delete_teacher(data: Dict):
    teacher = Teacher.query.filter(Teacher.tid == data['key']).first()
    db.session.delete(teacher)
    db.session.commit()


def update_teacher(data: Dict):
    new_tid = data['tid']
    teacher = Teacher.query.filter(Teacher.tid == new_tid).first()
    teacher.tname = data['tname']
    teacher.gender = data['gender']
    teacher.office = data['office']
    teacher.title = data['title']
    teacher.aname = data['aname']
    print(teacher)
    db.session.commit()