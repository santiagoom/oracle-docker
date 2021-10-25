#------------------------------------------------------------------------------
# query.py (Section 1.3 and 1.4)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Copyright (c) 2017, 2021, Oracle and/or its affiliates. All rights reserved.
#------------------------------------------------------------------------------

import cx_Oracle
import db_config

from pyutils.logger_d2 import  setup_logger

logger = setup_logger("./log/cx_oracle",name="cx_oracle")

con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)


cur = con.cursor()
cur.execute("select * from testword2 order by g_id")
res = cur.fetchall()
for row in res:
    print(row)
    logger.info(row)

cur.close()
con.close()