import streamlit as st

st.set_page_config(page_title="حاسبة BMI", page_icon="⚖️", layout="centered")

st.markdown("<h2 style='text-align: center; color: #2c3e50;'>حاسبة مؤشر كتلة الجسم (BMI)</h2>", unsafe_allow_html=True)
st.markdown("---")

# إدخال البيانات
weight = st.number_input("أدخل وزنك بالكيلوغرام:", min_value=1.0, format="%.2f")
height_cm = st.number_input("أدخل طولك بالسنتيمتر:", min_value=1.0, format="%.2f")

# حساب BMI
if st.button("احسب"):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    st.markdown(f"### مؤشر كتلة الجسم (BMI): `{bmi:.2f}`")

    if bmi < 18.5:
        st.info("أنت تعاني من النحافة")
    elif 18.5 <= bmi < 25:
        st.success("وزنك طبيعي")
    elif 25 <= bmi < 30:
        st.warning("تعاني من زيادة الوزن")
    else:
        st.error("تعاني من السمنة")