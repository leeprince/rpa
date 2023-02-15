#!/usr/local/bin/python3

import pymysql;

# --------------------基本用法------------------
# # 打开数据库连接
# db = pymysql.connect("localhost", "root", "leeprince",  "my_optimize")

# # 使用 cursor() 方法创建一个游标对象
# cursor = db.cursor()

# # 使用 execute() 方法执行 sql 语句
# cursor.execute("select version()");

# # fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# # fetchall(): 接收全部的返回结果行.
# # rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
# data = cursor.fetchone()

# # 关闭数据库
# cursor.close()
# print("数据库版本为：%s" % data)
# --------------------基本用法 - end------------------

# 数据库版本
def version(cursor):
    # 使用 excute() 方法执行 sql 语句
    cursor.execute("select version()");
    # fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    # fetchall(): 接收全部的返回结果行.
    # rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
    data = cursor.fetchone()
    print("数据库版本为：%s" % data)

def select(db, cursor):
    sql = 'select id, name from p_procedure where id = %d' % (1)

    try:
        cursor.execute(sql)

        # 获取单条数据
        # results = cursor.fetchone()
        # print(results)
        # print("[获取单条数据]ID：%s -- name：%s" % (results[0], results[1]))

        # 获取多条数据
        results = cursor.fetchall()
        for x in results:
            # print(x)
            print("[获取多条数据]ID：%s -- name：%s" % (x[0], x[1]))
            pass
        pass
    except Exception as e:
        raise
    else:
        pass
    finally:
        pass

# 插入数据
def insert(db, cursor):
    # sql = '''
    #     insert into p_procedure (name) values ('pythonInsert01')
    # '''
    sql = "insert into p_procedure (name) values ('%s')" % ('pythonInsert02')
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        raise
    else:
        pass
    finally:
        pass

# 打开数据库连接
db = pymysql.connect("localhost", "root", "leeprince",  "my_optimize")
# 使用 cursor() 方法创建一个游标对象
cursor = db.cursor()

# version(cursor)
select(db, cursor)
# insert(db, cursor)

# 关闭数据库
# cursor.close()

