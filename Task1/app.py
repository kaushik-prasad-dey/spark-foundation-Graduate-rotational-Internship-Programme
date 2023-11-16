#import streamlit 
#by default port is 8501 
import streamlit as st
import numpy as np
import joblib
st.title("Linear regression web application")
#model path
my_model_path="linear_regressor_model.sav"
#load your joblib model
model=joblib.load(my_model_path)
#required one user input
user_input= st.text_input("How many hours student studied!!")

#create button Make prediction
if st.button("Make Prediction"):
    #convert the userinput float
    numeric_value = np.float64(user_input)
    #now once it is convert we can reshape that data 1d to 2d array
    reshaped_my_data= np.array(numeric_value).reshape(-1,1)
    prediction = model.predict(reshaped_my_data)
    st.write(f'if a student studies for {numeric_value} hrs/day, then his/her score might be : {prediction}')
