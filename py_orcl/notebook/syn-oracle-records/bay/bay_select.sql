spool D:\repos\syn-oracle-records\bay\bay_record.txt
select g_id,name,mtime,to_char(mdate, 'dd-mm-yyyy hh24:mi:ss') from testword2 where mdate > to_date('28-03-2011 00:00:00', 'dd-mm-yyyy hh24:mi:ss') order by g_id;
spool off;