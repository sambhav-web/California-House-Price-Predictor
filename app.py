import streamlit as st
import dill
import numpy as np
with open('model.pkl','rb') as f:
  finalmodel=dill.load(f)
st.title('California House Price Predictor')
Inc=st.number_input('MedIncome',min_value=0.0,max_value=20.0)
HouseAge=st.number_input('HouseAge',min_value=0.0,max_value=60.0)
Rooms=st.number_input('Rooms',min_value=0.0,max_value=30.0)
Bedrms=st.number_input('Bedrooms',min_value=0.0,max_value=12.0)
Population=st.number_input('Population',min_value=1.0,max_value=10000.0)
Occup=st.number_input('Occupancy Field',min_value=0.0,max_value=20.0)
Lat=st.number_input('Latitude',min_value=2.0,max_value=42.0)
Long=st.number_input('Longitude',min_value=-125.0,max_value=-110.0)
def predict(inc,age,rooms,bedrms,pop,occup,lat,lng):
  input_data=(inc,age,rooms,bedrms,pop,occup,lat,lng)
  input_array=np.array(input_data).reshape(1,-1)
  prediction=finalmodel.predict(input_array)[0]
  return prediction

if st.button('Predict Price'):
  price=predict(Inc,HouseAge,Rooms,Bedrms,Population,Occup,Lat,Long)
  st.success(f"The House Price is ${price*100000:,}")