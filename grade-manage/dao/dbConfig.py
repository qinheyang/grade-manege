import pymysql

"""数据源配置信息"""
localSourceConfig = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    'db': 'grade-manage',
    'charset': 'utf8',
    'cursorclass' : pymysql.cursors.DictCursor
}



