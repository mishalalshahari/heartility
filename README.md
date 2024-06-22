# Heart Disease Prediction ❤️

<div style="display: flex; justify-content: center; align-items: center; width: 100%; margin: 20px;">
  <img src="https://github.com/mishalalshahari/heartility/blob/main/blob/main/images/background.png" height="285" style="object-fit: contain; margin: 10px; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);" />
</div>

## Overview

Heartilty is a comprehensive heart disease prediction system that leverages machine learning algorithms to predict the likelihood of heart disease based on various factors. The system consists of a frontend built using React, a backend developed using Node.js and Express, and a database powered by MongoDB. Additionally, the system integrates with a Python-based core project, Heartilty Core, which is deployed on Streamlit and interacted with through a sandbox environment.

<div style="display: flex; justify-content: center; align-items: center; width: 100%; margin: 20px;">
  <img src="https://github.com/mishalalshahari/heartility/blob/main/blob/main/images/architecture.png" height="250" style="object-fit: contain; margin: 10px; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);" />
  <img src="https://github.com/mishalalshahari/heartility/blob/main/blob/main/images/workflow.png" height="250" style="object-fit: contain; margin: 10px; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);" />
</div>


## How to Use
- Visit the deployed project at https://heartility.onrender.com
- Login using your Google account or create a new account.
- Click the "Heartility" button to predict heart disease.
- Fill in the required input fields to get a heart disease prediction.
- Click the "Predict" button to see the result.
- For additional inforrmation about you're predicted result click on "Medical Suggestions" button on sidebar .

## Setup

To use the app, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/mishalalshahari/heartility.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   pip install -U streamlit
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Once the app is running, you can input the parameters such as age, gender, chest pain type, etc., in the sidebar. After inputting the parameters, click on the "Predict" button to get the prediction result and medical suggestions.

## Input Parameters

The following input parameters are available in the sidebar:

- **Age**: Age of the patient in years.
- **Gender**: Gender of the patient (Male/Female).
- **Chest Pain Type**: Type of chest pain experienced.
- **Resting Blood Pressure (mmHg)**: Resting blood pressure in millimeters of mercury (mmHg).
- **Serum Cholesterol (mg/dl)**: Serum cholesterol level in milligrams per deciliter (mg/dl).
- **Fasting Blood Sugar > 120 mg/dl**: Fasting blood sugar level greater than 120 mg/dl.
- **Resting ECG**: Resting electrocardiographic results.
- **Max Heart Rate Achieved**: Maximum heart rate achieved during exercise.
- **Exercise Induced Angina**: Presence of exercise-induced angina.
- **ST Depression**: ST depression induced by exercise relative to rest.
- **Peak Exercise ST Segment**: Slope of the peak exercise ST segment.
- **Number of Major Vessels**: Number of major vessels colored by flourosopy.
- **Thalassemia**: Thalassemia type.

## Medical Suggestions

The app also provides medical suggestions based on the input parameters. These suggestions are generated using a machine learning model trained on medical data. After making a prediction, the app displays relevant medical suggestions to help users understand potential health risks and preventive measures.

## Contributing
Contributions to the project are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.

## Deployement
The project is deployed on [Render](https://render.com/) and can be accessed at:
- For hdps - core visit [here >>>](https://hdps-heartility.streamlit.app/)
- For complete Project visit [here >>>](https://heartility.onrender.com/)

## License

This project is licensed under the MIT License. See the [`LICENSE`](LICENSE) file for details.

## Acknowledgments
- [[Mishal Al Shahari](https://github.com/mishalalshahari/heartility)] for developing the Heartilty project
- [[Navneet](https://github.com/navneetguptacse/heartility), [Ashwani Singh](https://github.com/iemashwani/heartility), [Om Prakash](https://github.com/<user_name>/heartility)] for their contributions to the project

I hope this README file provides a comprehensive overview of the Heartilty project! Let me know if you need any further modifications.

**Note:** This project is for educational purposes and should not be used as a substitute for professional medical advice.
