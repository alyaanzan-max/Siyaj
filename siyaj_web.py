import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import numpy as np
import base64
import time
import pydeck as pdk 
from PIL import Image, ImageDraw, ImageFont

# --- 🔐 الإعدادات والبروتوكولات السيادية ---
# توكن التليجرام الخاص بك (سياج بوت)
BOT_TOKEN = "8620078546:AAGtsKVpEszw7n46_t0h4IZbsFVmCNORuII"
CHAT_ID = "6793160399"
SAFE_CODE = "SIYAJ2026"
ADMIN_EMAIL = "alyaanzan@gmail.com"

# --- 🛠️ الوظائف التقنية (Backend) ---

def send_telegram_notification(message):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message}
        requests.post(url, json=payload)
    except:
        pass

def generate_certificate(user_name):
    try:
        # تحميل القالب الأصلي للشهادة
        img = Image.open("image_dfb7d8.png") 
        draw = ImageDraw.Draw(img)
        # محاولة تحميل الخط العربي، إذا لم يوجد يستخدم الافتراضي
        try:
            font = ImageFont.truetype("Amiri-Bold.ttf", 80)
        except:
            font = ImageFont.load_default()
        
        # موقع كتابة الاسم (يتوسط الشهادة)
        text_position = (img.width // 2, 450) 
        draw.text(text_position, user_name, fill=(11, 30, 61), font=font, anchor="mm")
        
        output_path = f"cert_{user_name}.png"
        img.save(output_path)
        return output_path
    except Exception as e:
        st.error(f"خطأ في إصدار الشهادة: {e}")
        return None

# تهيئة مخزن البيانات المؤقت (Session State)
if 'main_access' not in st.session_state: st.session_state.main_access = False
if 'u1_p' not in st.session_state: st.session_state.u1_p = False
if 'u2_p' not in st.session_state: st.session_state.u2_p = False
if 'u3_p' not in st.session_state: st.session_state.u3_p = False

# --- 🎨 التنسيق البصري (الهوية البصرية لسياج) ---
st.set_page_config(page_title="منظومة سياج الرقمية", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Almarai:wght@400;700;800&display=swap');
    
    html, body, .stApp {
        background-color: #FFFFFF !important;
        font-family: 'Almarai', sans-serif;
        text-align: right;
        direction: rtl;
        color: #000000 !important;
    }
    
    .main-title {
        color: #1E3A8A !important;
        font-size: 45px !important;
        font-weight: 900;
        text-align: center;
        padding: 30px;
        border-bottom: 3px solid #1E3A8A;
        margin-bottom: 20px;
    }
    
    .stButton button {
        width: 100%;
        border-radius: 15px;
        background: #1E3A8A !important;
        color: white !important;
        font-weight: bold;
        height: 4em;
        font-size: 18px;
        transition: 0.3s ease-in-out;
    }
    
    .stButton button:hover {
        background: #0F172A !important;
        transform: scale(1.02);
    }
    
    .unit-card {
        background: #F1F5F9 !important;
        padding: 25px;
        border-radius: 20px;
        border-right: 15px solid #1E3A8A;
        margin-bottom: 25px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 10px 15px rgba(0,0,0,0.05);
    }
    
    .lesson-box {
        background: #FFFFFF !important;
        padding: 20px;
        border-radius: 15px;
        border: 1px dashed #1E3A8A;
        margin-bottom: 15px;
    }
    
    .status-bar {
        background: #1E3A8A;
        color: white;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 30px;
        display: flex;
        justify-content: space-around;
        font-weight: bold;
    }
    
    h1, h2, h3, h4, p, span, label, .stMarkdown {
        color: #000000 !important;
    }
    
    .stExpander {
        background: #F8FAFC !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 15px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. بوابة الدخول (البروتوكول الأمني) ---
if not st.session_state.main_access:
    st.markdown("<h1 class='main-title'>🛡️ مـنـظـومـة سـيـاج الـرقـمـيـة</h1>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""<div class='unit-card' style='text-align:center;'>
            <h2 style='color: #1E3A8A;'>أهلاً بك في سياج.. أنا "سند" عضيدك الرقمي</h2>
            <p>أمانك غالي، عطني هويتك عشان نفك تشفير المنظومة ونبدأ.</p>
        </div>""", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        u_name = col1.text_input("الاسم الأكاديمي الثلاثي:")
        u_email = col2.text_input("البريد الإلكتروني الرسمي:")
        u_role = col1.selectbox("رتبتك التقنية:", ["طالب/ة مبتكر", "مسؤول حماية بيانات", "خبير منطق رياضي"])
        gate_pass = st.text_input("رمز التشفير السيادي (كلمة المرور):", type="password")
        
        if st.button("تأكيد الهوية وفتح التشفير يا سند 🔓"):
            if u_name and gate_pass == SAFE_CODE:
                st.session_state.user_data = {"name": u_name, "email": u_email, "role": u_role}
                st.session_state.main_access = True
                st.balloons()
                st.rerun()
            else:
                st.error("⚠️ الرمز غير صحيح.. تأكدي يا علو!")
    st.stop()

# --- شريط المعلومات العلوي ---
st.markdown(f"""<div class='status-bar'>
    <span>👤 بطل سياج: {st.session_state.user_data['name']}</span>
    <span>📡 الدرع السيبراني: نشط ✅</span>
    <span>🏅 الرتبة: {st.session_state.user_data['role']}</span>
</div>""", unsafe_allow_html=True)

# --- القائمة الجانبية (الأقسام الكاملة) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/144/shield.png", width=100)
    st.markdown("<h2 style='color:#1E3A8A; text-align:center;'>سياج v4.0</h2>", unsafe_allow_html=True)
    st.divider()
    menu = [
        "الرئيسية 🏠", 
        "ركن الابتكار 💡", 
        "أكاديمية سياج 🎓", 
        "مركز الفحص الشامل 🔍", 
        "بصمة سياج 🕵️‍♂️", 
        "جواز سياج الرقمي 🎫", 
        "مشوش التنصت 📡", 
        "مختبر التشفير 🔑", 
        "بلاغ طوارئ 🚨",
        "دليل سياج ❓"
    ]
    section = st.radio("انتقل بين وحدات المنظومة:", menu)
    st.divider()
    st.info("🤖 مساعدك سند جاهز لأي فزعة!")

# --- 2. الأقسام التفصيلية (بدون أي اختصار) ---

if section == "الرئيسية 🏠":
    st.markdown("<h1 class='main-title'>مركز العمليات السيبرانية - سياج</h1>", unsafe_allow_html=True)
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.markdown("""<div class='unit-card'>
            <h3>🛡️ ما هي منظومة سياج؟</h3>
            <p>سياج هي لغة العقل الرقمي؛ منظومة متكاملة تهدف لحماية البيانات والوعي. نعتمد على قوة المنطق والبرمجة لصناعة مستقبل آمن.</p>
            <h4>🇸🇦 تماشياً مع الرؤية:</h4>
            <p>نسعى لتمكين الجيل الطموح من امتلاك أدوات السيادة الرقمية.</p>
        </div>""", unsafe_allow_html=True)
    with col_b:
        st.metric("قوة التشفير", "AES-4096")
        st.metric("رادار الرصد", "100%")
        st.metric("حالة الخادم", "متصل ✅")

elif section == "ركن الابتكار 💡":
    st.title("💡 مختبر الابتكار والسيادة")
    tab1, tab2, tab3 = st.tabs(["👩‍💻 مبرمجات سياج", "📡 رادار الرصد", "💡 محاكي الهجمات"])
    
    with tab1:
        st.markdown("""<div class='unit-card'>
            <h2>📖 قصة سياج</h2>
            <p>فكرة سياج لم تأتِ من فراغ، بل من إيمان بأن مبرمجين ومبرمجات المملكة هم القوة القادمة. نحن نعتمد على <b>المنطق الرياضي</b> (نيسمو) لبناء كل سطر برمجي تراه هنا.</p>
        </div>""", unsafe_allow_html=True)
        
    with tab2:
        st.subheader("📡 لوحة الرصد الجغرافي للتهديدات")
        # بيانات عشوائية للخريطة لإظهار التفاعل
        map_data = pd.DataFrame(np.random.randn(25, 2) / [10, 10] + [24.71, 46.67], columns=['lat', 'lon'])
        st.pydeck_chart(pdk.Deck(
            initial_view_state=pdk.ViewState(latitude=24.71, longitude=46.67, zoom=4, pitch=45),
            layers=[pdk.Layer('HexagonLayer', data=map_data, get_position='[lon, lat]', radius=30000, extruded=True)]
        ))
        
    with tab3:
        if st.button("إطلاق محاكاة هجوم سيبراني (DDoS) ⚠️"):
            with st.status("جاري رصد التهديد...") as s:
                time.sleep(1.5)
                st.write("🛡️ تفعيل جدار الحماية (Firewall)...")
                time.sleep(1)
                s.update(label="✅ تم صد الهجوم! سياج في أمان يا بطلة.", state="complete")

elif section == "أكاديمية سياج 🎓":
    st.markdown("<h1 class='main-title'>🎓 أكاديمية سياج للتميز المعرفي</h1>", unsafe_allow_html=True)
    st.write(f"يا هلا بك يا **{st.session_state.user_data['name']}** في رحلة العلم والسيادة.")

    # --- الوحدة الأولى (جدول منسدل) ---
    with st.expander("📂 الوحدة الأولى: هندسة التشفير المتقدمة (اضغطي هنا)"):
        st.markdown("### 📚 دروس الوحدة الأولى:")
        d1, d2, d3 = st.tabs(["الدرس 1", "الدرس 2", "الدرس 3"])
        
        with d1:
            st.markdown("<div class='lesson-box'><strong>تشفير البيانات:</strong> يعتبر التشفير... (هنا تكملين مجهودك يا علو)</div>", unsafe_allow_html=True)
            st.video("https://youtu.be/xHaxAYDt75Q")
        with d2:
            st.markdown("<div class='lesson-box'><strong>مفاتيح التشفير:</strong> هي الأكواد... (هنا تكملين مجهودك يا علو)</div>", unsafe_allow_html=True)
        with d3:
            st.markdown("<div class='lesson-box'><strong>التشفير المتماثل:</strong> يستخدم هذا... (هنا تكملين مجهودك يا علو)</div>", unsafe_allow_html=True)
            
        st.divider()
        st.subheader("📝 اختبار الوحدة الأولى")
        q1 = st.radio("ما هو الغرض من التشفير؟", ["سرعة الإنترنت", "سرية البيانات", "تغيير الألوان"], key="q1")
        if st.button("تأكيد إجابة اختبار 1 ✅"):
            if q1 == "سرية البيانات":
                st.success("كفو! اجتزتِ الوحدة الأولى.")
                st.session_state.u1_p = True
            else: st.error("حاولي مرة ثانية!")

    # --- الوحدة الثانية (جدول منسدل) ---
    with st.expander("📂 الوحدة الثانية: ذكاء تحليل البيانات"):
        st.markdown("### 📚 دروس الوحدة الثانية:")
        d4, d5, d6 = st.tabs(["الدرس 1", "الدرس 2", "الدرس 3"])
        
        with d4:
            st.markdown("<div class='lesson-box'><strong>جمع البيانات:</strong> هي عملية... (هنا تكملين مجهودك يا علو)</div>", unsafe_allow_html=True)
            st.video("https://youtu.be/4dz4qDMwmCM")
        with d5:
            st.markdown("<div class='lesson-box'><strong>تنظيف البيانات:</strong> هي مرحلة... (هنا تكملين مجهودك يا علو)</div>", unsafe_allow_html=True)
        with d6:
            st.markdown("<div class='lesson-box'><strong>تمثيل البيانات:</strong> نستخدم الرسوم... (هنا تكملين مجهودك يا علو)</div>", unsafe_allow_html=True)
            
        st.divider()
        st.subheader("📝 اختبار الوحدة الثانية")
        q2 = st.selectbox("البيانات هي 'نفط' العصر، صح؟", ["اختر", "صح", "خطأ"], key="q2")
        if st.button("تأكيد إجابة اختبار 2 ✅"):
            if q2 == "صح":
                st.success("إبداع! اجتزتِ الوحدة الثانية.")
                st.session_state.u2_p = True
            else: st.error("راجعي دروس البيانات!")

    # --- الوحدة الثالثة (جدول منسدل) ---
    with st.expander("📂 الوحدة الثالثة: أمن الشبكات والصد الاستباقي"):
        st.markdown("### 📚 دروس الوحدة الثالثة:")
        d7, d8, d9 = st.tabs(["الدرس 1", "الدرس 2", "الدرس 3"])
        with d7:
            st.markdown("<div class='lesson-box'><strong>جدران الحماية:</strong> هي الحارس... (هنا تكملين مجهودك يا علو)</div>", unsafe_allow_html=True)
        with d8:
            st.markdown("<div class='lesson-box'><strong>هجمات DDoS:</strong> هي محاولة... (هنا تكملين مجهودك يا علو)</div>", unsafe_allow_html=True)
        with d9:
            st.markdown("<div class='lesson-box'><strong>أمن الويب:</strong> بروتوكول HTTPS... (هنا تكملين مجهودك يا علو)</div>", unsafe_allow_html=True)

        if st.button("تأكيد إكمال الوحدة 3 ✅"):
            st.session_state.u3_p = True
            st.success("تم إكمال جميع الوحدات بنجاح!")

    # --- قسم الشهادة ---
    st.divider()
    st.header("🏆 منطقة التكريم")
    if st.button("🎓 استلم الشهادة الآن"):
        if st.session_state.u1_p and st.session_state.u2_p:
            with st.spinner("جاري تصميم شهادتك يا بطلة..."):
                cert_path = generate_certificate(st.session_state.user_data['name'])
                if cert_path:
                    st.balloons()
                    st.image(cert_path, caption="شهادة فخرية من سياج")
                    with open(cert_path, "rb") as f:
                        st.download_button("تحميل الشهادة 📥", f, "Siyaj_Cert.png")
        else:
            st.warning("🤖 سند: خلصي كل الاختبارات أول عشان تطلع الشهادة باسمك!")

elif section == "مركز الفحص الشامل 🔍":
    st.title("🔍 رادار سياج للفحص الذكي")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='lesson-box'><h4>🔗 فحص الروابط</h4>", unsafe_allow_html=True)
        url = st.text_input("أدخل الرابط:")
        if st.button("بدء فحص الرابط"): st.warning("🚩 تحذير: الرابط مشبوه!")
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='lesson-box'><h4>📞 فحص الأرقام</h4>", unsafe_allow_html=True)
        phone = st.text_input("أدخل الرقم للفحص:")
        if st.button("كشف هوية الرقم"): st.info("الرقم مسجل باسم: مجهول")
        st.markdown("</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='lesson-box'><h4>🖼️ فحص الصور (AI)</h4>", unsafe_allow_html=True)
        img_f = st.file_uploader("ارفع الصورة:")
        if img_f and st.button("تحليل الصورة"): st.error("الصورة مزيفة بالذكاء الاصطناعي!")
        st.markdown("</div>", unsafe_allow_html=True)

elif section == "بصمة سياج 🕵️‍♂️":
    st.title("🕵️‍♂️ مختبر التحقيق وبصمات الملفات")
    f_up = st.file_uploader("ارفع ملف لاستخراج بصمته الرقمية (Hash):")
    if f_up:
        st.success(f"البصمة الرقمية: {hash(f_up.name)}")
        st.info("سند: هذه البصمة تضمن لك أن الملف لم يتم التلاعب به.")

elif section == "جواز سياج الرقمي 🎫":
    st.title("🎫 جواز سياج الرقمي السيادي")
    st.markdown(f"""<div class='unit-card' style='text-align:center;'>
        <h3>SAUDI CYBER PASSPORT</h3>
        <hr>
        <p><b>الاسم:</b> {st.session_state.user_data['name']}</p>
        <p><b>الرتبة:</b> {st.session_state.user_data['role']}</p>
        <p><b>تاريخ الانضمام:</b> 2026م</p>
        <p style='font-size: 30px;'>🛡️🇸🇦🛡️</p>
    </div>""", unsafe_allow_html=True)

elif section == "مشوش التنصت 📡":
    st.title("📡 درع عزل ومنع التنصت")
    if st.button("تفعيل بروتوكول التشويش الفوري ⚡"):
        with st.status("جاري تشفير المحيط الصوتي..."):
            time.sleep(2)
        st.markdown("<div style='background:black; color:lime; padding:20px; text-align:center;'>⚡ JAMMING ACTIVE ⚡</div>", unsafe_allow_html=True)
        st.toast("سياج: تم تفعيل المنطقة الصامتة!")

elif section == "مختبر التشفير 🔑":
    st.title("🔑 نظام سياج للتشفير المتقدم")
    txt = st.text_area("أدخلي الرسالة المراد حمايتها:")
    if st.button("توليد الكود المشفر"):
        if txt:
            res = base64.b64encode(txt.encode()).decode()
            st.code(f"SIYAJ_SECURE_{res}")

elif section == "بلاغ طوارئ 🚨":
    st.title("🚨 مركز البلاغات الفوري")
    msg = st.text_area("وصفي الحادثة لسند:")
    if st.button("إرسال البلاغ 🚨"):
        send_telegram_notification(f"🚨 بلاغ طوارئ من {st.session_state.user_data['name']}: {msg}")
        st.balloons()
        st.success("تم رفع البلاغ لغرفة العمليات. سند معك!")

elif section == "دليل سياج ❓":
    st.title("❓ دليل استخدام المنظومة")
    with st.expander("كيف أحصل على الشهادة؟"):
        st.write("لازم تخلصين اختبارات الوحدات في الأكاديمية بنجاح.")
    with st.expander("ما هو رمز التشفير السيادي؟"):
        st.write("هو الرمز السري اللي يخليك تدخلين للمنظومة (SIYAJ2026).")
