# #1、创建数据库
# import mysql.connector
# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='root'
# )
# mycursor = mydb.cursor()
# mycursor.execute('create database zhuzhu')#创建zhuzhu数据库


# #2、连接数据库[检查数据库是否存在]
# import mysql.connector
# mydb = mysql.connector.connect(
#     host='locahost',
#     user='root',
#     passwd='root'
# )
# mycursor = mydb.cursor()
# mycursor.execute('show databases')
# for i in mycursor:
#     print(i)

# #3、创建表【表字段】
# import mysql.connector
# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='root',
#     database='zhuzhu'
# )
# mysursor = mydb.cursor()
# mysursor.execute("CREATE TABLE Students (name VARCHAR(255), address VARCHAR(255))")#在zhuzhu库创建students表[第一步]
# #如果存在表了，需要增加在表创建多一条数据需要用alter...add【运行了第一步之后要注释第一步才可以运行此语句】
# mysursor.execute("alter table students add column id int auto_increment primary key")

# #4、插入数据[insert into 表名 (列名) values (对应数值)]
# import mysql.connector
# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='root',
#     database='zhuzhu'
# )
# mycursor = mydb.cursor()

# #场景一，插入一条数据操作显示
# sql = "insert into students (name,address) values (%s,%s)"
# var = ("Michelle", "Blue Village")
# mycursor.execute(sql,var)
# mydb.commit()#插入数据，以及更改数据都需要用到mydb.commit()语句
#print(mycursor.rowcount,"record inserted.")#计算插入显示多少条数据，例如：本次插入一条，返回值则：1 record inserted.
#print("1 record inserted, ID:",mycursor.lastrowid)#如果插入不止一行，则返回最后插入行的 id

# #场景二，插入多条数据显示要用executemany()方法
# sql = "insert into students (name,address) values (%s,%s)"
# var = [
#     ('Peter', 'Lowstreet 4'),
#     ('Amy', 'Apple st 652'),
#     ('Hannah', 'Mountain 21'),
#     ('Michael', 'Valley 345'),
#     ('Sandy', 'Ocean blvd 2'),
#     ('Betty', 'Green Grass 1'),
#     ('Richard', 'Sky st 331'),
# ]
# mycursor.executemany(sql,var)
# mydb.commit()
# print(mycursor.rowcount,"record inserted.")

#5、查询数据[select ..from] 和返回值需要用fetchall() 方法，该方法从最后执行的语句中获取所有，fetchone() 方法，该方法返回第一行
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='zhuzhu'
)
mycursor = mydb.cursor()

# sql = "select * from students"#编写sql语句
# mycursor.execute(sql)#传参执行sql语句
# result = mycursor.fetchall()#fetchall()方法返回全部  fetchone()方法返回第一行
# for i in result:
#     print(i)

#查询数据的时候，防止sql的注入【sql注入是常见的网络黑客技术，可以破坏或滥用您的数据库】
sql = "select * from students where address = %s"#使用占位符 ％s 方法来转义查询值
adr = ('Mountain 21',)#注意是字符串要加上逗号【，】
mycursor.execute(sql,adr)
result = mycursor.fetchall()
for i in result:
    print(i)