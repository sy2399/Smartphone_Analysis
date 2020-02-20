# Smartphone_Analysis
From smartphone data collection to modeling

## 1. Data Collection

link : https://github.com/sy2399/ATM_Automated-Time-Management


## 2. Data Preprocessing
### 2-1. App
1. to Datetime
2. Drop Background(e.g.,backround app - cashwalk) 
3. App Categorizing (with Crawling)

Result : [uid, date, stime, etime, packageName, Category]

4. Time Mapping : to count total duration of app usage

Result : [timestamp, package, Category]

## 3. Feature Extraction
### 3-1. App
- Count, Freauency
  * count of each category in a day (Using categorized data)
  * transition count of category (Using categorized data)
  * duration of each category in a day (Using time_mapped data)
- LDA
  * 유저의 앱 사용 기록을 카테고리화 (google-play store)
  * 유저의 일별 모든 앱 사용의 카테고리를 하나의 문서로 취급
  * LDA 적용: 일별 앱 사용을 문서화 하여, 일별 앱 사용 패턴의 Topic 도출
  * ISSUE : Communication 카테고리의 사용 count 가 너무 많음


  (file : Code/02.Feature Extraction/LDA_TopicModeling)
  
- Graph

