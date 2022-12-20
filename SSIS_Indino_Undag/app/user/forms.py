from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField, SelectField


class UserForm(FlaskForm):
    idnum = StringField('ID Number', [validators.DataRequired(), validators.Length(min=3, max=20)])
    firstname = StringField('First Name', [validators.DataRequired(), validators.Length(min=3, max=20)])
    lastname = StringField('Last Name', [validators.DataRequired(), validators.Length(min=3, max=20)])
    college = SelectField('College', [validators.DataRequired()],
    choices=[('College of Science and Mathematics','CSM'),
    ('College of Economics, Business, and Accountancy','CEBA'),
    ('College of Education','CED'),
    ('College of Nursing','CON'),
    ('College of Arts and Sciences','CASS'),
    ('College of Computer Studies','CCS'),
    ('College of Engineering and Technology','COET')])
    course = SelectField('Course', [validators.DataRequired()],
    choices=[('Bachelor of Arts in English','(CASS) AB English'),
    ('Bachelor of Science in Psychology','(CASS) BS Psych'),
    ('Bachelor of Arts in Filipino','(CASS) AB Filipino'),
    ('Bachelor of Arts in Histor','(CASS) AB History'),
    ('Bachelor of Arts in Political Science','(CASS) AB Pol Sci'),
    ('Bachelor of Science in Civil Engineering','(COET) BSCE'),
    ('Bachelor of Science in Ceramics Engineering','(COET) BSCerE'),
    ('Bachelor of Science in Chemical Engineering','(COET) BSChE'),
    ('Bachelor of Science in Computer Engineering','(COET) BSCompE'),
    ('Bachelor of Science in Electrical Engineering','(COET) BSEE'),
    ('Bachelor of Science in Mining Engineering.','(COET) BSMinE'),
    ('Bachelor of Science in Metallurgical Engineering','(COET) BSMetE'),
    ('Bachelor of Science in Biology (Botany)','(CSM) BS Bio-Botany'),
    ('Bachelor of Science in Biology (Zoology)','(CSM) BS Bio-Zoo'),
    ('Bachelor of Science in Biology (Animal)','(CSM) BS Bio-AnimalBio'),
    ('Bachelor of Science in Statistics','(CSM) BS Stat'),
    ('Bachelor of Science in Chemistry','(CSM) BS Chem'),
    ('Bachelor of Science in Physics','(CSM) BS Physics'),
    ('Bachelor of Science in Mathematics','(CSM) BS Math'),
    ('Bachelor of Science in Accountancy','(CEBA) BSA'),
    ('Bachelor of Science in Business Administration (Economics)','(CEBA) BSBA - Econ'),
    ('Bachelor of Science in Business Administration (Business Economics)','(CEBA) BSBA - Bus Econ'),
    ('Bachelor of Science in Hotel and Management','(CEBA) BS HRM'),
    ('Bachelor of Science in Information Technology','(CCS) BSIT'),
    ('Bachelor of Science in Information Systems','(CCS) BSIS'),
    ('Bachelor of Science in Computer Science','(CCS) BSCS'),
    ('Bachelor of Science in Nursing','Course'),
    ('Bachelor of Science in Nursing',' (CON) BSN'),
    ('Bachelor of Secondary Education (Mathematics)','(CED) BSED - Math'),
    ('Bachelor of Elementary Education (English)','(CED) BSED - English'),
    ('Bachelor of Elementary Education(Filipino)','(CED) BSED - Filipino'),
    ('Bachelor of Secondary Education (PHYSICS)','(CED) BSED - PhySci'),
    ('Bachelor of Secondary Education (MAPEH)','(CED) BSED - MAPEH'),
    ('Bachelor of Secondary Education (TLE)','(CED) BSED - TLE')
    ])
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
    email = StringField('Email Address', [validators.Length(min=10, max=50)])
    password = PasswordField('Password', [validators.DataRequired()])
    
    submit = SubmitField("Submit")
