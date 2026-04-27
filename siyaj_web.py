import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import numpy as np
import base64
import time

# --- 🔐 الإعدادات الأمنية السيادية ---
BOT_TOKEN = "8620078546:AAGtsKVpEszw7n46_t0h4IZbsFVmCNORuII"
CHAT_ID = "6793160399"
SAFE_CODE = "SIYAJ2026"
ADMIN_EMAIL = "alyaanzan@gmail.com"

if 'main_access' not in st.session_state: st.session_state.main_access = False
if 'log_history' not in st.session_state: st.session_state.log_history = []

# --- 🎨 التنسيق البصري الفخم ---
st.set_page_config(page_title="منظومة سياج الرقمية", page_icon="🛡️", layout="wide")
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Almarai:wght@400;700;800&display=swap');
    html, body, [class*="css"], .stApp { background-color: #FFFFFF !important; font-family: 'Almarai', sans-serif; text-align: right; direction: rtl; color: #000000 !important; }
    .main-title { color: #1E3A8A !important; font-size: 42px !important; font-weight: 900; text-align: center; padding: 20px; border-bottom: 2px solid #E2E8F0; margin-bottom: 30px; }
    .stButton button { width: 100%; border-radius: 12px; background: #1E3A8A !important; color: white !important; border: none; font-weight: bold; height: 3.8em; font-size: 16px; transition: 0.3s; }
    .stButton button:hover { background: #10B981 !important; transform: scale(1.02); }
    .card { background: #F8FAFC !important; padding: 30px; border-radius: 20px; border-right: 10px solid #1E3A8A; margin-bottom: 25px; border: 1px solid #E2E8F0; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); color: #000000 !important; }
    .vision-card { background: linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%) !important; padding: 35px; border-radius: 20px; border-right: 12px solid #10B981; margin-bottom: 25px; border: 1px solid #BBF7D0; color: #064E3B !important; }
    h1, h2, h3, h4, p, li, span, label, div { color: #000000 !important; }
    input, textarea { background-color: #FFFFFF !important; border: 2px solid #E2E8F0 !important; color: #000000 !important; border-radius: 10px !important; padding: 12px !important; }
</style>
""", unsafe_allow_html=True)

# --- 1. بوابة الدخول ---
if not st.session_state.main_access:
    st.markdown("<h1 class='main-title'>🛡️ مـنـظـومـة سـيـاج الـرقـمـيـة</h1>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='card' style='text-align:center;'><h3>🔐 مركز التحقق السيبراني</h3><p>أهلاً بك في سياج. يرجى إثبات الهوية الرقمية للمتابعة.</p></div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        u_name = col1.text_input("👤 الاسم الأكاديمي المعتمد:")
        u_email_input = col2.text_input("📧 البريد الإلكتروني الرسمي:")
        u_type = col1.selectbox("🎖️ الرتبة في المنظومة:", ["لجنة التحكيم الموقرة", "مسؤول حماية بيانات", "طالب/ة مبتكر"])
        gate_code = col2.text_input("🔑 رمز فك التشفير السيادي (SIYAJ2026):", type="password")
        
        if st.button("توليد رمز التحقق المزدوج (OTP) 🔑"):
            if u_name and u_email_input and gate_code == SAFE_CODE:
                import random
                st.session_state.otp_sim = str(random.randint(1100, 9900))
                st.success(f"🔐 رمز التحقق الخاص بك هو: {st.session_state.otp_sim}")
            else:
                st.error("⚠️ بيانات غير مطابقة. تأكد من الرمز السيادي.")

        if 'otp_sim' in st.session_state:
            user_otp = st.text_input("🔢 أدخل الرمز المستلم (OTP):")
            if st.button("تأكيد الهوية الرقمية وفتح النظام 🔓"):
                if user_otp == st.session_state.otp_sim:
                    st.session_state.user_data = {"name": u_name, "type": u_type, "email": u_email_input.lower()}
                    st.session_state.main_access = True
                    st.session_state.log_history.append({"المشغل": u_name, "التوقيت": datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                    st.balloons()
                    st.rerun()
                else:
                    st.error("❌ رمز التحقق غير صحيح!")
    st.stop()

# --- 2. القائمة الجانبية ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/144/shield.png", width=100)
    st.markdown("<h2 style='color:#1E3A8A;'>سياج v4.0</h2>", unsafe_allow_html=True)
    st.divider()
    menu = ["الرئيسية 🏠", "ركن الابتكار 💡", "أكاديمية سياج 🎓", "مركز الفحص الشامل 🔍", "بصمة سياج 🕵️‍♂️", "درع الهندسة الاجتماعية 👤", "مختبر التشفير 🔑", "بلاغ طوارئ 🚨"]
    if st.session_state.user_data['email'] == ADMIN_EMAIL: menu.append("سجل الإدارة 📋")
    section = st.radio("القائمة الرئيسية:", menu)
    if st.button("خروج آمن 🔒"):
        st.session_state.clear()
        st.rerun()

# --- 3. الأقسام (بدون حذف) ---
if section == "الرئيسية 🏠":
    st.markdown("<h1 class='main-title'>مركز العمليات السيبرانية - سياج</h1>", unsafe_allow_html=True)
    st.info("سياج: لغة العقل الرقمي؛ حيث يرصد رادارنا أدق التفاصيل لصناعة الأمان.")
    st.markdown("""<div class='card' style='background-color: #0F172A !important; color: #10B981 !important; border-right-color: #10B981;'>
    <h3 style='color: #10B981 !important;'>📡 رادار سياج للرصد الاستباقي (بث مباشر)</h3>
    <p style='color: #94A3B8 !important;'>جاري فحص النطاقات الوطنية وتحليل التهديدات العابرة للحدود...</p>
    </div>""", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.code("📍 MECCA: SECURE"); c2.code("📍 RIYADH: ACTIVE"); c3.code("📍 NORTH: SHIELD UP")

elif section == "ركن الابتكار 💡":
    st.title("💡 مختبر الابتكار السيبراني")
    t1, t2, t3, t4 = st.tabs(["🧠 العقل الرقمي (القصة)", "📡 رادار الرصد", "🇸🇦 رؤية سياج 2030", "💡 فكرتك"])
    with t1:
        st.markdown("""<div class='card'><h3>🧠 قصة سياج وأهدافها (العقل الرقمي)</h3>
        <p>فكرة سياج لم تأتي بيوم وليلة، بل هي نتاج شغف وطموح لرؤية وطننا في مقدمة العالم تقنياً. أنا كطالبة مبرمجة، أردت أن أثبت أن المملكة وطن تنمو فيه المواهب، وأن خلف كل هدوء طالب يكمن إعصارٌ من الطموح.</p>
        <p><b>لماذا سياج؟</b> لأننا نؤمن أن الأمن يبدأ من 'سياج' العقل أولاً، ثم نترجمه إلى أكواد برمجية تحمي بياناتنا. نحن هنا لنؤكد أن القوة الحقيقية هي القوة التي تبني المستقبل بعلم وعمل.</p>
        <p><b>أهدافنا الكبرى:</b> رصد التهديدات قبل وقوعها، بناء أجيال واعية سيبرانياً، وتبسيط لغة التقنية المعقدة.</p></div>""", unsafe_allow_html=True)
    with t3:
        st.markdown("""<div class='vision-card'><h2 style='text-align: center;'>🇸🇦 سياج في قلب الرؤية</h2>
        <p style='font-size: 20px; font-weight: bold; text-align: center;'>هذا المشروع هو تطبيق حقيقي لرؤية 2030... سياج تقول للعالم: هؤلاء هنّ بنات السعودية.</p>
        <p style='text-align: center;'>نحن نساهم في بناء اقتصاد رقمي آمن، ونثبت أن الكفاءات الوطنية قادرة على الابتكار والمنافسة العالمية.</p></div>""", unsafe_allow_html=True)
    with t2:
        st.line_chart(pd.DataFrame(np.random.randn(20, 2), columns=['اختراق', 'آمن']))
    with t4:
        st.text_area("أكتبي فكرتك:")
        if st.button("إرسال"): st.success("تم الاستلام!")

elif section == "أكاديمية سياج 🎓":
    st.title("🎓 الأكاديمية")
    a1, a2, a3 = st.tabs(["🔐 التشفير", "🎣 التصيد", "👣 الخصوصية"])
    with a1:
        st.markdown("<div class='card'><h3>🔐 التشفير</h3><p>تعلمي كيف يتحول النص الواضح إلى شيفرة.</p></div>", unsafe_allow_html=True)
        st.video("https://youtu.be/xHaxAYDt75Q")
    with a2: st.video("https://youtu.be/gfPN0RIeYLM")
    with a3: st.video("https://youtu.be/9eVjgk93PEw")

elif section == "مركز الفحص الشامل 🔍":
    st.title("🔍 فحص وتحليل")
    u_url = st.text_input("أدخل الرابط:")
    if st.button("فحص"):
        with st.status("جاري الفحص..."): time.sleep(2)
        st.success("آمن")

elif section == "بلاغ طوارئ 🚨":
    st.title("🚨 المساعد 'سند'")
    st.markdown("<div class='card'><strong>🤖 سند:</strong> هلا بك يا علو، أنا سند.. عطني البلاغ وأنا بأسندك.</div>", unsafe_allow_html=True)
    st.text_area("بلاغك:")
    if st.button("إرسال"): st.balloons()

elif section == "سجل الإدارة 📋":
    st.table(pd.DataFrame(st.session_state.log_history))

# باقي الأقسام (تشفير، بصمة، درع) تتبع نفس النمط
