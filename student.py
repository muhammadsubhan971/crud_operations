from app import app
from flask import request
from model.student_m import student

obj=student()

@app.route('/view/student')
def student_view():
    return obj.get_students()

@app.route('/add/student',methods=['POST'])
def student_add():
    return obj.add_student(request.form)
@app.route('/update/student',methods=['PUT'])
def student_update():
    return obj.update_student(request.form)

@app.route('/delete/student/<id>',methods=['DELETE'])
def student_delete(id):
    return obj.delete_student(id)


@app.route('/patch/student/<id>', methods=['PATCH'])
def student_patch(id):
    # data = request.form  # This contains the form data submitted in the request
    return obj.patch_student(request.form, id)

@app.route('/view/port')
def port_view():
    return obj.get_student_port()
@app.route('/add/port', methods=['POST'])
def port_add():
    return obj.add_student_port(request.form)
@app.route('/update/port', methods=['PUT'])
def port_update():
    return obj.update_student_port(request.form)

@app.route('/delete/port/<id>', methods=['DELETE'])
def port_delete(id):
    return obj.delete_student_port(id)



if __name__ == '__main__':
    app.run(debug=True)