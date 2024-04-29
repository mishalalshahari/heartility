import numpy as np # type: ignore
import pickle
import streamlit as st # type: ignore
import requests

# Loading the saved model
loaded_model = pickle.load(open('./model/trained_model.sav', 'rb'))

# Function for prediction
def heart_disease_prediction(input_data):
    prediction = loaded_model.predict([input_data])[0]
    return prediction

# Function to get medical suggestions from AI model
def get_medical_suggestions(input_data):
    # Construct the request payload
    payload = {
        "contents": [{
            "parts": [{
                "text": "Medical suggestions based on input parameters: {}".format(input_data)
            }]
        }]
    }

    # Define the API endpoint URL
    api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyAfcQCLyAb2-9rbjBMyEHyErpVTjx1ty34"

    # Add the API key to the headers
    headers = {
        "Content-Type": "application/json"
    }

    # Make the API request
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        if response.status_code == 200:
            suggestions = response.json()["candidates"][0]["content"]["parts"][0]["text"]
            return suggestions
        else:
            return "Error: Unable to fetch medical suggestions. Status code: {}".format(response.status_code)
    except Exception as e:
        return "Error: {}".format(str(e))

# UI
def main():
    # Set the page title and favicon
    st.sidebar.markdown("<h1>Welcome in <span style='color:#d11111'>Heartility ❤️</span></h1>", unsafe_allow_html=True)

    # Create an expander in the sidebar
    with st.sidebar.expander("About"):
        # HTML content explaining the purpose of the application
        st.write(
        """
            <div style='text-align: justify;'>
                Cardiovascular diseases, including heart attacks and disorders, constitute a significant global health challenge, with millions of lives lost each year. Heartility is here to help you assess your heart's health with ease and convenience. Simply input your medical parameters, and Heartility will provide you with a prediction regarding the presence or absence of heart disease. Additionally, you can explore personalized medical suggestions generated based on your input parameters, providing further insights and recommendations for maintaining heart health. Take the first step towards a healthier heart with Heartility today!
            </div>
        """,
        unsafe_allow_html=True)

    
    with st.sidebar.expander("How to Use"):
        # Markdown content explaining how to use the application
        st.markdown(
            """
            1. **Enter Medical Parameters:** Use the interactive sliders and dropdown menus to input various medical parameters related to your heart health, such as age, gender, chest pain type, blood pressure, cholesterol levels, and more.

            2. **Predict Heart Disease:** Click the "Predict" button to analyze the input parameters and receive a prediction regarding the presence or absence of heart disease.

            3. **Review Medical Report:** After prediction, explore a detailed medical report summary, including key information such as age, gender, medical parameters, and the prediction outcome.

            4. **Access Medical Suggestions:** Explore personalized medical suggestions generated based on your input parameters, providing further insights and recommendations for maintaining heart health.
            """
        )
    
    with st.sidebar.expander("Help & Support"):
        # Provide contact information for help or support
        st.write("For any queries or assistance, please contact us at:")
        st.write("☎ Call us at: +91 9252365332")
        st.write("✉ Email us at: help@heartility.com")
        st.write("➤ Naini, Allahabad, Uttar Pradesh, India - 211008")

    # Setting up the app title and sidebar
    st.title("Know your heart's health now! 🩺")
    st.write("Enter your medical parameters to predict the presence of heart disease and receive personalized medical suggestions.")

    with st.container(border = True):
        # Sidebar Inputs with Help Sections
        age = st.slider("Age", 20, 100, 50, help="Age of the patient in years")
        sex = st.radio("Gender", ("Male", "Female"), help="Gender of the patient")
        cp = st.selectbox("Chest Pain Type", ("Typical Angina", "Atypical Angina", "Non-anginal pain", "Asymptotic"), help="Type of chest pain experienced")
        trestbps = st.slider("Resting Blood Pressure (mmHg)", 90, 200, 120, help="Resting blood pressure (in mmHg)")
        chol = st.slider("Serum Cholesterol (mg/dl)", 100, 600, 200, help="Serum cholesterol level (in mg/dl)")
        fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", ("True", "False"), help="Fasting blood sugar level (>120 mg/dl)")
        restecg = st.selectbox("Resting ECG", ("Normal", "Having ST-T wave abnormality", "Left ventricular hypertrophy"), help="Resting electrocardiographic results")
        thalach = st.slider("Max Heart Rate Achieved", 50, 220, 150, help="Maximum heart rate achieved")
        exang = st.radio("Exercise Induced Angina", ("Yes", "No"), help="Exercise induced angina")
        oldpeak = st.slider("ST Depression", 0.0, 6.0, 0.0, help="ST depression induced by exercise relative to rest")
        slope = st.selectbox("Peak Exercise ST Segment", ("Upsloping", "Flat", "Downsloping"), help="Slope of the peak exercise ST segment")
        ca = st.slider("Number of Major Vessels", 0, 3, 0, help="Number of major vessels colored by flourosopy")
        thal = st.slider("Thalassemia", 0, 3, 2, help="Thalassemia")

        # Mapping categorical inputs to numerical values
        sex = 1 if sex == "Male" else 0
        cp_mapping = {"Typical Angina": 0, "Atypical Angina": 1, "Non-anginal pain": 2, "Asymptotic": 3}
        cp = cp_mapping[cp]
        fbs = 1 if fbs == "True" else 0
        restecg_mapping = {"Normal": 0, "Having ST-T wave abnormality": 1, "Left ventricular hypertrophy": 2}
        restecg = restecg_mapping[restecg]
        exang = 1 if exang == "Yes" else 0
        slope_mapping = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
        slope = slope_mapping[slope]

        # Button for prediction
        if st.button("Predict"):
            input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            prediction = heart_disease_prediction(input_data)
            if prediction == 1:
                st.success("Prediction: The person does not have heart disease.")
            else:
                st.error("Prediction: The person have heart disease.")
            
            st.empty()

            # Medical report summary
            with st.expander("See medical report"):
                st.subheader("Medical Report Summary")
                st.write("Age:", age)
                st.write("Gender:", "Male" if sex == 1 else "Female")
                st.write("Chest Pain Type:", cp)
                st.write("Resting Blood Pressure (mmHg):", trestbps)
                st.write("Serum Cholesterol (mg/dl):", chol)
                st.write("Fasting Blood Sugar > 120 mg/dl:", "Yes" if fbs == 1 else "No")
                st.write("Resting ECG:", restecg)
                st.write("Max Heart Rate Achieved:", thalach)
                st.write("Exercise Induced Angina:", "Yes" if exang == 1 else "No")
                st.write("ST Depression:", oldpeak)
                st.write("Peak Exercise ST Segment:", slope)
                st.write("Number of Major Vessels:", ca)
                st.write("Thalassemia:", thal)
                st.write("\n")

            # Fetch and display medical suggestions
            with st.sidebar.expander("See Medical Suggestions"):
                medical_suggestions = get_medical_suggestions(input_data)
                st.subheader("Medical Suggestions")
                st.write(medical_suggestions)

if __name__ == "__main__":
    main()
