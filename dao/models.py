from global_var import db


class Academy(db.Model):
    __tablename__ = 'academy'
    aname = db.Column(db.String(20), primary_key=True)
    aid = db.Column(db.Integer, nullable=False)
    number = db.Column(db.Integer, nullable=False, default=0)
    majors = db.relationship('Major', backref='academy', cascade='all, delete-orphan', passive_deletes=True)
    teachers = db.relationship('Teacher', backref='academy', cascade='all, delete-orphan', passive_deletes=True)
    courses = db.relationship('Course', backref='academy', cascade='all, delete-orphan', passive_deletes=True)


class Major(db.Model):
    __tablename__ = 'major'
    mid = db.Column(db.Integer, primary_key=True)
    mname = db.Column(db.String(10), nullable=False)
    aname = db.Column(db.String(20), db.ForeignKey('academy.aname', ondelete='CASCADE'))
    classes = db.relationship('Class', backref='major')


class Class(db.Model):
    __tablename__ = 'class'
    cid = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(10), nullable=False)
    # 班级class与专业major的外键mid
    mid = db.Column(db.Integer, db.ForeignKey('major.mid', ondelete='CASCADE'))
    students = db.relationship('Student', backref='_class', cascade='all, delete-orphan', passive_deletes=True)


class Student(db.Model):
    __tablename__ = 'student'
    sid = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.Enum("男", "女"), nullable=False)
    cid = db.Column(db.Integer, db.ForeignKey('class.cid', ondelete='CASCADE'))     #外键
    aname = db.Column(db.Integer, db.ForeignKey('academy.aname', ondelete='CASCADE'))     #外键
    courses = db.relationship('Course', secondary='elective', backref='student')


class Course(db.Model):
    __tablename__ = 'course'
    cid = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(10), nullable=False)
    credit = db.Column(db.Integer, nullable=False)
    term = db.Column(db.String(10), nullable=False)
    period = db.Column(db.String(3), nullable=True)
    tid = db.Column(db.Integer, db.ForeignKey('teacher.tid', ondelete='CASCADE'))
    aname = db.Column(db.String(20), db.ForeignKey('academy.aname', ondelete='CASCADE'))  # 新增外键，表示具有关系
    students = db.relationship('Student', secondary='elective', backref='course')


class Teacher(db.Model):
    __tablename__ = 'teacher'
    tid = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.Enum("男", "女"), nullable=False)
    office = db.Column(db.String(20), nullable=True)
    title = db.Column(db.Enum('教授', '副教授', '讲师'), nullable=False)
    aname = db.Column(db.String(20), db.ForeignKey('academy.aname', ondelete='CASCADE'))
    courses = db.relationship('Course', backref='teacher', cascade='all, delete-orphan', passive_deletes=True)


class Elective(db.Model):
    __tablename__ = 'elective'
    eid = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.Integer, db.ForeignKey('student.sid'))
    cid = db.Column(db.Integer, db.ForeignKey('course.cid'))
    grade = db.Column(db.Integer, nullable=False)


class Login(db.Model):
    __tablename__ = 'login'
    username = db.Column(db.String(20), primary_key=True)
    pwd = db.Column(db.String(50), nullable=False)


# if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()