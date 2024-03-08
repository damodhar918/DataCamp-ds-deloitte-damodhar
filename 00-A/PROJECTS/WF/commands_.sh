[3:37 PM] Jangam, Damodhar

Error
/apps/dat/etlcapad/dev/cap/mktg/curated/logs
ls -ltr -- for latest error

Error
vi t_acct_dtl_fdr_temp_4_cardss_2023-08-29_06-13-41.log --> /Excep -->Applicationid
yarn logs -applicationId application_1702349003221_7114 > /tmp/log.txt; vi /tmp/log.txt

Lookup
/Error or /Excep or key words
yarn logs -applicationId application_1699607101405_223321 > /tmp/log.txt; vi /tmp/log.txt

Jils for sit/uit/prod
/apps/src/developers/cap/cap-dev-tools/gen_jil.ksh -e damodhar.jangam@ccc.com -f
CAP_D_MKTG_CUR_T_CEE_FNDTN_TMP6_DEV_CM.jil

[3:38 PM] Jangam, Damodhar

Hive1

Show table
show create table CAP_CURATED_MKTG_TEMP.t_acct_dtl_fdr_temp_4_cardss;

View table
select \* from CAP_CURATED_MKTG_TEMP.t_acct_dtl_fdr_temp_4_cardss;

Drop table
Drop table CAP_CURATED_MKTG_TEMP.t_acct_dtl_fdr_temp_4_cardss;

Show like db's
show databases like '_consumer_fdr_';

Show like tables
use dev_consumer_fdr_sanitized;

show tables like '_consumer_fdr_';
spark.sql("""SHOW TABLES IN dev_consumer_fdr_sanitized LIKE 't_c2t%'""").show()

spark.sql("""SHOW TABLES IN curated_mktg_uat LIKE 't_c2t\*'""").show()

INSERT OVERWRITE TABLE curated_mktg_uat.t_c2t_email_addr
PARTITION ( businessdate = '20230614' )
SELECT \* FROM sit_mrm_c2t_sanitized.t_c2t_email_addr;

Copy to another env
hadoop distcp maprfs://edl-uat-b01/datalake/cap/curated/mktg/temp/t_cust_x_acct_drv_temp/\* maprfs://edl-dev-b02/datalake/cap/curated/mktg/uat/temp/t_cust_x_acct_drv_temp

export MAPR_TICKETFILE_LOCATION=/apps/src/developers/cap/cap-mktg-common/uat_maprticket/maprticket_uat_dev_etlcapau_etlcapad

distcp
hadoop distcp maprfs://edl-uat-b01/datalake/cap/sdg/tdm/tdm_uat_dsr_ih_sanitized/pr_data_ih_dim_ihaction/\* maprfs://edl-dev-b02/datalake/cap/curated/mktg/uat/temp_table

scp
scp /apps/src/developers/k078158/home/sdgp k078158@wuvra92a0897:/var/tmp/

source
/apps/src/etlcapad/dev/cap/mktg/curated/t_ecn/ddl

Modify path
/apps/run/etlcapad/dev/cap/mktg/curated/ =====/common

/apps/src/etlcapas/sit/cap/mktg/curated/t_ecn/common

/apps/run/etlcapas/sit/cap/mktg/curated/t_ecn/common

/apps/src/etlcapau/uat/cap/mktg/curated/====/common

kill
for x in $(yarn application -list -appTypes SPARK/RUNNING/ACCEPTED | awk 'NR > 2 { print $1 }'); do yarn application -kill $x; done
for x in $(yarn application -list -appTypes SPARK | awk 'NR > 2 { print $1 }'); do yarn application -kill $x; done

CREATE EXTERNAL TABLE IF NOT EXISTS cap_bi_marketing_mockup.bmgpdd_tran_dy_hist_hg_sanitized_app_tmp30(acct_num decimal(30,0),co_id decimal(30,0),post_dt date,led_bal decimal(30,2),TRAN_SEQ_NUM decimal(30,0))
PARTITIONED BY (eapp_dct_business_effective_date date) row format delimited fields terminated by ',' stored as textFile LOCATION 'maprfs:/datalake/cap/bi/marketing/temp/mockdata/bmgpdd_tran_dy_hist_hg_sanitized';

hadoop fs -put -f BMGPDD_TRAN_DY_HIST_HG_sanitized_app_temp30.csv maprfs:///datalake/cap/bi/marketing/temp/mockdata

LOAD DATA INPATH 'maprfs:/datalake/cap/bi/marketing/temp/mockdata/BMGPDD_TRAN_DY_HIST_HG_sanitized_app_temp30.csv'
INTO TABLE cap_bi_marketing_mockup.bmgpdd_tran_dy_hist_hg_sanitized_app_tmp30
PARTITION(eapp_dct_business_effective_date='2023-09-25');

Jil test
#IMPLEMENT:CAP:damodhar.jangam@ccc.com

(echo "From: Customer Analytical Platform@ccc.com "
echo "To: damodhar.jangam@ccc.com; Sathyanarayana.K.B@ccc.com; P.Vasudev@ccc.com; "
echo "Content-Type: text/html; "
echo "Subject: Automated mail- CNAPP_CCR tables created successfully"
echo "<html><body><style> p {color:#003366;} </style><p>Hi Team,<br><br><pr>Tables($tableName) are created <b>successfully</b>. Ingestion <b>In Progress</b>.</pr><br><br><pr>Thanks,<br>OE Team</pr></p></body></html>")
| /usr/sbin/sendmail -t

#Inserting data into the consr*crd_risk_ctrl_tbl
$HIVE_BIN_PATH/beeline -u $HIVE_JDBC_URI -n $(whoami) --hivevar APP_STATE=$APP_STATE -e "${ctrlQuery}"> ${LOG_DIR}/${fileName}*${RUN_DATE}.log 2>&1

if [ $? -ne 0 ]; then
(
echo "From: ${FROM_EMAIL}"
       echo "To: ${EMAIL_TO_LIST}"
       echo "Content-Type: text/html; "
       echo "Subject: Automated mail- Control file ingestion is failed for ${fileName} -${today}"
echo "<html>
<body>
Hi Team,<br><br><pr>Control file <b>${ctrlFileName}</b> is failed. Please take necessary action.</pr><br><br><pr>Thanks,
<br>OE Team</pr></body></html>"
) | /usr/sbin/sendmail -t
exit 1

else
(
echo "From: ${FROM_EMAIL}"
       echo "To: ${EMAIL_TO_LIST}"
       echo "Content-Type: text/html; "
       echo "Subject: Automated mail- Control file ingestion is successful for ${fileName} -${today}"
echo "<html>
<body>
Hi Team,<br><br><pr>Control file <b>${ctrlFileName}</b> is successfully ingested into <b> ${TMP_DATABASE}.consr_crd_risk_ctrl_tbl</b> table.</pr><br><br><pr>Thanks,
<br>OE Team</pr></body></html>"
) | /usr/sbin/sendmail -t
fi

/opt/mapr/hive/hive-2.3/bin/beeline -u 'jdbc:hive2://edl-b01-services.dev.bigdata.ccc.net:10000/default;auth=maprsasl;saslQop=auth-conf;ssl=true;' -n aasconad -f /apps/src/developers/k078158/home/automation/ddl/CONSR_CRD_RISK_STRTG_PCLI_CNT_raw.hql --hivevar APP_STATE=dev

/opt/mapr/hive/hive-2.3/bin/beeline -u 'jdbc:hive2://edl-b01-services.dev.bigdata.ccc.net:10000/default;auth=maprsasl;saslQop=auth-conf;ssl=true;' -n aasconad -e 'DESCRIBE dev_ccr_shr_raw.CONSR_CRD_RISK_STRTG_PCLI_CNT' --hivevar APP_STATE=dev