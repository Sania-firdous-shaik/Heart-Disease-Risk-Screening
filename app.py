import streamlit as st
import pandas as pd
import joblib

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Heart Disease Risk Screening",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# LOAD MODEL
# =====================================================

@st.cache_resource
def load_model():
    return joblib.load("heart_disease_model.joblib")


model = load_model()

# Original model class representing heart disease.
# Verify this against the training dataset.
DISEASE_CLASS = 0

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #142D4E;
    --blue: #2563EB;
    --teal: #0F766E;
    --background: #F3F6FB;
    --white: #FFFFFF;
    --text: #172B4D;
    --muted: #53657D;
    --border: #D8E1EC;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: var(--background);
    color: var(--text);
}

[data-testid="stMain"] {
    background: var(--background);
}

[data-testid="stHeader"] {
    background: var(--background);
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background: #142D4E !important;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

[data-testid="stSidebar"] hr {
    border-color: #49617E !important;
}

/* MAIN HEADINGS */

.main-title {
    font-size: 36px;
    font-weight: 800;
    color: #142D4E !important;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 15px;
    color: #53657D !important;
    margin-bottom: 25px;
}

/* INPUT LABELS */

[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] label {
    color: #243B5A !important;
    font-weight: 600 !important;
}

/* NUMBER INPUT */

[data-testid="stNumberInput"] input {
    background: #FFFFFF !important;
    color: #172B4D !important;
    border: 1px solid #B8C7D9 !important;
    border-radius: 9px !important;
}

/* SELECTBOX */

[data-baseweb="select"] > div {
    background: #FFFFFF !important;
    color: #172B4D !important;
    border: 1px solid #B8C7D9 !important;
    border-radius: 9px !important;
}

[data-baseweb="select"] * {
    color: #172B4D !important;
}

[data-baseweb="popover"] {
    background: #FFFFFF !important;
}

[data-baseweb="popover"] * {
    color: #172B4D !important;
}

/* SECTION HEADINGS */

.section-heading {
    font-size: 20px;
    font-weight: 700;
    color: #142D4E !important;
}

.section-subtitle {
    font-size: 13px;
    color: #53657D !important;
    margin-bottom: 18px;
}

/* BUTTONS */

div.stButton > button,
div.stFormSubmitButton > button {
    background: #2563EB !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    min-height: 48px;
}

div.stButton > button:hover,
div.stFormSubmitButton > button:hover {
    background: #1D4ED8 !important;
    color: #FFFFFF !important;
}

/* METRIC CARDS */

[data-testid="stMetric"] {
    background: #FFFFFF !important;
    border: 1px solid #D8E1EC !important;
    border-radius: 14px;
    padding: 18px;
}

[data-testid="stMetricLabel"] {
    color: #53657D !important;
}

[data-testid="stMetricValue"] {
    color: #142D4E !important;
}

/* RESULT CARD */

.result-card {
    background: #142D4E !important;
    padding: 30px;
    border-radius: 18px;
    border: 1px solid #29486D;
    color: #FFFFFF !important;
    margin-top: 15px;
}

.result-card h2,
.result-card h3,
.result-card p {
    color: #FFFFFF !important;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #53657D !important;
    font-size: 12px;
    padding: 25px 0;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# SIDEBAR NAVIGATION
# =====================================================

with st.sidebar:

    st.markdown("# ❤️ Cardio AI")
    st.markdown("### INTELLIGENT HEALTH SCREENING")

    st.divider()

    page = st.radio(
        "Navigation",
        ["Risk Assessment", "Model Overview"],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("### About the Project")

    st.write(
        "A machine-learning-based heart disease "
        "risk screening prototype using clinical "
        "parameters and a trained classification model."
    )

    st.divider()

    st.markdown("### Model Information")

    st.write("**Algorithm:** Logistic Regression")
    st.write("**Dataset:** Cleveland Heart Disease")
    st.write("**Features:** 13")

    st.divider()

    st.caption("AI & DATA SCIENCE PROJECT")
    st.caption("EDUCATIONAL USE ONLY")


# =====================================================
# PAGE 1: RISK ASSESSMENT
# =====================================================

if page == "Risk Assessment":

    st.markdown(
        '<div class="main-title">Heart Health Assessment</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Enter clinical parameters to generate an AI-based '
        'heart disease screening result.'
        '</div>',
        unsafe_allow_html=True
    )

    # TOP METRICS

    col1, col2, col3 = st.columns(3)

    col1.metric("Assessment Type", "AI Screening")
    col2.metric("Selected Model", "Logistic Regression")
    col3.metric("Input Features", "13")

    st.write("")

    # INPUT FORM

    with st.form("heart_assessment_form"):

        # PERSONAL INFORMATION

        st.markdown(
            '<div class="section-heading">'
            '01 · Personal Information'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-subtitle">'
            'Enter basic patient information.'
            '</div>',
            unsafe_allow_html=True
        )

        c1, c2 = st.columns(2)

        with c1:

            age = st.number_input(
                "Age (years)",
                min_value=20,
                max_value=100,
                value=45
            )

            sex = st.selectbox(
                "Sex",
                options=[0, 1],
                format_func=lambda x: (
                    "Female" if x == 0 else "Male"
                )
            )

        with c2:

            cp = st.selectbox(
                "Chest Pain Type",
                options=[0, 1, 2, 3],
                format_func=lambda x: f"Category {x}"
            )

            trestbps = st.number_input(
                "Resting Blood Pressure (mm Hg)",
                min_value=80,
                max_value=250,
                value=120
            )

        st.divider()

        # CLINICAL MEASUREMENTS

        st.markdown(
            '<div class="section-heading">'
            '02 · Clinical Measurements'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-subtitle">'
            'Enter the recorded clinical measurements.'
            '</div>',
            unsafe_allow_html=True
        )

        c1, c2 = st.columns(2)

        with c1:

            chol = st.number_input(
                "Serum Cholesterol (mg/dL)",
                min_value=100,
                max_value=600,
                value=200
            )

            fbs = st.selectbox(
                "Fasting Blood Sugar",
                options=[0, 1],
                format_func=lambda x: (
                    "No" if x == 0 else "Yes"
                )
            )

            restecg = st.selectbox(
                "Resting ECG",
                options=[0, 1, 2],
                format_func=lambda x: f"Category {x}"
            )

        with c2:

            thalach = st.number_input(
                "Maximum Heart Rate Achieved",
                min_value=60,
                max_value=220,
                value=150
            )

            exang = st.selectbox(
                "Exercise-Induced Angina",
                options=[0, 1],
                format_func=lambda x: (
                    "No" if x == 0 else "Yes"
                )
            )

            oldpeak = st.number_input(
                "ST Depression (Oldpeak)",
                min_value=0.0,
                max_value=6.0,
                value=1.0,
                step=0.1
            )

        st.divider()

        # ADDITIONAL PARAMETERS

        st.markdown(
            '<div class="section-heading">'
            '03 · Additional Parameters'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-subtitle">'
            'Enter the remaining clinical parameters.'
            '</div>',
            unsafe_allow_html=True
        )

        c1, c2 = st.columns(2)

        with c1:

            slope = st.selectbox(
                "ST Slope",
                options=[0, 1, 2],
                format_func=lambda x: f"Category {x}"
            )

            ca = st.selectbox(
                "Number of Major Vessels",
                options=[0, 1, 2, 3]
            )

        with c2:

            thal = st.selectbox(
                "Thalassemia Category",
                options=[0, 1, 2, 3],
                format_func=lambda x: f"Category {x}"
            )

        st.write("")

        submitted = st.form_submit_button(
            "❤️ Analyze Heart Health",
            use_container_width=True
        )

    # =====================================================
    # PREDICTION
    # =====================================================

    if submitted:

        input_data = pd.DataFrame([{

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
            "ca": ca,
            "thal": thal,

            # ENGINEERED FEATURES

            "chol_per_age": chol / (age + 1e-9),
            "bps_per_age": trestbps / (age + 1e-9)

        }])

        try:

            # ORIGINAL MODEL PREDICTION

            raw_prediction = int(
                model.predict(input_data)[0]
            )

            # UPDATED CLASS MAPPING
            # Original class 0 -> displayed class 1
            # Original class 1 -> displayed class 0

            prediction = int(
                raw_prediction == DISEASE_CLASS
            )

            # UPDATED PROBABILITY MAPPING

            probabilities = model.predict_proba(
                input_data
            )[0]

            positive_class_index = list(
                model.classes_
            ).index(DISEASE_CLASS)

            score = float(
                probabilities[positive_class_index]
            )

            st.divider()

            st.markdown("## Screening Results")

            if prediction == 1:

                st.markdown(
                    f"""
                    <div class="result-card">
                        <p>MODEL SCREENING OUTPUT</p>
                        <h2>Elevated Risk Classification</h2>
                        <p>
                            The remapped classification
                            is class 1.
                        </p>
                        <h3>Model score: {score * 100:.1f}%</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f"""
                    <div class="result-card">
                        <p>MODEL SCREENING OUTPUT</p>
                        <h2>Lower Risk Classification</h2>
                        <p>
                            The remapped classification
                            is class 0.
                        </p>
                        <h3>Model score: {score * 100:.1f}%</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.write("")

            # ASSESSMENT SUMMARY

            st.markdown("### Assessment Summary")

            c1, c2, c3 = st.columns(3)

            c1.metric("Age", f"{age} years")
            c2.metric("Cholesterol", f"{chol} mg/dL")
            c3.metric("Resting BP", f"{trestbps} mm Hg")

            st.markdown("### Model Output Score")

            st.progress(float(score))

            st.caption(
                f"This score corresponds to original model "
                f"class {DISEASE_CLASS}, displayed as class 1. "
                "It is not a clinically validated probability."
            )

            st.warning(
                "This application is an educational screening "
                "prototype and does not provide a medical diagnosis. "
                "The configured class mapping must be verified "
                "against the training dataset. "
                "The prediction should not be used to make medical "
                "decisions. Consult a qualified healthcare professional "
                "for medical evaluation."
            )

        except Exception as e:

            st.error(f"Prediction failed: {e}")


# =====================================================
# PAGE 2: MODEL OVERVIEW
# =====================================================

elif page == "Model Overview":

    st.markdown(
        '<div class="main-title">Model Performance Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Evaluation results from the trained heart disease '
        'classification model.'
        '</div>',
        unsafe_allow_html=True
    )

    # HOLDOUT TEST METRICS

    st.markdown("### Logistic Regression Performance")

    c1, c2, c3 = st.columns(3)

    c1.metric("Accuracy", "88.52%")
    c2.metric("Precision", "83.87%")
    c3.metric("Recall", "92.86%")

    c1, c2, c3 = st.columns(3)

    c1.metric("F1 Score", "88.14%")
    c2.metric("ROC-AUC", "96.54%")
    c3.metric("Evaluation", "Holdout Test")

    st.caption(
        "These are the original training notebook metrics. "
        "Class-specific metrics must be recalculated if "
        "the positive class definition changes."
    )

    st.divider()

    # MODEL COMPARISON

    st.markdown("### Cross-Validation Model Comparison")

    comparison = pd.DataFrame({

        "Model": [
            "Logistic Regression",
            "Random Forest",
            "Voting Ensemble",
            "XGBoost"
        ],

        "Repeated CV AUC": [
            0.897080,
            0.893195,
            0.892095,
            0.872247
        ]

    })

    st.bar_chart(
        comparison.set_index("Model"),
        y="Repeated CV AUC",
        color="#2563EB"
    )

    st.dataframe(
        comparison.style.format({
            "Repeated CV AUC": "{:.4f}"
        }),
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "Logistic Regression was selected because it achieved "
        "the highest repeated cross-validation AUC among "
        "the evaluated models."
    )

    st.divider()

    # PROJECT INFORMATION

    st.markdown("### Project Information")

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("#### Dataset")

        st.write("Cleveland Heart Disease Dataset")
        st.write("Original dimensions: 303 rows × 14 columns")
        st.write("Target converted into binary classification.")

    with c2:

        st.markdown("#### Model Pipeline")

        st.write("Missing value imputation")
        st.write("Feature engineering")
        st.write("Categorical encoding")
        st.write("Numerical feature scaling")
        st.write("Logistic Regression classifier")

    st.divider()

    # ENGINEERED FEATURES

    st.markdown("### Engineered Features")

    st.code(
        """
chol_per_age = chol / age
bps_per_age = trestbps / age
        """,
        language="python"
    )

    st.caption(
        "The deployed pipeline uses a small numerical epsilon "
        "in the denominator to avoid division by zero."
    )

    st.warning(
        "These evaluation metrics are from the notebook's "
        "reported experiment. They do not establish clinical "
        "validity or guarantee performance on new populations."
    )


# =====================================================
# FOOTER
# =====================================================

st.markdown(
    """
    <div class="footer">
        ❤️ Heart Disease Risk Screening |
        Machine Learning Project |
        Educational Use Only
    </div>
    """,
    unsafe_allow_html=True
)