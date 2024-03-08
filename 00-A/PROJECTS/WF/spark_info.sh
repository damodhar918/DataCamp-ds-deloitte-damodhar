
 
 
/opt/mapr/spark/spark-2.4.4/bin/spark-shell
 
 
[3:05 PM] B, Shruti
 
@WUVRA90A0897
 
[3:09 PM] B, Shrut
 
su - etlcapau
 
/opt/mapr/spark/spark-2.4.4/bin/spark-sql
/opt/mapr/spark/spark-2.4.8/bin/spark-sql
/opt/mapr/spark/spark-2.4.8/bin/pyspark
 
Spark-shell
 
spark.conf.set("spark.sql.session.timeZone", "MST")
spark.conf.set("spark.executor.cores", "4")
spark.conf.set("spark.executor.memory", "20G")
spark.conf.set("spark.executor.instances", "20")
spark.conf.set("spark.driver.memory", "10G")
spark.conf.set("spark.dynamicAllocation.enabled", "true")
spark.conf.set("spark.yarn.executor.memoryOverhead", "2048M")
spark.conf.set("spark.yarn.driver.memoryOverhead", "1024M")
spark.conf.set("spark.yarn.am.memory", "8g")
spark.conf.set("spark.yarn.am.cores", "4")
 
 
spark.sql("""SELECT COUNT(*) FROM(SELECT CAST(cis_customer_nr as decimal(15,0)) as ecn,min(date_sub(RECEIVED_DT, 29)) AS eff_dt,min(received_dt) as exp_dt ,COUNT(DISTINCT A.application_id) AS comp_cnt FROM uat_consumer_edacp_sanitized.eiw_s_acaps_cc_s1_dly_cc_appl A inner join uat_consumer_edacp_sanitized.eiw_s_acaps_cc_s1_dly_cc_icu_appl B on A.application_id = B.application_id where TRIM(A.SOR_ID) = 'C01' and TRIM(B.product_cd) = 'EC' and TRIM(A.ECPR_PD_ID) = 'PD00000125' and TRIM(A.CURR_ACT_STATUS_CD) ='BK' and received_dt >= date_sub(current_date,7) group by CAST(cis_customer_nr as decimal(15,0)))""").show(false)
 
spark.sql("""SELECT COUNT(*) FROM uat_consumer_edacp_sanitized.eiw_s_acaps_cc_s1_dly_cc_appl""").show()
spark.sql("""SELECT COUNT(*) FROM dev_consumer_edacp_sanitized.eiw_s_acaps_cc_s1_dly_cc_appl""").show()
 
Spark-sql
 
set spark.submit.deployMode=cluster;
set spark.executor.cores=4;
set spark.executor.memory=20G;
set spark.executor.instances=20;
set spark.driver.memory=8G;
set spark.driver.cores=4;
set spark.dynamicAllocation.enabled=true;
set spark.yarn.executor.memoryOverhead=2048M;
set spark.yarn.driver.memoryOverhead=1024M;
set spark.yarn.am.memory=8g;
set spark.yarn.am.cores=4;
set spark.sql.session.timeZone=MST
 
SELECT COUNT(*) FROM(SELECT CAST(cis_customer_nr as decimal(15,0)) as ecn,min(date_sub(RECEIVED_DT, 29)) AS eff_dt,min(received_dt) as exp_dt ,COUNT(DISTINCT A.application_id) AS comp_cnt FROM uat_consumer_edacp_sanitized.eiw_s_acaps_cc_s1_dly_cc_appl A inner join uat_consumer_edacp_sanitized.eiw_s_acaps_cc_s1_dly_cc_icu_appl B on A.application_id = B.application_id where TRIM(A.SOR_ID) = 'C01' and TRIM(B.product_cd) = 'EC' and TRIM(A.ECPR_PD_ID) = 'PD00000125' and TRIM(A.CURR_ACT_STATUS_CD) ='BK' and received_dt >= date_sub(current_date,7) group by CAST(cis_customer_nr as decimal(15,0)));