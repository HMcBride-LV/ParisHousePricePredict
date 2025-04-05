!pip install streamlit
import streamlit as st
import joblib

model = joblib.load('/content/Paris_Housing_Prediction.pkl')

st.title('Paris Housing Price Prediction')
st.write('Predict the house price in Paris')

squareMeters = st.number_input('Enter Desired Square Meters')
numberOfRooms = st.number_input('Enter Desired Number Of Rooms')
hasYard = st.checkbox('Has Yard')
hasPool = st.checkbox('Has Pool')
floors = st.number_input('Enter Desired Number of Floors')
cityCode = st.number_input('Enter Desired City Code')
cityPartRange = st.number_input('Enter Desired City Part Range: 1 - 10')
numPrevOwners = st.number_input('Enter Desired Number of Previous Owners')
made = st.number_input('Enter Desired Year of Build')
isNewBuilt = st.checkbox('New Build?')
hasStormProtector	= st.checkbox('Has Storm Protectors')
basement = st.number_input('Enter Desired Basement Size in Square Meters')
attic = st.number_input('Enter Desired Attic Size in Square Meters')
garage = st.number_input('Enter Desired Attic Size in Square Meters')
hasStorageRoom = st.checkbox('Has Storage Room')
hasGuestRoom = st.number_input('Enter Desired Number Of Guest Rooms')

if st.button('Predict Price'):
  features = [[squareMeters, 
               numberOfRooms, 
               hasYard, hasPool, 
               floors, 
               cityCode, 
               cityPartRange, 
               numPrevOwners, 
               made, 
               isNewBuilt, 
               hasStormProtector, 
               basement, 
               attic, 
               garage, 
               hasStorageRoom, 
               hasGuestRoom]]

               prediction = model.predict([features])[0]
               st.write(f'Your predicted price is: {prediction}')
