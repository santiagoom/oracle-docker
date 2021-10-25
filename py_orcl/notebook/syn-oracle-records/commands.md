
```
SQL> desc testword2;
Name      Type           Nullable Default Comments 
--------- -------------- -------- ------- -------- 
G_ID      NUMBER(6)      Y                         
L_ID      NUMBER(3)      Y                         
NAME      VARCHAR2(100)  Y                         
PRON      VARCHAR2(100)  Y                         
P         VARCHAR2(1)    Y                         
M         VARCHAR2(2000) Y                         
MDATE     DATE           Y                         
L_NA      VARCHAR2(5)    Y                         
MEANING   VARCHAR2(2000) Y                         
BOOK_NAME VARCHAR2(24)   Y                         
MTIME     NUMBER(2)      Y  
```

```
insert into RECORD (G_ID, L_ID, NAME, PRON, P, M, MDATE, L_NA, MEANING, BOOK_NAME, MTIME)
values (7596, null, 'integrate', '/ˈɪntɪɡreɪt/', null, 'verb<br>' || chr(10) || ': to combine (two or more things) to form or create something<br>' || chr(10) || ': to make (something) a part of another larger thing<br>' || chr(10) || ': to make (a person or group) part of a larger group or organization<br>' || chr(10) || '', to_date('10-01-2019 10:40:12', 'dd-mm-yyyy hh24:mi:ss'), null, 'v. 整合, 使...成整体<br>' || chr(10) || '<br>' || chr(10) || 'v.<br>' || chr(10) || '1: make into a whole or make part of a whole<br>' || chr(10) || '', null, 1);

```

```
select count(*) from testword2 where MDATE is not null;
select count(*) from testword2
```

```
select   to_char(sysdate, 'yyyy-MM-dd   HH24:mm:ss ')   from   dual;
to_date('17-03-2018 17:24:16', 'dd-mm-yyyy hh24:mi:ss')

```

```
spool D:\repos\syn-oracle-records\record.txt
select g_id,mtime,to_char(mdate, 'dd-mm-yyyy hh24:mi:ss') from record where mdate is not null;
spool off;
```

```
spool D:\repos\syn-oracle-records\record_.txt
select g_id,mtime,to_char(mdate, 'dd-mm-yyyy hh24:mi:ss') from record where mdate > to_date('28-03-2019 00:00:00', 'dd-mm-yyyy hh24:mi:ss') order by mdate;
spool off;
```



```
update record set(g_id, mtime, mdate) = (17155, 1, to_date('17-03-2018 17:24:16', 'dd-mm-yyyy hh24:mi:ss')) where g_id = 17155;
```

```
update record set mtime = 1, mdate = to_date('17-03-2018 17:24:16', 'dd-mm-yyyy hh24:mi:ss')
where g_id = 17155;
```

```
sql = "update record set mtime = " + mtime + ", mdate = to_date(" + mdate + ", 'dd-mm-yyyy hh24:mi:ss') where g_id = " + g_id + ";\n";

```
