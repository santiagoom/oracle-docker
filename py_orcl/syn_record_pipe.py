import cx_Oracle
import db_config
import os
from datetime import datetime

from pyutils.logger_d2 import setup_logger

logger = setup_logger("./log/recordlog.txt", name="nmajor")


def query_records():
    con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)
    cur = con.cursor()
    # sql = 'select * from SampleQueryTab where id = :bvid'
    sql = 'select g_id,name,mtime,to_char(mdate, \'dd-mm-yyyy hh24:mi:ss\') from testword2 where mdate > to_date(\'28-03-2011 00:00:00\', \'dd-mm-yyyy hh24:mi:ss\') order by mdate'
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    con.close()
    return res


def read_records():
    filename = "record.txt"
    if not os.path.isfile(filename):
        print("record file is not exist...")
        exit(-1)
    with open(filename, mode="r") as f:
        lines = f.readlines()
    records = []
    for line in lines:
        g_id = line.strip().split(",")[0].strip()[1:]
        name = line.strip().split(",")[1].strip()[:]
        mtime = line.strip().split(",")[2].strip()
        mdate = line.strip().split(",")[3].strip()[:-1]
        mdate = datetime.strptime(mdate, "%d-%m-%Y %H:%M:%S")
        records.append((g_id, name, mtime, mdate))
    return records


def merge_records(records, query):
    merge_records_dict = {}

    for record in records:
        g_id = int(record[0])
        name = record[1]
        mtime = int(record[2])
        mdate = record[3]
        merge_records_dict[g_id] = (name, mtime, mdate)

    for record in query:
        g_id = record[0]
        name = record[1]
        mtime = record[2]
        mdate = datetime.strptime(record[3], "%d-%m-%Y %H:%M:%S")

        if g_id in merge_records_dict:
            name_merge = merge_records_dict[g_id][0]
            mtime_merge = merge_records_dict[g_id][1]
            mdate_merge = merge_records_dict[g_id][2]

            if (name == name_merge) and (mtime == mtime_merge) and mdate == mdate_merge:
                pass
            else:
                mtime = max(mtime, mtime_merge)
                if mdate > mdate_merge:
                    merge_records_dict[g_id] = (name, mtime, mdate)
                else:
                    merge_records_dict[g_id] = (name, mtime, mdate_merge)
        else:
            merge_records_dict[g_id] = (name, mtime, mdate)

    update_list = []
    for key, val in merge_records_dict.items():
        flag = True
        for record in query:
            g_id = record[0]
            if key == g_id:
                flag = False
                name = record[1]
                mtime = record[2]
                mdate = datetime.strptime(record[3], "%d-%m-%Y %H:%M:%S")
                name_merge = val[0]
                mtime_merge = val[1]
                mdate_merge = val[2]
                if (name == name_merge) and (mtime == mtime_merge) and mdate == mdate_merge:
                    break
                else:
                    update_list.append((key, val[0], val[1], val[2]))
                    break
        if (flag):
            update_list.append((key, val[0], val[1], val[2]))

    record_all = "record_all.txt"
    merged = sorted(merge_records_dict.items(), key=lambda d: d[1][2])
    if os.path.isfile(record_all):
        os.remove(record_all)
    with open(record_all, mode="w", encoding="utf8") as f:
        f.write("")
    for each in merged:
        g_id = each[0]
        name = each[1][0]
        mtime = each[1][1]
        mdate = each[1][2]
        mdate = mdate.strftime("%d-%m-%Y %H:%M:%S")
        record = "({},{},{},{})".format(g_id, name, mtime, mdate)

        # logger.info(each)
        with open(record_all, mode="a", encoding="utf8") as f:
            f.write(record + "\n")

    update_list_sort = sorted(update_list, key=lambda d: d[3])

    for each in update_list_sort:
        logger.info(each)

    return update_list_sort


def update_records(update_list):
    con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)
    cur = con.cursor()
    rows = []
    for record in update_list:
        row = {}
        row["g_id"] = record[0]
        row["name"] = record[1]
        row["mtime"] = record[2]
        row["mdate"] = record[3].strftime("%d-%m-%Y %H:%M:%S")
        rows.append(row)

    sql = "update testword2 set name = :name, mtime = :mtime, mdate = to_date(:mdate, \'dd-mm-yyyy hh24:mi:ss\') where g_id = :g_id"
    # sql1 = "update testword2 set mtime = null, mdate = null where g_id = 18204"

    for row in rows:
        cur.execute(sql, {"name": row["name"], "mtime": row["mtime"], "mdate": row["mdate"], "g_id": row["g_id"]})
    con.commit()

    cur.close()
    con.close()

    logger.info("update {} rows...".format(len(rows)))
    logger.info("commit complete...")


def update_individual():
    con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)
    cur = con.cursor()

    sql1 = "update testword2 set mtime = null, mdate = null where g_id = 47253"
    cur.execute(sql1)
    sql2 = "update testword2 set mtime = null, mdate = null where g_id = 219295"
    cur.execute(sql2)
    sql3 = "update testword2 set mtime = null, mdate = null where g_id = 18204"
    cur.execute(sql3)
    con.commit()
    cur.close()
    con.close()
    pass


def run():
    flag = True
    # flag = False
    if flag:
        records = read_records()
        if len(records) <= 0:
            print("record file is not empty...")
            exit(-1)
            return
        query = query_records()
        update_list = merge_records(records, query)
        update = update_records(update_list)
    else:
        update_individual()


if __name__ == '__main__':
    run()
