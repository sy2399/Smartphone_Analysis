# Smartphone_Analysis
From smartphone data collection to modeling

## 1. Data Collection : ATM [link](https://github.com/sy2399/ATM_Automated-Time-Management)
- Smartphone Passive Sensing
- EMA (Ecological Momentary Assessment)


******
## 2. Data Preprocessing

1. to Datetime
2. Preprocessing
  - App 
    - App Categorizing (with Crawling)
    - Drop Background(e.g.,backround app - cashwalk) 
  - Location
    - GMM
3. Time Mapping : to count total duration of app usage

******
## 3. Feature Extraction
### 3-1. App
- [x] Count, Frequency  [Code Link](https://github.com/sy2399/Smartphone_Analysis/blob/master/Code/02.Feature%20Extraction/App_Features_1_Basic%20(count%2C%20frequency).ipynb, "code_link1")


- [x] 💡LDA [Code Link](https://github.com/sy2399/Smartphone_Analysis/blob/master/Code/02.Feature%20Extraction/App_Features_2_LDA%20(app%20to%20text).ipynb], "code_link2")
- [x] 💡Graph-Network [Code Link](https://github.com/sy2399/Smartphone_Analysis/blob/master/Code/02.Feature%20Extraction/App_Features_3_Graph(app%20to%20graph).ipynb], "code_link3")

### 3-2. Activity
- count, duration of each activity (moving, not moving)

### 3-3. Location
- Location change
- Time spent on Campus

### 3-4. Sleep
- sleep duration
- wakeup time, sleep on time

******
## 4. Model
### 4-1. SWB Trend Prediction 

![DP_SWB_change](https://user-images.githubusercontent.com/25919167/77882060-2be2c280-729b-11ea-9068-081062fef085.jpeg)

- Purpose
  - (1) 삶의 만족도가 증가하는 시점, 감소하는 시점 파악
  - (2) 삶의 만족도가 증가할 때의 사용자 행동 패턴 파악
  - (3) 삶의 만족도가 감소하는 시점에(1), 삶의 만족도가 증가할 때의 사용자 패턴을 추천(2)

- X : Smartphone Features (Activity, App usage, Loc, Sleep)
- Y : Subjective Well-being Trend (Increase, Decrease, No change)

- Model 
  - [x] Simple : Randomforest, LogisticRegression, Adaboost [Code Link](https://github.com/sy2399/Smartphone_Analysis/blob/master/Code/03.%20Modeling/00.%20%5BSWB%5DModel%20Simple.ipynb)
  - [x] Best : LSTM [Code Link](https://github.com/sy2399/Smartphone_Analysis/blob/master/Code/03.%20Modeling/01.%20%5BSWB%5DModel%20Deep.ipynb)

- Paper : Rhim, S., Lee, U., & Han, K. (2020). Tracking and Modeling Subjective Well-Being Using Smartphone-Based Digital Phenotype. International Conference on User Modeling, Adaptation, and Personalization (UMAP), ACM. (acceptance rate: 23%)   




******
## 5. Next Step
- [ ] 💡using GCN
- [ ] 💡using NLP
