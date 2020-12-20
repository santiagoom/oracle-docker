# import cx_Oracle
# con = cx_Oracle.connect('imajor/immajor@127.0.0.1/orcl')
# print(con.version)
# con.close()

import cx_Oracle

# conn_str = u'user/password@host:port/service'
conn_str = u'imajor/immajor@127.0.0.1:1521/service'
conn = cx_Oracle.connect(conn_str)
c = conn.cursor()
# c.execute(u'select your_col_1, your_col_2 from your_table')
# for row in c:
#     print row[0], "-", row[1]
# conn.close()