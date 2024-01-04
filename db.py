import sqlite3

class database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY,
        name varchar(100),
        age varchar(100),
        doj varchar(100),
        email varchar(100),
        gender varchar(100),
        contact varchar(100),
        address varchar(100)
        )"""
        self.cur.execute(sql)
        self.con.commit()

    #insert values
    def insert(self,name,age,doj,email,gender,contact,address):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",(name,age,doj,email,gender,contact,address))
        self.con.commit()

    #get all data
    def fetch(self):
        self.cur.execute("select * from employees")
        row = self.cur.fetchall()
        print(row)
        return row

    #delete a row
    def remove(self,id):
        self.cur.execute("delete from employees where id = ?",(id,))
        self.con.commit()

    #update a row
    def update(self,id,name,age,doj,email,gender,contact,address):
        self.cur.execute("update employees set name=?,age=?,doj=?,email=?,gender=?,contact=?,address=? where id=?"
                         ,(name,age,doj,email,gender,contact,address,id))

# ob = database('employee.db')
# ob.insert('ra',"21","12-06-2002","a@12","male","233232","ggfghfghfgfd")
# ob.fetch()
# ob.remove(5)