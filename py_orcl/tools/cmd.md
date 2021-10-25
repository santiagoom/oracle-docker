

sqlplus major_2020_8_24_1@127.0.0.1:1521/helowin

sqlplus -l system/systempassword@localhost/orclpdb1 @create_user
sqlplus -l system/orcl@192.168.1.196:1521/helowin @create_user


sqlplus system@192.168.1.196:1521/helowin

sqlplus major_2020_8_24_1@192.168.1.196/helowin

sqlplus system@192.168.1.196/helowin
sqlplus sys@192.168.1.196/helowin

sqlplus -l major_2020_8_24_1@192.168.1.196/helowin
sqlplus -l major_2020_8_24_1/nmajor@192.168.1.196/helowin

sqlplus -l system/system@192.168.1.196:1521/helowin  @sql/create_user

cxtest
cxtest


sqlplus -l cxtest/cxtest@192.168.1.196:1521/helowin @@sql/setup_tables
