

plsql

ed mode


create table USERS
(
  USERNAME VARCHAR2(20),
  PASSWORD VARCHAR2(20)
)
tablespace USERS
  pctfree 10
  initrans 1
  maxtrans 255
  storage
  (
    initial 64K
    next 1M
    minextents 1
    maxextents unlimited
  );


insert into USERS (USERNAME, PASSWORD) values ('NMajor', 'n');
insert into USERS (USERNAME, PASSWORD) values ('Jerry', '1234');
commit;

select  count(*)  from testword2 where MDATE is not NULL;