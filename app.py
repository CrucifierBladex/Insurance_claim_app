import streamlit as st
import pandas as pd
import pickle

# Load the trained machine learning model
model_path = 'model.pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit web app title
st.title('Insurance Claim Amount Prediction')

# Sidebar with user inputs
st.sidebar.header('User Input Features')

# Collect user inputs for prediction
age = st.sidebar.slider('Age', 18, 100, 25)
gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
bmi = st.sidebar.number_input('BMI', 10.0, 50.0, 25.0)
bloodpressure = st.sidebar.number_input('Blood Pressure', 50, 200, 120)
diabetic = st.sidebar.selectbox('Diabetic', ['No', 'Yes'])
children = st.sidebar.number_input('Number of Children', 0, 10, 0)
smoker = st.sidebar.selectbox('Smoker', ['No', 'Yes'])
region = st.sidebar.selectbox('Region', ['Northeast', 'Northwest', 'Southeast', 'Southwest'])

# Convert categorical inputs to numerical values
gender = 1 if gender == 'Male' else 0
diabetic = 1 if diabetic == 'Yes' else 0
smoker = 1 if smoker == 'Yes' else 0

# Map regions to numerical values
region_mapping = {'Northeast': 0, 'Northwest': 1, 'Southeast': 2, 'Southwest': 3}
region = region_mapping[region]

# Create a DataFrame for prediction
data = pd.DataFrame({'age': [age], 'gender': [gender], 'bmi': [bmi],
                     'bloodpressure': [bloodpressure], 'diabetic': [diabetic],
                     'children': [children], 'smoker': [smoker], 'region': [region]})

# Make predictions
prediction = model.predict(data)

# Display prediction result
st.subheader('Predicted Claim Amount')
st.write(f'The predicted claim amount is ${prediction[0]:.2f}')

# Optionally, you can display additional information or visualizations here

# Streamlit web app footer
st.sidebar.text('Powered by Streamlit')

# To run the Streamlit app, use this command in your terminal:
# streamlit run your_app.py
