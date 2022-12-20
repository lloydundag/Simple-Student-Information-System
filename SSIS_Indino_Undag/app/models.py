from app import mysql


class Users(object):

    def __init__(self, idnum=None, firstname=None, lastname=None,college=None, 
    course=None, yearlevel=None, gender=None, password=None, email=None):
        self.idnum = idnum
        self.firstname = firstname
        self.lastname = lastname
        self.college = college
        self.course = course
        self.yearlevel = yearlevel
        self.gender = gender
        self.password = password
        self.email = email
        

    def add(self):
        cursor = mysql.connection.cursor()

        sql = f"INSERT INTO users(idnum, firstname, lastname, college, course, yearlevel, gender, email,password) \
                VALUES('{self.idnum}', '{self.firstname}', '{self.lastname}','{self.college}', '{self.course}', '{self.yearlevel}', '{self.gender}', '{self.email}', md5('{self.password}'))" 

        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from users"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def delete(cls,id):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from users where id= {id}"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except:
            return False

        
