from flask import Flask, Blueprint, jsonify, request
from flask_cors import CORS
# from api.educational_management import educational_management
import config
from global_var import db
from service.query_student import query_all_students_info, query_students_info_by_any
from service.manage_student import add_student_info, update_student_info, delete_student
from service.query_teacher import query_all_teachers_info, query_teacher_courses_info_by_tid, query_teachers_info_by_any
from service.manage_teacher import add_teacher_info, delete_teacher, update_teacher
from service.query_elective import query_all_courses_info, query_courses_info_by_term_and_sid,\
    query_all_elective_grade_info, query_courses_info_by_any, query_students_grades_by_class_and_term,\
    query_all_elective_info, query_elective_table_info, query_elective_info_by_any
from service.manage_elective import add_course_info, delete_course_info, update_course_info
from service.query_academy import query_course_info_by_academy, query_teachers_info_by_title_and_aname,\
    query_all_academies_info, query_academies_info_by_any
from service.query_class import query_all_classes_info, query_classes_info_by_any
from service.manage_class import add_class_info, update_class_info, delete_class_info
from service.manage_academy import add_academy_info, delete_academy_info, update_academy_info
from service.query_major import query_all_majors_info, query_majors_info_by_any
from service.manage_major import add_major_info, delete_major_info, update_major_info
from service.manage_elective import add_elective_info, delete_elective_info, update_elective_info
from service.login import judge_user

app = Flask(__name__)
app.config.from_object(config)
CORS(app, resources=r'/*', supports_credentials=True)

# app.register_blueprint(educational_management)


with app.app_context():
    db.init_app(app=app)


@app.route('/')
def home_page():
    return "home page"


@app.route('/query/students_info', methods=['POST'])
def query_all_students():
    return jsonify({'success': True, 'all_students_info': query_all_students_info()})


@app.route('/add/student_info', methods=['POST'])
def add_students():
    data = request.get_json(silent=True)
    add_student_info(data)
    return jsonify({'success': True, 'added_student_info': data})


@app.route('/update/student_info', methods=['POST'])
def update_students():
    data = request.get_json(silent=True)
    update_student_info(data)
    return jsonify({'success': True, 'updated_student_info': data})


@app.route('/delete/student', methods=['POST'])
def delete_students():
    data = request.get_json(silent=True)
    print(data['key'])
    delete_student(data)
    return jsonify({'success': True, 'deleted_student_info': data})


@app.route('/query/teachers_info', methods=['POST'])
def query_all_teachers():
    return jsonify({'success': True, 'all_teachers_info': query_all_teachers_info()})


@app.route('/add/teacher', methods=['POST'])
def add_teachers():
    data = request.get_json(silent=True)
    add_teacher_info(data)
    return jsonify({'success': True, 'added_teacher_info': data})


@app.route('/delete/teacher_info', methods=['POST'])
def delete_teachers():
    data = request.get_json(silent=True)
    delete_teacher(data)
    return jsonify({'success': True, 'deleted_teacher_info': data})


@app.route('/update/teacher_info', methods=['POST'])
def update_teachers():
    data = request.get_json(silent=True)
    print(data)
    update_teacher(data)
    return jsonify({'success': True, "updated_teacher_info": data})


@app.route('/query/courses_info', methods=['POST'])
def query_all_courses():
    return jsonify({'success': True, 'all_courses_info': query_all_courses_info()})


@app.route('/add/course_info', methods=['POST'])
def add_courses():
    data = request.get_json(silent=True)
    add_course_info(data)
    return jsonify({'success': True, 'added_course_info': data})


@app.route('/delete/course_info', methods=['POST'])
def delete_courses():
    data = request.get_json(silent=True)
    delete_course_info(data)
    return jsonify({'success': True, 'deleted_course_info': data})


@app.route('/update/course_info', methods=['POST'])
def update_courses():
    data = request.get_json(silent=True)
    update_course_info(data)
    return jsonify({'success': True, 'updated_course_info': data})


@app.route('/query/courses_info_by_term_and_sid', methods=['POST'])
def query_courses_info_by_sid_and_term():
    data = request.get_json(silent=True)
    return jsonify({'success': True, 'query_courses_info_by_term_and_sid': query_courses_info_by_term_and_sid(data)})


@app.route('/query/course_info_by_tid', methods=['POST'])
def query_teacher_courses_info():
    data = request.get_json(silent=True)
    return jsonify({'success': True, 'query_course_info_by_tid': query_teacher_courses_info_by_tid(data)})


@app.route('/query/students_info_by_any', methods=['POST'])
def query_students_info_by_condition():
    data = request.get_json(silent=True)
    return jsonify({'success': True, 'query_students_info_by_condition': query_students_info_by_any(data)})


@app.route('/query/courses_info_by_academy', methods=['POST'])
def query_courses_info_by_aname():
    data = request.get_json(silent=True)
    return jsonify({'success': True, 'query_courses_info_by_aname': query_course_info_by_academy(data)})


@app.route('/query/teachers_info_by_title_and_aname', methods=['POST'])
def query_teachers_info_by_title_and_academy():
    data = request.get_json(silent=True)
    return jsonify({'success': True, 'query_teachers_info_by_title_and_aname': query_teachers_info_by_title_and_aname(data)})


@app.route('/query/teachers_info_by_any', methods=['POST'])
def query_teachers_info_by_condition():
    data = request.get_json(silent=True)
    return jsonify({'success': True, 'query_teachers_info_by_condition': query_teachers_info_by_any(data)})


@app.route('/query/courses_info_by_any', methods=['POST'])
def query_courses_info_by_condition():
    data = request.get_json(silent=True)
    return jsonify({'success': True, 'query_courses_info_by_condition': query_courses_info_by_any(data)})


@app.route('/query/stu_elective_courses_info', methods=['POST'])
def query_elective_courses_info():
    return jsonify({'success': True, 'query_elective_courses_info': query_all_elective_info()})


@app.route('/query/all_classes_info', methods=['POST'])
def query_classes_info():
    return jsonify({'success': True, 'query_all_classes_info': query_all_classes_info()})


@app.route('/add/class_info', methods=['POST'])
def add_classes_info():
    data = request.get_json(silent=True)
    add_class_info(data)
    return jsonify({'success': True, 'added_class_info': data})


@app.route('/update/class_info', methods=['POST'])
def update_classes_info():
    data = request.get_json(silent=True)
    update_class_info(data)
    return jsonify({'success': True, 'updated_class_info': data})


@app.route('/delete/class_info', methods=['POST'])
def delete_classes_info():
    data = request.get_json(silent=True)
    delete_class_info(data)
    return jsonify({'success': True, 'deleted_class_info': data})


@app.route('/query/classes_info_by_any', methods=['POST'])
def query_classes_info_by_condition():
    data = request.get_json()
    return jsonify({'success': True, 'query_classes_info_by_any': query_classes_info_by_any(data)})


@app.route('/query/all_academies_info', methods=['POST'])
def query_academies_info():
    return jsonify({'success': True, 'query_all_academies_info': query_all_academies_info()})


@app.route('/add/academy_info', methods=['POST'])
def add_academies_info():
    data = request.get_json(silent=True)
    add_academy_info(data)
    return jsonify({'success': True, 'added_academy_info': data})


@app.route('/delete/academy_info', methods=['POST'])
def delete_academies_info():
    data = request.get_json(silent=True)
    delete_academy_info(data)
    return jsonify({'success': True, 'deleted_academy_info': data})


@app.route('/update/academy_info', methods=['POST'])
def update_academies_info():
    data = request.get_json(silent=True)
    update_academy_info(data)
    return jsonify({'success': True, 'updated_academy_info': data})


@app.route('/query/academies_info_by_any', methods=['POST'])
def query_academies_info_by_condition():
    data = request.get_json(silent=True)
    return jsonify({'success': True, 'query_academies_info_by_any': query_academies_info_by_any(data)})


@app.route('/query/all_majors_info', methods=['POST'])
def query_majors_info():
    return jsonify({'success': True, 'query_all_majors_info': query_all_majors_info()})


@app.route('/add/major_info', methods=['POST'])
def add_majors_info():
    data = request.get_json(silent=True)
    add_major_info(data)
    return jsonify({'success': True, 'added_major_info': data})


@app.route('/delete/major_info', methods=['POST'])
def delete_majors_info():
    data = request.get_json(silent=True)
    delete_major_info(data)
    return jsonify({'success': True, 'deleted_major_info': data})


@app.route('/update/major_info', methods=['POST'])
def update_majors_info():
    data = request.get_json(silent=True)
    update_major_info(data)
    return jsonify({'success': True, 'updated_major_info': data})


@app.route('/query/majors_info_by_any', methods=['POST'])
def query_majors_info_by_condition():
    data = request.get_json(silent=True)
    return jsonify({'success': True, 'query_majors_info_by_any': query_majors_info_by_any(data)})


@app.route('/query/all_elective_info', methods=['POST'])
def query_elective_info():
    return jsonify({'success': True, 'query_all_elective_info': query_all_elective_grade_info()})


@app.route('/query/students_grades_by_class_and_term', methods=['POST'])
def query_elective_info_by_cid_and_term():
    data = request.get_json(silent=True)
    return jsonify({'success': True, 'query_elective_info_by_cid_and_term': query_students_grades_by_class_and_term(data)})


@app.route('/login', methods=['POST'])
def judge_is_user_legal():
    data = request.get_json(silent=True)
    return {'success': judge_user(data)}


@app.route('/query/elective_table_info', methods=['POST'])
def query_all_elective_table_info():
    return jsonify({'success': True, 'elective_table_info': query_elective_table_info()})


@app.route('/add/elective_info', methods=['POST'])
def add_elective_table_info():
    data = request.get_json(silent=True)
    add_elective_info(data)
    return jsonify({'success': True, 'added_elective_info': data})


@app.route('/delete/elective_info', methods=['POST'])
def delete_elective_table_info():
    data = request.get_json(silent=True)
    delete_elective_info(data)
    return jsonify({'success': True, 'deleted_elective_info': data})


@app.route('/update/elective_info', methods=['POST'])
def update_elective_table_info():
    data = request.get_json(silent=True)
    update_elective_info(data)
    return jsonify({'success': True, 'updated_elective_info': data})


@app.route('/query/elective_info_by_any', methods=['POST'])
def query_elective_table_info_by_any():
    data = request.get_json(silent=True)
    return jsonify({'success': True, 'query_elective_info_by_any': query_elective_info_by_any(data)})


if __name__ == '__main__':
    app.run(debug=True)
