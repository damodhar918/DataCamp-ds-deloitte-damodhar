
/opt/mapr/hive/hive-2.3/bin/beeline 
-u "jdbc:hive2://edl-b01-services.dev.bigdata.ccc.net:10000/default;auth=maprsasl;saslQop=auth-conf;ssl=true;"

 
desc dev_consumer_pcli_raw.consr_crd_risk_ctrl_tbl
 
CREATE EXTERNAL TABLE dev_consumer_pcli_raw.consr_crd_risk_ctrl_tbl2(
SOURCE_CODE string,
DATA_FILE_NAME string,
DATE_OF_DATA timestamp,
RECORD_COUNT int,
FILE_CREATION_DATE timestamp,
TIME_STAMP string,
TOTAL_BYTE_COUNT int,
FILE_VERSION string,
CONTROL_FILE_VERSION string,
ENV string,
eapp_dct_source_system_id string,
eapp_dct_feed_name string,
eapp_dct_run_id string,
eapp_dct_create_dttm string,
eapp_dct_create_user_id string
)
PARTITIONED BY (
eapp_dct_business_effective_date date)
ROW FORMAT SERDE
'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 'maprfs:/datalake_dev/consumer/ccr_shr/raw/CONSR_CRD_RISK_CTRL_TBL2';
 
MSCK REPAIR TABLE dev_consumer_pcli_raw.consr_crd_risk_ctrl_tbl2;
 
show tables;
show create table cap_bi_marketing_temp.PROD_fact_tableau_ih_summ;
 
drop table cap_bi_marketing_temp.PROD_fact_tableau_ih_summ;


 
Deleting from path:
hadoop fs -rm -r maprfs:/datalake/cap/bi/marketing/temp/PROD_fact_tableau_ih_summ
-- Files size sum
hadoop fs -du -h <path> | awk '{s+=$1} END {print s}'


/opt/mapr/hive/hive-2.3/bin/beeline 
-u 'jdbc:hive2://edl-b01-services.dev.bigdata.ccc.net:10000/default;auth=maprsasl;saslQop=auth-conf;ssl=true;' 
-n aasconad 
-f /apps/src/developers/k078158/home/automation/ddl/CONSR_CRD_RISK_STRTG_PCLI_CNT_raw.hql 
--hivevar APP_STATE=dev

/opt/mapr/hive/hive-2.3/bin/beeline 
-u 'jdbc:hive2://edl-b01-services.dev.bigdata.ccc.net:10000/default;auth=maprsasl;saslQop=auth-conf;ssl=true;' 
-n aasconad 
-e 'DESCRIBE dev_ccr_shr_raw.CONSR_CRD_RISK_STRTG_PCLI_CNT' 
--hivevar APP_STATE=dev