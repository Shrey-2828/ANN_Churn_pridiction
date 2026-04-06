import numpy as np
import steamlit as st
import joblib

# Page configuration
st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="centered"
)

model=joblib.load('model.sav')

def predict(data):
    ans=model.predict(data)
    return ans[0]

st.title("Customer Churn Prediction..")

Credit_Score = st.number_input('Credit_score',min_value=0.0)
Age = st.number_input('Age',min_value=0,max_value=110)
Tenure = st.number_input('Tenure',min_value=0,max_value=10)


    
    