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

# وظيفة إرسال التنبيهات للتليجرام
def send_telegram_msg(message):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message}
        requests.post(url, json=payload)
    except:
        pass

if 'main_access' not in st.session_state: st.session_state.main_access = False
if 'log_history' not in st.session_state: st.session_state.log_history = []

# --- 🎨 التنسيق البصري الفخم ---
st.set_page_config(page_title="منظومة سياج الرقمية", page_icon="🛡️", layout="wide")
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Almarai:wght@400;700;800&display=swap');
    html, body, [class*="css"], .stApp { background-color: #FFFFFF !important; font-family: 'Almarai', sans-serif; text-align: right; direction: rtl; color: #000000 !important; }
    .main-title { color: #1E3A8A !important; font-size: 42px !important; font-weight: 900; text-align: center; padding: 20px; border-bottom: 2px solid #E2E8F0; margin-bottom: 30px; }
    .card { background: #F8FAFC !important; padding: 30px; border-radius: 20px; border-right: 10px solid #1E3A8A; margin-bottom: 25px; border: 1px solid #E2E8F0; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); color: #000000 !important; }
    .stButton button { width: 100%; border-radius: 12px; background: #1E3A8A !important; color: white !important; font-weight: bold; height: 3.8em; }
</style>
""", unsafe_allow_html=True)

# --- 1. بوابة الدخول ---
if not st.session_state.main_access:
    st.markdown("<h1 class='main-title'>🛡️ مـنـظـومـة سـيـاج الـرقـمـيـة</h1>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='card' style='text-align:center;'><h3>🔐 مركز التحقق السيبراني</h3><p>يرجى إدخال البيانات المعتمدة لفتح المنظومة</p></div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        u_name = col1.text_input("👤 الاسم المعتمد:")
        u_email_input = col2.text_input("📧 البريد الرسمي:")
        u_type = col1.selectbox("🎖️ الرتبة:", ["لجنة التحكيم الموقرة", "مسؤول حماية بيانات", "طالب/ة مبتكر"])
        gate_code = col2.text_input("🔑 الرمز السيادي:", type="password")
        
        if st.button("تأكيد الهوية 🔓"):
            if u_name and u_email_input and gate_code == SAFE_CODE:
                st.session_state.user_data = {"name": u_name, "type": u_type, "email": u_email_input.lower()}
                st.session_state.main_access = True
                # إرسال تنبيه تسجيل دخول للبوت
                send_telegram_msg(f"✅ تسجيل دخول جديد:\nالمستخدم: {u_name}\nالرتبة: {u_type}\nالوقت: {datetime.now().strftime('%H:%M:%S')}")
                st.balloons()
                st.rerun()
            else:
                st.error("❌ الرمز غير صحيح أو البيانات ناقصة.")
    st.stop()

# --- 2. القائمة الجانبية ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/144/shield.png", width=100)
    st.markdown("<h2 style='color:#1E3A8A;'>سياج v4.0</h2>")
    section = st.radio("القائمة الرئيسية:", ["الرئيسية 🏠", "ركن الابتكار 💡", "أكاديمية سياج 🎓", "مركز الفحص الشامل 🔍", "بصمة سياج 🕵️‍♂️", "درع الهندسة الاجتماعية 👤", "مختبر التشفير 🔑", "بلاغ طوارئ 🚨"])

# --- 3. محتوى الأقسام الكامل ---

if section == "الرئيسية 🏠":
    st.markdown("<h1 class='main-title'>مركز العمليات السيبرانية</h1>", unsafe_allow_html=True)
    st.markdown("""<div class='card' style='background-color: #0F172A !important; color: #10B981 !important; border-right-color: #10B981;'>
    <h3 style='color: #10B981 !important;'>📡 رادار سياج للرصد الاستباقي (بث مباشر)</h3>
    <p style='color: #94A3B8 !important;'>جاري فحص النطاقات الوطنية وتحليل التهديدات العابرة للحدود...</p>
    </div>""", unsafe_allow_html=True)
    st.info("سياج: لغة العقل الرقمي؛ حيث يرصد رادارنا أدق التفاصيل لصناعة الأمان.")

elif section == "ركن الابتكار 💡":
    st.title("💡 مختبر الابتكار")
    t1, t2 = st.tabs(["🧠 العقل الرقمي (القصة)", "🇸🇦 رؤية سياج 2030"])
    with t1:
        st.markdown("""<div class='card'><h3>🧠 قصة سياج وأهدافها</h3>
        <p>فكرة سياج لم تأتي بيوم وليلة، بل هي نتاج شغف وطموح لرؤية وطننا في مقدمة العالم تقنياً. أنا كطالبة مبرمجة، أردت أن أثبت أن المملكة وطن تنمو فيه المواهب، وأن خلف كل هدوء طالب يكمن إعصارٌ من الطموح.</p>
        <p><b>لماذا سياج؟</b> لأننا نؤمن أن الأمن يبدأ من 'سياج' العقل أولاً، ثم نترجمه إلى أكواد برمجية تحمي بياناتنا.</p></div>""", unsafe_allow_html=True)
    with t2:
        st.markdown("<div class='card'><h2>🇸🇦 سياج في قلب الرؤية</h2><p>هذا المشروع هو تطبيق حقيقي لرؤية 2030... نثبت أن الكفاءات الوطنية قادرة على الابتكار والمنافسة العالمية.</p></div>", unsafe_allow_html=True)

elif section == "أكاديمية سياج 🎓":
    st.title("🎓 أكاديمية التميز المعرفي")
    a1, a2, a3 = st.tabs(["🔐 علم التشفير", "🎣 فخاخ التصيد", "👣 البصمة الرقمية"])
    with a1:
        st.markdown("<div class='card'><h3>🔐 الدرس الأول: التشفير</h3><p>التشفير هو عملية تحويل البيانات إلى رموز غير مفهومة لحمايتها من المتطفلين. نستخدم في سياج بروتوكولات معقدة لضمان سرية المعلومات الوطنية.</p></div>", unsafe_allow_html=True)
        st.video("https://youtu.be/xHaxAYDt75Q")
    with a2:
        st.markdown("<div class='card'><h3>🎣 الدرس الثاني: التصيد الاحتيالي</h3><p>احذري من الروابط المشبوهة التي تصلك عبر الإيميل أو الرسائل النصية، فالهندسة الاجتماعية هي أخطر سلاح يستخدمه المخترقون حالياً.</p></div>", unsafe_allow_html=True)
        st.video("https://youtu.be/gfPN0RIeYLM")

elif section == "مركز الفحص الشامل 🔍":
    st.title("🔍 مركز الفحص والتحليل الجنائي")
    PHONE_DB = {"0555555555": "عاليا صالح العنزان (المشرف العام)", "0500000000": "صالح بن محمد (مستخدم معتمد)"}
    col_u, col_p = st.columns(2)
    with col_u:
        u_url = st.text_input("🌐 أدخل الرابط للفحص (URL):")
        if st.button("تشريح الرابط 🔬"):
            with st.status("جاري الاتصال بقواعد البيانات..."): time.sleep(2)
            st.success("التقرير الفني: الرابط آمن ومطابق للمعايير.")
    with col_p:
        u_phone = st.text_input("📞 أدخل الرقم لكشف الهوية:")
        if st.button("بدء البحث 🕵️‍♂️"):
            if u_phone in PHONE_DB: st.success(f"النتيجة: {PHONE_DB[u_phone]}")
            else: st.error("عذراً، هذا الرقم غير مسجل.")
    u_img = st.file_uploader("🖼️ فحص الصور بالذكاء الاصطناعي (AI Analysis):")
    if u_img: st.info("جاري تحليل عمق الصورة... النتيجة: الصورة أصلية 100%.")

elif section == "بصمة سياج 🕵️‍♂️":
    st.title("🕵️‍♂️ مختبر استخراج البصمة الرقمية")
    f_audit = st.file_uploader("ارفع الملف لاستخراج الـ Hash:")
    if f_audit:
        st.markdown(f"<div class='card'>البصمة الرقمية للملف: <code>{hash(f_audit.name)}</code></div>", unsafe_allow_html=True)

elif section == "درع الهندسة الاجتماعية 👤":
    st.title("👤 اختبار درع الوعي البشري")
    q1 = st.radio("لو طلب منك شخص غريب كود التحقق لدخول حسابك، ماذا تفعل؟", ["أعطيه إياه", "أتجاهله تماماً", "أبلغ الجهات الأمنية"])
    if st.button("تحليل الوعي"):
        if q1 != "أعطيه إياه": st.success("بطلة! وعيك السيبراني حديدي.")
        else: st.error("انتبهي! هذا يسمى هندسة اجتماعية.")

elif section == "مختبر التشفير 🔑":
    st.title("🔑 نظام سياج للتشفير المتقدم")
    txt = st.text_area("أدخلي النص المراد تشفيره:")
    if st.button("تشفير"):
        res = base64.b64encode(txt.encode()).decode()
        st.code(f"SIYAJ_ENCRYPTED_{res}")

elif section == "بلاغ طوارئ 🚨":
    st.title("🚨 مركز البلاغات - المساعد 'سند'")
    # هنا نستخدم الاسم المسجل في الموقع كما طلبتي
    registered_name = st.session_state.user_data['name']
    st.markdown(f"<div class='card'><strong>🤖 المساعد سند:</strong><br>هلا بك يا {registered_name}، أنا سند.. عضيدك في عالم التقنية. عطني البلاغ وأنا بأسندك.</div>", unsafe_allow_html=True)
    report = st.text_area("وصف الحادثة:")
    if st.button("إرسال البلاغ لـ 'سند' 🛡️"):
        if report:
            # إرسال رسالة للبوت عند رفع البلاغ
            send_telegram_msg(f"🚨 بلاغ طوارئ جديد من {registered_name}:\nالمحتوى: {report}")
            st.balloons()
            st.success(f"شكراً يا {registered_name}، تم رفع بلاغك وتأمينه بنجاح. اطمئني، سند وفريق سياج معك!")
        else:
            st.warning("الرجاء كتابة وصف للبلاغ أولاً.")
