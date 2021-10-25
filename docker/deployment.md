# process
```
code
su root
root
su oracle
orcl
```

```
docker run -it -v /Users/tianm/docker/volume/:/home/oracle/volume -p 8002:22  -p 1521:1521 -p 8020:8080 --name orcl-11g-v1 imagezero/orcl-11g:v1 /bin/bash

su root
root

vi /home/oracle/.bashrc
export ORACLE_HOME=/home/oracle/app/oracle/product/11.2.0/dbhome_2
export ORACLE_SID=helowin
export PATH=$ORACLE_HOME/bin:$PATH

add 
source /etc/profile
to /root/.bashrc

/home/oracle/app/oracle/oradata/helowin/
cp /home/oracle/orcl_kits/oradata/helowin/* /home/oracle/app/oracle/oradata/helowin/

sqlplus /nolog;
conn /as sysdba;

SQL> show parameter control_files;

NAME				     TYPE	 VALUE
------------------------------------ ----------- ------------------------------
control_files			     string	 /home/oracle/app/oracle/oradat
						 a/helowin/control01.ctl, /home
						 /oracle/app/oracle/flash_recov
						 ery_area/helowin/control02.ctl

[oracle@ac660b9382df helowin]$ ll /home/oracle/app/oracle/oradata/helowin/control01.ctl
-rw-r----- 1 oracle oinstall 10076160 Dec 20 13:13 /home/oracle/app/oracle/oradata/helowin/control01.ctl
[oracle@ac660b9382df helowin]$ 
[oracle@ac660b9382df helowin]$ ll /home/oracle/app/oracle/flash_recovery_area/helowin/control02.ctl
-rw-r----- 1 oracle oinstall 10076160 Aug 24 02:24 /home/oracle/app/oracle/flash_recovery_area/helowin/control02.ctl

[oracle@ac660b9382df helowin]$ ll /home/oracle/app/oracle/flash_recovery_area/helowin/
total 19360
-rw-r----- 1 oracle oinstall 10076160 Aug 24 02:24 control02.ctl
-rw-r----- 1 oracle oinstall  9748480 Jan  4  2016 control02.ctl.bak

cp /home/oracle/app/oracle/oradata/helowin/control01.ctl /home/oracle/app/oracle/flash_recovery_area/helowin/

cd /home/oracle/app/oracle/flash_recovery_area/helowin/
cp control01.ctl control02.ctl
[oracle@ac660b9382df helowin]$ ll
total 39040
-rw-r----- 1 oracle oinstall 10076160 Dec 20 13:28 control01.ctl
-rw-r----- 1 oracle oinstall 10076160 Dec 20 13:30 control02.ctl
-rw-r----- 1 oracle oinstall  9748480 Jan  4  2016 control02.ctl.bak
-rw-r----- 1 oracle oinstall 10076160 Dec 20 13:29 control02.ctl.bak_2020-12-20-0



sql> shutdown immediate;

sql> startup mount; --> The mount was successful.

sql> alter database open;


java -version
javac -version

vi /etc/profile
#set Java environment
export JAVA_HOME=/usr/local/java
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:JAVA_HOME/lib:JRE_HOME/lib:${CLASSPATH}
export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH

[root@ac660b9382df local]# source /etc/profile
[root@ac660b9382df local]# java -version
java version "1.8.0_202"
Java(TM) SE Runtime Environment (build 1.8.0_202-b08)
Java HotSpot(TM) 64-Bit Server VM (build 25.202-b08, mixed mode)
[root@ac660b9382df local]# 
[root@ac660b9382df local]# javac -version
javac 1.8.0_202
[root@ac660b9382df local]# 

nce
ince_2020_8_24_1
ince

major
imajor_2020_8_24_1
major

word
word_2020_8_24_1
word

vi /usr/local/Tomcat/webapps/wordweb/WEB-INF/classes/c3p0-config.xml
vi /usr/local/Tomcat/webapps/terminal/WEB-INF/classes/c3p0-config.xml
vi /usr/local/Tomcat/webapps/bay/WEB-INF/classes/c3p0-config.xml
vi /usr/local/Tomcat/webapps/nce/WEB-INF/classes/c3p0-config.xml
vi /usr/local/Tomcat/webapps/major/WEB-INF/classes/c3p0-config.xml

```





# password update

```
[oracle@f327fab1f269 ~]$ sqlplus /nolog;

SQL*Plus: Release 11.2.0.1.0 Production on Mon Mar 1 10:19:03 2021
Copyright (c) 1982, 2009, Oracle.  All rights reserved.

SQL> conn major_2020_8_24_1
Enter password: 
ERROR:
ORA-28001: the password has expired

Changing password for major_2020_8_24_1
New password: 
Retype new password: 
Password changed
Connected.
SQL> 


2020-8-24-1 22:24:27
add new major


create
create user major_2020_8_24_1 identified by nmajor;
grant connect,resource,dba to major_2020_8_24_1;

imp 'major_2020_8_24_1/nmajor' file=/home/oracle/volume/tianm/orcl/oracle20190521/shabay.dmp full=Y
vi /usr/local/Tomcat/webapps/nmajor/WEB-INF/classes/c3p0-config.xml
vi /usr/local/Tomcat/webapps/imajor/WEB-INF/classes/c3p0-config.xml


alter
alter  user  major_2020_8_24_1  identified by nmajor;


select username from dba_users;

tianm@localhost instantclient_19_8 % export ORACLE_SID=helowin
tianm@localhost instantclient_19_8 % export PATH=~/Downloads/instantclient_19_8:$PATH
https://docs.oracle.com/database/121/NETAG/concepts.htm#NETAG253

correct:
sqlplus major_2020_8_24_1@127.0.0.1:1521/helowin
```

