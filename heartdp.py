import streamlit as st
import joblib

# Load the fine-tuned model
model = joblib.load(open("fine_tuned_model.pkl", "rb"))

# Create input boxes for the data
age = st.number_input("Age", min_value=0, max_value=150, value=30)
sex = st.selectbox("Sex", ["Female", "Male"])
cp = st.selectbox(
    "Chest Pain Type",
    ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"],
)
trestbps = st.number_input(
    "Resting Blood Pressure (mm Hg)", min_value=0, max_value=300, value=120
)
chol = st.number_input(
    "Serum Cholestoral (mg/dl)", min_value=0, max_value=600, value=200
)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["False", "True"])
restecg = st.selectbox(
    "Resting Electrocardiographic Results",
    [
        "Nothing to Note",
        "ST-T Wave Abnormality",
        "Possible or Definite Left Ventricular Hypertrophy",
    ],
)
thalach = st.number_input(
    "Maximum Heart Rate Achieved", min_value=0, max_value=300, value=150
)
exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
oldpeak = st.number_input(
    "ST Depression Induced by Exercise Relative to Rest",
    min_value=0,
    max_value=10,
    value=0,
)
slope = st.selectbox(
    "Slope of the Peak Exercise ST Segment", ["Upsloping", "Flatsloping", "Downsloping"]
)
ca = st.number_input(
    "Number of Major Vessels Colored by Flourosopy", min_value=0, max_value=3, value=0
)
thal = st.selectbox(
    "Thalium Stress Result", ["Normal", "Fixed Defect", "Reversible Defect"]
)

# Convert categorical variables to numerical
sex = 1 if sex == "Male" else 0
cp_mapping = {
    "Typical Angina": 0,
    "Atypical Angina": 1,
    "Non-Anginal Pain": 2,
    "Asymptomatic": 3,
}
cp = cp_mapping[cp]
fbs = 1 if fbs == "True" else 0
restecg_mapping = {
    "Nothing to Note": 0,
    "ST-T Wave Abnormality": 1,
    "Possible or Definite Left Ventricular Hypertrophy": 2,
}
restecg = restecg_mapping[restecg]
exang = 1 if exang == "Yes" else 0
slope_mapping = {"Upsloping": 0, "Flatsloping": 1, "Downsloping": 2}
slope = slope_mapping[slope]
thal_mapping = {"Normal": 1, "Fixed Defect": 6, "Reversible Defect": 7}
thal = thal_mapping[thal]

# Create a feature vector
features = [
    [
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal,
    ]
]

# Make predictions
prediction = model.predict(features)

# Display the prediction
if prediction[0] == 1:
    st.write("The person is predicted to have heart disease.")
else:
    st.write("The person is predicted to not have heart disease.")
