from tool import MySQL
import hashlib

def make_password(psword):
    hl = hashlib.md5()
    hl.update(psword.encode(encoding='utf-8'))
    return hl.hexdigest()


con = MySQL()
# 插入数据，传入表名和字典数据
def insert_data(db,data):
    data['id'] = 0
    sql = '''insert into {} '''.format(db)+str(tuple(data.keys())).replace("'",'')+''' values{} '''.format(tuple(data.values()))
    print(sql)
    try:
        con.query(sql)
        con.commit()
    except:
        return None


#查询表所有内容
def select_all(db):
    sql = '''select * from {}'''.format(db)
    try:
        con.query(sql)
        return con.show()
    except:
        return None


# 查询表条件
def select_where(db,where):
    sql = '''select * from {} where {}'''.format(db,where)
    try:
        print(sql)
        con.query(sql)
        return con.show()
    except:
        return None


def select_wheres(db):
    sql = '''select * from {}'''.format(db)
    try:
        print(sql)
        con.query(sql)
        return con.show()
    except:
        return None


# 修改
def change(db,content,where):
    sql = '''update {} set {} where {}'''.format(db,content,where)
    try:
        print(sql)
        con.query(sql)
        con.commit()
    except:
        return None

# 删除
def delete_from(db,where):
    sql = '''delete from {} where {}'''.format(db,where)
    print(sql)
    try:
        con.query(sql)
        con.commit()
    except:
        return None


#分页查询
def finds_from(db,where,start,end):
    sql = '''select * from {} where {} limit {},{}'''.format(db,where,start,end)
    print(sql)
    try:
        con.query(sql)
        con.commit()
    except:
        return None

# insert_data('student',{'name':'xingmengshuo','number':'123','classnumber':'12','picture':'/home/xms/桌面/project/tool/2019-04-16-230221.jpg'})