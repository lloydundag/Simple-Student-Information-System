from flask import render_template, redirect, request, jsonify, url_for, flash, send_file
from . import user_bp
import app.models as models
from app.user.forms import UserForm
from werkzeug.utils import secure_filename
from app import UPLOAD_FOLDER
from app.utils.utils import create_pdf
import os


def save_image(image_data):
    if len(image_data.filename) != 0:
        image_filename = secure_filename(image_data.filename)
        image_data.save(os.path.join(UPLOAD_FOLDER, image_filename))
        return image_filename
    else:
        return False


@user_bp.route('/student')
@user_bp.route('/')
@user_bp.route('/search')
def index():
    students = models.Students.all()
    form = UserForm()
    form.college.choices = models.Colleges.all()
    form.course.choices = models.Courses.all()

    args = {'query': None, 'college': None, 'course': None}

    if len(request.args):
        for key in args.keys():
            args[key] = request.args.get(key)

        students = models.Students.search(**args)
        print(args)
        return render_template('index.html', data=students, title='Home', form=form, search_items=args)
    else:
        return render_template('index.html', data=students, title='Home', form=form, search_items=args)

@user_bp.route('/<id>.pdf')
def student_pdf(id):
    user = models.Students.get(id)

    pdf = create_pdf(name=f"{user[2]} {user[3]}", idno=user[1], image=user[6], 
                    college=user[10], course=user[8], gender=user[5], yearlevel=user[4]
                    )

    pdf.seek(0)
    return send_file(pdf, as_attachment=True, mimetype='application/pdf',
        download_name=f'{user[1]}-{user[3]}.pdf')

@user_bp.route('/student/register', methods=['POST','GET'])
def register():
    form = UserForm()
    form.college.choices = models.Colleges.all()
    form.course.choices = models.Courses.all()
    if form.validate_on_submit():
        image_filename = save_image(form.image.data)
        user = models.Students(firstname=form.firstname.data, lastname=form.lastname.data, yearlevel=form.yearlevel.data, 
                                gender=form.gender.data, image=image_filename)        
        enroll = models.Enrollment(college_id=form.college.data, course_id=form.course.data)
        user.add()
        enroll.add()
        return redirect('/')
    else:
        return render_template('signup.html', form=form, title='Enroll Student')

@user_bp.route('/student/<string:id>/edit', methods=['POST'])
def edit(id):
    print(id)
    form = UserForm(request.form)
    user = models.Students(firstname=form.firstname.data, lastname=form.lastname.data,  
                            yearlevel=form.yearlevel.data, gender=form.gender.data, id=id)
    enroll = models.Enrollment(college_id=form.college.data, course_id=form.course.data)
    if user.exists():
        image_filename = save_image(request.files['image'])
        user.image = image_filename
        user.edit()
        print(models.Students.get(id)[0])
        enroll.edit(models.Students.get(id)[0])
        flash(f"Updated Student ID {id}")
        return redirect('/')
    else:
        flash(f"Update Error")
        return redirect('/')

@user_bp.route("/student/delete", methods=["POST"])
def delete():
    id = request.form['id']
    id = models.Students.get(id)
    os.remove(os.path.join(UPLOAD_FOLDER, id[6]))
    if models.Enrollment.delete(id[0]) and models.Students.delete(id[0]):
        flash(f"Student {id[1]} deleted.")
        return jsonify(success=True,message="Successfully deleted")
    else:
        return jsonify(success=False,message="Failed")
