#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pandas as pd
import numpy as np
from pandas import DataFrame as df
from datetime import date, time, datetime, timedelta


# In[ ]:


from matplotlib import rc
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import seaborn as sns
import matplotlib.font_manager as fm
plt.rcParams["figure.figsize"] = (20, 10)
register_matplotlib_converters()

## Cralwing
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import HTTPError



rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False




def toDatetime(df, timeCol , format_):

    """
     param
     - df : dataframe 
     - timeCol : columns of timestamp (ex, [timestamp] or [stime, etime])
     - format : data format (format without any space, reg)
     
     usage : util.toDatetime(df, ['stime', 'etime'], '%Y-%m-%d %H:%M:%S')
     
    """
    if len(timeCol) <=1:
        df[timeCol[0]] = df[timeCol[0]].astype(str)
        df[timeCol[0]] = df[timeCol[0]].str.replace(" ", "")
        df[timeCol[0]] = df[timeCol[0]].str.replace("-", "")
        df[timeCol[0]] = df[timeCol[0]].str.replace(":", "")
        df[timeCol[0]] = df[timeCol[0]].str.replace(".", "")


        df[timeCol[0]] = pd.to_datetime(df[timeCol[0]], format=format_)
        
    else:
        for col in timeCol:
            df[col] = df[col].astype(str)
            df[col] = df[col].str.replace(" ", "")
            df[col] = df[col].str.replace("-", "")
            df[col] = df[col].str.replace(":", "")
            df[col] = df[col].str.replace(".", "")


            df[col] = pd.to_datetime(df[col], format=format_) 
            
    return df


def getGoogleCategory(App, cat_list):
    """
    param
    - App : package Full name 
    
    usage : util.getGoogleCategory('com.no.color')

    """
#    cat_list = pd.read_csv('Cat_group.csv') #grouped category list

    url = "https://play.google.com/store/apps/details?id="+App
    google_Category = ""
    grouped_Category = ""
    try:
        html = urlopen(url)

    except HTTPError as e:

        google_Category = 'Unknown or Background'
        grouped_Category = 'Unknown or Background'
        
    else:
        source = html.read()
        html.close() 

        soup = BeautifulSoup(source,'html.parser')
        table=soup.find_all("a",{'itemprop':'genre'})
        name=soup.find_all("h1",{'itemprop':'name'})

        if(len(table)==0):
            google_Category = 'Unknown or Background'

        genre=table[0].get_text()
        appName = name[0].get_text()
        
        google_Category = genre
        
        grouped = cat_list[cat_list['App Category'] == genre]['Grouped Category'].values
        # print(grouped)
        
        if len(grouped)>0:
            grouped_Category = grouped[0]
        else:
            grouped_Category = 'NotMapped'

        # print(appName, "/ google: ", google_Category, "/category: ", grouped_Category)

        return grouped_Category


def appTimeMapping(df, columns):
    """
    Time Mapping
    ex. Category1 stime : 10:00:00 , etime 10:05:00
    10:00, 10:01, 10:02, 10:03, 10:04, 10:05 ==> Category1

    params : columns
    - columns[0] = timestamp
    - columns[1] = packageFullName
    - columns[2] = category

    - columns[3] = stime
    - columns[4] = etime
    - columns[5] = uid
    
    usage : to count duration of each category in a day

    """
    app_parse = pd.DataFrame(columns = [columns[0], columns[1], columns[2]])

    start = time.time()  # 시작 시간 저장
    count = 0;
    for index,row in df.iterrows():
       
        print("{:.2f}".format((float(index)/df.shape[0])*100), end = '\r')
        uid = row[columns[5]]
        df_stime = row[columns[3]]
        df_etime = row[columns[4]]
        app_name = row[columns[1]]
        app_cat = row[columns[2]]

        while df_stime <= df_etime:
            df_stime = df_stime + timedelta(minutes=1)
            app_parse.loc[(count), ("uid")] =  uid

            app_parse.loc[(count), ("timestamp")] =  df_stime
            app_parse.loc[(count), ("packageName")] =  app_name
            app_parse.loc[(count), ("category")] =  app_cat
            count +=1;
#             print(index)
    # print("total time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
    return app_parse

def removeDuplicate(sample, timeColName, pkColName):
    del_index = []

    for index,row in sample.iterrows():
        print("{:.2f}".format((float(index+1)/sample.shape[0])*100), end = '\r')
        tstamp = row[timeColName]
        duplicated = sample[sample[timeColName] == tstamp]

        if duplicated.shape[1]>1:
            dup_index = duplicated.index
            for idx in dup_index:
                del_index.append(idx)
            count_pkg = duplicated.groupby(pkColName).count().reset_index()
            max_pkg = count_pkg.loc[count_pkg[timeColName].idxmax()][pkColName]
            max_index = duplicated[duplicated[pkColName] == max_pkg].head(1).index[0]

            del_index = [item for item in del_index if item != max_index ]

    delDf = sample.index.isin(list(set(del_index)))
    return sample[~delDf]

def filelist(dirname):
        f_list = []
        try:
            filenames = os.listdir(dirname)
            for filename in filenames:
                name = os.path.join(dirname, filename)
                f_list.append(name)
        except:
            print("none")
        return f_list

def search(dirname, data):
    csvs = []

    try:
        filenames = os.listdir(dirname)        
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)

            if data+ ".csv" in full_filename:
                #print("full", full_filename)
                csvs.append(full_filename)
    except:
        print("none")

    return csvs
    
def make_df(data_file):
    df_all = pd.DataFrame()
    count = 0
    for dfile in data_file: 
        if len(dfile) > 0:
            if count ==0:
                df_all = pd.read_csv(dfile[0])   
            else:
                tmp_all = pd.read_csv(dfile[0])   
                df_all = pd.concat([df_all, tmp_all])
        count = count + 1
    return df_all
    

def labeling(r_id, score, compare_id, compare_score):
    result = 0;
    if np.isnan(compare_id) != True:
        if r_id == compare_id:
            if score < compare_score:
                result = 0
                
            elif score > compare_score:
                result = 1
                
            elif score == compare_score:
                result = 2
                
        print(r_id, compare_id, score, compare_score, result)
        return result

