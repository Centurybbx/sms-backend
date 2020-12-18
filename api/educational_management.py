from typing import *
from service.query_student import query_all_students_info as query_all_students_info_api
from service.query_student import query_students_info_by_id
from flask import Blueprint

educational_management = Blueprint('educational_management', __name__, url_prefix='/management')


@educational_management.route('/query_all_students', methods=['POST'])
def get_all_students_info():
    return {'all_students_info': query_all_students_info_api()}