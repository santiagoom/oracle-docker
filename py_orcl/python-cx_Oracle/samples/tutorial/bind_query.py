#------------------------------------------------------------------------------
# bind_query.py (Section 4.1)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Copyright (c) 2017, 2021, Oracle and/or its affiliates. All rights reserved.
#------------------------------------------------------------------------------

import cx_Oracle
import db_config

con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)
cur = con.cursor()

# sql = "select * from dept where deptno = :id order by deptno"
sql = "select * from testword2 where g_id = :gid"

cur.execute(sql, gid = 1)
res = cur.fetchall()
print(res)

cur.execute(sql, gid = 2)
res = cur.fetchall()
print(res)
