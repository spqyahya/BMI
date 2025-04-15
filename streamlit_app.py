import streamlit as st
import time
import random

st.set_page_config(page_title="BMI Game", page_icon="⚖️", layout="centered")

# شخصيات مساعد افتراضي
assistant_faces = ["(•◡•)", "(•‿•)", "(ง'̀-'́)ง", "(✿◠‿◠)", "(ಠ_ಠ)", "(☞ﾟヮﾟ)☞"]
face = random.choice(assistant_faces)

# ترحيب تفاعلي
st.markdown(f"<h2 style='text-align: center;'>مرحبًا بك في <span style='color:#e74c3c;'>لعبة BMI!</span> {face}</h2>", unsafe_allow_html=True)
st.markdown("### هل أنت مستعد لمعرفة مستوى قوتك؟")
st.markdown("---")

# إدخال البيانات
weight = st.slider("اختر وزنك بالكيلوغرام:", min_value=30, max_value=200, step=1)
height_cm = st.slider("اختر طولك بالسنتيمتر:", min_value=100, max_value=220, step=1)

col1, col2 = st.columns([1, 1])
with col1:
    calculate = st.button("ابدأ التحدي!")
with col2:
    restart = st.button("أعد المحاولة")

if calculate:
    with st.spinner("جارٍ التحليل..."):
        time.sleep(2)
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)

        result_color = "#2ecc71" if 18.5 <= bmi < 25 else "#f39c12" if bmi < 30 else "#e74c3c"
        st.markdown(f"<h3 style='text-align: center; color:{result_color}'>نتيجتك: {bmi:.2f}</h3>", unsafe_allow_html=True)

        messages = {
            "thin": ["أنت خفيف مثل الريشة!", "نحتاج نعطيك بيتزا... أو 2", "أين اختفيت؟!"],
            "normal": ["ممتاز! مثل أبطال الألعاب", "استمر هكذا، أنت رائع!", "اللياقة عندك نار!"],
            "over": ["أوه، قليلاً زيادة!", "نصيحة: العب جيم أكثر", "فيك شحم بطل!"],
            "obese": ["لازم تدخل تحدي الدايت!", "كلنا نمر بفترة زيادة...", "وقتك تنقذ نفسك!"]
        }

        if bmi < 18.5:
            st.info(random.choice(messages["thin"]))
        elif 18.5 <= bmi < 25:
            st.success(random.choice(messages["normal"]))
        elif 25 <= bmi < 30:
            st.warning(random.choice(messages["over"]))
        else:
            st.error(random.choice(messages["obese"]))

        level = "🌱 مبتدئ" if bmi < 18.5 else "⚡ متوازن" if bmi < 25 else "🔥 تحتاج تطوير"
        st.markdown(f"<h4 style='text-align: center;'>مستواك: {level}</h4>", unsafe_allow_html=True)

if restart:
    st.experimental_rerun()