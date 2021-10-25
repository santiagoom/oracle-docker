path = "nce_record.txt"
with open(path, encoding='utf8', mode='r') as file:
    content = file.readlines()

sql_update = "nce_update.sql"
record_refine = "nce_record_refine.txt"
update = open(sql_update, encoding='utf8', mode='w')
record = open(record_refine, encoding='utf8', mode='w')
for line in content:
    parts = line.split()
    # to_date('17-03-2018 17:24:16', 'dd-mm-yyyy hh24:mi:ss')
    if (len(parts) == 5):
        for each in parts:
            record.write(each + "\t\t")
        record.write("\n")
        g_id = parts[0]
        mtime = parts[2]
        date = parts[3]
        time = parts[4]
        mdate = "'" + date + " " + time + "'"
        sql = "update testword2 set mtime = " + mtime + ", mdate = to_date(" + mdate + ", 'dd-mm-yyyy hh24:mi:ss') where g_id = " + g_id + ";\n";
        print(sql)
        update.write(sql)

update.write("commit;")
record.close()
update.close()
