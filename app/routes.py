from flask import Blueprint, request, jsonify, render_template
from .models import db, Student
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(
        first_name=data['first_name'],
        last_name=data['last_name'],
        dob=datetime.strptime(data['dob'], '%Y-%m-%d').date(),
        amount_due=data['amount_due']
    )
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student created successfully'}), 201

@main.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{
        'student_id': student.student_id,
        'first_name': student.first_name,
        'last_name': student.last_name,
        'dob': student.dob.strftime('%Y-%m-%d'),
        'amount_due': student.amount_due
    } for student in students])

@main.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get_or_404(student_id)
    return jsonify({
        'student_id': student.student_id,
        'first_name': student.first_name,
        'last_name': student.last_name,
        'dob': student.dob.strftime('%Y-%m-%d'),
        'amount_due': student.amount_due
    })

@main.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    student = Student.query.get_or_404(student_id)
    if 'first_name' in data:
        student.first_name = data['first_name']
    if 'last_name' in data:
        student.last_name = data['last_name']
    if 'dob' in data:
        student.dob = datetime.strptime(data['dob'], '%Y-%m-%d').date()
    if 'amount_due' in data:
        student.amount_due = data['amount_due']
    db.session.commit()
    return jsonify({'message': 'Student updated successfully'})

@main.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted successfully'})
