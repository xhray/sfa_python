# -*- coding: utf-8 -*-

'数据库操作工具类'

__author__ = 'Ray.Tan'

import sys

sys.path.append('..')

from connection_model import connection_model

def fetchdata(q, **kwargs):
    '''根据语句和关键字参数获取数据'''
    conn = connection_model.get_oracle_connection()
    cursor = conn.cursor()
    cursor.execute(q, **kwargs)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def execute(q, **kwargs):
    '''更新/插入/删除数据'''
    conn = connection_model.get_oracle_connection()

    try:
        cursor = conn.cursor()
        cursor.execute(q, **kwargs)
        cursor.close()
        conn.commit()
    except Exception, e:
        conn.rollback()
        raise e
    finally:
        conn.close()


if __name__ == '__main__':
    sql = 'select 1 as id, 2 as name from dual where 1 = :id and 2 = :sup_type'
    r = fetchdata(sql, id = 1, sup_type = 2)

    for x in r:
        print '%s, %s' % (x[0], x[1])