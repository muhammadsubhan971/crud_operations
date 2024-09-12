import mysql.connector as conect
import json
from flask import make_response
from app import app
class student:
    
    def __init__(self):
        try:
            self.con=conect.connect(host="localhost",user='root',password="subhan971",database='student_demo')
            self.cur=self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
        except:
            print("Could not connect to")
    
    def get_students(self):
        self.cur.execute('SELECT * FROM student_demo')
        
        result=self.cur.fetchall()
        if len(result) > 0:
            result1= make_response({'Data':result},200)
            return result1
        else:
            return make_response({'Message':'Not found'},204)
    def add_student(self,data):
        sql = "INSERT INTO student_demo (age, class, name) VALUES (%s, %s, %s)"
        values = (data['age'], data['class'], data['name'])
        self.cur.execute(sql, values)

        if self.cur.rowcount >0:
            return make_response({'Message':'Data entered suceesfully'},201)
        else:
            return make_response({'Message':'Data not entered suceesfully'},204)
    
    def update_student(self,data):
        self.cur.execute(f"UPDATE student_demo SET name='{data['name']}',age='{data['age']}',class='{data['class']}' WHERE id={data['id']}")
        if self.cur.rowcount >0:
            return make_response({'Message':'Data updated suceesfully'},201)
        else:
            return make_response({'Message':'Data not updated suceesfully'},204)
    def delete_student(self, id):
        self.cur.execute(f"DELETE FROM student_port WHERE cid={id}")
    # Then delete the parent record
        self.cur.execute(f"DELETE FROM student_demo WHERE id={id}")
        if self.cur.rowcount > 0:
            return make_response({'Message': 'Data deleted successfully'}, 201)
        else:
            return make_response({'Message': 'Data not deleted successfully'}, 204)

    
    def patch_student(self,data,id):
        qry="UPDATE student_demo SET "
        for key in data:
            qry=qry + f"{key}='{data[key]}' ,"
            
        qr=qry[:-1] +f" WHERE id={id}"
        self.cur.execute(qr)
        if self.cur.rowcount >0:
            return make_response({'Message':'Data updated suceesfully'},201)
        else:
            return make_response({'Message':'Data not updated suceesfully'},204)
        
    def get_student_port(self):
        self.cur.execute('SELECT * FROM student_port')
        
        result=self.cur.fetchall()
        if len(result) > 0:
            result1= make_response({'Data':result},200)
            return result1
        else:
            return make_response({'Message':'Not found'},204)
    
    def add_student_port(self,data):
        sql = "INSERT INTO student_port (marks, grade,cid) VALUES (%s, %s, %s)"
        values = (data['marks'], data['grade'], data['cid'])
        self.cur.execute(sql, values)
        if self.cur.rowcount >0:
            return make_response({'Message':'Data entered suceesfully'},201)
        else:
            return make_response({'Message':'Data not entered suceesfully'},204)
    def update_student_port(self,data):
        self.cur.execute(f"UPDATE student_port SET marks='{data['marks']}',grade='{data['grade']}' WHERE cid={data['cid']}")
        if self.cur.rowcount >0:
            return make_response({'Message':'Data updated suceesfully'},201)
        else:
            return make_response({'Message':'Data not updated suceesfully'},204)
    
    def delete_student_port(self, cid):
        self.cur.execute(f"DELETE FROM student_port WHERE cid={cid}")
        if self.cur.rowcount >0:
            return make_response({'Message':'Data deleted suceesfully'},201)
        else:
            return make_response({'Message':'Data not deleted suceesfully'},204)
        

if __name__ == "__main__":
    app.run(debug=True)