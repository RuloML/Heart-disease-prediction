import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(page_title="Heart Disease Screening (SCR)", layout="centered")

st.title("Heart Disease Screening — Logistic Regression (SCR)")
st.write(
    "Educational demo: estimates heart disease risk using a recall-oriented Logistic Regression model. "
    "Not medical advice."
)



@st.cache_resource
def load_model():
    repo_root = Path(__file__).resolve().parents[1]   # sube de app/ a la raíz del repo
    model_path = repo_root / "artifacts" / "model_scr.joblib"
    return joblib.load(model_path)
    artifacts_dir = repo_root / "artifacts"
    candidate_names = ["model_scr.joblib", "model_scr .joblib"]

    for name in candidate_names:
        model_path = artifacts_dir / name
        if model_path.exists():
            return joblib.load(model_path)

    available_files = ", ".join(sorted(p.name for p in artifacts_dir.glob("*.joblib"))) or "none"
    raise FileNotFoundError(
        f"Model file not found in {artifacts_dir}. "
        f"Expected one of: {candidate_names}. Available: {available_files}"
    )
model = load_model()

st.subheader("Patient inputs (SCR features)")


# Inputs aligned with SCR features
age = st.number_input("Age", min_value=1, max_value=120, value=45)
sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female (0)" if x == 0 else "Male (1)")
cp = st.selectbox("Chest Pain Type (cp)", options=[0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=50, max_value=250, value=120)
chol = st.number_input("Cholesterol (chol)", min_value=50, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", options=[0, 1])
restecg = st.selectbox("Resting ECG (restecg)", options=[0, 1, 2])
thalach = st.number_input("Max Heart Rate (thalach)", min_value=50, max_value=250, value=150)
exang = st.selectbox("Exercise Induced Angina (exang)", options=[0, 1])
oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
slope = st.selectbox("Slope", options=[0, 1, 2])

input_df = pd.DataFrame([{
    "age": age,
    "sex": sex,
    "cp": cp,
    "trestbps": trestbps,
    "chol": chol,
    "fbs": fbs,
    "restecg": restecg,
    "thalach": thalach,
    "exang": exang,
    "oldpeak": oldpeak,
    "slope": slope,
}])

st.subheader("Decision threshold")
threshold = st.slider(
    "Set probability threshold (lower = higher recall, more false positives)",
    min_value=0.05, max_value=0.95, value=0.25, step=0.01
)

with st.expander("Show input data"):
    st.dataframe(input_df)

if st.button("Predict"):
    proba = float(model.predict_proba(input_df)[0, 1])
    pred = int(proba >= threshold)

    st.subheader("Result")
    st.write(f"Predicted probability of heart disease: **{proba:.3f}**")
    st.write(f"Decision (threshold = {threshold:.2f}): **{pred}**  (1 = disease, 0 = no disease)")

    st.caption("Disclaimer: Educational demo only. Not medical advice.")
