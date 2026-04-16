import numpy as np
import pickle
import streamlit as st

# Loading the Saved Model
loaded_model = pickle.load(open("C:/Users/Lenovo/OneDrive/Desktop/Diabites ML Project/training model.sav", "rb"))

# Creating a function for prediction

def diabetes_prediction(input_data):
    
     # changing the array as we are predicting for one instance
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance 
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)


    if (prediction[0] == 0):
        print("The Person is Not Diabetic")
    else:
        print("The person is Diabetic")
        
def main():
    
    #giving a title
    st.title("Diabetes Prediction Web Apps")
    
    # Getting The input data from the user
    
    Pregnancies = st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Glucose Level")
    BloodPressure = st.text_input("Blood Pressure value")
    SkinThickness = st.text_input("Skin Thickness Value")
    Insulin = st.text_input("Insulin Level")
    BMI = st.text_input("BMI Value")
    DiabetesPedigreeFuntion = st.text_input("Diabetes Pedigree Funtion")
    Age = st.text_input("Age of the Person")
    
    # code for prediction
    diagnosis = " "
    
    # Creating a button for prediction
    
    if st.button("Diabetes Test Result"):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFuntion, Age])
        
    st.success(diagnosis)
    
if __name__ == '__main__':
     main()