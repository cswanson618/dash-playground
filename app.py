import streamlit as st
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt

@st.cache
def loaddf():
    Alabama = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Alabama/allcounties")
    Alaska = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Alaska/allcounties")
    Arizona = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Arizona/allcounties")
    Arkansas = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Arkansas/allcounties")
    California = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/California/allcounties")
    Colorado = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Colorado/allcounties")
    Connecticut = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Connecticut/allcounties")
    DC = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/District%20of%20Columbia/allcounties")
    Delaware = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Delaware/allcounties")
    Florida = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Florida/allcounties")
    Georgia = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Georgia/allcounties")
    Hawaii = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Hawaii/allcounties")
    Idaho = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Idaho/allcounties")
    Illinois = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Illinois/allcounties")
    Indiana = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Indiana/allcounties")
    Iowa = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Iowa/allcounties")
    Kansas = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Kansas/allcounties")
    Kentucky = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Kentucky/allcounties")
    Louisiana = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Louisiana/allcounties")
    Maine = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Maine/allcounties")
    Maryland = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Maryland/allcounties")
    Massachusetts = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Massachusetts/allcounties")
    Michigan = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Michigan/allcounties")
    Minnesota = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Minnesota/allcounties")
    Mississippi = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Mississippi/allcounties")
    Missouri = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Missouri/allcounties")
    Montana = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Montana/allcounties")
    Nebraska = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Nebraska/allcounties")
    Nevada = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Nevada/allcounties")
    New_Hampshire = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/New%20Hampshire/allcounties")
    New_Jersey = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/New%20Jersey/allcounties")
    New_Mexico = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/New%20Mexico/allcounties")
    New_York = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/New%20York/allcounties")
    North_Carolina = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/North%20Carolina/allcounties")
    North_Dakota = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/North%20Dakota/allcounties")
    Ohio = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Ohio/allcounties")
    Oklahoma = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Oklahoma/allcounties")
    Oregon = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Oregon/allcounties")
    Pennsylvania = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Pennsylvania/allcounties")
    Rhode_Island = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Rhode%20Island/allcounties")
    South_Carolina = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/South%20Carolina/allcounties")
    South_Dakota = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/South%20Dakota/allcounties")
    Tennessee = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Tennessee/allcounties")
    Texas = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Texas/allcounties")
    Utah = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Utah/allcounties")
    Vermont = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Vermont/allcounties")
    Virginia = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Virginia/allcounties")
    Washington = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Washington/allcounties")
    West_Virginia = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/West%20Virginia/allcounties")
    Wisconsin = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Wisconsin/allcounties")
    Wyoming = pd.read_json("https://api-pc6dbtrtla-uc.a.run.app/API/us/timeseries/Wyoming/allcounties")
    dfall = pd.DataFrame().append(Alabama).append(Alaska).append(Arizona).append(Arkansas).append(California).append(Colorado).append(Connecticut).append(Delaware).append(Florida).append(Georgia).append(Hawaii).append(Idaho).append(Illinois).append(Indiana).append(Iowa).append(Kansas).append(Kentucky).append(Louisiana).append(Maine).append(Maryland).append(Massachusetts).append(Michigan).append(Minnesota).append(Mississippi).append(Missouri).append(Montana).append(Nebraska).append(Nevada).append(New_Hampshire).append(New_Jersey).append(New_Mexico).append(New_York).append(North_Carolina).append(North_Dakota).append(Ohio).append(Oklahoma).append(Oregon).append(Pennsylvania).append(Rhode_Island).append(South_Carolina).append(South_Dakota).append(Tennessee).append(Texas).append(Utah).append(Vermont).append(Virginia).append(Washington).append(Wisconsin).append(Wyoming).append(DC).append(West_Virginia)
    return dfall

df = loaddf()

statelist = df["State"].unique()

st.title("COVID 19 USA Data Dashboard TEST")

statedata = st.selectbox("Select State", statelist)

datalist = []
for index, row in df.iterrows():
    if row["State"] == statedata: 
        data = (row["State"], row["County"], row["Totals as of Date"], row["Cases"], row["Deaths"])
        datalist.append(data)
        
statedf = pd.DataFrame(datalist, columns = ["State", "County", "Totals as of Date", "Cases", "Deaths"])

st.write(statedf)

countylist = []
for index, row in statedf.iterrows():
    counties = row["County"]
    countylist.append(counties)

countyn = np.array(countylist)
countyunique = np.unique(countyn)

countydata = st.selectbox("Select County", countyunique)

datalistc = []
for index, row in statedf.iterrows():
    if row["County"] == countydata: 
        datac = (row["State"], row["County"], row["Totals as of Date"], row["Cases"], row["Deaths"])
        datalistc.append(datac)
        
cdf = pd.DataFrame(datalistc, columns = ["State", "County", "Totals as of Date", "Cases", "Deaths"])

st.write(cdf)


