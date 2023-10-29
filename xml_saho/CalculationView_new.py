
#Python code for parsing of XML files 
# importing the required modules 
import csv 
import xml.etree.ElementTree as ET 
import xml.dom.minidom
import pandas as pd
import os
import shutil
from functools import reduce
from collections import OrderedDict
from datetime import datetime
import numpy as np
import warnings


def parseXML(path): 
  

    ID=[]
    TYPESRC=[]
    ATTRIBUTE_ID=[]
    ATTRIBUTE_ORDER=[]
    ATTRIBUTE_DEFAULTDESCRIPTION=[]
    ATTRIBUTE_COLUMNOBJECTNAME=[]
    ATTRIBUTE_COLUMNNAME=[]
    ATTRIBUTE_TYPE=[]
    ATTRIBUTE_OBJ_NM=[]
    ATTRIBUTE_COL_NM=[]
    ATTRIBUTE_DESC=[]
    ATTRIBUTE_DATATYPE=[]
    ATTRIBUTE_LENGTH=[]
    ATTRIBUTE_FORMULA=[]
    ATTRIBUTE_AGG_TYPE=[]
    FILE_NAME_DS=[]
    FILE_NAME_ATR=[]
    FILE_NAME_VR=[]
    FILE_NAME_LJ=[]
    LOC_VAR_ID=[]
    LOC_VAR_DESC=[]
    LOC_VAR_TYPE=[]
    LJ_OBJ_URI=[]
    LJ_ATTRIB_REF=[]
    LJ_ATTRIB_NM=[]
    LJ_CARD=[]
    LJ_JO=[]
    LJ_JT=[]
    LJ_ATTREIB_REF_ALIAS=[]
    SCHEMA_NAME=[]
    RESOURCE_URI=[]
    DESC=[]
    text_file=[]
    filenames=[]
    CALCULATION_VW_ID=[]
    FILE_NAME_CV=[]
    FILE_NAME_ST=[]
    SOURCE=[]
    TARGET=[]
    CV=[]
    countlv=0
    countlv1=0
    countlv2=0

    #dest="C:/Users/anirbdas/Documents/Parser"
    dest=path
   
    test=os.listdir(dest)
    #print(test)
    for item in test:
        
        if item.endswith(".calculationview"):
            os.remove(os.path.join(dest,item))

    #text_file = open("C:/Users/anirbdas/Documents/Parser/UserInput.txt")
    text_file = open(path+"/Input/CalculationView_UserInput.txt")
    
    
    line_list = text_file.readlines();

    for line in line_list:

        stripped_line=line.strip()
        #print(stripped_line)
        
        shutil.copy(stripped_line,dest+'/Code')
    #print(os.listdir(path))     
    for filename in os.listdir(path+'/Code'):
       
        
       if filename.endswith('.calculationview') :
           filenames.append(filename)
           
           #print(filenames)

    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    df3 = pd.DataFrame()
    df4 = pd.DataFrame()
    df5 = pd.DataFrame()
    df6 = pd.DataFrame(columns=['FILE_NAME','CV','SOURCE','TARGET'])
    df7 = pd.DataFrame()
    df8 = pd.DataFrame()
    df9 = pd.DataFrame()
    df10 = pd.DataFrame()
    df11 = pd.DataFrame()
    df12 = pd.DataFrame()
    df13 = pd.DataFrame()
    df14 = pd.DataFrame()
    df_comb = pd.DataFrame()
    df_merged = pd.DataFrame()
    df_merged_dummy= pd.DataFrame()
    df_unnesting=pd.DataFrame()
    df_merged_final= pd.DataFrame()
    df_merged_final1= pd.DataFrame()
    final_df= pd.DataFrame()
    df_merged_id=pd.DataFrame()
    df_merged_final1_lsv=pd.DataFrame()
    df_merged_final_lsv=pd.DataFrame()
    dfcount1=pd.DataFrame()
    dfcount_dummy3=pd.DataFrame()
    df_merged2a = pd.DataFrame()
    df_merged2 = pd.DataFrame()
    df_merged_rank_final= pd.DataFrame()

    
    for filename in filenames:
       #print("processing file=>", filename)
       
       doc = xml.dom.minidom.parse(filename)
       
       #print (doc.nodeName)
       #print (doc.firstChild.tagName)

       tree1 = ET.parse(filename)
       root1 = tree1.getroot()         
    
      
       #DataSource = doc.getElementsByTagName("DataSource")
       #ColumnObject = doc.getElementsByTagName("columnObject")
       #ResourceUri = doc.getElementsByTagName("resourceUri")
       #print ("%d DataSource:" % DataSource.length)
       
       List3=[]
       
       node_list=doc.getElementsByTagName("DataSource")
       
       for n3 in node_list:
         str121=""
         List3.append(str121.join(n3.getAttribute('id')))
       
         
         
       
       TYPEDS=[]
       SCHEMA_NAME=[]
       RESOURCE_URI=[]
       ID_DS=[]
       FILE_NAME_DS=[]
       ITEMS_100=OrderedDict()
       ITEMS_200=OrderedDict()
       ITEMS_300=OrderedDict()
       ITEMS_400=OrderedDict()
       ITEMS_110=OrderedDict()
       
       count3=0
       
       for data1 in List3:
          #if "Join" in data1: 
                #print(data1)
                 count3=count3+1
                 
                 
                 for  data5 in root1.iterfind(".//DataSource[@id='{}']".format(data1)):
                     ITEMS_6=OrderedDict()
                     ITEMS_7=OrderedDict()
                     FILE_NAME_DS.append(filename)
                     ID_DS1=[]
                     str2=""
                     ID_DS1.append(data5.get("id"))

                     str4=""
                     ITEMS_100[str4.join(ID_DS1)]=filename

                     for data9 in root1.iterfind(".//DataSource[@id='{}']".format(data1)):
                       FILE_NAME_DS.append(filename)
                       TYPE_DS1=[]
                       str3=""
                       
                       TYPE_DS1.append(data9.get("type"))
                       
                           
                     ITEMS_110[str3.join(ID_DS1)]=TYPE_DS1
                     #print(ITEMS_110)

                     for data11 in root1.iterfind(".//DataSource[@id='{}']/".format(data1)):
                         FILE_NAME_DS.append(filename)
                         SCHEMA_NAME1=[]
                         str4=""
                         if (data11.get("schemaName")) is not None:
                            SCHEMA_NAME1.append(data11.get("schemaName"))
                         else:
                            SCHEMA_NAME1.append("-")
                     str4=""
                     str16=""
                     ITEMS_200[str4.join(ID_DS1)]=SCHEMA_NAME1
                     #print(ITEMS_200)
                     

                     for data12 in root1.iterfind(".//DataSource[@id='{}']".format(data1)):
                           FILE_NAME_DS.append(filename)
                           RESOURCE_URI1=[]
                           str5=""
                           if (data12.find('resourceUri')) is not None:
                                RESOURCE_URI1.append(data12.find('resourceUri').text)
                           #elif (data12.get("value")) is not None:
                                #FILTER1.append(data12.get("value")) 
                           else:
                                RESOURCE_URI1.append("-")
                     ITEMS_300[str4.join(ID_DS1)]= RESOURCE_URI1
                    
                     for data14 in root1.iterfind(".//DataSource[@id='{}']/".format(data1)):
                         FILE_NAME_DS.append(filename)
                         CLMN_OBJ_NAME=[]
                         str7=""
                         if (data14.get("columnObjectName")) is not None:
                            CLMN_OBJ_NAME.append(data14.get("columnObjectName"))
                            
                         else:
                             CLMN_OBJ_NAME.append("-")
                                                          
                            
                     str7=""
                     
                     ITEMS_400[str7.join(ID_DS1)]=CLMN_OBJ_NAME
                     #print(ITEMS_400)

    
      #Attribute Details

       ListAtr=[]
       
       node_list_atr=doc.getElementsByTagName("attribute")
       
       for n3 in node_list_atr:
         stratr=""
         ListAtr.append(stratr.join(n3.getAttribute('id')))
       
                              
       ID_ATR=[]
       FILE_NAME_ATR=[]
       ITEMS_ATR=OrderedDict()
       ITEMS_ATR1=OrderedDict()
       ITEMS_ATR2=OrderedDict()
       ITEMS_ATR3=OrderedDict()
       ITEMS_ATR4=OrderedDict()
       ITEMS_ATR5=OrderedDict()
       ITEMS_ATR6=OrderedDict()
       ITEMS_ATR7=OrderedDict()
       ITEMS_ATR8=OrderedDict()
       ITEMS_ATR9=OrderedDict()
       ITEMS_ATR10=OrderedDict()
       ITEMS_ATR11=OrderedDict()
       ITEMS_ATR12=OrderedDict()
       ITEMS_ATR13=OrderedDict()
       
       countatr=0
       for data1 in ListAtr:
          #if "Join" in data1: 
                #print(data1)
                 countatr=countatr+1
                 

                 for  data5 in root1.iterfind(".//attribute[@id='{}']".format(data1)):
                     
                     FILE_NAME_ATR.append(filename)
                     ID_ATR=[]
                     ID_ATR.append(data5.get("id"))
                     stratr=""
                     ITEMS_ATR[stratr.join(ID_ATR)]=filename

                     for data9 in root1.iterfind(".//attribute[@id='{}']".format(data1)):
                       FILE_NAME_ATR.append(filename)
                       ATTRIBUTE_ORDER=[]
                       ATTRIBUTE_BASE_MASURE_ATR=[]
                       LOGICAL_OPERATOR_ATR=[]
                       FILTER_ATTRIBUTE_NAME_ATR=[]
                       SINGLE_VALUE_FILTER_ATR=[]
                       stratr3=""
                       stratr12=""
                       stratr13=""
                       stratr14=""
                       stratr15=""

                       ATTRIBUTE_ORDER.append(data9.get('order'))
                       ATTRIBUTE_BASE_MASURE_ATR.append("-")
                       LOGICAL_OPERATOR_ATR.append("-")
                       FILTER_ATTRIBUTE_NAME_ATR.append("-")
                       SINGLE_VALUE_FILTER_ATR.append("-")

                     ITEMS_ATR1[stratr3.join(ID_ATR)]=ATTRIBUTE_ORDER
                     ITEMS_ATR10[stratr12.join(ID_ATR)]=ATTRIBUTE_BASE_MASURE_ATR
                     ITEMS_ATR11[stratr13.join(ID_ATR)]=LOGICAL_OPERATOR_ATR
                     ITEMS_ATR12[stratr14.join(ID_ATR)]=FILTER_ATTRIBUTE_NAME_ATR
                     ITEMS_ATR13[stratr15.join(ID_ATR)]=SINGLE_VALUE_FILTER_ATR

                     for data11 in root1.iterfind(".//attribute[@id='{}']/descriptions".format(data1)):
                         FILE_NAME_ATR.append(filename)
                         ATTRIBUTE_DESC=[]
                         
                         stratr4=""
                         
                         ATTRIBUTE_DESC.append(data11.get('defaultDescription'))
                         
                            
                     stratr4=""
                     
                     ITEMS_ATR2[stratr4.join(ID_ATR)]=ATTRIBUTE_DESC

                     for data11 in root1.iterfind(".//attribute[@id='{}']/keyMapping".format(data1)):
                         FILE_NAME_ATR.append(filename)
                         ATTRIBUTE_OBJ_NAME=[]
                         ATTRIBUTE_COL_NAME=[]
                         ATTRIBUTE_TYPE=[]
                         ATTRIBUTE_DATATYPE=[]
                         ATTRIBUTE_LENGTH=[]
                         ATTRIBUTE_FORMULA=[]
                         ATTRIBUTE_AGG_TYPE=[]

                         ATTRIBUTE_OBJ_NAME.append(data11.get('columnObjectName'))
                         ATTRIBUTE_COL_NAME.append(data11.get('columnName'))
                         ATTRIBUTE_TYPE.append("DIRECT")
                         ATTRIBUTE_DATATYPE.append("-")
                         ATTRIBUTE_LENGTH.append("-")
                         ATTRIBUTE_FORMULA.append("-")
                         ATTRIBUTE_AGG_TYPE.append("-")
                     stratr5=""
                     stratr6=""
                     stratr7=""
                     stratr8=""
                     stratr9=""
                     stratr10=""
                     stratr11=""
                     
                     ITEMS_ATR3[stratr5.join(ID_ATR)]=ATTRIBUTE_OBJ_NAME
                     ITEMS_ATR4[stratr6.join(ID_ATR)]=ATTRIBUTE_COL_NAME
                     ITEMS_ATR5[stratr7.join(ID_ATR)]=ATTRIBUTE_TYPE
                     ITEMS_ATR6[stratr8.join(ID_ATR)]=ATTRIBUTE_DATATYPE
                     ITEMS_ATR7[stratr9.join(ID_ATR)]=ATTRIBUTE_LENGTH
                     ITEMS_ATR8[stratr10.join(ID_ATR)]=ATTRIBUTE_FORMULA
                     ITEMS_ATR9[stratr11.join(ID_ATR)]=ATTRIBUTE_AGG_TYPE
 
       #Calculated Attribute Details
                     
       ListCa=[]
       
       node_list_ca=doc.getElementsByTagName("calculatedAttribute")
       
       for n3 in node_list_ca:
         strca=""
         ListCa.append(strca.join(n3.getAttribute('id')))
       
                              
       ID_CA=[]
       FILE_NAME_CA=[]
       ITEMS_CA=OrderedDict()
       ITEMS_CA1=OrderedDict()
       ITEMS_CA2=OrderedDict()
       ITEMS_CA3=OrderedDict()
       ITEMS_CA4=OrderedDict()
       ITEMS_CA5=OrderedDict()
       ITEMS_CA6=OrderedDict()
       ITEMS_CA7=OrderedDict()
       ITEMS_CA8=OrderedDict()
       ITEMS_CA9=OrderedDict()
       ITEMS_CA10=OrderedDict()
       ITEMS_CA11=OrderedDict()
       ITEMS_CA12=OrderedDict()
       ITEMS_CA13=OrderedDict()
       
       countca=0
       for data1 in ListCa:
          #if "Join" in data1: 
                #print(data1)
                 countca=countca+1
                 

                 for  data5 in root1.iterfind(".//calculatedAttribute[@id='{}']".format(data1)):
                     
                     FILE_NAME_CA.append(filename)
                     ID_CA=[]
                     ID_CA.append(data5.get("id"))
                     strca=""
                     ITEMS_CA[strca.join(ID_CA)]=filename

                     for data9 in root1.iterfind(".//calculatedAttribute[@id='{}']".format(data1)):
                       FILE_NAME_CA.append(filename)
                       ATTRIBUTE_ORDER_CA=[]
                       ATTRIBUTE_BASE_MEASURE_CA=[]
                       LOGICAL_OPERATOR_CA=[]
                       FILTER_ATTRIBUTE_NAME_CA=[]
                       SINGLE_VALUE_FILTER_CA=[]
                       strca3=""
                       strca12=""
                       strca13=""
                       strca14=""
                       strca15=""

                       ATTRIBUTE_ORDER_CA.append(data9.get('order'))
                       ATTRIBUTE_BASE_MEASURE_CA.append("-")
                       LOGICAL_OPERATOR_CA.append("-")
                       FILTER_ATTRIBUTE_NAME_CA.append("-")
                       SINGLE_VALUE_FILTER_CA.append("-")
                       
                     ITEMS_CA1[strca3.join(ID_CA)]=ATTRIBUTE_ORDER_CA
                     ITEMS_CA10[strca12.join(ID_CA)]=ATTRIBUTE_BASE_MEASURE_CA
                     ITEMS_CA11[strca13.join(ID_CA)]=LOGICAL_OPERATOR_CA
                     ITEMS_CA12[strca14.join(ID_CA)]=FILTER_ATTRIBUTE_NAME_CA
                     ITEMS_CA13[strca15.join(ID_CA)]=SINGLE_VALUE_FILTER_CA

                     for data11 in root1.iterfind(".//calculatedAttribute[@id='{}']/descriptions".format(data1)):
                         FILE_NAME_CA.append(filename)
                         ATTRIBUTE_DESC_CA=[]
                         
                         strca4=""
                         
                         ATTRIBUTE_DESC_CA.append(data11.get('defaultDescription'))
                         
                            
                     strca4=""
                     
                     ITEMS_CA2[strca4.join(ID_CA)]=ATTRIBUTE_DESC_CA

                     for data11 in root1.iterfind(".//calculatedAttribute[@id='{}']/keyCalculation".format(data1)):
                         FILE_NAME_CA.append(filename)
                         ATTRIBUTE_OBJ_NAME_CA=[]
                         ATTRIBUTE_COL_NAME_CA=[]
                         ATTRIBUTE_TYPE_CA=[]
                         ATTRIBUTE_DATATYPE_CA=[]
                         ATTRIBUTE_LENGTH_CA=[]
                         ATTRIBUTE_FORMULA_CA=[]
                         ATTRIBUTE_AGG_TYPE_CA=[]

                         ATTRIBUTE_OBJ_NAME_CA.append("-")
                         ATTRIBUTE_COL_NAME_CA.append("-")
                         ATTRIBUTE_TYPE_CA.append("CALCULATED")
                         ATTRIBUTE_DATATYPE_CA.append(data11.get('datatype'))
                         ATTRIBUTE_LENGTH_CA.append(data11.get('length'))
                         ATTRIBUTE_FORMULA_CA.append(data11.find('formula').text)
                         ATTRIBUTE_AGG_TYPE_CA.append("-")
                                              
                     strca5=""
                     strca6=""
                     strca7=""
                     strca8=""
                     strca9=""
                     strca10=""
                     strca11=""
                     
                     ITEMS_CA3[strca5.join(ID_CA)]=ATTRIBUTE_OBJ_NAME_CA
                     ITEMS_CA4[strca6.join(ID_CA)]=ATTRIBUTE_COL_NAME_CA
                     ITEMS_CA5[strca7.join(ID_CA)]=ATTRIBUTE_TYPE_CA
                     ITEMS_CA6[strca8.join(ID_CA)]=ATTRIBUTE_DATATYPE_CA
                     ITEMS_CA7[strca9.join(ID_CA)]=ATTRIBUTE_LENGTH_CA
                     ITEMS_CA8[strca10.join(ID_CA)]=ATTRIBUTE_FORMULA_CA                
                     ITEMS_CA9[strca11.join(ID_CA)]=ATTRIBUTE_AGG_TYPE_CA
      #Measure Details
                     
       ListMsr=[]
       
       node_list_msr=doc.getElementsByTagName("measure")
       
       for n3 in node_list_msr:
         strmsr=""
         ListMsr.append(strmsr.join(n3.getAttribute('id')))
       
                              
       ID_MSR=[]
       FILE_NAME_MSR=[]
       ITEMS_MSR=OrderedDict()
       ITEMS_MSR1=OrderedDict()
       ITEMS_MSR2=OrderedDict()
       ITEMS_MSR3=OrderedDict()
       ITEMS_MSR4=OrderedDict()
       ITEMS_MSR5=OrderedDict()
       ITEMS_MSR6=OrderedDict()
       ITEMS_MSR7=OrderedDict()
       ITEMS_MSR8=OrderedDict()
       ITEMS_MSR9=OrderedDict()
       ITEMS_MSR10=OrderedDict()
       ITEMS_MSR11=OrderedDict()
       ITEMS_MSR12=OrderedDict()
       ITEMS_MSR13=OrderedDict()
       
       countmsr=0
       for data1 in ListMsr:
          #if "Join" in data1: 
                #print(data1)
                 countmsr=countmsr+1
                 

                 for  data5 in root1.iterfind(".//measure[@id='{}']".format(data1)):
                     
                     FILE_NAME_MSR.append(filename)
                     ID_MSR=[]
                     if data5.get('baseMeasure') is None:
                       ID_MSR.append(data5.get("id"))
                       strmsr=""
                       ITEMS_MSR[strmsr.join(ID_MSR)]=filename

                     for data9 in root1.iterfind(".//measure[@id='{}']".format(data1)):
                       FILE_NAME_MSR.append(filename)
                       ATTRIBUTE_ORDER_MSR=[]
                       ATTRIBUTE_AGG_TYPE_MSR=[]
                       ATTRIBUTE_BASE_MEASURE_MSR=[]
                       LOGICAL_OPERATOR_MSR=[]
                       FILTER_ATR_NAME_MSR=[]
                       SINGLE_VALUE_FILTER_MSR=[]
                       strmsr3=""
                       strmsr11=""
                       strmsr12=""
                       strmsr13=""
                       strmsr14=""
                       strmsr15=""

                       ATTRIBUTE_ORDER_MSR.append(data9.get('order'))
                       ATTRIBUTE_AGG_TYPE_MSR.append(data9.get('aggregationType'))
                       ATTRIBUTE_BASE_MEASURE_MSR.append("-")
                       LOGICAL_OPERATOR_MSR.append("-")
                       FILTER_ATR_NAME_MSR.append("-")
                       SINGLE_VALUE_FILTER_MSR.append("-")

                     ITEMS_MSR1[strmsr3.join(ID_MSR)]=ATTRIBUTE_ORDER_MSR
                     ITEMS_MSR9[strmsr11.join(ID_MSR)]=ATTRIBUTE_AGG_TYPE_MSR
                     ITEMS_MSR10[strmsr12.join(ID_MSR)]=ATTRIBUTE_BASE_MEASURE_MSR
                     ITEMS_MSR11[strmsr13.join(ID_MSR)]=LOGICAL_OPERATOR_MSR
                     ITEMS_MSR12[strmsr14.join(ID_MSR)]=FILTER_ATR_NAME_MSR
                     ITEMS_MSR13[strmsr15.join(ID_MSR)]=SINGLE_VALUE_FILTER_MSR
                     
                     for data11 in root1.iterfind(".//measure[@id='{}']/descriptions".format(data1)):
                         FILE_NAME_MSR.append(filename)
                         ATTRIBUTE_DESC_MSR=[]
                         ATTRIBUTE_TYPE_MSR=[]
                         
                         strmsr4=""
                         
                         ATTRIBUTE_DESC_MSR.append(data11.get('defaultDescription'))
                         ATTRIBUTE_TYPE_MSR.append("MEASURE")
                            
                     strmsr4=""
                     strmsr7=""
                     
                     ITEMS_MSR2[strmsr4.join(ID_MSR)]=ATTRIBUTE_DESC_MSR
                     ITEMS_MSR5[strmsr7.join(ID_MSR)]=ATTRIBUTE_TYPE_MSR
                     
                     for data11 in root1.iterfind(".//measure[@id='{}']".format(data1)):
                         FILE_NAME_MSR.append(filename)
                         
                         ATTRIBUTE_FORMULA_MSR=[]
                         strmsr10=""
                         if (data11.find('formula')) is not None:
                         
                           ATTRIBUTE_FORMULA_MSR.append(data11.find('formula').text)
                         else :
                           ATTRIBUTE_FORMULA_MSR.append("-")  
                         
                            
                     strmsr10=""
                     
                     ITEMS_MSR8[strmsr10.join(ID_MSR)]=ATTRIBUTE_FORMULA_MSR

                     
                     countm=0
                     for data11 in root1.iterfind(".//measure[@id='{}']/measureMapping".format(data1)):
                         countm=countm+1
                         FILE_NAME_MSR.append(filename)
                         ATTRIBUTE_OBJ_NAME_MSR=[]
                         ATTRIBUTE_COL_NAME_MSR=[]
                         
                         ATTRIBUTE_DATATYPE_MSR=[]
                         ATTRIBUTE_LENGTH_MSR=[]
                         
                         if data11.get('columnObjectName') is not None:

                           ATTRIBUTE_OBJ_NAME_MSR.append(data11.get('columnObjectName'))
                         else:
                           ATTRIBUTE_OBJ_NAME_MSR.append("-")

                         if data11.get('columnName') is not None: 
                           ATTRIBUTE_COL_NAME_MSR.append(data11.get('columnName'))
                         else:
                           ATTRIBUTE_COL_NAME_MSR.append("-")
                           
                         
                         ATTRIBUTE_DATATYPE_MSR.append("-")
                         ATTRIBUTE_LENGTH_MSR.append("-")
                         
                         
                                              
                     strmsr5=""
                     strmsr6=""
                     
                     strmsr8=""
                     strmsr9=""
                     
                     if countm>0:
                     
                      ITEMS_MSR3[strmsr5.join(ID_MSR)]=ATTRIBUTE_OBJ_NAME_MSR
                      ITEMS_MSR4[strmsr6.join(ID_MSR)]=ATTRIBUTE_COL_NAME_MSR
                      
                      ITEMS_MSR6[strmsr8.join(ID_MSR)]=ATTRIBUTE_DATATYPE_MSR
                      ITEMS_MSR7[strmsr9.join(ID_MSR)]=ATTRIBUTE_LENGTH_MSR
                                     
       
       #Restricted Measure Details
                     
       ListRmsr=[]
       
       node_list_rmsr=root1.iterfind(".//restrictedMeasures/measure")
       
       for n3 in node_list_rmsr:
         strrmsr=""
         ListRmsr.append(strrmsr.join(n3.get('id')))
       
                              
       ID_RMSR=[]
       FILE_NAME_RMSR=[]
       ITEMS_RMSR=OrderedDict()
       ITEMS_RMSR1=OrderedDict()
       ITEMS_RMSR2=OrderedDict()
       ITEMS_RMSR3=OrderedDict()
       ITEMS_RMSR4=OrderedDict()
       ITEMS_RMSR5=OrderedDict()
       ITEMS_RMSR6=OrderedDict()
       ITEMS_RMSR7=OrderedDict()
       ITEMS_RMSR8=OrderedDict()
       ITEMS_RMSR9=OrderedDict()
       ITEMS_RMSR10=OrderedDict()
       ITEMS_RMSR11=OrderedDict()
       ITEMS_RMSR12=OrderedDict()
       ITEMS_RMSR13=OrderedDict()
       
       countrmsr=0
       for data1 in ListRmsr:
          #if "Join" in data1: 
                #print(data1)
                 countrmsr=countrmsr+1
                 LOGICAL_OPERATOR=[]
                 FILTER_ATTRIBUTE_NAME=[]
                 SINGLE_VALUE_FILTER=[]
                 ATTRIBUTE_OBJ_NAME_RMSR=[]
                 ATTRIBUTE_COL_NAME_RMSR=[]
                 ATTRIBUTE_TYPE_RMSR=[]
                 ATTRIBUTE_DATATYPE_RMSR=[]
                 ATTRIBUTE_LENGTH_RMSR=[]
                 ATTRIBUTE_FORMULA_RMSR=[]

                 
                 for  data5 in root1.iterfind(".//measure[@id='{}']".format(data1)):
                     
                     FILE_NAME_RMSR.append(filename)
                     ID_RMSR=[]
                     
                     ID_RMSR.append(data5.get("id"))
                     strrmsr=""
                     ITEMS_RMSR[strrmsr.join(ID_RMSR)]=filename

                     for data9 in root1.iterfind(".//measure[@id='{}']".format(data1)):
                       FILE_NAME_RMSR.append(filename)
                       ATTRIBUTE_ORDER_RMSR=[]
                       ATTRIBUTE_AGG_TYPE_RMSR=[]
                       strrmsr3=""
                       strrmsr11=""
                       strrmsr7=""
                       
                       ATTRIBUTE_ORDER_RMSR.append(data9.get('order'))
                       ATTRIBUTE_AGG_TYPE_RMSR.append("-")
                       ATTRIBUTE_TYPE_RMSR.append("RESTRICTED_MEASURE")
                           
                     ITEMS_RMSR1[strrmsr3.join(ID_RMSR)]=ATTRIBUTE_ORDER_RMSR
                     ITEMS_RMSR9[strrmsr11.join(ID_RMSR)]=ATTRIBUTE_AGG_TYPE_RMSR
                     ITEMS_RMSR5[strrmsr7.join(ID_RMSR)]=ATTRIBUTE_TYPE_RMSR

                     for data11 in root1.iterfind(".//measure[@id='{}']/descriptions".format(data1)):
                         FILE_NAME_RMSR.append(filename)
                         ATTRIBUTE_DESC_RMSR=[]
                         
                         strrmsr4=""
                         
                         ATTRIBUTE_DESC_RMSR.append(data11.get('defaultDescription'))
                         
                            
                     strrmsr4=""
                     
                     ITEMS_RMSR2[strrmsr4.join(ID_RMSR)]=ATTRIBUTE_DESC_RMSR

                     for data11 in root1.iterfind(".//measure[@id='{}']".format(data1)):
                         FILE_NAME_RMSR.append(filename)
                         
                         ATTRIBUTE_BASE_MEASURE=[]
                         strrmsr12=""
                         
                         
                         ATTRIBUTE_BASE_MEASURE.append(data11.get('baseMeasure'))
                         
                          
                         
                            
                     strrmsr12=""
                     
                     ITEMS_RMSR10[strrmsr12.join(ID_RMSR)]=ATTRIBUTE_BASE_MEASURE

                     
                     for data11 in root1.iterfind(".//measure[@id='{}']/restriction".format(data1)):
                         FILE_NAME_RMSR.append(filename)
                         
                         
                         strrmsr13=""
                         
                         
                         LOGICAL_OPERATOR.append(data11.get('logicalOperator'))
                         
                          
                         
                            
                     strrmsr13=""
                     
                     ITEMS_RMSR11[strrmsr13.join(ID_RMSR)]=LOGICAL_OPERATOR

                     for data11 in root1.iterfind(".//measure[@id='{}']/restriction/filter".format(data1)):
                         FILE_NAME_RMSR.append(filename)
                         
                         
                         strrmsr14=""
                         
                         
                         FILTER_ATTRIBUTE_NAME.append(data11.get('attributeName'))
                         
                          
                         
                            
                     strrmsr14=""
                     
                     ITEMS_RMSR12[strrmsr14.join(ID_RMSR)]=FILTER_ATTRIBUTE_NAME


                     for data11 in root1.iterfind(".//measure[@id='{}']/restriction/filter/valueFilter".format(data1)):
                         FILE_NAME_RMSR.append(filename)
                         
                                                  
                         SINGLE_VALUE_FILTER.append(data11.get('value'))
                         ATTRIBUTE_OBJ_NAME_RMSR.append("-")
                         ATTRIBUTE_COL_NAME_RMSR.append("-")
                         
                         ATTRIBUTE_DATATYPE_RMSR.append("-")
                         ATTRIBUTE_LENGTH_RMSR.append("-")
                         ATTRIBUTE_FORMULA_RMSR.append("-")
                                              
                     strrmsr5=""
                     strrmsr6=""
                     
                     strrmsr8=""
                     strrmsr9=""
                     strrmsr10=""
                     strrmsr15=""
                     
                     ITEMS_RMSR3[strrmsr5.join(ID_RMSR)]=ATTRIBUTE_OBJ_NAME_RMSR
                     ITEMS_RMSR4[strrmsr6.join(ID_RMSR)]=ATTRIBUTE_COL_NAME_RMSR
                     
                     ITEMS_RMSR6[strrmsr8.join(ID_RMSR)]=ATTRIBUTE_DATATYPE_RMSR
                     ITEMS_RMSR7[strrmsr9.join(ID_RMSR)]=ATTRIBUTE_LENGTH_RMSR
                     ITEMS_RMSR8[strrmsr10.join(ID_RMSR)]=ATTRIBUTE_FORMULA_RMSR
                     ITEMS_RMSR13[strrmsr15.join(ID_RMSR)]=SINGLE_VALUE_FILTER

      #Local Variables Details

       Listlv=[]
       
       node_list_lv=doc.getElementsByTagName("variable")
       
       for n3 in node_list_lv:
         strlv=""
         Listlv.append(strlv.join(n3.getAttribute('id')))
       
                              
       ID_LV=[]
       FILE_NAME_LV=[]
       ITEMS_LV=OrderedDict()
       ITEMS_LV1=OrderedDict()
       ITEMS_LV2=OrderedDict()
       ITEMS_LV3=OrderedDict()
       
       countlv=0
       for data1 in Listlv:
          #if "Join" in data1: 
                #print(data1)
                 countlv=countlv+1
                 

                 for  data5 in root1.iterfind(".//variable[@id='{}']".format(data1)):
                     
                     FILE_NAME_LV.append(filename)
                     ID_LV=[]
                     ID_LV.append(data5.get("id"))
                     strlv=""
                     ITEMS_LV[strlv.join(ID_LV)]=filename

                     for data9 in root1.iterfind(".//localVariables/variable[@id='{}']/descriptions".format(data1)):
                       FILE_NAME_LV.append(filename)
                       LOC_VAR_DESC=[]
                       strlv3=""
                       
                       LOC_VAR_DESC.append(data9.get('defaultDescription'))
                       
                           
                     ITEMS_LV1[strlv3.join(ID_LV)]=LOC_VAR_DESC
                     

                     for data11 in root1.iterfind(".//localVariables/variable[@id='{}']/variableProperties".format(data1)):
                         FILE_NAME_LV.append(filename)
                         LOC_VAR_TYPE=[]
                         LOC_VAR_DFLT_VAL=[]
                         strlv4=""
                         
                         LOC_VAR_TYPE.append(data11.get('datatype'))
                         LOC_VAR_DFLT_VAL.append(data11.get('defaultValue'))
                            
                     strlv4=""
                     strlv5=""
                     ITEMS_LV2[strlv4.join(ID_LV)]=LOC_VAR_TYPE
                     ITEMS_LV3[strlv5.join(ID_LV)]=LOC_VAR_DFLT_VAL
             
       #sharedDimensions Details

       Listsd=[]
       
       node_list_sd=doc.getElementsByTagName("logicalJoin")
       
       for n3 in node_list_sd:
         strsd=""
         Listsd.append(strsd.join(n3.getAttribute('associatedObjectUri')))
       
                              
       ID_SD=[]
       FILE_NAME_SD=[]
       ITEMS_SD=OrderedDict()
       ITEMS_SD1=OrderedDict()
       ITEMS_SD2=OrderedDict()
       ITEMS_SD3=OrderedDict()
       ITEMS_SD4=OrderedDict()
       ITEMS_SD5=OrderedDict()
       ITEMS_SD6=OrderedDict()
       ITEMS_SD7=OrderedDict()

       countsd=0
       for data1 in Listsd:
          #if "Join" in data1: 
                #print(data1)
                 countsd=countsd+1
                 
                 SD_ATTRIB_CARDINALITY=[]
                 SD_ATTRIB_JO=[]
                 SD_ATTRIB_JT=[]
                 
                 SD_ATTRIB_REF=[]
                 SD_ATTRIB_REF_ALIAS=[]
                 SD_ATTRIB_REF_ATTR_NAME=[]
                 
                 for  data5 in root1.iterfind(".//logicalJoin[@associatedObjectUri='{}']".format(data1)):
                     
                     FILE_NAME_SD.append(filename)
                     SD_ATTRIB_NAME=[]
                     ID_SD=[]
                     ID_SD.append(data5.get("associatedObjectUri"))
                     strsd=""
                     ITEMS_SD[strsd.join(ID_SD)]=filename

                     for data9 in root1.findall(".//logicalJoin[@associatedObjectUri='{}']/attributes/attributeRef".format(data1)):
                       FILE_NAME_SD.append(filename)
                       
                       
                       strsd3=""
                       
                       SD_ATTRIB_REF.append(data9.text)
                       
                     strsd3=""      
                     ITEMS_SD1[strsd3.join(ID_SD)]=SD_ATTRIB_REF
                     

                     for data11 in root1.iterfind(".//logicalJoin[@associatedObjectUri='{}']/associatedAttributeNames/attributeName".format(data1)):
                         FILE_NAME_SD.append(filename)
                         
                         strsd4=""
                         
                         SD_ATTRIB_NAME.append(data11.text)
                         
                            
                     strsd4=""
                     
                     ITEMS_SD2[strsd4.join(ID_SD)]=SD_ATTRIB_NAME
                                             
                            
                     for data11 in root1.iterfind(".//logicalJoin[@associatedObjectUri='{}']/properties".format(data1)):
                         FILE_NAME_SD.append(filename)
                         
                         strsd5=""
                         strsd6=""
                         strsd7=""
                         
                         SD_ATTRIB_CARDINALITY.append(data11.get('cardinality'))
                         SD_ATTRIB_JO.append(data11.get('joinOperator'))
                         SD_ATTRIB_JT.append(data11.get('joinType'))
                            
                     strsd5=""
                     strsd6=""
                     strsd7=""
                     
                     ITEMS_SD3[strsd5.join(ID_SD)]=SD_ATTRIB_CARDINALITY
                     ITEMS_SD4[strsd6.join(ID_SD)]=SD_ATTRIB_JO
                     ITEMS_SD5[strsd7.join(ID_SD)]=SD_ATTRIB_JT

                     for data11 in root1.iterfind(".//logicalJoin[@associatedObjectUri='{}']/associatedAttributeFeatures/attributeReference".format(data1)):
                         FILE_NAME_SD.append(filename)
                         
                         strsd8=""
                         
                         SD_ATTRIB_REF_ALIAS.append(data11.get('alias'))
                         
                            
                     strsd8=""
                     
                     ITEMS_SD6[strsd8.join(ID_SD)]=SD_ATTRIB_REF_ALIAS

                     for data11 in root1.iterfind(".//logicalJoin[@associatedObjectUri='{}']/associatedAttributeFeatures/attributeReference".format(data1)):
                         FILE_NAME_SD.append(filename)
                         
                         strsd9=""
                         
                         SD_ATTRIB_REF_ALIAS.append(data11.get('attributeName'))
                         
                            
                     strsd9=""
                     
                     ITEMS_SD7[strsd9.join(ID_SD)]=SD_ATTRIB_REF_ATTR_NAME

       #This block of code is commented out as it is producing a redundant worksheet.Projection information is already captured in Logical_Seq_View Worksheet#
       #CALCULATION_VIEW-PROJECTION
       calculationView = doc.getElementsByTagName("calculationView")
       mapping = doc.getElementsByTagName("mapping")
       level={'Projection_1','Projection_2','Projection_3','Projection_4','Projection_5','Projection_6','Projection_7','Projection_8','Projection_9','Projection_10','Projection_11','Projection_12','Projection_13','Projection_14','Projection_15','Projection_16','Projection_17','Projection_18','Projection_19','Projection_20'}
       #print (level)

       TYPE=[]
       ST=[]
       FLR=[]
       JOIN_CD=[]
       JOIN_TYPE=[]
       FILE_NAME_CV=[]
       List2=[]
       countproj=0
       for n2 in calculationView:
         str21=""
         List2.append(str21.join(n2.getAttribute('id')))
       for data1 in List2:
          if "Join" not in data1:
            countproj=countproj+1  
           #print(data1)

            for  data7 in root1.iterfind(".//calculationView[@id='{}']".format(data1)):
                FILE_NAME_CV.append(filename)
                FILTER=[]
                str3=""
                if data7.find('filter') is not None:
                  FILTER.append(data7.find('filter').text)
                else:
                  FILTER.append("Filters Not Available")
                
           
                for  data5 in root1.iterfind(".//calculationView[@id='{}']/input".format(data1)):
                       FILE_NAME_CV.append(filename)
                       SOURCE_TABLE=[]
                       str20=""
                       SOURCE_TABLE.append(data5.get("node"))   
          
                       for  data3 in root1.iterfind(".//calculationView[@id='{}']".format(data1)):
                          #print (data3)
                          FILE_NAME_CV.append(filename)
                          CALCULATION_VW_ID=[]
                          str1=""
                          CALCULATION_VW_ID.append(data3.get("id"))
                          #print(CALCULATION_VW_ID)
             #SOURCE.append("-")
             #TARGET.append("-")                                 
                    
                 
                          for data2 in root1.iterfind(".//calculationView[@id='{}']/input/mapping".format(data1)):
                    
                    
                             FILE_NAME_CV.append(filename)
                             TYPE.append(str1.join(CALCULATION_VW_ID))
                             ST.append(str20.join(SOURCE_TABLE))
                             FLR.append(str3.join(FILTER))
                             JOIN_CD.append("-")
                             JOIN_TYPE.append("-")
                  #length_list=len(CALCULATION_VW_ID)
                  #for i in range(length_list):
                 #SOURCE.append(data.attrib.get("source"))
                 #TARGET.append(data.attrib.get("target"))   
                             SOURCE.append(data2.get("source"))
                             #print(SOURCE)
                             TARGET.append(data2.get("target"))
                  #print(TARGET)

                  #End of Projection View Parsing#
        
       #JOIN VIEW-PROJECTION
       calculationView = doc.getElementsByTagName("calculationView")
       mapping = doc.getElementsByTagName("mapping")
       leveljoin={'Join_1','Join_2','Join_3','Join_4','Join_5','Join_6','Join_7','Join_8','Join_9','Join_10','Join_11','Join_12','Join_13','Join_14','Join_15','Join_16'}
       levelproj={'#CRMC_ERMS_CAT_CA','#Projection_1','#Projection_2','#Projection_3','#Projection_4','#Projection_5','#Projection_6','#Projection_7','#Projection_8','#Projection_9','#Projection_10','#Join_1','#Join_2','#Join_3','#Join_4','#Join_5','#Join_6','#Join_7','#Join_8','#Join_9','#Join_10'}
       #print(leveljoin)
       #print(levelproj)

       List1=[]
       ds1=dict()
       node_list=doc.getElementsByTagName("calculationView")
       for node in node_list:
         lst=node.getElementsByTagName('input')
         List1=[]
         for n1 in lst:
           List1.append(n1.attributes['node'].value)
         str4=""
         ds1[str4.join(node.getAttribute('id'))]=List1

       TYPE1=[]
       ST1=[]
       FLR1=[]
       J_CD1=[]
       JT1=[]
       FILE_NAME_JN=[]
       SOURCE1=[]
       TARGET1=[]
       ITEMS_1=OrderedDict()
       ITEMS_2=OrderedDict()
       ITEMS_3=OrderedDict()
       ITEMS_4=OrderedDict()
       ITEMS_5=OrderedDict()
       ITEMS_6=OrderedDict()
       ITEMS_7=OrderedDict()
       ITEMS_8=OrderedDict()
       ITEMS_10=OrderedDict()
       count=0
       for data1 in ds1:
          #if "Join" in data1: 
                #print(data1)
                 count=count+1
                 JOIN_CD1=[]
                 FILTER1=[]

                 for  data5 in root1.iterfind(".//calculationView[@id='{}']".format(data1)):
                     ITEMS_6=OrderedDict()
                     ITEMS_7=OrderedDict()
                     FILE_NAME_JN.append(filename)
                     CALCULATION_VW_ID1=[]
                     str2=""
                     CALCULATION_VW_ID1.append(data5.get("id"))
                     str4=""
                     ITEMS_10[str4.join(CALCULATION_VW_ID1)]=filename

                     for data9 in root1.iterfind(".//calculationView[@id='{}']".format(data1)):
                       FILE_NAME_JN.append(filename)
                       JOIN_TYPE1=[]
                       str3=""
                       if (data9.get("joinType")) is not None:
                           JOIN_TYPE1.append(data9.get("joinType"))
                       else:
                           JOIN_TYPE1.append("-")
                     ITEMS_1[str3.join(CALCULATION_VW_ID1)]=JOIN_TYPE1
                     #print(ITEMS_1)

                     for data11 in root1.iterfind(".//calculationView[@id='{}']/joinAttribute".format(data1)):
                         FILE_NAME_JN.append(filename)
                         #JOIN_CD1=[]
                         str4=""
                         if (data11.get("name")) is not None:
                            JOIN_CD1.append(data11.get("name"))
                         else:
                            JOIN_CD1.append("-")
                     str4=""
                     str16=""
                     ITEMS_2[str4.join(CALCULATION_VW_ID1)]=JOIN_CD1
                     #print(ITEMS_2)
                     

                     for data12 in root1.iterfind(".//calculationView[@id='{}']".format(data1)):
                           FILE_NAME_JN.append(filename)
                           FILTER1=[]
                           str5=""
                           if (data12.find('filter')) is not None:
                                FILTER1.append(data12.find('filter').text)
                           #elif (data12.get("value")) is not None:
                                #FILTER1.append(data12.get("value")) 
                           else:
                                FILTER1.append("Filters Not Available")
                     ITEMS_3[str4.join(CALCULATION_VW_ID1)]=FILTER1          
                     #ITEMS_10[str16.join(CALCULATION_VW_ID1)]=filename
                     #print(ITEMS_3)
                     #print(ITEMS_10)

                     for k,v in ds1.items():
                       if (k==data1):
                         values=v
                         for v1 in values:
                           SOURCE_TABLE1=[]
                           ITEMS_4=OrderedDict()
                           for data8 in root1.iterfind(".//calculationView/input[@node='{}']/".format(v1)):
                              SOURCE1=[]
                              TARGET1=[]
                              CHILD_NODE=[] 
                              CHILD_NODE.append(v1)
                              count=0
                              for data2 in root1.iterfind(".//calculationView[@id='{}']/input[@node='{}']/mapping".format(data1,v1)):
                                 count=count+1
                                 FILE_NAME_JN.append(filename)
                                 if (data2.get("source")) is not None:
                                     SOURCE1.append(data2.get("source"))
                                     TARGET1.append(data2.get("target"))
                                 else :
                                     SOURCE1.append("Constant")
                                     TARGET1.append(data2.get("target"))
                                 str4=""
                                 str5=""
                                 ITEMS_6[str4.join(CHILD_NODE)]=SOURCE1
                                 ITEMS_7[str5.join(CHILD_NODE)]=TARGET1
                                 
                                 
                                 
                     str4=""
                     str5=""
                     ITEMS_5[str4.join(CALCULATION_VW_ID1)]=ITEMS_6
                     ITEMS_8[str5.join(CALCULATION_VW_ID1)]=ITEMS_7
                     #print(ITEMS_5)
                     #print(ITEMS_7)

       #Calculated View Attribute
       List10=[]
       ds10=dict()
       node_list=doc.getElementsByTagName("calculationView")
       for node in node_list:
         str4=""
         #ds10[str4.join(node.getAttribute('id'))]=List10
         List10.append(str4.join(node.getAttribute('id')))

       TYPECVA1=[]
       STCVA1=[]
       FLRCVA1=[]
       JCVA_CD1=[]
       JTCVA1=[]
       FILE_NAME_CVA=[]
       SOURCECVA1=[]
       TARGETCVA1=[]
       ITEMSCVA_1=OrderedDict()
       ITEMSCVA_2=OrderedDict()
       ITEMSCVA_3=OrderedDict()
       ITEMSCVA_4=OrderedDict()
       ITEMSCVA_5=OrderedDict()
       ITEMSCVA_6=OrderedDict()
       ITEMSCVA_7=OrderedDict()
       ITEMSCVA_8=OrderedDict()
       ITEMSCVA_10=OrderedDict()
       ITEMSCVA_11=OrderedDict()
       ITEMSCVA_12=OrderedDict()
       countcva=0
       for data1 in List10:
          #if "Join" in data1: 
                #print(data1)
                 
                 JOIN_CD1=[]
                 FILTER1=[]
                 countcva1=0
                 SOURCE_C=[]
                 TARGET_C=[]

                 for data2 in root1.iterfind(".//calculationView[@id='{}']/calculatedViewAttributes/calculatedViewAttribute".format(data1)):
                            #print(data1)
                            countcva=countcva+1
                            FILE_NAME_CVA.append(filename)                    
                            countcva1+=1
                            SOURCECVA1=[]
                            TARGETCVA1=[]
                            countcva1=countcva1+1
                            SOURCE_C.append(data2.find('formula').text)
                            TARGET_C.append(data2.get("id"))
                                 
                 str4=""
                 str5=""
                 if countcva1>0:

                      ITEMSCVA_5[str4.join(data1)]=SOURCE_C
                      ITEMSCVA_8[str5.join(data1)]=TARGET_C
                                                                                          
                      for  data5 in root1.iterfind(".//calculationView[@id='{}']".format(data1)):
                        ITEMSCVA_6=OrderedDict()
                        ITEMSCVA_7=OrderedDict()
                        FILE_NAME_CVA.append(filename)
                        CALCULATION_VW_ID1=[]
                        str2=""
                        CALCULATION_VW_ID1.append(data5.get("id"))
                        str4=""
                        ITEMSCVA_10[str4.join(CALCULATION_VW_ID1)]=filename

                      for data9 in root1.iterfind(".//calculationView[@id='{}']".format(data1)):
                        FILE_NAME_CVA.append(filename)
                        JOIN_TYPE1=[]
                        STCVA=[]
                        CFCVA=[]
                        str3=""
                        strcva3=""
                        strcva4=""
                       
                        STCVA.append("-")
                        CFCVA.append("-")                   
                        if (data9.get("joinType")) is not None:
                           JOIN_TYPE1.append(data9.get("joinType"))
                        else:
                           JOIN_TYPE1.append("-")
                        ITEMSCVA_1[str3.join(CALCULATION_VW_ID1)]=JOIN_TYPE1
                        ITEMSCVA_11[strcva3.join(CALCULATION_VW_ID1)]=STCVA
                        ITEMSCVA_12[strcva4.join(CALCULATION_VW_ID1)]=CFCVA
                        #print(ITEMSCVA_1)

                      for data11 in root1.iterfind(".//calculationView[@id='{}']/joinAttribute".format(data1)):
                         FILE_NAME_CVA.append(filename)
                         #JOIN_CD1=[]
                         str4=""
                         if (data11.get("name")) is not None:
                            JOIN_CD1.append(data11.get("name"))
                         else:
                            JOIN_CD1.append("-")
                         str4=""
                         str16=""
                      ITEMSCVA_2[str4.join(CALCULATION_VW_ID1)]=JOIN_CD1
                      #print(ITEMSCVA_2)
                     

                      for data12 in root1.iterfind(".//calculationView[@id='{}']".format(data1)):
                           FILE_NAME_CVA.append(filename)
                           FILTER1=[]
                           str5=""
                           if (data12.find('filter')) is not None:
                                FILTER1.append(data12.find('filter').text)
                           #elif (data12.get("value")) is not None:
                                #FILTER1.append(data12.get("value")) 
                           else:
                                FILTER1.append("Filters Not Available")
                      ITEMSCVA_3[str4.join(CALCULATION_VW_ID1)]=FILTER1          
                      #ITEMS_10[str16.join(CALCULATION_VW_ID1)]=filename
                      #print(ITEMSCVA_3)
                      #print(ITEMSCVA_10)

       #Rank Logic#
                      
       List1 = []
       ds1=dict()
       node_list=doc.getElementsByTagName("calculationView")
       for node in node_list:
         lst=node.getElementsByTagName('input')
         List1=[]
         for n1 in lst:
             List1.append(n1.attributes['node'].value)
             str4=""
             ds1[str4.join(node.getAttribute('id'))]=List1

       finalDict = dict()
       for k,v in ds1.items():
         ListTemp = []
         for data5 in root1.iterfind(".//calculationView[@id='{}']/windowFunction".format(k)):
            ListTemp.append(k)
            str4 = ""
            finalDict[str4.join(k)]=v

       ITEMS_1_Rnk=OrderedDict()     
       ITEMS_2_Rnk=OrderedDict()
       ITEMS_3_Rnk=OrderedDict()
       ITEMS_4_Rnk=OrderedDict()
       ITEMS_5_Rnk=OrderedDict()

       count_rnk=0

       for data1 in finalDict:
            count_rnk = count_rnk+1
            for data5 in root1.iterfind(".//calculationView[@id='{}']".format(data1)):
                str4 = ""
                ITEMS_1_Rnk[str4.join(filename)]=data1
                List1 = []
                j=0
                for i in root1.findall('.//partitionViewAttributeName'):
                    str4=""
                           
                    List1.append(i.text)
                        
                ITEMS_2_Rnk[str4.join(data1)]= List1
                List2 = []
                List3 = []
                for data12 in root1.iterfind(".//calculationView[@id='{}']/windowFunction/order".format(data1)):
                    str4=""
                    List2.append(data12.get("byViewAttributeName"))
                    List3.append(data12.get("direction"))
                ITEMS_3_Rnk[str4.join(data1)]= List2
                ITEMS_4_Rnk[str4.join(data1)]= List3
                List4=[]
                for data12 in root1.iterfind(".//calculationView[@id='{}']/windowFunction/rankThreshold/value".format(data1)):
                    List4.append(data12.text)
                    str4 = ""
                ITEMS_5_Rnk[str4.join(data1)]= List4
             
                                                                                                                 
       #Column Filter
       List3=[]
       countprojcf=0
       final_proj_list=[]     
       for n3 in calculationView:
           str210=""
           List3.append(str210.join(n3.getAttribute('id')))
           for data1 in List3:
               countprojcf=countprojcf+1
               if data1 not in final_proj_list:
                   #print(data1)
                   final_proj_list.append(data1)

       dict200=dict()
       dict300=dict()
       for data1 in final_proj_list:
           dict200=dict()
           dict300[data1]=dict200
           for data2 in root1.iterfind(".//calculationView[@id='{}']/viewAttributes/viewAttribute".format(data1)):
               attrib_id=data2.get("id")
               for data3 in root1.iterfind(".//calculationView[@id='{}']/viewAttributes/viewAttribute[@id='{}']/filter".format(data1,attrib_id)):
                   if data3.get("value") =="":
                     dict200[attrib_id]="BLANK"
                   else:
                     dict200[attrib_id]=data3.get("value")
             
       #Rank Dataframe
       df1_rnk=pd.DataFrame(ITEMS_1_Rnk.items(),columns=['File_name','Window_Id'])
       #print (df1_rnk)
       df2_rnk=pd.DataFrame(finalDict.items(),columns=['Window_Id','Node_Name'])
       #print(df2_rnk)
       df3_rnk=pd.DataFrame(ITEMS_2_Rnk.items(),columns=['Window_Id','Partitioned_Attrib'])
       #print(df3_rnk)
       df4_rnk=pd.DataFrame(ITEMS_3_Rnk.items(),columns=['Window_Id','Order_By_Attrib'])
       #print(df4_rnk)
       df5_rnk=pd.DataFrame(ITEMS_4_Rnk.items(),columns=['Window_Id','Order_By_Dir'])
       #print(df5_rnk)
       df6_rnk=pd.DataFrame(ITEMS_5_Rnk.items(),columns=['Window_Id','Rank_Val'])
       #print(df6_rnk)
       dataframes=[df1_rnk,df2_rnk,df3_rnk,df4_rnk,df5_rnk,df6_rnk]

       df_merged_rank = reduce(lambda left,right: pd.merge(left,right,on=['Window_Id'],how='outer'),dataframes)
       df_merged_rank['Node_Name']=df_merged_rank['Node_Name'].str.join(',')
       df_merged_rank['Partitioned_Attrib']=df_merged_rank['Partitioned_Attrib'].str.join(',')
       df_merged_rank['Order_By_Attrib']=df_merged_rank['Order_By_Attrib'].str.join(',')
       df_merged_rank['Order_By_Dir']=df_merged_rank['Order_By_Dir'].str.join(',')
       df_merged_rank['Rank_Val']=df_merged_rank['Rank_Val'].str.join(',')
       df_merged_rank['Node_Name'] = df_merged_rank['Node_Name'].apply(lambda x : x[1:] if x.startswith("#") else x)
       df_merged_rank['Node_Name']=df_merged_rank['Node_Name'].str.split('\::').str[-1].str.strip()
       
       #print(df_merged_rank)
       #final_rank = df_merged_rank[["File_name","Window_Id","Node_Name","Partitioned_Attrib","Order_By_Attrib","Order_By_Dir","Rank_Val"]]
       #final_rank.columns = ['File_name','Window_Id','Node_Name','Partitioned_Attrib','Order_By_Attrib','Order_By_Dir','Rank_Val']
       #df_merged_rank_final=df_merged_rank_final.append(final_rank)

       #print('loop')

       #print(ITEMS_3)
       #print(ITEMS_1)
       #print(ITEMS_5)
       #print(ITEMS_8)
       #print(ITEMS_10)
       #print(ITEMS_2)
       #Datasource View
       
       if(count3>0):
           
         df90=pd.DataFrame(ITEMS_100.items(),columns=['DS_Id','File_Name_DS'])
         
         #print(df90)
         df91=pd.DataFrame(ITEMS_110.items(),columns=['DS_Id','DS_Type'])
         #print(df91)
         df92=pd.DataFrame(ITEMS_200.items(),columns=['DS_Id','Schema_Name'])
         #print(df92)
         df93=pd.DataFrame(ITEMS_300.items(),columns=['DS_Id','ResourceUri'])
         
         #print(df93)

         dfclmnobj=pd.DataFrame(ITEMS_400.items(),columns=['DS_Id','ColumnObject'])
         df94= pd.merge(df90,df91,on='DS_Id',how='left')
         #print (df94)

         df95= pd.merge(df94,df92,on='DS_Id',how='left')
         #print (df95)

         df_merged1= pd.merge(df95,df93,on='DS_Id',how='left')

         df_merged2a= pd.merge(df_merged1,dfclmnobj,on='DS_Id',how='left')

         df_merged2a['DS_Type']=df_merged2a['DS_Type'].str.join(',')
         df_merged2a['Schema_Name']=df_merged2a['Schema_Name'].str.join(',')
         df_merged2a['ResourceUri']=df_merged2a['ResourceUri'].str.join(',')
         df_merged2a['ColumnObject']=df_merged2a['ColumnObject'].str.join(',')
         final_df2 = df_merged2a[["File_Name_DS","DS_Id","ColumnObject","DS_Type","Schema_Name","ResourceUri"]]
         final_df2.columns = ['File_Name_DS','DS_Id','ColumnObject','DS_Type','Schema_Name','ResourceUri']
         df_merged2=df_merged2.append(final_df2)
         
         final_df1 = df_merged2[["File_Name_DS","DS_Id","ColumnObject","DS_Type","Schema_Name","ResourceUri"]] 
         
         final_df1.DS_Id=np.where(final_df1.DS_Type.eq('DATA_BASE_TABLE'), final_df1.ColumnObject, final_df1.DS_Id)
         df_merged_ds=final_df1[["File_Name_DS","DS_Id","DS_Type","Schema_Name","ResourceUri"]]
         
         df_merged_ds['DS_Id']=df_merged_ds['DS_Id'].str.split('\::').str[-1].str.strip()  
         df_merged_ds.columns = ['FILE_NAME','ID','TYPE','SCHEMA_NAME','RESOURCE_URI']
         df_merged_final1=df_merged_final1.append(df_merged_ds)
         df_merged_final1=df_merged_final1.drop_duplicates(subset=None, keep='first', inplace=False)
       
       #Unnesting for Logical Seq View
       df80=pd.DataFrame([(k,k1,v1) for k,v in dict300.items() for k1,v1 in v.items()],columns=['STCF','TCCF','CF'])
       
       def unnesting(df,explode):
         idx=df.index.repeat(df[explode[0]].str.len())
         df1=pd.concat([pd.DataFrame({x: np.concatenate(df[x].values)}) for x in explode], axis =1)
         df1.index=idx
         return df1.join(df.drop(explode,1),how='left')
       
       if(count>0):
           
         df9=pd.DataFrame(ITEMS_10.items(),columns=['Join_Id','File_Name_Jn'])
         #print(df9)
         df10=pd.DataFrame(ITEMS_1.items(),columns=['Join_Id','Join_Type_Jn'])
         df11=pd.DataFrame(ITEMS_2.items(),columns=['Join_Id','Join_Cond'])
         df13=pd.DataFrame([(k,k1,v1) for k,v in ITEMS_5.items() for k1,v1 in v.items()],columns=['Join_Id','ST_Jn','SC'])
         df14=pd.DataFrame([(k,k1,v1) for k,v in ITEMS_8.items() for k1,v1 in v.items()],columns=['Join_Id','ST_Jn','TC'])
         df_comb=pd.merge(df13,df14,left_on=['Join_Id','ST_Jn'],right_on=['Join_Id','ST_Jn'],how='left')         
         df12=pd.DataFrame(ITEMS_3.items(),columns=['Join_Id','Filter_Cond'])
         
         dataframes=[df9,df10,df11,df_comb,df12]
       
         df_merged= reduce(lambda left,right: pd.merge(left,right,on=['Join_Id'],how='outer'),dataframes)

         df_unnesting = unnesting(df_merged,['SC','TC'])

         final_df = df_unnesting[["File_Name_Jn","Join_Id","Join_Type_Jn","Join_Cond","SC","TC","ST_Jn","Filter_Cond"]]

         #print(df_unnesting)

         #df_unnesting.columns=['FILE_NAME','ID','JOIN_TYPE','JOIN_CONDITION','SELECT','AS','FROM','WHERE']
         #df_merged_final=df_merged_final.append(df_unnesting)
         
         final_df['Filter_Cond']=final_df['Filter_Cond'].str.join(',')
         final_df['Join_Type_Jn']=final_df['Join_Type_Jn'].str.join(',')
         final_df['Join_Cond']=final_df['Join_Cond'].str.join(',')
         #final_df.sort_values(by=['File_Name_Jn','Join_Id'],inplace=True)
         final_df_cf=final_df.merge(df80,how='left',left_on=['Join_Id','TC'],right_on =['STCF','TCCF'])
         final_df_cf1 = final_df_cf[["File_Name_Jn","Join_Id","Join_Type_Jn","Join_Cond","SC","TC","ST_Jn","Filter_Cond","CF"]]

         final_df_cf1["CF"]=final_df_cf1["CF"].fillna("-")
         final_df_cf1["CF"]=final_df_cf1["CF"].replace(['BLANK'],'')    
                 

         dfcva9=pd.DataFrame(ITEMSCVA_10.items(),columns=['Join_Cva_Id','File_Name_Cva'])
         #print(dfcva9)
         dfcva10=pd.DataFrame(ITEMSCVA_1.items(),columns=['Join_Cva_Id','Join_Type_Cva'])
         dfcva11=pd.DataFrame(ITEMSCVA_2.items(),columns=['Join_Cva_Id','Join_Cond_Cva'])
         dfcva13=pd.DataFrame(ITEMSCVA_11.items(),columns=['Join_Cva_Id','ST_Cva'])
         dfcva16=pd.DataFrame(ITEMSCVA_12.items(),columns=['Join_Cva_Id','CF_Cva'])
         dfcva12=pd.DataFrame(ITEMSCVA_3.items(),columns=['Join_Cva_Id','Filter_Cond_Cva'])
         dfcva14=pd.DataFrame(ITEMSCVA_5.items(),columns=['Join_Cva_Id','SC_Cva'])
         dfcva15=pd.DataFrame(ITEMSCVA_8.items(),columns=['Join_Cva_Id','TC_Cva'])
                           
         
         dataframes_cva=[dfcva9,dfcva10,dfcva11,dfcva13,dfcva14,dfcva15,dfcva16,dfcva12]
         

         df_cva_merged= reduce(lambda left,right: pd.merge(left,right,on=['Join_Cva_Id'],how='outer'),dataframes_cva)
         if countcva>0:
           df_cva_unnesting = unnesting(df_cva_merged,['SC_Cva','TC_Cva'])

           final_cva_df = df_cva_unnesting[["File_Name_Cva","Join_Cva_Id","Join_Type_Cva","Join_Cond_Cva","SC_Cva","TC_Cva","ST_Cva","Filter_Cond_Cva","CF_Cva"]]
                  
           final_cva_df['Filter_Cond_Cva']=final_cva_df['Filter_Cond_Cva'].str.join(',')
           final_cva_df['Join_Type_Cva']=final_cva_df['Join_Type_Cva'].str.join(',')
           final_cva_df['Join_Cond_Cva']=final_cva_df['Join_Cond_Cva'].str.join(',')
           final_cva_df['ST_Cva']=final_cva_df['ST_Cva'].str.join(',')  
           final_cva_df['CF_Cva']=final_cva_df['CF_Cva'].str.join(',')

           final_cva_df.columns=final_df_cf1.columns
           final_df_cf1=final_df_cf1.append(final_cva_df,ignore_index=True)
             
         #final_df_cf1.sort_values(by=['Join_Id'])

           grouped_df=final_df_cf1.groupby(['Join_Id'],sort=False)

           for key,item in grouped_df:
             final_df_cf2=grouped_df.get_group(key)
             final_df_cf2.columns=['FILE_NAME','ID','JOIN_TYPE','JOIN_CONDITION','SELECT','AS','FROM','WHERE','COLUMN_FILTER']
             df_merged_final=df_merged_final.append(final_df_cf2)
             df_merged_final['FROM'] = df_merged_final['FROM'].apply(lambda x : x[1:] if x.startswith("#") else x)
             df_merged_final['FROM']=df_merged_final['FROM'].str.split('\::').str[-1].str.strip()

             df_merged_final1_lsv=df_merged2.copy()
             #print (df_merged_final1_lsv)
             df_merged_final1_lsv['KEY']=df_merged_final1_lsv['File_Name_DS']+'-'+df_merged_final1_lsv['DS_Id'].str.split('\::').str[-1].str.strip()
             df_merged_final1_lsv=df_merged_final1_lsv.drop(['File_Name_DS'],axis=1)

             df_merged_final['KEY']=df_merged_final['FILE_NAME']+'-'+df_merged_final['FROM']

             df_merged_final_lsv=pd.merge(df_merged_final, df_merged_final1_lsv, how='left', on='KEY')

             df_merged_final_lsv["New"]=np.where(df_merged_final_lsv['Schema_Name']=='-',df_merged_final_lsv['FROM'],df_merged_final_lsv['Schema_Name']+'.'+df_merged_final_lsv['ColumnObject'].str.split('\::').str[-1].str.strip())
             df_merged_final_lsv["New1"]=np.where(df_merged_final_lsv['New']=='NaN',df_merged_final_lsv['FROM'],df_merged_final_lsv['New'])
             df_merged_final_lsv['New1']=df_merged_final_lsv['New1'].fillna(df_merged_final_lsv['FROM'])

             df_merged_final_lsv['FROM']=df_merged_final_lsv['New1']
             df_merged_final_lsv=df_merged_final_lsv.drop(['KEY','New','New1','DS_Type','Schema_Name','ResourceUri','DS_Id','ColumnObject'],axis=1)
             #print(df_merged_final_lsv)
             df_merged_rank_final = pd.merge(df_merged_final_lsv,df_merged_rank, how='left', left_on=['FILE_NAME', 'ID','FROM'], right_on=['File_name', 'Window_Id','Node_Name'])
             #print(df_merged_rank_final)
             df_merged_rank_final = df_merged_rank_final.drop(['File_name','Window_Id','Node_Name'],axis = 1)
             df_merged_rank_final.drop_duplicates(subset=None, keep='first', inplace=True)
             
         else:
             final_df_cf1.columns=['FILE_NAME','ID','JOIN_TYPE','JOIN_CONDITION','SELECT','AS','FROM','WHERE','COLUMN_FILTER']
             df_merged_final=df_merged_final.append(final_df_cf1)
             df_merged_final['FROM'] = df_merged_final['FROM'].apply(lambda x : x[1:] if x.startswith("#") else x)
             df_merged_final['FROM']=df_merged_final['FROM'].str.split('\::').str[-1].str.strip()  

             df_merged_final1_lsv=df_merged2.copy()
             #print (df_merged_final1_lsv)
             df_merged_final1_lsv['KEY']=df_merged_final1_lsv['File_Name_DS']+'-'+df_merged_final1_lsv['DS_Id'].str.split('\::').str[-1].str.strip()
             df_merged_final1_lsv=df_merged_final1_lsv.drop(['File_Name_DS'],axis=1)

             df_merged_final['KEY']=df_merged_final['FILE_NAME']+'-'+df_merged_final['FROM']

             df_merged_final_lsv=pd.merge(df_merged_final, df_merged_final1_lsv, how='left', on='KEY')

             #New Code Added

             df_merged_final_lsv["New"]=np.where(df_merged_final_lsv['Schema_Name']=='-',df_merged_final_lsv['FROM'],df_merged_final_lsv['Schema_Name']+'.'+df_merged_final_lsv['ColumnObject'].str.split('\::').str[-1].str.strip())
                        
             df_merged_final_lsv["New1"]=np.where(df_merged_final_lsv['New']=='NaN',df_merged_final_lsv['FROM'],df_merged_final_lsv['New'])
             df_merged_final_lsv['New1']=df_merged_final_lsv['New1'].fillna(df_merged_final_lsv['FROM'])

             df_merged_final_lsv['FROM']=df_merged_final_lsv['New1']
             df_merged_final_lsv=df_merged_final_lsv.drop(['KEY','New','New1','DS_Type','Schema_Name','ResourceUri','DS_Id','ColumnObject'],axis=1)
             
             #df_merged_rank_copy=df_merged_rank.copy()
             df_merged_rank_final = pd.merge(df_merged_final_lsv,df_merged_rank, how='left', left_on=['FILE_NAME', 'ID','FROM'], right_on=['File_name', 'Window_Id','Node_Name'])
             df_merged_rank_final = df_merged_rank_final.drop(['File_name','Window_Id','Node_Name'],axis = 1)
             df_merged_rank_final.drop_duplicates(subset=None, keep='first', inplace=True)
         
         #ID List
         df_id=df9[["File_Name_Jn","Join_Id"]]
         df_id.columns=['FILE_NAME','ID']
         df_merged_id=df_merged_id.append(df_id)

                            
                
       if ((countatr>0) or (countca>0) or (countmsr>0) or (countrmsr>0)) :
         dfatr90=pd.DataFrame(ITEMS_ATR.items(),columns=['ID_ATR','File_Name_Atr'])
                  
         dfatr91=pd.DataFrame(ITEMS_ATR1.items(),columns=['ID_ATR','Order'])
         
         dfatr92=pd.DataFrame(ITEMS_ATR2.items(),columns=['ID_ATR','ATR_DESC'])
         
         dfatr93=pd.DataFrame(ITEMS_ATR3.items(),columns=['ID_ATR','ATR_OBJ_NAME'])
         dfatr94=pd.DataFrame(ITEMS_ATR4.items(),columns=['ID_ATR','ATR_COL_NAME'])
         dfatr95=pd.DataFrame(ITEMS_ATR5.items(),columns=['ID_ATR','ATR_TYPE'])
         dfatr96=pd.DataFrame(ITEMS_ATR6.items(),columns=['ID_ATR','ATR_DATATYPE'])
         dfatr97=pd.DataFrame(ITEMS_ATR7.items(),columns=['ID_ATR','ATR_LENGTH'])
         dfatr98=pd.DataFrame(ITEMS_ATR8.items(),columns=['ID_ATR','ATR_FORMULA'])
         dfatr99=pd.DataFrame(ITEMS_ATR9.items(),columns=['ID_ATR','ATR_AGG_TYPE'])
         dfatr100=pd.DataFrame(ITEMS_ATR10.items(),columns=['ID_ATR','ATR_BASE_MEASURE'])
         dfatr101=pd.DataFrame(ITEMS_ATR11.items(),columns=['ID_ATR','LOGICAL_OPERATOR'])
         dfatr102=pd.DataFrame(ITEMS_ATR12.items(),columns=['ID_ATR','FILTER_ATR_NAME'])
         dfatr103=pd.DataFrame(ITEMS_ATR13.items(),columns=['ID_ATR','SINGLE_VALUE_FILTER'])

         dataframes_atr=[dfatr90,dfatr91,dfatr92,dfatr93,dfatr94,dfatr95,dfatr96,dfatr97,dfatr98,dfatr99,dfatr100,dfatr101,dfatr102,dfatr103]
         
         df_atr_merged= reduce(lambda left,right: pd.merge(left,right,on=['ID_ATR'],how='outer'),dataframes_atr) 
         
         df_atr_merged['Order']=df_atr_merged['Order'].str.join(',')
         df_atr_merged['ATR_DESC']=df_atr_merged['ATR_DESC'].str.join(',')
         df_atr_merged['ATR_OBJ_NAME']=df_atr_merged['ATR_OBJ_NAME'].str.join(',')
         df_atr_merged['ATR_COL_NAME']=df_atr_merged['ATR_COL_NAME'].str.join(',')
         df_atr_merged['ATR_TYPE']=df_atr_merged['ATR_TYPE'].str.join(',')
         df_atr_merged['ATR_DATATYPE']=df_atr_merged['ATR_DATATYPE'].str.join(',')
         df_atr_merged['ATR_LENGTH']=df_atr_merged['ATR_LENGTH'].str.join(',')
         df_atr_merged['ATR_FORMULA']=df_atr_merged['ATR_FORMULA'].str.join(',')
         df_atr_merged['ATR_AGG_TYPE']=df_atr_merged['ATR_AGG_TYPE'].str.join(',')
         df_atr_merged['ATR_BASE_MEASURE']=df_atr_merged['ATR_BASE_MEASURE'].str.join(',')
         df_atr_merged['LOGICAL_OPERATOR']=df_atr_merged['LOGICAL_OPERATOR'].str.join(',')
         df_atr_merged['FILTER_ATR_NAME']=df_atr_merged['FILTER_ATR_NAME'].str.join(',')
         df_atr_merged['SINGLE_VALUE_FILTER']=df_atr_merged['SINGLE_VALUE_FILTER'].str.join(',')
         
         df2_dummy_atr = df_atr_merged[["File_Name_Atr","ID_ATR","Order","ATR_OBJ_NAME","ATR_COL_NAME","ATR_TYPE","ATR_DESC","ATR_DATATYPE","ATR_LENGTH","ATR_FORMULA","ATR_AGG_TYPE","ATR_BASE_MEASURE","LOGICAL_OPERATOR","FILTER_ATR_NAME","SINGLE_VALUE_FILTER"]] 
                
         dfca90=pd.DataFrame(ITEMS_CA.items(),columns=['ID_CA','File_Name_Ca'])
                  
         dfca91=pd.DataFrame(ITEMS_CA1.items(),columns=['ID_CA','Order_CA'])
         
         dfca92=pd.DataFrame(ITEMS_CA2.items(),columns=['ID_CA','ATR_DESC_CA'])
         
         dfca93=pd.DataFrame(ITEMS_CA3.items(),columns=['ID_CA','ATR_OBJ_NAME_CA'])
         dfca94=pd.DataFrame(ITEMS_CA4.items(),columns=['ID_CA','ATR_COL_NAME_CA'])
         dfca95=pd.DataFrame(ITEMS_CA5.items(),columns=['ID_CA','ATR_TYPE_CA'])
         dfca96=pd.DataFrame(ITEMS_CA6.items(),columns=['ID_CA','ATR_DATATYPE_CA'])
         dfca97=pd.DataFrame(ITEMS_CA7.items(),columns=['ID_CA','ATR_LENGTH_CA'])
         dfca98=pd.DataFrame(ITEMS_CA8.items(),columns=['ID_CA','ATR_FORMULA_CA'])
         dfca99=pd.DataFrame(ITEMS_CA9.items(),columns=['ID_CA','ATR_AGG_TYPE_CA'])
         dfca100=pd.DataFrame(ITEMS_CA10.items(),columns=['ID_CA','ATR_BASE_MEASURE'])
         dfca101=pd.DataFrame(ITEMS_CA11.items(),columns=['ID_CA','LOGICAL_OPERATOR'])
         dfca102=pd.DataFrame(ITEMS_CA12.items(),columns=['ID_CA','FILTER_ATR_NAME'])
         dfca103=pd.DataFrame(ITEMS_CA13.items(),columns=['ID_CA','SINGLE_VALUE_FILTER'])

         dataframes_ca=[dfca90,dfca91,dfca92,dfca93,dfca94,dfca95,dfca96,dfca97,dfca98,dfca99,dfca100,dfca101,dfca102,dfca103]
         
         df_ca_merged= reduce(lambda left,right: pd.merge(left,right,on=['ID_CA'],how='outer'),dataframes_ca) 
         
         df_ca_merged['Order_CA']=df_ca_merged['Order_CA'].str.join(',')
         df_ca_merged['ATR_DESC_CA']=df_ca_merged['ATR_DESC_CA'].str.join(',')
         df_ca_merged['ATR_OBJ_NAME_CA']=df_ca_merged['ATR_OBJ_NAME_CA'].str.join(',')
         df_ca_merged['ATR_COL_NAME_CA']=df_ca_merged['ATR_COL_NAME_CA'].str.join(',')
         df_ca_merged['ATR_TYPE_CA']=df_ca_merged['ATR_TYPE_CA'].str.join(',')
         df_ca_merged['ATR_DATATYPE_CA']=df_ca_merged['ATR_DATATYPE_CA'].str.join(',')
         df_ca_merged['ATR_LENGTH_CA']=df_ca_merged['ATR_LENGTH_CA'].str.join(',')
         df_ca_merged['ATR_FORMULA_CA']=df_ca_merged['ATR_FORMULA_CA'].str.join(',')
         df_ca_merged['ATR_AGG_TYPE_CA']=df_ca_merged['ATR_AGG_TYPE_CA'].str.join(',')
         df_ca_merged['ATR_BASE_MEASURE']=df_ca_merged['ATR_BASE_MEASURE'].str.join(',')
         df_ca_merged['LOGICAL_OPERATOR']=df_ca_merged['LOGICAL_OPERATOR'].str.join(',')
         df_ca_merged['FILTER_ATR_NAME']=df_ca_merged['FILTER_ATR_NAME'].str.join(',')
         df_ca_merged['SINGLE_VALUE_FILTER']=df_ca_merged['SINGLE_VALUE_FILTER'].str.join(',')
                  
         df2_dummy_ca = df_ca_merged[["File_Name_Ca","ID_CA","Order_CA","ATR_OBJ_NAME_CA","ATR_COL_NAME_CA","ATR_TYPE_CA","ATR_DESC_CA","ATR_DATATYPE_CA","ATR_LENGTH_CA","ATR_FORMULA_CA","ATR_AGG_TYPE_CA","ATR_BASE_MEASURE","LOGICAL_OPERATOR","FILTER_ATR_NAME","SINGLE_VALUE_FILTER"]] 
               
         dfmsr90=pd.DataFrame(ITEMS_MSR.items(),columns=['ID_MSR','File_Name_Msr'])
                  
         dfmsr91=pd.DataFrame(ITEMS_MSR1.items(),columns=['ID_MSR','Order_MSR'])
         
         dfmsr92=pd.DataFrame(ITEMS_MSR2.items(),columns=['ID_MSR','ATR_DESC_MSR'])
         
         dfmsr93=pd.DataFrame(ITEMS_MSR3.items(),columns=['ID_MSR','ATR_OBJ_NAME_MSR'])
         dfmsr94=pd.DataFrame(ITEMS_MSR4.items(),columns=['ID_MSR','ATR_COL_NAME_MSR'])
         dfmsr95=pd.DataFrame(ITEMS_MSR5.items(),columns=['ID_MSR','ATR_TYPE_MSR'])
         dfmsr96=pd.DataFrame(ITEMS_MSR6.items(),columns=['ID_MSR','ATR_DATATYPE_MSR'])
         dfmsr97=pd.DataFrame(ITEMS_MSR7.items(),columns=['ID_MSR','ATR_LENGTH_MSR'])
         dfmsr98=pd.DataFrame(ITEMS_MSR8.items(),columns=['ID_MSR','ATR_FORMULA_MSR'])
         dfmsr99=pd.DataFrame(ITEMS_MSR9.items(),columns=['ID_MSR','ATR_AGG_TYPE_MSR'])
         dfmsr100=pd.DataFrame(ITEMS_MSR10.items(),columns=['ID_MSR','ATR_BASE_MEASURE'])
         dfmsr101=pd.DataFrame(ITEMS_MSR11.items(),columns=['ID_MSR','LOGICAL_OPERATOR'])
         dfmsr102=pd.DataFrame(ITEMS_MSR12.items(),columns=['ID_MSR','FILTER_ATR_NAME'])
         dfmsr103=pd.DataFrame(ITEMS_MSR13.items(),columns=['ID_MSR','SINGLE_VALUE_FILTER'])

         dataframes_msr=[dfmsr90,dfmsr91,dfmsr92,dfmsr93,dfmsr94,dfmsr95,dfmsr96,dfmsr97,dfmsr98,dfmsr99,dfmsr100,dfmsr101,dfmsr102,dfmsr103]
         
         df_msr_merged= reduce(lambda left,right: pd.merge(left,right,on=['ID_MSR'],how='outer'),dataframes_msr) 
         
         df_msr_merged['Order_MSR']=df_msr_merged['Order_MSR'].str.join(',')
         df_msr_merged['ATR_DESC_MSR']=df_msr_merged['ATR_DESC_MSR'].str.join(',')
         df_msr_merged['ATR_OBJ_NAME_MSR']=df_msr_merged['ATR_OBJ_NAME_MSR'].str.join(',')
         df_msr_merged['ATR_COL_NAME_MSR']=df_msr_merged['ATR_COL_NAME_MSR'].str.join(',')
         df_msr_merged['ATR_TYPE_MSR']=df_msr_merged['ATR_TYPE_MSR'].str.join(',')
         df_msr_merged['ATR_DATATYPE_MSR']=df_msr_merged['ATR_DATATYPE_MSR'].str.join(',')
         df_msr_merged['ATR_LENGTH_MSR']=df_msr_merged['ATR_LENGTH_MSR'].str.join(',')
         df_msr_merged['ATR_FORMULA_MSR']=df_msr_merged['ATR_FORMULA_MSR'].str.join(',')
         df_msr_merged['ATR_AGG_TYPE_MSR']=df_msr_merged['ATR_AGG_TYPE_MSR'].str.join(',')
         df_msr_merged['ATR_BASE_MEASURE']=df_msr_merged['ATR_BASE_MEASURE'].str.join(',')
         df_msr_merged['LOGICAL_OPERATOR']=df_msr_merged['LOGICAL_OPERATOR'].str.join(',')
         df_msr_merged['FILTER_ATR_NAME']=df_msr_merged['FILTER_ATR_NAME'].str.join(',')
         df_msr_merged['SINGLE_VALUE_FILTER']=df_msr_merged['SINGLE_VALUE_FILTER'].str.join(',')
                  
         df2_dummy_msr = df_msr_merged[["File_Name_Msr","ID_MSR","Order_MSR","ATR_OBJ_NAME_MSR","ATR_COL_NAME_MSR","ATR_TYPE_MSR","ATR_DESC_MSR","ATR_DATATYPE_MSR","ATR_LENGTH_MSR","ATR_FORMULA_MSR","ATR_AGG_TYPE_MSR","ATR_BASE_MEASURE","LOGICAL_OPERATOR","FILTER_ATR_NAME","SINGLE_VALUE_FILTER"]] 

         dfrmsr90=pd.DataFrame(ITEMS_RMSR.items(),columns=['ID_RMSR','File_Name_Rmsr'])
                  
         dfrmsr91=pd.DataFrame(ITEMS_RMSR1.items(),columns=['ID_RMSR','Order_RMSR'])
         
         dfrmsr92=pd.DataFrame(ITEMS_RMSR2.items(),columns=['ID_RMSR','ATR_DESC_RMSR'])
         
         dfrmsr93=pd.DataFrame(ITEMS_RMSR3.items(),columns=['ID_RMSR','ATR_OBJ_NAME_RMSR'])
         dfrmsr94=pd.DataFrame(ITEMS_RMSR4.items(),columns=['ID_RMSR','ATR_COL_NAME_RMSR'])
         dfrmsr95=pd.DataFrame(ITEMS_RMSR5.items(),columns=['ID_RMSR','ATR_TYPE_RMSR'])
         dfrmsr96=pd.DataFrame(ITEMS_RMSR6.items(),columns=['ID_RMSR','ATR_DATATYPE_RMSR'])
         dfrmsr97=pd.DataFrame(ITEMS_RMSR7.items(),columns=['ID_RMSR','ATR_LENGTH_RMSR'])
         dfrmsr98=pd.DataFrame(ITEMS_RMSR8.items(),columns=['ID_RMSR','ATR_FORMULA_RMSR'])
         dfrmsr99=pd.DataFrame(ITEMS_RMSR9.items(),columns=['ID_RMSR','ATR_AGG_TYPE_RMSR'])
         dfrmsr100=pd.DataFrame(ITEMS_RMSR10.items(),columns=['ID_RMSR','ATR_BASE_MEASURE'])
         dfrmsr101=pd.DataFrame(ITEMS_RMSR11.items(),columns=['ID_RMSR','LOGICAL_OPERATOR'])
         dfrmsr102=pd.DataFrame(ITEMS_RMSR12.items(),columns=['ID_RMSR','FILTER_ATR_NAME'])
         dfrmsr103=pd.DataFrame(ITEMS_RMSR13.items(),columns=['ID_RMSR','SINGLE_VALUE_FILTER'])

         dataframes_rmsr=[dfrmsr90,dfrmsr91,dfrmsr92,dfrmsr93,dfrmsr94,dfrmsr95,dfrmsr96,dfrmsr97,dfrmsr98,dfrmsr99,dfrmsr100,dfrmsr101,dfrmsr102,dfrmsr103]
         
         df_rmsr_merged= reduce(lambda left,right: pd.merge(left,right,on=['ID_RMSR'],how='outer'),dataframes_rmsr) 
         
         df_rmsr_merged['Order_RMSR']=df_rmsr_merged['Order_RMSR'].str.join(',')
         df_rmsr_merged['ATR_DESC_RMSR']=df_rmsr_merged['ATR_DESC_RMSR'].str.join(',')
         df_rmsr_merged['ATR_OBJ_NAME_RMSR']=df_rmsr_merged['ATR_OBJ_NAME_RMSR'].str.join(',')
         df_rmsr_merged['ATR_COL_NAME_RMSR']=df_rmsr_merged['ATR_COL_NAME_RMSR'].str.join(',')
         df_rmsr_merged['ATR_TYPE_RMSR']=df_rmsr_merged['ATR_TYPE_RMSR'].str.join(',')
         df_rmsr_merged['ATR_DATATYPE_RMSR']=df_rmsr_merged['ATR_DATATYPE_RMSR'].str.join(',')
         df_rmsr_merged['ATR_LENGTH_RMSR']=df_rmsr_merged['ATR_LENGTH_RMSR'].str.join(',')
         df_rmsr_merged['ATR_FORMULA_RMSR']=df_rmsr_merged['ATR_FORMULA_RMSR'].str.join(',')
         df_rmsr_merged['ATR_AGG_TYPE_RMSR']=df_rmsr_merged['ATR_AGG_TYPE_RMSR'].str.join(',')
         df_rmsr_merged['ATR_BASE_MEASURE']=df_rmsr_merged['ATR_BASE_MEASURE'].str.join(',')
         df_rmsr_merged['LOGICAL_OPERATOR']=df_rmsr_merged['LOGICAL_OPERATOR'].str.join(',')
         df_rmsr_merged['FILTER_ATR_NAME']=df_rmsr_merged['FILTER_ATR_NAME'].str.join(',')
         df_rmsr_merged['SINGLE_VALUE_FILTER']=df_rmsr_merged['SINGLE_VALUE_FILTER'].str.join(',')
                 
         df2_dummy_rmsr = df_rmsr_merged[["File_Name_Rmsr","ID_RMSR","Order_RMSR","ATR_OBJ_NAME_RMSR","ATR_COL_NAME_RMSR","ATR_TYPE_RMSR","ATR_DESC_RMSR","ATR_DATATYPE_RMSR","ATR_LENGTH_RMSR","ATR_FORMULA_RMSR","ATR_AGG_TYPE_RMSR","ATR_BASE_MEASURE","LOGICAL_OPERATOR","FILTER_ATR_NAME","SINGLE_VALUE_FILTER"]] 

         df2_dummy_ca.columns=df2_dummy_atr.columns
         df2_dummy_msr.columns=df2_dummy_atr.columns
         df2_dummy_rmsr.columns=df2_dummy_atr.columns

         df2_dummy_atr =df2_dummy_atr.append([df2_dummy_ca,df2_dummy_msr,df2_dummy_rmsr],ignore_index=True)
       #df2_dummy_atr =df2_dummy_atr.append(df2_dummy_msr,ignore_index=True) 

         grouped_df_attr=df2_dummy_atr.groupby(['File_Name_Atr'],sort=False)

         for key,item in grouped_df_attr:
           df2_dummy=grouped_df_attr.get_group(key)
                         
             
           df2_dummy.columns = ['FILE_NAME','ATTRIBUTE_ID','ATTRIBUTE_ORDER','ATTRIBUTE_OBJ_NM','ATTRIBUTE_COL_NM','ATTRIBUTE_TYPE','ATTRIBUTE_DESC','ATTRIBUTE_DATATYPE','ATTRIBUTE_LENGTH','ATTRIBUTE_FORMULA','ATTRIBUTE_AGG_TYPE','ATTRIBUTE_BASE_MEASURE','LOGICAL_OPERATOR','FILTER_ATR_NAME','SINGLE_VALUE_FILTER']
           df2=df2.append(df2_dummy)
                         
    #Local Variables DataFrame
    
       if(countlv>0):
           
         dflv90=pd.DataFrame(ITEMS_LV.items(),columns=['ID_LV','File_Name_LV'])
                  
         dflv91=pd.DataFrame(ITEMS_LV1.items(),columns=['ID_LV','LOC_DESC'])
         
         dflv92=pd.DataFrame(ITEMS_LV2.items(),columns=['ID_LV','LOC_TYPE'])
         
         dflv93=pd.DataFrame(ITEMS_LV3.items(),columns=['ID_LV','LOC_DFLT_FILTER'])
                  
         dflv94= pd.merge(dflv90,dflv91,on='ID_LV',how='left')
         
         dflv95= pd.merge(dflv94,dflv92,on='ID_LV',how='left')
         
         df_merged_lv= pd.merge(dflv95,dflv93,on='ID_LV',how='left')

         df_merged_lv['LOC_DESC']=df_merged_lv['LOC_DESC'].str.join(',')
         df_merged_lv['LOC_TYPE']=df_merged_lv['LOC_TYPE'].str.join(',')
         df_merged_lv['LOC_DFLT_FILTER']=df_merged_lv['LOC_DFLT_FILTER'].str.join(',')

         df3_dummy = df_merged_lv[["File_Name_LV","ID_LV","LOC_DESC","LOC_TYPE","LOC_DFLT_FILTER"]]   
         df3_dummy.columns=['FILE_NAME','LOC_VAR_ID','LOC_VAR_DESC','LOC_VAR_TYPE','LOC_VAR_DEFAULT_FILTER']
         df3=df3.append(df3_dummy)

    
    #Shared Dimension DataFrame

       if (countsd>0):

         dfsd93=pd.DataFrame(ITEMS_SD.items(),columns=['LJ_OBJ_URI','FILE_NAME'])
         dfsd94=pd.DataFrame(ITEMS_SD1.items(),columns=['LJ_OBJ_URI','LJ_ATTRIB_REF'])
         dfsd95=pd.DataFrame(ITEMS_SD2.items(),columns=['LJ_OBJ_URI','LJ_ATTRIB_NM'])
         dfsd96=pd.DataFrame(ITEMS_SD3.items(),columns=['LJ_OBJ_URI','LJ_CARD'])
         dfsd97=pd.DataFrame(ITEMS_SD4.items(),columns=['LJ_OBJ_URI','LJ_JO'])
         dfsd98=pd.DataFrame(ITEMS_SD5.items(),columns=['LJ_OBJ_URI','LJ_JT'])
         dfsd99=pd.DataFrame(ITEMS_SD6.items(),columns=['LJ_OBJ_URI','LJ_ATTREIB_REF_ALIAS'])
         dfsd100=pd.DataFrame(ITEMS_SD7.items(),columns=['LJ_OBJ_URI','LJ_ATTREIB_REF_ATR_NM'])

         dataframes_sd=[dfsd93,dfsd94,dfsd95,dfsd96,dfsd97,dfsd98,dfsd99,dfsd100]
         
         df_sd_merged= reduce(lambda left,right: pd.merge(left,right,on=['LJ_OBJ_URI'],how='outer'),dataframes_sd)
         df_sd_merged['LJ_ATTRIB_REF']=df_sd_merged['LJ_ATTRIB_REF'].str.join(',')
         df_sd_merged['LJ_ATTRIB_NM']=df_sd_merged['LJ_ATTRIB_NM'].str.join(',')
         df_sd_merged['LJ_CARD']=df_sd_merged['LJ_CARD'].str.join(',')
         df_sd_merged['LJ_JO']=df_sd_merged['LJ_JO'].str.join(',')
         df_sd_merged['LJ_JT']=df_sd_merged['LJ_JT'].str.join(',')
         df_sd_merged['LJ_ATTREIB_REF_ALIAS']=df_sd_merged['LJ_ATTREIB_REF_ALIAS'].str.join(',')
         df_sd_merged['LJ_ATTREIB_REF_ATR_NM']=df_sd_merged['LJ_ATTREIB_REF_ATR_NM'].str.join(',')

         df4_dummy = df_sd_merged[["FILE_NAME","LJ_OBJ_URI","LJ_ATTRIB_REF","LJ_ATTRIB_NM","LJ_CARD","LJ_JO","LJ_JT","LJ_ATTREIB_REF_ALIAS","LJ_ATTREIB_REF_ATR_NM"]]
         df4_dummy.columns = ['FILE_NAME','LJ_OBJ_URI','LJ_ATTRIB_REF','LJ_ATTRIB_NM','LJ_CARD','LJ_JO','LJ_JT','LJ_ATTREIB_REF_ALIAS','LJ_ATTREIB_REF_ATR_NM']
         df4=df4.append(df4_dummy)

    
    #Model Count
    if len(df_merged_final1.index.values) != 0:
        df_merged_final3=pd.DataFrame()
        df_md=pd.DataFrame()
        df_md_count=pd.DataFrame()
        df_model=pd.DataFrame()
        df_merged_final3=df_merged_final1[["FILE_NAME"]]
        #df_merged_final1['count']=df_merged_final1.groupby('FILE_NAME')['FILE_NAME'].transform('nunique')
        df_merged_final3=df_merged_final3.drop_duplicates()
        df_md_count['Count']=df_merged_final3.count()
        df_md_count['Component']='MODEL'
        df_model=df_md_count[["Component","Count"]]
    else:
        data_m=[['MODEL',0]]
        df_model=pd.DataFrame(data_m,columns =['Component','Count'])

    #df_md= df_md.assign(component1=['MODEL'])
    #df_model=pd.merge([df_md,df_md_count],how='inner')
    #print(df_md_count)
    #print(df_md)

    #Table Count
    if len(df_merged_final1.index.values) != 0:
       df_merged_final4=pd.DataFrame()
       df_merged_final5=pd.DataFrame()
       df_table_count=pd.DataFrame()
       df_view_count=pd.DataFrame()
       df_table=pd.DataFrame()
       df_sum_view=pd.DataFrame()
       df_merged_final4=df_merged_final1[["ID","TYPE"]]
       df_merged_final5=df_merged_final4[(df_merged_final4.TYPE=='DATA_BASE_TABLE')]
       df_merged_final5=df_merged_final5[["ID"]]
       df_merged_final5=df_merged_final5.drop_duplicates()
    #print(df_merged_final5)
       df_table_count['Count']=df_merged_final5.count()
       df_table_count['Component']='TABLE'
       df_table=df_table_count[["Component","Count"]]
    else:
        data_t=[['TABLE',0]]
        df_table=pd.DataFrame(data_t,columns =['Component','Count'])
    #View Count

    if len(df_merged_final1.index.values) != 0:    
       df_merged_final43=df_merged_final1[["FILE_NAME","TYPE"]]
       df_merged_final43=df_merged_final43[["FILE_NAME"]]
       df_merged_final43=df_merged_final43.drop_duplicates()
    
       df_merged_final43['ID']=df_merged_final43['FILE_NAME'].str.split('.').str[0]
    
       df_merged_final43=df_merged_final43[["ID"]]

       df_merged_final44=df_merged_final1[["ID","TYPE"]]
       df_merged_final45=df_merged_final44[(df_merged_final44.TYPE=='CALCULATION_VIEW')]
       df_merged_final45=df_merged_final45[["ID"]]
       df_merged_final45=df_merged_final45.drop_duplicates()

       dfv1=[df_merged_final43,df_merged_final45]

       df_v1_concat=pd.concat(dfv1,ignore_index=True)
       df_v1_concat=df_v1_concat.drop_duplicates()

       df_view_count['Count']=df_v1_concat.count()
       df_view_count['Component']='VIEW'
       df_sum_view=df_view_count[["Component","Count"]]
    else:
        data_vw=[['VIEW',0]]
        df_sum_view=pd.DataFrame(data_vw,columns =['Component','Count'])
    #Direct Attribute Count

    if len(df2.index.values) != 0:
       df_merged_final6=pd.DataFrame()
       df_merged_final7=pd.DataFrame()
       df_da_count=pd.DataFrame()
       df_da=pd.DataFrame()
       df_merged_final6=df2[["ATTRIBUTE_ID","ATTRIBUTE_TYPE"]]
       df_merged_final7=df_merged_final6[(df_merged_final6.ATTRIBUTE_TYPE=='DIRECT')]
       df_merged_final7=df_merged_final7[["ATTRIBUTE_ID"]]
       df_da_count['Count']=df_merged_final7.count()
       df_da_count['Component']='DIRECT ATTRIBUTE'
       df_da=df_da_count[["Component","Count"]]
    else:
        data_da=[['DIRECT ATTRIBUTE',0]]
        df_da=pd.DataFrame(data_da,columns =['Component','Count'])

    #Calculated Attribute Count
    if len(df2.index.values) != 0:
       df_merged_final8=pd.DataFrame()
       df_merged_final9=pd.DataFrame()
       df_catr_count=pd.DataFrame()
       df_catr=pd.DataFrame()
       df_merged_final8=df2[["ATTRIBUTE_ID","ATTRIBUTE_TYPE"]]
       df_merged_final9=df_merged_final8[(df_merged_final8.ATTRIBUTE_TYPE=='CALCULATED')]
       df_merged_final9=df_merged_final9[["ATTRIBUTE_ID"]]
       df_catr_count['Count']=df_merged_final9.count()
       df_catr_count['Component']='CALCULATED ATTRIBUTE'
       df_catr=df_catr_count[["Component","Count"]]
    else:
       data_cr=[['CALCULATED ATTRIBUTE',0]]
       df_catr=pd.DataFrame(data_cr,columns =['Component','Count'])

    # Measure Count

    if len(df2.index.values) != 0:
      df_merged_final10=pd.DataFrame()
      df_merged_final11=pd.DataFrame()
      df_m_count=pd.DataFrame()
      df_m=pd.DataFrame()
      df_merged_final10=df2[["ATTRIBUTE_ID","ATTRIBUTE_TYPE"]]
      df_merged_final11=df_merged_final10[(df_merged_final10.ATTRIBUTE_TYPE=='MEASURE')]
      df_merged_final11=df_merged_final11[["ATTRIBUTE_ID"]]
      df_m_count['Count']=df_merged_final11.count()
      df_m_count['Component']='MEASURE ATTRIBUTE'
      df_m=df_m_count[["Component","Count"]]
    else:
       data_mr=[['MEASURE ATTRIBUTE',0]]
       df_m=pd.DataFrame(data_mr,columns =['Component','Count'])

    # Restricted Measure Count
    if len(df2.index.values) != 0:
      df_merged_final12=pd.DataFrame()
      df_merged_final13=pd.DataFrame()
      df_rm_count=pd.DataFrame()
      df_rm=pd.DataFrame()
      df_merged_final12=df2[["ATTRIBUTE_ID","ATTRIBUTE_TYPE"]]
      df_merged_final13=df_merged_final12[(df_merged_final12.ATTRIBUTE_TYPE=='RESTRICTED_MEASURE')]
      df_merged_final13=df_merged_final13[["ATTRIBUTE_ID"]]
      df_rm_count['Count']=df_merged_final13.count()
      df_rm_count['Component']='RESTRICTED MEASURE ATTRIBUTE'
      df_rm=df_rm_count[["Component","Count"]]
    else:
       data_rms=[['RESTRICTED MEASURE ATTRIBUTE',0]]
       df_rm=pd.DataFrame(data_rms,columns =['Component','Count'])
    # Variable Count

    if len(df3.index.values) != 0:

      df_merged_final14=pd.DataFrame()
      df_v_count=pd.DataFrame()
      df_v=pd.DataFrame()
      df_merged_final14=df3[["LOC_VAR_ID"]]
      df_v_count['Count']=df_merged_final14.count()
      df_v_count['Component']='VARIABLE'
      df_v=df_v_count[["Component","Count"]]
    else:
      data1=[['VARIABLE',0]]
      df_v=pd.DataFrame(data1,columns =['Component','Count'])


    # Shared Dimension Count

    df_merged_final15=pd.DataFrame()
    df_sdm_count=pd.DataFrame()
    df_sdm=pd.DataFrame()
    
    
    if len(df4.index.values) != 0:
    
      df_merged_final15=df4[["LJ_OBJ_URI"]]
      df_merged_final15=df_merged_final15.drop_duplicates()
      df_sdm_count['Count']=df_merged_final15.count()
      df_sdm_count['Component']='SHARED DIMENSION'
      df_sdm=df_sdm_count[["Component","Count"]]

    else:
      
      data=[['SHARED DIMENSION',0]]
      df_sdm=pd.DataFrame(data,columns =['Component','Count'])
            
    dfc=pd.DataFrame()
    df_model_vw=pd.DataFrame()
    
    dfc=[df_model,df_table,df_sum_view,df_da,df_catr,df_m,df_rm,df_v,df_sdm]

    df_model_vw=pd.concat(dfc,ignore_index=True)

   #Detail View Count
    df_attribute=pd.DataFrame() 
    df_direct_attribute=pd.DataFrame()
    df_calculated_attribute=pd.DataFrame()
    df_measure_attribute=pd.DataFrame()
    df_rmeasure_attribute=pd.DataFrame()
    df_variable=pd.DataFrame()
    df_shared_dm=pd.DataFrame()
    df_trans=pd.DataFrame()
    df_dt_table=pd.DataFrame()
    df_intr_vw=pd.DataFrame()
    
    if len(df2.index.values) != 0:
       
     df_attribute=pd.DataFrame()
     df_direct_attribute=pd.DataFrame()
     df_view_merge=pd.DataFrame()
     df_merged_final20=pd.DataFrame()
     df_merged_final21=pd.DataFrame()
     df_merged_final22=pd.DataFrame()
     df_merged_final20=df2[["FILE_NAME","ATTRIBUTE_ID"]]
    #df_merged_final20.groupby('FILE_NAME').agg({'ATTRIBUTE_ID':['count']}).reset_index().rename(columns={'ATTRIBUTE_ID':'ATTRIBUTE_COUNT'})
     df_attribute=df_merged_final20.groupby('FILE_NAME').agg({'ATTRIBUTE_ID':'count'}).rename(columns={'ATTRIBUTE_ID':'TOTAL ATTRIBUTE'}).reset_index()
    elif len(df3.index.values) != 0:
        df_attribute = df3[["FILE_NAME"]]
        df_attribute['TOTAL ATTRIBUTE'] = '0'
        df_attribute=df_attribute.drop_duplicates()
        
    elif len(df4.index.values) != 0:
        df_attribute = df4[["FILE_NAME"]]
        df_attribute['TOTAL ATTRIBUTE'] = '0'
        df_attribute=df_attribute.drop_duplicates()
    elif len(df_merged_id.index.values) != 0:
        df_attribute = df_merged_id[["FILE_NAME"]]
        df_attribute['TOTAL ATTRIBUTE'] = '0'
        df_attribute=df_attribute.drop_duplicates()
    elif len(df_merged_final1.index.values) != 0:
        df_attribute = df_merged_final1[["FILE_NAME"]]
        df_attribute['TOTAL ATTRIBUTE'] = '0'
        df_attribute=df_attribute.drop_duplicates()
    else :
        print("Test")
    if len(df2.index.values) != 0:    
     df_merged_final21=df2[["FILE_NAME","ATTRIBUTE_ID","ATTRIBUTE_TYPE"]]
     df_merged_final22=df_merged_final21[(df_merged_final21.ATTRIBUTE_TYPE=='DIRECT')]
     df_merged_final22=df_merged_final22[["FILE_NAME","ATTRIBUTE_ID"]]
     df_direct_attribute=df_merged_final22.groupby('FILE_NAME').agg({'ATTRIBUTE_ID':'count'}).rename(columns={'ATTRIBUTE_ID':'DIRECT ATTRIBUTE'}).reset_index()
    elif len(df3.index.values) != 0:
        df_direct_attribute = df3[["FILE_NAME"]]
        df_direct_attribute['DIRECT ATTRIBUTE'] = '0'
        df_direct_attribute=df_direct_attribute.drop_duplicates()
        
    elif len(df4.index.values) != 0:
        df_direct_attribute = df4[["FILE_NAME"]]
        df_direct_attribute['DIRECT ATTRIBUTE'] = '0'
        df_direct_attribute=df_direct_attribute.drop_duplicates()
    elif len(df_merged_id.index.values) != 0:
        df_direct_attribute = df_merged_id[["FILE_NAME"]]
        df_direct_attribute['DIRECT ATTRIBUTE'] = '0'
        df_direct_attribute=df_direct_attribute.drop_duplicates()
    elif len(df_merged_final1.index.values) != 0:
        df_direct_attribute = df_merged_final1[["FILE_NAME"]]
        df_direct_attribute['DIRECT ATTRIBUTE'] = '0'
        df_direct_attribute=df_direct_attribute.drop_duplicates()
    else :
        print("Test")
        
    if len(df2.index.values) != 0:
       
      df_merged_final23=df2[["FILE_NAME","ATTRIBUTE_ID","ATTRIBUTE_TYPE"]]
      df_merged_final24=df_merged_final23[(df_merged_final23.ATTRIBUTE_TYPE=='CALCULATED')]
      df_merged_final24=df_merged_final24[["FILE_NAME","ATTRIBUTE_ID"]]
      df_calculated_attribute=df_merged_final24.groupby('FILE_NAME').agg({'ATTRIBUTE_ID':'count'}).rename(columns={'ATTRIBUTE_ID':'CALCULATED ATTRIBUTE'}).reset_index()
    elif len(df3.index.values) != 0:
        df_calculated_attribute = df3[["FILE_NAME"]]
        df_calculated_attribute['CALCULATED ATTRIBUTE'] = '0'
        df_calculated_attribute=df_calculated_attribute.drop_duplicates()
    elif len(df4.index.values) != 0:
        df_calculated_attribute = df4[["FILE_NAME"]]
        df_calculated_attribute['CALCULATED ATTRIBUTE'] = '0'
        df_calculated_attribute=df_calculated_attribute.drop_duplicates()
    elif len(df_merged_id.index.values) != 0:
        df_calculated_attribute = df_merged_id[["FILE_NAME"]]
        df_calculated_attribute['CALCULATED ATTRIBUTE'] = '0'
        df_calculated_attribute=df_calculated_attribute.drop_duplicates()
    elif len(df_merged_final1.index.values) != 0:
        df_calculated_attribute = df_merged_final1[["FILE_NAME"]]
        df_calculated_attribute['CALCULATED ATTRIBUTE'] = '0'
        df_calculated_attribute=df_calculated_attribute.drop_duplicates()
    else :
        print("Test")
        
    if len(df2.index.values) != 0:
     df_merged_final25=df2[["FILE_NAME","ATTRIBUTE_ID","ATTRIBUTE_TYPE"]]
     df_merged_final26=df_merged_final25[(df_merged_final25.ATTRIBUTE_TYPE=='MEASURE')]
     df_merged_final26=df_merged_final26[["FILE_NAME","ATTRIBUTE_ID"]]
     df_measure_attribute=df_merged_final26.groupby('FILE_NAME').agg({'ATTRIBUTE_ID':'count'}).rename(columns={'ATTRIBUTE_ID':'MEASURE ATTRIBUTE'}).reset_index()
    elif len(df3.index.values) != 0:
        df_measure_attribute = df3[["FILE_NAME"]]
        df_measure_attribute['MEASURE ATTRIBUTE'] = '0'
        df_measure_attribute=df_measure_attribute.drop_duplicates()
    elif len(df4.index.values) != 0:
        df_measure_attribute = df4[["FILE_NAME"]]
        df_measure_attribute['MEASURE ATTRIBUTE'] = '0'
        df_measure_attribute=df_measure_attribute.drop_duplicates()
    elif len(df_merged_id.index.values) != 0:
        df_measure_attribute = df_merged_id[["FILE_NAME"]]
        df_measure_attribute['MEASURE ATTRIBUTE'] = '0'
        df_measure_attribute=df_measure_attribute.drop_duplicates()
    elif len(df_merged_final1.index.values) != 0:
        df_measure_attribute = df_merged_final1[["FILE_NAME"]]
        df_measure_attribute['MEASURE ATTRIBUTE'] = '0'
        df_measure_attribute=df_measure_attribute.drop_duplicates()
    else :
        print("Test")

    if len(df2.index.values) != 0:
       
     df_merged_final27=df2[["FILE_NAME","ATTRIBUTE_ID","ATTRIBUTE_TYPE"]]
     df_merged_final28=df_merged_final27[(df_merged_final27.ATTRIBUTE_TYPE=='RESTRICTED_MEASURE')]
     df_merged_final28=df_merged_final28[["FILE_NAME","ATTRIBUTE_ID"]]
     df_rmeasure_attribute=df_merged_final28.groupby('FILE_NAME').agg({'ATTRIBUTE_ID':'count'}).rename(columns={'ATTRIBUTE_ID':'RESTRICTED MEASURE ATTRIBUTE'}).reset_index()

    elif len(df3.index.values) != 0:
        df_rmeasure_attribute = df3[["FILE_NAME"]]
        df_rmeasure_attribute['RESTRICTED MEASURE ATTRIBUTE'] = '0'
        df_rmeasure_attribute=df_rmeasure_attribute.drop_duplicates()
    elif len(df4.index.values) != 0:
        df_rmeasure_attribute = df4[["FILE_NAME"]]
        df_rmeasure_attribute['RESTRICTED MEASURE ATTRIBUTE'] = '0'
        df_rmeasure_attribute=df_rmeasure_attribute.drop_duplicates()
    elif len(df_merged_id.index.values) != 0:
        df_rmeasure_attribute = df_merged_id[["FILE_NAME"]]
        df_rmeasure_attribute['RESTRICTED MEASURE ATTRIBUTE'] = '0'
        df_rmeasure_attribute=df_rmeasure_attribute.drop_duplicates()
    elif len(df_merged_final1.index.values) != 0:
        df_rmeasure_attribute = df_merged_final1[["FILE_NAME"]]
        df_rmeasure_attribute['RESTRICTED MEASURE ATTRIBUTE'] = '0'
        df_rmeasure_attribute=df_rmeasure_attribute.drop_duplicates()
    else :
        print("Test")

    if len(df3.index.values) != 0:
        
      df_merged_final29=df3[["FILE_NAME","LOC_VAR_ID"]]
      df_merged_final30=df_merged_final29[["FILE_NAME","LOC_VAR_ID"]]
      df_variable=df_merged_final30.groupby('FILE_NAME').agg({'LOC_VAR_ID':'count'}).rename(columns={'LOC_VAR_ID':'VARIABLE'}).reset_index()
     
          
    elif len(df2.index.values) != 0:
        df_variable = df2[["FILE_NAME"]]
        df_variable['VARIABLE'] = '0'
        df_variable=df_variable.drop_duplicates()
    elif len(df4.index.values) != 0:
        df_variable = df4[["FILE_NAME"]]
        df_variable['VARIABLE'] = '0'
        df_variable=df_variable.drop_duplicates()
    elif len(df_merged_id.index.values) != 0:
        df_variable = df_merged_id[["FILE_NAME"]]
        df_variable['VARIABLE'] = '0'
        df_variable=df_variable.drop_duplicates()
    elif len(df_merged_final1.index.values) != 0:
        df_variable = df_merged_final1[["FILE_NAME"]]
        df_variable['VARIABLE'] = '0'
        df_variable=df_variable.drop_duplicates()
    else :
        print("Test")
      
    if len(df4.index.values) != 0:
    
      df_merged_final31=df4[["FILE_NAME","LJ_OBJ_URI"]]
      df_merged_final32=df_merged_final31[["FILE_NAME","LJ_OBJ_URI"]]
      df_shared_dm=df_merged_final32.groupby('FILE_NAME').agg({'LJ_OBJ_URI':'count'}).rename(columns={'LJ_OBJ_URI':'SHARED DIMENSION'}).reset_index() 
      
    elif len(df2.index.values) != 0:
        df_shared_dm = df2[["FILE_NAME"]]
        df_shared_dm['SHARED DIMENSION'] = '0'
        df_shared_dm=df_shared_dm.drop_duplicates()
    elif len(df3.index.values) != 0:
        df_shared_dm = df3[["FILE_NAME"]]
        df_shared_dm['SHARED DIMENSION'] = '0'
        df_shared_dm=df_shared_dm.drop_duplicates()
    elif len(df_merged_id.index.values) != 0:
        df_shared_dm = df_merged_id[["FILE_NAME"]]
        df_shared_dm['SHARED DIMENSION'] = '0'
        df_shared_dm=df_shared_dm.drop_duplicates()
    elif len(df_merged_final1.index.values) != 0:
        df_shared_dm = df_merged_final1[["FILE_NAME"]]
        df_shared_dm['SHARED DIMENSION'] = '0'
        df_shared_dm=df_shared_dm.drop_duplicates()
    else :
        print("Test")
    if len(df_merged_id.index.values) != 0:
        
     df_merged_final33=df_merged_id[["FILE_NAME","ID"]]
     df_merged_final34=df_merged_final33[["FILE_NAME","ID"]]
     df_merged_final34=df_merged_final34.drop_duplicates()
     df_trans=df_merged_final34.groupby('FILE_NAME').agg({'ID':'count'}).rename(columns={'ID':'TRANSFORMATION'}).reset_index()  

    elif len(df2.index.values) != 0:
        df_trans = df2[["FILE_NAME"]]
        df_trans['TRANSFORMATION'] = '0'
        df_trans=df_trans.drop_duplicates()
        
    elif len(df3.index.values) != 0:
        df_trans = df3[["FILE_NAME"]]
        df_trans['TRANSFORMATION'] = '0'
        df_trans=df_trans.drop_duplicates()
    elif len(df4.index.values) != 0:
        df_trans = df4[["FILE_NAME"]]
        df_trans['TRANSFORMATION'] = '0'
        df_trans=df_trans.drop_duplicates()
    elif len(df_merged_final1.index.values) != 0:
        df_trans = df_merged_final1[["FILE_NAME"]]
        df_trans['TRANSFORMATION'] = '0'
        df_trans=df_trans.drop_duplicates()
    else :
        print("Test")
    if len(df_merged_final1.index.values) !=0:
     df_merged_final35=df_merged_final1[["FILE_NAME","ID","TYPE"]]
     df_merged_final36=df_merged_final35[(df_merged_final35.TYPE=='DATA_BASE_TABLE')]
     df_merged_final36=df_merged_final36[["FILE_NAME","ID"]]
     df_dt_table=df_merged_final36.groupby('FILE_NAME').agg({'ID':'count'}).rename(columns={'ID':'TABLE'}).reset_index()

    elif len(df2.index.values) != 0:
        df_dt_table = df2[["FILE_NAME"]]
        df_dt_table['TABLE'] = '0'
        df_dt_table=df_dt_table.drop_duplicates()
    elif len(df3.index.values) != 0:
        df_dt_table = df3[["FILE_NAME"]]
        df_dt_table['TABLE'] = '0'
        df_dt_table=df_dt_table.drop_duplicates()
    elif len(df4.index.values) != 0:
        df_dt_table = df4[["FILE_NAME"]]
        df_dt_table['TABLE'] = '0'
        df_dt_table=df_dt_table.drop_duplicates()
    elif len(df_merged_id.index.values) != 0:
        df_dt_table = df_merged_final1[["FILE_NAME"]]
        df_dt_table['TABLE'] = '0'
        df_dt_table=df_dt_table.drop_duplicates()
    else :
        print("Test")
    if len(df_merged_final1.index.values) !=0:
      df_merged_final37=df_merged_final1[["FILE_NAME","ID","TYPE"]]
      df_merged_final38=df_merged_final37[(df_merged_final37.TYPE=='CALCULATION_VIEW')]
      df_merged_final38=df_merged_final38[["FILE_NAME","ID"]]
      df_intr_vw=df_merged_final38.groupby('FILE_NAME').agg({'ID':'count'}).rename(columns={'ID':'INTERMEDIATE VIEW'}).reset_index()

    elif len(df2.index.values) != 0:
        df_intr_vw = df2[["FILE_NAME"]]
        df_intr_vw['INTERMEDIATE VIEW'] = '0'
        df_intr_vw=df_intr_vw.drop_duplicates()
    elif len(df3.index.values) != 0:
        df_intr_vw = df3[["FILE_NAME"]]
        df_intr_vw['INTERMEDIATE VIEW'] = '0'
        df_intr_vw=df_intr_vw.drop_duplicates()
    elif len(df4.index.values) != 0:
        df_intr_vw = df4[["FILE_NAME"]]
        df_intr_vw['INTERMEDIATE VIEW'] = '0'
        df_intr_vw=df_intr_vw.drop_duplicates()
    elif len(df_merged_id.index.values) != 0:
        df_intr_vw = df_merged_final1[["FILE_NAME"]]
        df_intr_vw['INTERMEDIATE VIEW'] = '0'
        df_intr_vw=df_intr_vw.drop_duplicates()
    else :
        print("Test")     

    df_view= [df_dt_table,df_intr_vw,df_attribute,df_direct_attribute,df_calculated_attribute,df_measure_attribute,df_rmeasure_attribute,df_variable,df_shared_dm,df_trans]
    df_view_merge= reduce(lambda left,right: pd.merge(left,right,on=['FILE_NAME'],how='outer'),df_view)
    df_view_merge.rename(columns={'FILE_NAME':'MODEL NAME'},inplace=True)
    #print(df_view_merge)
    df_view_merge=df_view_merge.fillna(0)
        
    df_view_merge['TOTAL ATTRIBUTE']=df_view_merge['TOTAL ATTRIBUTE'].astype(int)
    df_view_merge['DIRECT ATTRIBUTE']=df_view_merge['DIRECT ATTRIBUTE'].astype(int)
    df_view_merge['CALCULATED ATTRIBUTE']=df_view_merge['CALCULATED ATTRIBUTE'].astype(int)
    df_view_merge['MEASURE ATTRIBUTE']=df_view_merge['MEASURE ATTRIBUTE'].astype(int)
    df_view_merge['RESTRICTED MEASURE ATTRIBUTE']=df_view_merge['RESTRICTED MEASURE ATTRIBUTE'].astype(int)
    df_view_merge['VARIABLE']=df_view_merge['VARIABLE'].astype(int)
    #df_view_merge['SHARED DIMENSION']=df_view_merge['SHARED DIMENSION'].astype(int)
    df_view_merge['TRANSFORMATION']=df_view_merge['TRANSFORMATION'].astype(int)
    df_view_merge['TABLE']=df_view_merge['TABLE'].astype(int)
    df_view_merge['INTERMEDIATE VIEW']=df_view_merge['INTERMEDIATE VIEW'].astype(int)           

    cmplxty_cond = [

    (df_view_merge['TRANSFORMATION']==0) & (df_view_merge['TABLE']==0) & (df_view_merge['INTERMEDIATE VIEW']==0),
    ((df_view_merge['TRANSFORMATION']>=0) & (df_view_merge['TRANSFORMATION']<=10)) & 
	((df_view_merge['TABLE']>=0) & (df_view_merge['TABLE']<=5)) & 
	((df_view_merge['INTERMEDIATE VIEW']>=0) & (df_view_merge['INTERMEDIATE VIEW']<=5)) & 
	((df_view_merge['TOTAL ATTRIBUTE']>=0) & (df_view_merge['TOTAL ATTRIBUTE']<=400)),
    (((df_view_merge['TRANSFORMATION']>=11) & (df_view_merge['TRANSFORMATION']<=30)) & 
	((df_view_merge['TABLE']>=0) & (df_view_merge['TABLE']<=20)) & 
	((df_view_merge['INTERMEDIATE VIEW']>=0) & (df_view_merge['INTERMEDIATE VIEW']<=10)) & 
	((df_view_merge['TOTAL ATTRIBUTE']>=0) & (df_view_merge['TOTAL ATTRIBUTE']<=500))) |
    (((df_view_merge['TRANSFORMATION']>=6) & (df_view_merge['TRANSFORMATION']<=20)) & 
	((df_view_merge['TABLE']>=6) & (df_view_merge['TABLE']<=10)) & 
	((df_view_merge['INTERMEDIATE VIEW']>=0) & (df_view_merge['INTERMEDIATE VIEW']<=10)) & 
	((df_view_merge['TOTAL ATTRIBUTE']>=0) & (df_view_merge['TOTAL ATTRIBUTE']<=500))),
    ((df_view_merge['TRANSFORMATION']>30)) & 
	((df_view_merge['TABLE']>=10) & (df_view_merge['TABLE']<=50)) & 
	((df_view_merge['INTERMEDIATE VIEW']>=0) & (df_view_merge['INTERMEDIATE VIEW']<=20)) & 
	((df_view_merge['TOTAL ATTRIBUTE']>=0) & (df_view_merge['TOTAL ATTRIBUTE']<=1000))    
	]

    cmplxty_values = ['Complexity type need to be derived manually if table,view & transformation count is 0','Simple','Medium','Complex']

    df_view_merge['COMPLEXITY'] = np.select(cmplxty_cond, cmplxty_values,default='Please enter complexity type manually')
    #print(df_view_merge)
       #Saving the dataframe to CSV Files
       #df1.to_csv('DataSource_File.csv')
    
      #df_view_merge['COMPLEXITY'] = np.select(cmplxty_cond, cmplxty_values,default='Please enter manually')
    #print(df_view_merge)
       #Saving the dataframe to CSV Files
       #df1.to_csv('DataSource_File.csv')
       
    #writer = pd.ExcelWriter(r'C:\Users\anirbdas\Documents\Parser\AnalyzerOutput.xlsx', engine='xlsxwriter')

    dir_path = path+'/Output/'+'CalculationView_' + str(datetime.now().strftime('%Y%m%d%H%M%S'))
    os.makedirs(dir_path)

    
    CV_Analyzer='\CV_Analyzer_'+ str(datetime.now().strftime('%Y%m%d%H%M%S'))+'.xlsx'    
    writer = pd.ExcelWriter(dir_path+CV_Analyzer, engine='xlsxwriter')
       
       # PUSH EACH EXCEL SHEET TO THE XLSXWRITER ENGINE

    df_model_vw.to_excel(writer, sheet_name='Model_Summary_View', index=False)
    df_view_merge.to_excel(writer, sheet_name='Model_Detail_View', index=False)
    df_merged_final1.to_excel(writer, sheet_name='DataSource_File', index=False)
    df2.to_excel(writer, sheet_name='Attribute_File', index=False)
    df3.to_excel(writer, sheet_name='Variables_File', index=False)
    df4.to_excel(writer, sheet_name='SharedDimension_File', index=False)

    #The below Dataframe df5 contains Projection information which is redundant and will be captured in df_merged_final dataframe#
    #df5.to_excel(writer, sheet_name='Calculation_View', index=False)      

    #df_merged_final_lsv.to_excel(writer, sheet_name='Logical_Seq_View', index=False)
    df_merged_rank_final.to_excel(writer, sheet_name='Logical_Seq_View', index=False)
    df_merged_id.to_excel(writer, sheet_name='Id_List', index=False)
    #df_merged_final1_lsv.to_excel(writer, sheet_name='Id1_List', index=False)   
    #df_merged_final.to_excel(writer, sheet_name='Id2_List', index=False)
    #dftest.to_excel(writer, sheet_name='dftest', index=False)
    
    writer.save()

    text_file.close()

    

    """source_input=dest + '/' + 'CalculationView_UserInput.txt'
    source_output=dest + '/' + CV_Analyzer"""

    source_input=dest+'/Input/CalculationView_UserInput.txt'
    source_output=dest+'/Output'+CV_Analyzer

    
    file_list=os.listdir(dest+'/Code')


    
    for item in file_list:
        if item.endswith(".calculationview"):
            shutil.move(item,dir_path)

    """shutil.copy(source_input,dir_path)
    shutil.copy(source_output,dir_path)"""
     
def main(): 
  
    # parse xml file 
    
    #try:

      warnings.filterwarnings("ignore")

      #xmlitems = parseXML("C:/Users/anirbdas/Documents/Parser")
      xmlitems =parseXML(input("Enter Path:"))
      
    #except:

      #print("XML File structure needs to be rechecked.File parsing is not successful!")

    #else:
      
      print("Files parsed sucessfully!")
                  
if __name__ == "__main__": 
  
    #calling main function 
     main() 

