import mysql.connector
from configparser import ConfigParser

def connect_mysql():
    try:
        # 读取配置文件
        config = ConfigParser()
        config.read('config.ini')

        # 从配置文件中获取数据库连接信息
        host = config.get('mysql', 'host')
        user = config.get('mysql', 'user')
        password = config.get('mysql', 'password')
        database = config.get('mysql', 'database')

        # 连接数据库
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print("连接到 MySQL 数据库成功")

            # 创建游标
            cursor = connection.cursor()
            print("游标已打开")

            return connection, cursor

    except mysql.connector.Error as error:
        print("连接到 MySQL 数据库失败: {}".format(error))

# 使用示例
conn, cur = connect_mysql()
# 执行数据库操作