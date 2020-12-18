from dao.models import *
from global_var import db

# 打印学生基本信息情况


# s = Student.query.first()                 单个学生
# s_class = s._class
# print(s.sid, s.sname, s.gender, s_class.cname)

# students = Student.query.all()            #所有学生
# for stu in students:
#     stu_class = stu._class
#     print(stu.sid, stu.sname, stu.gender, stu_class.cname)


# 打印教师名单


# teachers = Teacher.query.all()
# for teacher in teachers:
#     aname = teacher.aname
#     print(teacher.tid, teacher.tname, teacher.gender, teacher.office_id, aname)


# 可以根据学生的属性进行查询


# stu = Student.query.filter(Student.gender == '男')
# for s in stu:
#     print(s.sid, s.sname, s.gender)


# 查询某学生某学期所选修的全部课程的学分、学时、成绩
#
# objs = db.session.query(Student, Course, Elective).filter(Student.sid == 1,
#                                                           Course.term == '2019-2020下',
#                                                           Elective.sid == Student.sid,
#                                                           Elective.cid == Course.cid)
# course_info = []
# elective_info = []
# for obj in objs:
#     for o in obj:
#         if type(o) == Course:
#             course_info.append(o)
#         if type(o) == Elective:
#             elective_info.append(o)
#
# print(len(course_info))
# print(len(elective_info))

# obj = Student.query.filter(Student.sid == '1').first()
# oc = obj.courses
# for o in oc:
#     print(obj.sid, obj.sname, o.cid, o.cname, o.credit, o.term)

# 查询某教师讲授的所有课程信息


# t = Teacher.query.filter(Teacher.tid == 2).first()
# course_info = t.courses
# for c in course_info:
#     print(t.tid, t.tname, t.gender, c.cid, c.cname, c.credit, c.term)


# 查询某班级某学期所有学生总成绩倒序的报表

# TODO:




# 查询各个系所拥有的各级职称的教师人数


# count = 0
# teachers = Teacher.query.all()
# for t in teachers:
#     count += 1
# print(count)


#查询出某学院所开设的各门课程的名称、学时


# db.session.query(Teacher, Course).filter(Teacher.aname == '计算机科学与技术').filter()


# courses = Academy.query.filter(Academy.aname == '计算机科学与技术').first().courses
# for c in courses:
#     print(c.cname, c.period)


