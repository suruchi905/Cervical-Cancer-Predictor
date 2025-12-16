%%writefile app.py
import streamlit as st

st.set_page_config(page_title="Cervical Cancer Risk Predictor", layout="centered")

st.title("🧬 Cervical Cancer Risk Predictor")
st.markdown("Provide your information below to estimate your risk level.")

# --- User Inputs ---
age = st.slider("Age", 18, 70)
partners = st.number_input("Number of sexual partners", min_value=0)
smokes = st.checkbox("Do you smoke?")
stds = st.checkbox("Do you have a history of STDs?")
hpv = st.checkbox("Have you received an HPV vaccine?")

# --- Prediction Logic ---
if st.button("🔍 Predict Risk"):
    risk_score = 0.2  # base risk

    if partners >= 4:
        risk_score += 0.2
    elif partners >= 2:
        risk_score += 0.1

    if smokes:
        risk_score += 0.2
    if stds:
        risk_score += 0.2
    if not hpv:
        risk_score += 0.2

    risk_score = min(risk_score, 1.0)

    st.markdown(f"### 🧪 Your Risk Score: `{risk_score:.2f}`")

    if risk_score > 0.7:
        st.error("⚠️ High Risk: Please consult a gynecologist immediately.")
    elif 0.4 < risk_score <= 0.7:
        st.warning("🩺 Moderate Risk: Screening recommended within 6 months.")
    else:
        st.success("✅ Low Risk: Routine check-up in 3 years.")

st.caption("This is a basic demo app and not a substitute for professional medical advice.")
