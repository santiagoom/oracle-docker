# Docker 拉取 oracle 11g镜像配置

https://www.jianshu.com/p/51f30378317f

开始记录docker拉取阿里的oracle11g 镜像并进行配置，

用pl/sql 可以登录为最终结果

navicat连接是在最后一步

这是我们所需要进行拉取oracle镜像的楼主所给出的说明

参考：https://blog.csdn.net/zwx521515/article/details/77982884

但是根据这个进行配置会有一些问题，所以写这篇记录一下，希望可以帮助其他人

开始：

 ①、开始拉取镜像-执行命令：

​     docker pull registry.cn-hangzhou.aliyuncs.com/helowin/oracle_11g

​    下载的过程少长，等待吧，喝杯咖啡，休息一会！（镜像6.8G）

​    下载完成后 查看镜像： docker images



![img](https:////upload-images.jianshu.io/upload_images/7843688-691737cf7b197fec.png?imageMogr2/auto-orient/strip|imageView2/2/w/1044/format/webp)

  可以看到已经下载好了

② 、创建容器

​    docker run -d -p 1521:1521 --name oracle11g registry.cn-hangzhou.aliyuncs.com/helowin/oracle_11g

​    这里说一下，命令后面的地址一定要是你下载的镜像地址也就是你拉取镜像名字，否则会出现名字已存在等问题！

​    如果创建成功能会返回容器id

③、启动容器 

​    docker start oracle11g



![img](https:////upload-images.jianshu.io/upload_images/7843688-2b75c4ab2dc2fb18.png?imageMogr2/auto-orient/strip|imageView2/2/w/493/format/webp)

④、进入镜像进行配置

   1、 docker exec -it oracle11g bash



![img](https:////upload-images.jianshu.io/upload_images/7843688-9ac634a7ce4ec7be.png?imageMogr2/auto-orient/strip|imageView2/2/w/614/format/webp)



   2、进行软连接

​      sqlplus /nolog



![img](https:////upload-images.jianshu.io/upload_images/7843688-f82e3ceafc3b5a70.png?imageMogr2/auto-orient/strip|imageView2/2/w/492/format/webp)

  发现没有这个命令，用不了

   3、切换到root 用户下

​      su root

​      密码：helowin



![img](https:////upload-images.jianshu.io/upload_images/7843688-0eddced6b38018ab.png?imageMogr2/auto-orient/strip|imageView2/2/w/423/format/webp)

​    注意这里还是在容器当中。。有朋友退去了。。。。。。。

   4、编辑profile文件配置ORACLE环境变量

​      export ORACLE_HOME=/home/oracle/app/oracle/product/11.2.0/dbhome_2

​      export ORACLE_SID=helowin

​      export PATH=$ORACLE_HOME/bin:$PATH



![img](https:////upload-images.jianshu.io/upload_images/7843688-2a22514587184acc.png?imageMogr2/auto-orient/strip|imageView2/2/w/576/format/webp)

​    在最后加上



![img](https:////upload-images.jianshu.io/upload_images/7843688-7698c3704e88c442.png?imageMogr2/auto-orient/strip|imageView2/2/w/760/format/webp)

​      保存并退出  ：wq

​    5、创建软连接

​      ln -s $ORACLE_HOME/bin/sqlplus /usr/bin

​    6、切换到oracle 用户

​       这里还要说一下，一定要写中间的内条 -  必须要，否则软连接无效



![img](https:////upload-images.jianshu.io/upload_images/7843688-6b62740171a6aab5.png?imageMogr2/auto-orient/strip|imageView2/2/w/465/format/webp)

 ⑤ 、登录sqlplus并修改sys、system用户密码

​    sqlplus /nolog

​    conn /as sysdba



![img](https:////upload-images.jianshu.io/upload_images/7843688-c4d67d0e26af0d5c.png?imageMogr2/auto-orient/strip|imageView2/2/w/659/format/webp)

​    接着执行下面命令

​    alter user system identified by system;

​    alter user sys identified by sys;

​    也可以创建用户 create user test identified by test;

​     并给用户赋予权限 grant connect,resource,dba to test;

  注意了这里的坑开始出现了

  当执行修改密码的时候出现 ：   database not open

   提示数据库没有打开，不急按如下操作

   输入：alter database open;

  注意了：这里也许还会提示  ：  ORA-01507: database not mounted

   不急！继续！



![img](https:////upload-images.jianshu.io/upload_images/7843688-a58de547bd761cdc.png?imageMogr2/auto-orient/strip|imageView2/2/w/458/format/webp)

  =========== 解决方法===========

   输入：alter database mount;

   输入 ：alter database open;



![img](https:////upload-images.jianshu.io/upload_images/7843688-cf6dbec2092880c6.png?imageMogr2/auto-orient/strip|imageView2/2/w/373/format/webp)

   然后就可执行 修改数据库密码的命令了

   改完之后输入：ALTER PROFILE DEFAULT LIMIT PASSWORD_LIFE_TIME UNLIMITED;

   刷新下表 

​    exit  是退休sql 软连接



![img](https:////upload-images.jianshu.io/upload_images/7843688-d72f3c5697df77dc.png?imageMogr2/auto-orient/strip|imageView2/2/w/766/format/webp)

⑥、使用pl/sql 进行连接 第7步是navicat连接的在最后

​     之前我们把端口映射到了1521上，所以我们需要进行配置 tnsnames.ora

  几个朋友不知道ora文件在哪，所以添加了这一步  

  pl/sql 安装包，汉化包，秘钥工具 https://download.csdn.net/download/qq_38380025/11168289

   plsql安装配置工具包  https://blog.csdn.net/qq_38380025/article/details/89677588

docker_oracle11 =

 (DESCRIPTION =

  (ADDRESS_LIST =

   (ADDRESS = (PROTOCOL = TCP)(HOST = 192.168.211.135)(PORT =1521))

  )

  (CONNECT_DATA =

   (SERVICE_NAME = orcl)

  )

)



  打开pl/sql 进行登录 ：提示监听程序当前无法识别连接描述符中请求的服务





![img](https:////upload-images.jianshu.io/upload_images/7843688-a687ea62b684887f.png?imageMogr2/auto-orient/strip|imageView2/2/w/505/format/webp)



![img](https:////upload-images.jianshu.io/upload_images/7843688-ded3ee9706e17033.png?imageMogr2/auto-orient/strip|imageView2/2/w/440/format/webp)

​    这时我们需要去看一下oracle 的 lsnrctl 服务



![img](https:////upload-images.jianshu.io/upload_images/7843688-3d700b20abac15b6.png?imageMogr2/auto-orient/strip|imageView2/2/w/807/format/webp)

​    看到这两个了么，任选其一，修改 tnsnames.ora的 service_name=helowinXDB

docker_oracle11 =

 (DESCRIPTION =

  (ADDRESS_LIST =

   (ADDRESS = (PROTOCOL = TCP)(HOST = 192.168.211.135)(PORT =1521))

  )

  (CONNECT_DATA =

   (SERVICE_NAME = helowinXDB)

  )

)

   欧克，登录成功。



![img](https:////upload-images.jianshu.io/upload_images/7843688-595ce4a3b383b824.png?imageMogr2/auto-orient/strip|imageView2/2/w/552/format/webp)

第7步是navicat连接

 有几个朋友用的是navicat连的所以故此添加这一步

打开navicat后（navicat12不用配置oci.dll文件了）

直接新建连接



