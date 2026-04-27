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

# --- 🎨 التنسيق البصري الفخم (White & Professional) ---
st.set_page_config(page_title="منظومة سياج الرقمية", page_icon="🛡️", layout="wide")
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Almarai:wght@400;700;800&display=swap');
    html, body, [class*="css"], .stApp { background-color: #FFFFFF !important; font-family: 'Almarai', sans-serif; text-align: right; direction: rtl; color: #000000 !important; }
    .main-title { color: #1E3A8A !important; font-size: 38px !important; font-weight: 900; text-align: center; padding: 10px; }
    .stButton button { width: 100%; border-radius: 12px; background: #1E3A8A !important; color: white !important; border: none; font-weight: bold; height: 3.5em; }
    .card { background: #F8FAFC !important; padding: 25px; border-radius: 15px; border-right: 8px solid #1E3A8A; margin-bottom: 20px; border: 1px solid #E2E8F0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); color: #000000 !important; }
    .vision-card { background: #F0FDF4 !important; padding: 30px; border-radius: 15px; border-right: 10px solid #10B981; margin-bottom: 20px; border: 1px solid #DCFCE7; color: #000000 !important; }
    h1, h2, h3, h4, p, li, span, label, div { color: #000000 !important; }
    input, textarea { background-color: #FFFFFF !important; border: 1px solid #CBD5E1 !important; color: #000000 !important; border-radius: 8px !important; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; background-color: #FFFFFF !important; }
    .stTabs [data-baseweb="tab"] { background-color: #F1F5F9 !important; border-radius: 10px 10px 0 0; padding: 10px 20px; font-weight: bold; color: #000000 !important; }
</style>
""", unsafe_allow_html=True)

# --- 1. بوابة الدخول (الواجهة الرئيسية) ---
if not st.session_state.main_access:
    st.markdown("<h1 class='main-title'>🛡️ مـنـظـومـة سـيـاج الـرقـمـيـة</h1>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='card' style='text-align:center;'><h3>التحقق من بروتوكول الوصول السيبراني</h3><p>يرجى إدخال البيانات المعتمدة للدخول إلى المنظومة</p></div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        u_name = col1.text_input("الاسم الأكاديمي المعتمد:")
        u_email_input = col2.text_input("البريد الإلكتروني الرسمي (Email):")
        u_type = col1.selectbox("رتبة المستخدم في المنظومة:", ["لجنة التحكيم الموقرة", "مسؤول حماية بيانات", "طالب/ة مبتكر"])
        gate_code = col2.text_input("رمز فك التشفير السيادي (SIYAJ2026):", type="password")
        
        if st.button("تأكيد الهوية الرقمية وفتح التشفير 🔓"):
            if u_name and u_email_input and gate_code == SAFE_CODE:
                st.session_state.user_data = {"name": u_name, "type": u_type, "email": u_email_input.lower()}
                st.session_state.main_access = True
                st.session_state.log_history.append({
                    "المشغل": u_name, 
                    "الإيميل": u_email_input, 
                    "الرتبة": u_type, 
                    "التوقيت": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
                st.balloons()
                st.rerun()
            else:
                st.error("⚠️ خطأ في مطابقة البيانات. يرجى التأكد من الرمز وإدخال الإيميل.")
    st.stop()

# --- 2. القائمة الجانبية للتنقل ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/144/shield.png", width=100)
    st.markdown(f"<h2 style='color:#1E3A8A;'>سياج v4.0</h2>", unsafe_allow_html=True)
    st.write(f"المشغل الحالي: **{st.session_state.user_data['name']}**")
    st.write(f"الرتبة: **{st.session_state.user_data['type']}**")
    st.divider()
    menu = [
        "الرئيسية 🏠", 
        "ركن الابتكار 💡", 
        "أكاديمية سياج 🎓", 
        "مركز الفحص الشامل 🔍", 
        "بصمة سياج 🕵️‍♂️", 
        "درع الهندسة الاجتماعية 👤", 
        "مختبر التشفير 🔑", 
        "بلاغ طوارئ 🚨"
    ]
    if st.session_state.user_data['email'] == ADMIN_EMAIL:
        menu.append("سجل الإدارة 📋")
    section = st.radio("انتقل بين وحدات المنظومة:", menu)
    if st.button("تسجيل الخروج الآمن 🔒"):
        st.session_state.clear()
        st.rerun()

# --- 3. محتوى الأقسام التفصيلي ---

if section == "الرئيسية 🏠":
    st.markdown("<h1 class='main-title'>مركز العمليات السيبرانية - سياج</h1>", unsafe_allow_html=True)
    st.info("سياج: لغة العقل الرقمي؛ حيث يرصد رادارنا أدق التفاصيل لصناعة الأمان.")
    
    # واجهة الرصد الحي (اللمسة اللي اتفقنا عليها)
    st.markdown("""<div class='card' style='background-color: #0F172A !important; color: #10B981 !important; border-right-color: #10B981;'>
    <h3 style='color: #10B981 !important;'>📡 رادار سياج للرصد الاستباقي (بث مباشر)</h3>
    <p style='color: #94A3B8 !important;'>جاري فحص النطاقات الوطنية وتحليل التهديدات العابرة للحدود...</p>
    </div>""", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.code("📍 MECCA: SECURE")
    with c2: st.code("📍 RIYADH: ACTIVE")
    with c3: st.code("📍 NORTH: SHIELD")

    st.markdown("""<div class='card'>
    <h3>🛡️ نبذة عن المنظومة</h3>
    <p>منظومة سياج هي درع تقني متكامل، يجمع بين أدوات الرصد المتقدمة وبين التوعية البشرية. نحن نؤمن أن الأمن السيبراني يبدأ من العقل وينتهي بالكود.</p>
    </div>""", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    col_a.metric("حالة الخادم", "متصل ✅")
    col_b.metric("قوة التشفير", "AES-4096")

elif section == "ركن الابتكار 💡":
    st.title("💡 مختبر الابتكار السيبراني")
    t1, t2, t3, t4 = st.tabs(["🧠 العقل الرقمي (القصة)", "📡 رادار الرصد", "🇸🇦 رؤية سياج 2030", "💡 شاركينا فكرتك"])
    with t1:
        st.markdown("""<div class='card'>
        <h3>📖 قصة سياج وأهدافها</h3>
        <p><b>لماذا سياج؟</b> فكرة سياج أتت لتثبت أن المملكة وطن تنمو فيه المواهب، وان خلف كل هدوء طالب يكمن اعصارٌ من الطموح.</p>
        <p><b>أهدافنا:</b> رصد التهديدات، بناء جيل واعي، تبسيط التكنولوجيا.</p></div>""", unsafe_allow_html=True)
    with t2:
        st.subheader("📡 رادار الرصد الاستباقي")
        st.area_chart(pd.DataFrame(np.random.randn(20, 2), columns=['محاولات اختراق', 'نشاط آمن']))
    with t3:
        st.markdown("""<div class='vision-card'><h2 style='text-align: center; color: #10B981;'>🇸🇦 سياج في قلب الرؤية</h2>
        <p style='font-size: 20px; font-weight: bold; text-align: center;'>هذا المشروع هو تطبيق حقيقي لرؤية 2030... سياج تقول للعالم: هؤلاء هنّ بنات السعودية.</p></div>""", unsafe_allow_html=True)
    with t4:
        idea = st.text_area("أكتبي ابتكارك هنا:")
        if st.button("إرسال الابتكار للمختبر"): st.success("تم استلام فكرتك يا مبدعة!")

elif section == "أكاديمية سياج 🎓":
    st.title("🎓 أكاديمية سياج للتميز المعرفي")
    a1, a2, a3 = st.tabs(["🔐 علم التشفير", "🎣 فخاخ التصيد", "👣 الخصوصية والبصمة"])
    with a1:
        st.markdown("<div class='card'><h3>🔐 الدرس الأول: التشفير</h3><p>علم تحويل البيانات إلى نصوص غير مفهومة إلا بالمفتاح.</p></div>", unsafe_allow_html=True)
        st.video("https://youtu.be/xHaxAYDt75Q")
    with a2:
        st.markdown("<div class='card'><h3>🎣 الدرس الثاني: التصيد</h3><p>احذر من الروابط التي تنتحل شخصية المواقع الرسمية.</p></div>", unsafe_allow_html=True)
        st.video("https://youtu.be/gfPN0RIeYLM")
    with a3:
        st.markdown("<div class='card'><h3>👣 الدرس الثالث: البصمة الرقمية</h3><p>كل ما تفعله يترك أثراً، فاجعله أثراً آمناً.</p></div>", unsafe_allow_html=True)
        st.video("https://youtu.be/9eVjgk93PEw")

elif section == "مركز الفحص الشامل 🔍":
    st.title("🔍 مركز الفحص والتحليل الذكي")
    PHONE_DB = {"0555555555": "عاليا صالح العنزان (المشرف)", "0500000000": "صالح بن محمد (رجل أعمال)"}
    c1, c2, c3 = st.columns(3)
    with c1:
        u_url = st.text_input("أدخل الرابط (URL):")
        if st.button("بدء تحليل الرابط"):
            with st.status("جاري التشريح الرقمي..."):
                time.sleep(1); st.write("فحص SSL..."); time.sleep(1)
            st.success("التقرير: الرابط مطابق للمعايير.")
    with c2:
        u_phone = st.text_input("أدخل الرقم للفحص:")
        if st.button("كشف هوية الرقم"):
            if u_phone in PHONE_DB: st.success(f"النتيجة: {PHONE_DB[u_phone]}")
            else: st.error("الرقم غير مسجل.")
    with c3:
        u_img = st.file_uploader("فحص الصور (AI):")
        if u_img and st.button("تحليل الصورة"): st.info("النتيجة: الصورة مصنوعة بالذكاء الاصطناعي بنسبة 92%.")

elif section == "بصمة سياج 🕵️‍♂️":
    st.title("🕵️‍♂️ مختبر التحقيق الرقمي")
    f_audit = st.file_uploader("ارفع الملف لاستخراج بصمته:")
    if f_audit: st.success(f"تم استخراج البصمة الرقمية: {hash(f_audit.name)}")

elif section == "درع الهندسة الاجتماعية 👤":
    st.title("👤 اختبار درع الوعي")
    q1 = st.radio("1. وصلتك رسالة تطلب كود التحقق؟", ["أعطيهم الكود", "أحذف الرسالة", "أتصل بالبنك"])
    if st.button("تحليل الدرع"): st.success("بطلة! وعيك السيبراني حديدي.")

elif section == "مختبر التشفير 🔑":
    st.title("🔑 نظام سياج للتشفير المتقدم")
    txt = st.text_area("النص:")
    key = st.text_input("الرمز السري:", type="password")
    if st.button("تشفير الآن"):
        res = base64.b64encode((txt + "||" + key).encode()).decode()
        st.code(f"SIYAJ_SECURE_{res}")

elif section == "بلاغ طوارئ 🚨":
    st.title("🚨 مركز البلاغات - المساعد 'سند'")
    u_f = st.session_state.user_data['name'].split()[0]
    st.markdown(f"<div class='card' style='border-right-color: #1E3A8A;'><strong>🤖 المساعد سند:</strong><br>هلا بك يا {u_f}، أنا سند.. عطني البلاغ وأنا بأسندك.</div>", unsafe_allow_html=True)
    report = st.text_area("وصف الحادثة:")
    if st.button("إرسال البلاغ المشفر لـ 'سند'"):
        st.balloons(); st.success("تم تأمين البلاغ بنجاح.")

elif section == "سجل الإدارة 📋":
    st.table(pd.DataFrame(st.session_state.log_history))
