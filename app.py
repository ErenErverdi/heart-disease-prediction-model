import streamlit as st
from knn_algo import Predict

st.markdown(
    "<h1 style='text-align: center;'>Heart Disease Predictor</h1>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input("Age")
    trestbps = st.text_input("Resting Blood Pressure")
    restecg = st.selectbox("Resting ECG", [0, 1, 2])
    oldpeak = st.text_input("Old Peak")

with col2:
    sex = st.selectbox("Sex", ["Male", "Female"])
    chol = st.text_input("Cholesterol")
    thalach = st.text_input("Max Heart Rate")
    slope = st.text_input("Slope")
    thal = st.text_input("Thal")

with col3:
    cp = st.selectbox(
        "Chest Pain",
        ["typical angina", "atypical angina",
         "pain that is not angina", "asymptomatic"]
    )
    fbs = st.text_input("Fasting Blood Sugar")
    exang = st.selectbox("Exercise Induced Angina", ["no", "yes"])
    ca = st.text_input("Coronary Arteries")

st.write("")

if st.button("Predict"):
    try:
        # Encode categorical
        sex = 1 if sex == "Male" else 0
        exang = 1 if exang == "yes" else 0

        cp_map = {
            "typical angina": 0,
            "atypical angina": 1,
            "pain that is not angina": 2,
            "asymptomatic": 3
        }
        cp = cp_map[cp]

        # Convert to numeric
        age = int(age)
        trestbps = int(trestbps)
        chol = int(chol)
        fbs = int(fbs)
        thalach = int(thalach)
        oldpeak = float(oldpeak)
        slope = int(slope)
        ca = int(ca)
        thal = int(thal)

        prediction = Predict(
            age, sex, cp, trestbps, chol,
            fbs, restecg, thalach,
            exang, oldpeak, slope, ca, thal
        )

        if prediction == 1:
            st.error("You have a risk of heart disease")
        else:
            st.success("You do not have a risk of heart disease")

    except ValueError:
        st.warning("Fill the empity boxes!!!")

with st.expander("Input Informations"):
    st.markdown("""

### Resting ECG (restecg)
- **0** → Normal  
- **1** → ST-T wave abnormality  
- **2** → Left ventricular hypertrophy  

---

### Fasting Blood Sugar (fbs)
- **1** → > 120 mg/dl (High)  
- **0** → ≤ 120 mg/dl (Normal)  

---


### Slope (ST Segment Slope)
- **0** → Upsloping  
- **1** → Flat  
- **2** → Downsloping  

---

### Thal
- **1** → Normal  
- **2** → Fixed defect  
- **3** → Reversible defect  

---

### Coronary Arteries (ca)
- **0** → 0 major vessels  
- **1** → 1 major vessel  
- **2** → 2 major vessels  
- **3** → 3 major vessels  
""")
