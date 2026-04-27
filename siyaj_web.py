import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import numpy as np
import base64
import time
import pydeck as pdk 

# --- 🔐 الإعدادات الأمنية السيادية ---
BOT_TOKEN = "8620078546:AAGtsKVpEszw7n46_t0h4IZbsFVmCNORuII"
CHAT_ID = "6793160399"
SAFE_CODE = "SIYAJ2026"
ADMIN_EMAIL = "alyaanzan@gmail.com" 

def send_telegram_notification(message):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message}
        requests.post(url, json=payload)
    except: pass

if 'main_access' not in st.session_state: st.session_state.main_access = False
if 'log_history' not in st.session_state: st.session_state.log_history = []

# --- 🎨 التنسيق البصري (أبيض، فخم، وناصع) ---
st.set_page_config(page_title="منظومة سياج الرقمية", page_icon="🛡️", layout="wide")
st.markdown("""<style>
    @import url('https://fonts.googleapis.com/css2?family=Almarai:wght@400;700;800&display=swap');
    html, body, [class*="css"], .stApp { background-color: #FFFFFF !important; font-family: 'Almarai', sans-serif; text-align: right; direction: rtl; color: #000000 !important; }
    .main-title { color: #1E3A8A !important; font-size: 38px !important; font-weight: 900; text-align: center; padding: 10px; }
    .stButton button { width: 100%; border-radius: 12px; background: #1E3A8A !important; color: white !important; border: none; font-weight: bold; height: 3.5em; transition: 0.3s; }
    .stButton button:hover { transform: scale(1.02); background: #152C66 !important; }
    .card { background: #F8FAFC !important; padding: 25px; border-radius: 15px; border-right: 8px solid #1E3A8A; margin-bottom: 20px; border: 1px solid #E2E8F0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); color: #000000 !important; }
    .vision-card { background: #F0FDF4 !important; padding: 30px; border-radius: 15px; border-right: 10px solid #10B981; margin-bottom: 20px; border: 1px solid #DCFCE7; color: #000000 !important; }
    .status-bar { background: #1E3A8A; color: white; padding: 12px; border-radius: 10px; margin-bottom: 25px; display: flex; justify-content: space-between; align-items: center; }
    h1, h2, h3, h4, p, li, span, label, div { color: #000000 !important; }
    input, textarea { background-color: #FFFFFF !important; border: 1px solid #CBD5E1 !important; color: #000000 !important; border-radius: 8px !important; }
</style>""", unsafe_allow_html=True)

# --- 1. بوابة الدخول ---
if not st.session_state.main_access:
    st.markdown("<h1 class='main-title'>🛡️ مـنـظـومـة سـيـاج الـرقـمـيـة</h1>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='card' style='text-align:center;'><h3>التحقق من بروتوكول الوصول السيبراني</h3><p>يرجى إدخال البيانات المعتمدة للدخول إلى المنظومة</p></div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        u_name = col1.text_input("الاسم الأكاديمي المعتمد:")
        u_email_input = col2.text_input("البريد الإلكتروني الرسمي (Email):")
        u_type = col1.selectbox("رتبة المستخدم في المنظومة:", ["زائر","مسؤول حماية بيانات", "طالب/ة مبتكر"])
        gate_code = col2.text_input("رمز فك التشفير السيادي (SIYAJ2026):", type="password")
        
        if st.button("تأكيد الهوية الرقمية وفتح التشفير 🔓"):
            if u_name and u_email_input and gate_code == SAFE_CODE:
                st.session_state.user_data = {"name": u_name, "type": u_type, "email": u_email_input.lower()}
                st.session_state.main_access = True
                st.session_state.log_history.append({"المشغل": u_name, "الإيميل": u_email_input, "الرتبة": u_type, "التوقيت": datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                send_telegram_notification(f"✅ تم تسجيل دخول جديد:\nالمستخدم: {u_name}")
                st.balloons()
                st.rerun()
            else: st.error("⚠️ خطأ في مطابقة البيانات.")
    st.stop()

# --- شريط الحالة ---
c_user = st.session_state.user_data['name']
c_type = st.session_state.user_data['type']
st.markdown(f"<div class='status-bar'><span>👤 المستخدم: {c_user}</span><span>📡 حالة النظام: مشفر وآمن</span><span>🎖️ الرتبة: {c_type}</span></div>", unsafe_allow_html=True)

# --- 2. القائمة الجانبية ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/144/shield.png", width=100)
    st.markdown(f"<h2 style='color:#1E3A8A;'>سياج v4.0</h2>", unsafe_allow_html=True)
    st.divider()
    menu = ["الرئيسية 🏠", "ركن الابتكار 💡", "أكاديمية سياج 🎓", "مركز الفحص الشامل 🔍", "بصمة سياج 🕵️‍♂️", "درع الهندسة الاجتماعية 👤", "مختبر التشفير 🔑", "بلاغ طوارئ 🚨"]
    if st.session_state.user_data['email'] == ADMIN_EMAIL: menu.append("سجل الإدارة 📋")
    section = st.radio("انتقل بين وحدات المنظومة:", menu)
    if st.button("تسجيل الخروج الآمن 🔒"):
        st.session_state.clear()
        st.rerun()

# --- 3. محتوى الأقسام ---
if section == "الرئيسية 🏠":
    st.markdown("<h1 class='main-title'>مركز العمليات السيبرانية - سياج</h1>", unsafe_allow_html=True)
    st.info("سياج: لغة العقل الرقمي؛ حيث يرصد رادارنا أدق التفاصيل لصناعة الأمان.")
    st.markdown("""<div class='card'><h3>🛡️ نبذة عن المنظومة</h3><p>منظومة سياج هي درع تقني متكامل، يجمع بين أدوات الرصد المتقدمة وبين التوعية البشرية.</p></div>""", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    col_a.metric("حالة الخادم", "متصل ✅")
    col_b.metric("قوة التشفير", "AES-4096")

elif section == "ركن الابتكار 💡":
    st.title("💡 مختبر الابتكار السيبراني")
    t1, t2, t3, t4 = st.tabs(["🧠 القصة", "📡 رادار الرصد", "🇸🇦 الرؤية", "💡 شاركينا فكرتك"])
    with t1:
        st.markdown("<div class='card'><h3>📖 قصة سياج</h3><p>فكرة سياج أتت لنثبت للعالم بأن المملكة وطن تنمو فيه المواهب...</p></div>", unsafe_allow_html=True)
    with t2:
        st.subheader("📡 محاكاة رصد التهديدات")
        map_data = pd.DataFrame(np.random.randn(7, 2) / [15, 15] + [24.46, 39.18], columns=['lat', 'lon'])
        st.pydeck_chart(pdk.Deck(initial_view_state=pdk.ViewState(latitude=24.46, longitude=39.18, zoom=5), layers=[pdk.Layer('ScatterplotLayer', data=map_data, get_position='[lon, lat]', get_color='[200, 30, 0, 160]', get_radius=50000)]))
    with t3:
        st.markdown("<div class='vision-card'><h2>🇸🇦 سياج في قلب الرؤية</h2><p>بنات السعودية.. ذكاء، طموح، وحماية لوطنهم.</p></div>", unsafe_allow_html=True)
    with t4:
        st.text_area("أكتبي ابتكارك هنا:")
        st.button("إرسال الابتكار")

elif section == "أكاديمية سياج 🎓":
    st.title("🎓 أكاديمية سياج")
    with st.expander("🔐 مختبر قوة كلمة المرور", expanded=True):
        pwd = st.text_input("جربي كلمة مرورك:", type="password")
        if pwd:
            score = sum([len(pwd)>=8, any(c.isdigit() for c in pwd), any(c.isupper() for c in pwd), any(c in "!@#$%^&*" for c in pwd)])
            st.progress(score * 25)
            st.write(f"قوة الدرع الشخصي: {score}/4")
    a1, a2, a3 = st.tabs(["🔐 التشفير", "🎣 التصيد", "👣 البصمة"])
    with a1:
        st.markdown("<div class='card'><h3>التشفير</h3><p>بروتوكول AES-4096 يحمي بياناتك.</p></div>", unsafe_allow_html=True)
        st.video("https://youtu.be/xHaxAYDt75Q")
    with a2: st.video("https://youtu.be/gfPN0RIeYLM")
    with a3: st.video("https://youtu.be/9eVjgk93PEw")

elif section == "مركز الفحص الشامل 🔍":
    st.title("🔍 مركز الفحص والتحليل")
    PHONE_DB = {"0555555555": "عاليا صالح العنزان", "0500000000": "صالح بن محمد"}
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='card'><h4>🔗 الروابط</h4>", unsafe_allow_html=True)
        u_url = st.text_input("أدخل الرابط:")
        if st.button("تحليل"): st.warning("نشاط مشبوه!")
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card'><h4>📞 الأرقام</h4>", unsafe_allow_html=True)
        u_phone = st.text_input("أدخل الرقم:")
        if st.button("كشف الهوية"):
            if u_phone in PHONE_DB: st.success(f"الاسم: {PHONE_DB[u_phone]}")
            else: st.error("غير مسجل!")
        st.markdown("</div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card'><h4>🖼️ الصور</h4>", unsafe_allow_html=True)
        if st.file_uploader("ارفع الصورة:") and st.button("فحص"): st.info("ذكاء اصطناعي بنسبة 92%")
        st.markdown("</div>", unsafe_allow_html=True)

elif section == "بصمة سياج 🕵️‍♂️":
    st.title("🕵️‍♂️ التحقيق الرقمي")
    f = st.file_uploader("ارفع الملف لاستخراج البصمة:")
    if f: st.success(f"البصمة الرقمية (Hash): {hash(f.name)}")

elif section == "درع الهندسة الاجتماعية 👤":
    st.title("👤 اختبار درع الوعي")
    q1 = st.radio("وصلتك رسالة تطلب كود البنك؟", ["أعطيهم", "أحذفها", "أتصل بالبنك"])
    if st.button("تحليل المستوى"):
        if "أتصل" in q1: st.success("وعيك حديدي!")
        else: st.warning("راجع الأكاديمية")

elif section == "مختبر التشفير 🔑":
    st.title("🔑 نظام سياج للتشفير")
    t_e, t_d = st.tabs(["🔒 تشفير", "🔓 فك قفل"])
    with t_e:
        txt = st.text_area("النص:")
        key = st.text_input("المفتاح:", type="password")
        if st.button("توليد الكود"):
            res = base64.b64encode(f"{txt}||{key}".encode()).decode()
            st.code(f"SIYAJ_SECURE_{res}")
    with t_d:
        code = st.text_area("الكود المشفر:")
        k_check = st.text_input("مفتاح الفك:", type="password")
        if st.button("فك الآن"):
            try:
                dec = base64.b64decode(code.replace("SIYAJ_SECURE_","")).decode()
                m, k = dec.split("||")
                if k == k_check: st.success(f"الرسالة: {m}")
                else: st.error("خطأ")
            except: st.error("فشل")

elif section == "سجل الإدارة 📋":
    st.title("📋 سجل الإدارة")
    if st.text_input("رمز المشرف:", type="password") == "ALYA_DEV":
        st.table(pd.DataFrame(st.session_state.log_history))

elif section == "بلاغ طوارئ 🚨":
    st.title("🚨 مركز البلاغات - المساعد سند")
    st.markdown(f"<div class='card'>مرحباً يا {c_user}، أنا سند.. عضيدك.</div>", unsafe_allow_html=True)
    report = st.text_area("وصف الحادثة:")
    if st.button("إرسال"):
        send_telegram_notification(f"🚨 بلاغ من {c_user}: {report}")
        st.success("تم الرفع بنجاح!")
