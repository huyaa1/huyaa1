# -*- coding: utf-8 -*-            
# @Author : 测试小牛
# @Time : 07/09/2023 16:13
import pymysql

# 建立数据库连接
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    db='user'
)

try:
    # 创建游标
    cursor = conn.cursor()

    # 执行查询
    cursor.execute('SELECT * FROM student where id =1')

    # 获取所有结果
    rows = cursor.fetchall()

    # 遍历结果
    for row in rows:
        # 处理每一行的数据
        print(row)

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # 关闭游标和数据库连接
    cursor.close()
    conn.close()