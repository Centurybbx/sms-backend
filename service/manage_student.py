from typing import *
from dao.models import Student
from global_var import db


def add_student_info(data: Dict):
    student = Student(sid=data['sid'],
                      sname=data['sname'],
                      gender=data['gender'],
                      cid=data['cid'],
                      aname=data['aname'])
    db.session.add(student)
    db.session.commit()


def update_student_info(new_stu: Dict):
    new_sid = new_stu['sid']
    user = Student.query.filter(Student.sid == new_sid).first()
    user.sname = new_stu['sname']
    user.gender = new_stu['gender']
    user.cid = new_stu['cid']
    user.aname = new_stu['aname']
    db.session.commit()


def delete_student(data: Dict):
    deleted_sid = data['key']
    student = Student.query.filter(Student.sid == deleted_sid).first()
    db.session.delete(student)
    db.session.commit()
