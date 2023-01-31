from app import mysql


class Students(object):

    def __init__(self, id=None, firstname=None, lastname=None,college=None, 
    course=None, yearlevel=None, gender=None, image=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.college = college
        self.course = course
        self.yearlevel = yearlevel
        self.gender = gender
        self.image = image
        

    def add(self):
        cursor = mysql.connection.cursor()

        sql = f"""
        CALL insert_student('{self.firstname}', '{self.lastname}', '{self.yearlevel}', '{self.gender}', '{self.image}');
        """
        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = f"""
        SELECT students.student_id, students.firstname, students.lastname, students.yearlevel, students.gender, students.image, courses.id as course_id, 
                courses.name as course, colleges.id as college_id, colleges.name as college
        FROM students
        LEFT JOIN enrollment ON students.id = enrollment.student_id
        LEFT JOIN courses ON enrollment.course_id = courses.id
        LEFT JOIN colleges ON enrollment.college_id = colleges.id;
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def get(cls, id):
        cursor = mysql.connection.cursor()

        sql = f"""
        SELECT students.*, courses.id as course_id, courses.name as course, colleges.id as college_id, colleges.name as college
        FROM students
        LEFT JOIN enrollment ON students.id = enrollment.student_id
        LEFT JOIN courses ON enrollment.course_id = courses.id
        LEFT JOIN colleges ON enrollment.college_id = colleges.id
        WHERE students.student_id = '{id}';
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        return result[0]

    @classmethod
    def search(cls, query=None, college=None, course=None):
        cursor = mysql.connection.cursor()

        # SQL statement
        sql = """
        SELECT students.student_id, students.firstname, students.lastname, students.yearlevel, students.gender, students.image, courses.id as course_id, 
                courses.name as course, colleges.id as college_id, colleges.name as college
        FROM students
        LEFT JOIN enrollment ON students.id = enrollment.student_id
        LEFT JOIN courses ON enrollment.course_id = courses.id
        LEFT JOIN colleges ON enrollment.college_id = colleges.id
        """
        # Add filters to the SQL statement
        where_clause = []
        if query:
            where_clause.append(f"CONCAT(students.firstname, ' ', students.lastname) LIKE '%{query}%'")
        if college:
            where_clause.append(f"colleges.name = '{college}'")
        if course:
            where_clause.append(f"courses.name = '{course}'")
        if where_clause:
            sql += " WHERE " + " AND ".join(where_clause)

        cursor.execute(sql)
        result = cursor.fetchall()
        return result



    def exists(self):
        cursor = mysql.connection.cursor()
        sql = f"SELECT EXISTS (SELECT 1 FROM students WHERE student_id = '{self.id}')"
        cursor.execute(sql)
        return cursor.fetchall()[0][0]



    def edit(self):
            cursor = mysql.connection.cursor()
            if self.image:
                sql = f"""
                        UPDATE students 
                        SET firstname = '{self.firstname}', lastname = '{self.lastname}', yearlevel = '{self.yearlevel}', gender = '{self.gender}', image = '{self.image}' 
                        WHERE student_id = '{self.id}'
                        """
            else:
                sql = f"""
                        UPDATE students
                        SET firstname = '{self.firstname}', lastname = '{self.lastname}', yearlevel = '{self.yearlevel}', gender = '{self.gender}'
                        WHERE student_id = '{self.id}'
                        """

            cursor.execute(sql)
            mysql.connection.commit()

    @classmethod
    def delete(cls, id):
        try:
            cursor = mysql.connection.cursor()
            sql = f"""
            DELETE FROM students WHERE id = {id}
            """
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except:
            return False

        

class Colleges(object):

    def __init__(self, id=None, firstname=None, lastname=None):
        self.id = id
        self.code = lastname
        self.name = firstname

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from colleges;"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def naming():
        cursor = mysql.connection.cursor()

        sql = "SELECT id, name from colleges;"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def add(self):
         cursor = mysql.connection.cursor()

         sql = f"INSERT INTO colleges (name, code) VALUES ('{self.name}', '{self.code}');"
         cursor.execute(sql)
         mysql.connection.commit()

    @classmethod
    def get(cls, id):
        cursor = mysql.connection.cursor()

        sql = f"""
        SELECT * from colleges
        LEFT JOIN enrollment ON colleges.id = enrollment.college_id
        LEFT JOIN students ON enrollment.student_id = students.id
        LEFT JOIN courses ON enrollment.course_id = courses.id
        WHERE colleges.id = '{id}';
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        return result[0]


    @classmethod
    def delete(cls, id):
        try:
            cursor = mysql.connection.cursor()
            sql = f"""
            DELETE FROM colleges WHERE id = {id}
            """
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except:
            return False

    
    def edit(self):
         cursor = mysql.connection.cursor()

         sql = f"UPDATE colleges set name = '{self.name}', code = '{self.code}' WHERE id = {self.id};"
         cursor.execute(sql)
         mysql.connection.commit()

class Courses(object):

    def __init__(self, id=None, firstname=None, lastname=None):
        self.id = id
        self.name = firstname
        self.code = lastname

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from courses;"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def naming():
        cursor = mysql.connection.cursor()

        sql = "SELECT id, code from courses;"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def add(self):
        cursor = mysql.connection.cursor()

        sql = f"INSERT INTO courses (name, code) VALUES ('{self.name}', '{self.code}');"
        cursor.execute(sql)
        mysql.connection.commit()
    
    @classmethod
    def delete(cls, id):
        try:
            cursor = mysql.connection.cursor()
            sql = f"""
            DELETE FROM courses WHERE id = {id}
            """
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except:
            return False

    def edit(self):
         cursor = mysql.connection.cursor()

         sql = f"UPDATE courses set name = '{self.name}', code = '{self.code}' WHERE id = {self.id};"
         cursor.execute(sql)
         mysql.connection.commit()


class Enrollment(object):
    def __init__(self, course_id=None, college_id=None):
        self.course_id = course_id
        self.college_id = college_id

    def add(self):
        cursor = mysql.connection.cursor()

        sql = f"""
        INSERT INTO enrollment (student_id, course_id, college_id)
        VALUES (LAST_INSERT_ID(), (SELECT id FROM courses WHERE id = {self.course_id}), (SELECT id FROM colleges WHERE id = {self.college_id}));
        """
        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from enrollment"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


    def edit(self, id):
        cursor = mysql.connection.cursor()
        sql = f"""
        UPDATE enrollment
        SET course_id = {self.course_id}, college_id = {self.college_id}
        WHERE student_id = {id};
        """

        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def delete(cls, id):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE FROM enrollment WHERE student_id = '{id}';"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except:
            return False




