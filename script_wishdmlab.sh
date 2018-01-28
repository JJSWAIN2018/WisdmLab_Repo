#! /user/bin/bash

db_user=more
db_passwd=wishdmlab@123
sqlplus -s ${db_user} | ${db_passwd}<<!>>dev/null2>&1
spool /home/more/user_ids/user_id_list.lst;
set heading off;
set pagesize 0;
set feedback off;
set echo off;
set verify off;
set linesize 100;
select 'UID|lastlogin' from dual
select UID,last login from user_table_name
spool off;
for i in `cat user_id_list.lst`
    echo  $i | cut -f1 > Vout.txt
    cn=`wc -l Vout.txt`
    cnn=`expr cn + 1`
echo "You are the visitor no:$cnn"


