#!/bin/bash
# > more oe_create_table_script_tmp.ksh
#################################################################################
#  Script Name : cap_curated_hive_db_tbl_creation_adhoc.ksh
#  Creator    Date          Comment
#Sathyanarayana 03/03
#################################################################################
#  PURPOSE : This is a sample script created to check create and drop tables
#################################################################################
########  SETTING & VALIDATING INPUT PARAMETER  ########
 
export APP_PROFILE="etlcap"
echo "APP_PROFILE = "$APP_PROFILE
#source /$APPS/$SRC/$(whoami)/$APP_STATE/$APP_NAME/$APP_PROJ_COMMON/$APP_PROFILE.profile
 
echo "APP_STATE = " $APP_STATE
export ddls_dir="/apps/src/developers/cap/cap-mktg-common/scripts/shell/test/ddl"
export tableNameFF="v_codi_temp_ing"
export tbl_db="cap_curated_mktg"
export postinstall_dir="/apps/src/developers/cap/cap-mktg-common/scripts/shell/test/log"
export HIVE_BIN_PATH="/opt/mapr/hive/hive-2.3/bin"
export HIVE_JDBC_URI="jdbc:hive2://edl-b01-services.dev.bigdata.ccc.net:10000/default;auth=maprsasl;saslQop=auth-conf;ssl=true;"
export LOG_DIR="/apps/src/developers/cap/cap-mktg-common/scripts/shell/test/log/oe_exe_log.dat"
echo "ddls_filename : " $ddls_dir
echo "TABLE_NAME  :" $tableNameFF
echo "LOG_DIR       : " $LOG_DIR
echo "Hive Table Creation through Beeline Starting...." > $LOG_DIR
echo "Hive Bin Path :" $HIVE_BIN_PATH
echo "Hive JDBC Uri :" $HIVE_JDBC_URI
 
#Creation of Tables during deployment- t_txn_daily_test_ff
       $HIVE_BIN_PATH/beeline -u $HIVE_JDBC_URI -n $(whoami) -f "$ddls_dir/consr_crd_risk_ctrl_tbl2.hql" --hivevar APP_STATE=$APP_STATE >> $LOG_DIR
 
    if [ $? -ne 0 ]; then
        echo "ERROR:error running hql script $ddls_dir/$tableNameFF.hql command failed to execute in $APP_STATE - $TIMESTAMP"
 
exit 1
       else
               echo "SUCCESS: SUCCESS running hql script $ddls_dir/$tableNameFF.hql command created Target TBL/DB $tableNameFF in $APP_STATE - $TIMESTAMP"
       fi
 
(
echo "From: Customer Analytical Platform@ccc.com "
echo "To: Sathyanarayana.K.B@ccc.com; Priya.Swetha@ccc.com; Shruti.B@ccc.com; Anwesha.Das@ccc.com; P.Vasudev@ccc.com; Deve
n.Tak@ccc.com "
echo "Content-Type: text/html; "
echo "Subject: Automated mail- CAP_CUR_OE tables created successfully"
echo "<html>
<body>
<style> p  {color:#003366;} </style><p>
Hi Team,<br><br><pr>Tables($tableNameFF) are created <b>successfully</b>. Ingestion <b>In Progress</b>.</pr><br><br><pr>Thanks,<br>OE Team</pr></p></body></h
tml>"
) | /usr/sbin/sendmail -t
 