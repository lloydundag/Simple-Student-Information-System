from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, SelectField
from flask_wtf.file import FileAllowed, FileRequired, FileField

class UserForm(FlaskForm):

    image = FileField('Image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    
    firstname = StringField('First Name', [validators.DataRequired(), validators.Length(min=3, max=20)])
    lastname = StringField('Last Name', [validators.DataRequired(), validators.Length(min=3, max=20)])
    college = SelectField('College', [validators.DataRequired()])

    course = SelectField('Course', [validators.DataRequired()])

    yearlevel = SelectField('Year Level', [validators.DataRequired()],
    choices=[('First Year','First Year'),
    ('Second Year','Second Year'),
    ('Third Year','Third Year'),
    ('Fourth Year','Fourth Year')
    ])
    
    gender = SelectField('Gender', [validators.DataRequired()],
    choices=[('Male','Male'),
    ('Female','Female'),
    ('LGBTQ+','LGBTQ+')
    ])
    
    submit = SubmitField("Submit")

