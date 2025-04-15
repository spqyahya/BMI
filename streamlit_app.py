import streamlit as st
import time

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
        background-image: linear-gradient(to top left, rgba(255,255,255,0.9), rgba(240,244,247,0.7));
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }
    .stButton > button {
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #2980b9;
        transform: scale(1.05);
    }
    .result {
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        padding-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h2 style='text-align: center; color: #2c3e50;'>حاسبة مؤشر كتلة الجسم (BMI)</h2>", unsafe_allow_html=True)
st.markdown("---")

# واجهة الإدخال
with st.container():
    weight = st.number_input("أدخل وزنك بالكيلوغرام:", min_value=1.0, format="%.2f")
    height_cm = st.number_input("أدخل طولك بالسنتيمتر:", min_value=1.0, format="%.2f")

    col1, col2 = st.columns([1, 1])
    with col1:
        calc = st.button("احسب")
    with col2:
        reset = st.button("إعادة")

# الحساب
if calc:
    with st.spinner("جارٍ الحساب..."):
        time.sleep(1.8)
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        st.markdown(f"<div class='result'>مؤشر كتلة الجسم (BMI): {bmi:.2f}</div>", unsafe_allow_html=True)

        time.sleep(0.6)
        if bmi < 18.5:
            st.info("أنت تعاني من النحافة")
        elif 18.5 <= bmi < 25:
            st.success("وزنك طبيعي")
        elif 25 <= bmi < 30:
            st.warning("تعاني من زيادة الوزن")
        else:
            st.error("تعاني من السمنة")

if reset:
    st.experimental_rerun()