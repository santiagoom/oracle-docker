


查看Oracle数据库中的所有用户名
select username from dba_users;

oracle中的scott账户以sysdba身份登陆时，为什么查询不到emp和dept表搜索
sysdba身份登录的用户是sys用户，和scott用户是一样一样的，sys用户是管理用户，下面的表如果没有授权scott用户是看不到的，同样，scott下面的表sys用户也是看不到的。
emp和dept表是scott用户下表，so...

查询当前数据库中的所有表
SELECT * FROM ALL_TABLES;系统里有权限的表
SELECT * FROM DBA_TABLES; 系统表
SELECT * FROM USER_TABLES; 当前用户下的表

查看当前对象下的所有对象。
SELECT	* FROM	  user_catalog ;


