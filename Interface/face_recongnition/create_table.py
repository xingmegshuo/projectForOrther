import pymysql
from insert_db import make_password

#连接数据库
def connect_db():
    con = pymysql.connect(host='localhost',port=3306,user='root',db='project',passwd='528012',charset='utf8')
    return con.cursor(),con

#执行mysql语句
def do_sql(con,sql):
    try:
        con.execute(sql)
    except Exception as e:
        print(e)
        


def create():
    create_user = '''create table user(id int auto_increment primary key,account varchar(30),password varchar(300),carrer bool default False)'''
    create_stu = '''create table student(id int auto_increment primary key,name varchar(30),number varchar(30),classnumber varchar(30),picture varchar(50))'''
    create_check = '''create table check_in(id int auto_increment primary key,stu_id int,foreign key(stu_id) references student(id),status varchar(30),classname varchar(30),time timestamp not null default now())'''
    create_super = '''insert user (id,account,password,carrer) values(0,123,'{}',True)'''.format(make_password('123'))
    con,conn = connect_db()
    do_sql(con,create_user)
    do_sql(con,create_stu)
    do_sql(con,create_check)
    select_conent = '''select * from user'''
    con.execute(select_conent)
    try:
        con.fetchall()[0]
    except:
        do_sql(con,create_super)
        conn.commit()
