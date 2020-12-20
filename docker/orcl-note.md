## docker run

```
root@yons-B365M-POWER:~# docker run -it -v /home/yons/tianm/volume/:/root/volume --restart=always -p 8002:22  -p 1521:1521 -p 8020:8080 --name orcl-init registry.cn-hangzhou.aliyuncs.com/helowin/oracle_11g /bin/bash
/home/oracle/app/oracle/product/11.2.0/dbhome_2
Processing Database instance "helowin": log file /home/oracle/app/oracle/product/11.2.0/dbhome_2/startup.log
Fixed Size                  2213776 bytes
Variable Size             402655344 bytes
Database Buffers         1191182336 bytes
Redo Buffers                7360512 bytes
Database mounted.
Database opened.
SQL> Disconnected from Oracle Database 11g Enterprise Edition Release 11.2.0.1.0 - 64bit Production
With the Partitioning, OLAP, Data Mining and Real Application Testing options

/home/oracle/app/oracle/product/11.2.0/dbhome_2/bin/dbstart: Database instance "helowin" warm started.
tail: unrecognized file system type 0x794c7630 for `/home/oracle/app/oracle/product/11.2.0/dbhome_2/startup.log'. Reverting to polling.


```



```
su root
密码：helowin
```



```


su root
vi /home/oracle/.bashrc
export ORACLE_HOME=/home/oracle/app/oracle/product/11.2.0/dbhome_2
 
export ORACLE_SID=helowin
 
export PATH=$ORACLE_HOME/bin:$PATH

sqlplus /nolog;
conn /as sysdba;
alter user system identified by system;
alter user sys identified by sys;
alter user test identified by test;

-- 创建用户
create user itest identified by imtest;
-- 向用户授权
grant connect,resource,dba to itest;

connect  itest/imtest;

SQL> shutdown immediate;
Database closed.
Database dismounted.
ORACLE instance shut down.

SQL> startup mount;
ORACLE instance started.

Total System Global Area 1603411968 bytes
Fixed Size                  2213776 bytes
Variable Size             402655344 bytes
Database Buffers         1191182336 bytes
Redo Buffers                7360512 bytes
Database mounted.


SQL> alter database open;

Database altered.


```



## ORA-00214

https://aprakash.wordpress.com/2010/02/01/ora-00214-controlfiles-inconsistent/

将数据拷贝过去即可

copy file 并保持访问权限一致

oracle oinstall

**Solution:**

Ensure existing control file locations with following:

```
SQL> show parameter control_files
NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
control_files                        string      /u01/app/oracle/oradata/RTS/co
                                                 ntrol01.ctl, /u01/app/oracle/o
                                                 radata/RTS/control02.ctl
```

There are 2 control files mentioned in CONTROL_FILES parameter, Ensure which control file is not available.

```
[oracle@PR]$ ll /u01/app/oracle/oradata/RTS/control01.ctl
-rw-r-----. 1 oracle oinstall 9748480 Jun 24 03:37 /u01/app/oracle/oradata/RTS/control01.ctl
[oracle@PR]$ ll /u01/app/oracle/oradata/RTS/control02.ctl
ls: cannot access /u01/app/oracle/oradata/RTS/control02.ctl: No such file or directory
```

So, control02.ctl is not available, issue following alter command in order to edit only one control file location in CONTROL_FILES parameter.

```
SQL> alter system set control_files='/u01/app/oracle/oradata/RTS/control01.ctl' scope=spfile;
System altered.
```

Shutdown the database and start it up:

```
https://aprakash.wordpress.com/2010/02/01/ora-00214-controlfiles-inconsistent/
```

ORA-00214 – CONTROLFILES INCONSISTENT

Posted on [February 1, 2010](https://aprakash.wordpress.com/2010/02/01/ora-00214-controlfiles-inconsistent/) by [Anand](https://aprakash.wordpress.com/author/aprakash/)

Today’s morning started with “ORA-00214”.I get happy when i get errors or issues.Coming back to point, here i would show the steps taken to resolve it.

*“An ORA-00214 is issued whenever Oracle detects an inconsistency between two mirrored copies of the control file.”*

One of the UAT db was unable to mount cause of inconsistencies in the multiplexed controlfiles. It gave the below error during startup :-

```
sql> startup
ORACLE instance started.

Total System Global Area  209715200 bytes
Fixed Size                  1295896 bytes
Variable Size             146803176 bytes
Database Buffers           54525952 bytes
Redo Buffers                7090176 bytes
ORA-00214: controlfile 'D:\ORACLE\PRODUCT\10.2.0\ORADATA\CONTROL01.CTL' version 17404
inconsistent with file 'D:\ORACLE\PRODUCT\10.2.0\ORADATA\CONTROL03.CTL' version 17409
```

Steps taken to resolve it:-

\1. Show parameter control_file

\2. As from the above error it could been seen that the version <number> for CONTROL03.CTL is higher, compared to CONTROL01.CTL, so

```
sql> alter system set control_files='D:\oracle\product\10.2.0\oradata\CONTROL03.CTL' scope=spfile;

sql> shutdown immediate;

sql> startup mount; --> The mount was successful.

sql> alter database open;
```

Checked for is some error in alert log.Everything seemed to be ok.Changed the control_files parameter,switched the logfile groups and the made the database down.

```
sql> alter system set control_files='D:\oracle\product\10.2.0\oradata\CONTROL01.CTL',
'D:\oracle\product\10.2.0\oradata\CONTROL02.CTL','D:\oracle\product\10.2.0\oradata\CONTROL03.CTL' scope=spfile;

sql> alter system switch logfile;
sql> alter system switch logfile;
sql> shutdown immediate;
```

Copied the CONTROL03.CTL , made two copies of it ,renamed it to CONTROL01.CTL and CONTROL02.CTL and started up the database.

```
sql >startup
ORACLE instance started.

Total System Global Area  209715200 bytes
Fixed Size                  1295896 bytes
Variable Size             146803176 bytes
Database Buffers           54525952 bytes
Redo Buffers                7090176 bytes
Database mounted.
Database opened.
sql>
sql>
```

NOTE:- When in step 2 the control_files parameter was set to ‘D:\oracle\product\10.2.0\oradata\CONTROL01.CTL’, SCN mismatch occurred between the redo logfiles and the controlfile and the database didn’t go to mount stage.





## ORA-01113

https://dbatricksworld.com/ora-01113-file-n-needs-media-recovery-ora-01110-data-file-n-system01-data4/

```
SELECT MEMBER FROM V$LOG G, V$LOGFILE F WHERE G.GROUP# = F.GROUP# AND G.STATUS = 'CURRENT';

show parameter control_files

```



## lsnrctl

```
lsnrctl status
lsnrctl start
```





```
下载好后解压到你的盘中。

填写E:\instantclient_11_2\oci.dll填写到下方。（两个位置一致）

进入这个目录找到tnsnames.ora 文件双击打开

E:\instantclient_11_2\NETWORK\ADMIN\tnsnames.ora

添加如下配置，（请更改成自己的文件配置）

docker_oracle11 =
 (DESCRIPTION =
   (ADDRESS_LIST =
     (ADDRESS = (PROTOCOL = TCP)(HOST = 192.168.211.135)(PORT =1521))
   )
   (CONNECT_DATA =
     (SERVICE_NAME = helowinXDB)
   )
)
 

保存，

安装pl/sql 好后，双击打开，不要登录会进入默认页面




填写E:\instantclient_11_2\oci.dll填写到下方。（两个位置一致）
```



## docker oracle
```
docker run -it -v /home/yons/tianm/volume/:/home/oracle/volume --restart=always -p 8002:22  -p 1521:1521 -p 8020:8080 --name orcl-11g 
docker run -it -v /Users/tianm/docker/volume/:/root/volume --restart=always -p 8002:22  -p 1521:1521 --name oral

/Users/tianm/docker/volume
docker run --privileged --name oracle11g -p 1521:1521 -v /home/yons/tianm/volume/tianm/orcl:/install jaspeen/oracle-11g
docker run -it -v /Users/tianm/docker/volume/:/home/oracle/volume -p 8002:22  -p 1521:1521 -p 8020:8080 --name orcl-11g 

mac config
→→~: docker run -it -v /Users/tianm/docker/volume/:/home/oracle/volume -p 8002:22  -p 1521:1521 -p 8020:8080 --name orcl-11g imagezero/orcl-11g:init /bin/bash
/home/oracle/app/oracle/product/11.2.0/dbhome_2
Processing Database instance "helowin": log file /home/oracle/app/oracle/product/11.2.0/dbhome_2/startup.log
ORA-00214: control file
'/home/oracle/app/oracle/flash_recovery_area/helowin/control02.ctl' version
2864 inconsistent with file
'/home/oracle/app/oracle/oradata/helowin/control01.ctl' version 841

SQL> Disconnected from Oracle Database 11g Enterprise Edition Release 11.2.0.1.0 - 64bit Production
With the Partitioning, OLAP, Data Mining and Real Application Testing options

/home/oracle/app/oracle/product/11.2.0/dbhome_2/bin/dbstart: Database instance "helowin" warm started.
tail: unrecognized file system type 0x794c7630 for `/home/oracle/app/oracle/product/11.2.0/dbhome_2/startup.log'. Reverting to polling.

```
