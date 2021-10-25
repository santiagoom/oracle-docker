# import cx_Oracle
# con = cx_Oracle.connect('imajor/immajor@127.0.0.1/orcl')
# print(con.version)
# con.close()

import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir="/Users/tianm/Downloads/instantclient_19_8")


connection = cx_Oracle.connect('major_2020_8_24_1', 'nmajor',
                                cx_Oracle.makedsn('127.0.0.1',1521,'helowin') )
# connection = cx_Oracle.connect('major_2020_8_24_1', 'nmajor',
#                                 cx_Oracle.makedsn('127.0.0.1',1521,'orcl') )

# conn_str = u'user/password@host:port/service'
# conn_str = u'imajor/immajor@127.0.0.1:1521/service'
# conn_str = u'major_2020_8_24_1/nmajor@127.0.0.1:1521/orcl'
# conn = cx_Oracle.connect(conn_str)
c = connection.cursor()
# c.execute(u'select your_col_1, your_col_2 from your_table')
# for row in c:
#     print row[0], "-", row[1]
# conn.close()
