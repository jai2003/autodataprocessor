import streamlit as st 
import pandas as pd
import numpy as np 
st.title("Data Autopreprocessor")
uploaded_file = st.file_uploader("Please choose a CSV file")
if uploaded_file is not None:  
  df = pd.read_csv(uploaded_file)
  st.write(df)
st.text("choose the percentage of missing values present to drop down columns")
c=st.number_input("choose number")
c=c/100
df3=df[df.columns[df.isnull().mean() < c]]
st.write(df3.isnull().sum())
df3=pd.get_dummies(df3)
df3=df3.drop_duplicates()
df3=df3.dropna(how='all')
st.write(df3.shape)
option = st.selectbox('How would you like to fill the null values?',('Mean', 'Median', 'Mode')) 
if option == "Mean":
   df3.fillna(df3.mean(),inplace=True)
elif option == "Mode":
  for i in df3.columns:
    num=df3[i].mode()[0]
    df3[i].fillna(num,inplace=True)
elif option == "Median":
    df3.fillna(df3.median(),inplace=True)
st.write(df3.isnull().sum())
st.write(df.skew())
st.write(df.skew().mean())
o = st.selectbox('How would you like to fill the null values?',('z-score', 'IQR','default'))
l=[]
l=df.select_dtypes(include=['int','float64'])
st.write(l)
st.write(df3)
st.write(df3.isnull().sum())
st.write(df3.shape)
if o=='default':
 for i in l:
   if df3[i].skew()==0:
     lower=df3[i].mean()-3*df3[i].std()
     upper=df3[i].mean()+3*df3[i].std()
     df3=df3[(df3[i]<upper)|(df3[i]>lower)]
   else:
     p1=df3[i].quantile(0.25)
     p2=df3[i].quantile(0.75)
     iqr=p2-p1
     lower=p1-(1.5*iqr)
     upper=p2+(1.5*iqr)
     df3=df3[((df3[i]<upper)|(df3[i]>lower))]
if o=='IQR':
    for i in l: 
     p1=df3[i].quantile(0.25)
     p2=df3[i].quantile(0.75)
     iqr=p2-p1
     lower=p1-(1.5*iqr)
     upper=p2+(1.5*iqr)
     df3=df3[((df3[i]<upper)|(df3[i]>lower))]
if o=='z-score':
   for i in l:
    if df3[i].skew()==0:
      lower=df3[i].mean()-3*df3[i].std()
      upper=df3[i].mean()+3*df3[i].std()
      df3=df3[(df3[i]<upper)|(df3[i]>lower)]

st.write(df3)
st.write(df3.isnull().sum())
st.write(df3.shape)