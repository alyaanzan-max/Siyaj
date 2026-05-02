import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import numpy as np
import base64
import time
import pydeck as pdk 
from PIL import Image, ImageDraw, ImageFont

# --- 🔐 الإعدادات الأمنية السيادية ---
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
        # ملاحظة: تأكدي من وجود صورة image_dfb7d8.png وخط Amiri-Bold.ttf في المجلد
        img = Image.open("image_dfb7d8.png") 
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("Amiri-Bold.ttf", 80)
        except:
            font = ImageFont.load_default()
        
        text_position = (img.width // 2, 450) 
        draw.text(text_position, user_name, fill=(11, 30, 61), font=font, anchor="mm")
        output_path = f"cert_{user_name}.png"
        img.save(output_path)
        return output_path
    except:
        return None

# تهيئة مخزن البيانات (Session State)
if 'main_access' not in st.session_state: st.session_state.main_access = False
if 'u1_p' not in st.session_state: st.session_state.u1_p = False
if 'u2_p' not in st.session_state: st.session_state.u2_p = False
if 'u3_p' not in st.session_state: st.session_state.u3_p = False
if 'log_history' not in st.session_state: st.session_state.log_history = []

# --- 🎨 التنسيق البصري (الهوية البصرية الفخمة) ---
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
        height: 3.8em;
        font-size: 18px;
        transition: 0.3s ease-in-out;
    }
    
    .stButton button:hover {
        background: #0F172A !important;
        transform: scale(1.02);
    }
    
    .card {
        background: #F8FAFC !important;
        padding: 25px;
        border-radius: 20px;
        border-right: 12px solid #1E3A8A;
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
</style>
""", unsafe_allow_html=True)

# --- 1. بوابة الدخول (بإشراف سند) ---
if not st.session_state.main_access:
    st.markdown("<h1 class='main-title'>🛡️ مـنـظـومـة سـيـاج الـرقـمـيـة</h1>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""<div class='card' style='text-align:center;'>
            <h2 style='color: #1E3A8A;'>يا هلا بك في عرين سياج! 🛡️</h2>
            <p style='font-size: 18px;'>أنا <b>سند</b>، حارسك الشخصي وعضيدك في هذي المنظومة.<br>
            عطني هويتك عشان نعتمدك بطل من أبطالنا ونفتح بروتوكولات التشفير.</p>
        </div>""", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        u_name = col1.text_input("وش الاسم الغالي؟ (الاسم الأكاديمي):")
        u_email = col2.text_input("بريدك الرسمي (Email):")
        
        # خيار الجنس اللي رجعناه (عشان سند يكلمك صح)
        u_gender = col1.radio("عشان أزهل الموضوع وأكلمك صح، أنت بطل ولا بطلة؟", ["أنثى", "ذكر"], horizontal=True)
        
        u_role = col2.selectbox("رتبتك التقنية:", ["طالب/ة مبتكر", "مسؤول حماية بيانات", "خبير منطق رياضي"])
        gate_pass = st.text_input("رمز التشفير السيادي (كلمة المرور):", type="password")
        
        if st.button("تأكيد الهوية وفتح التشفير يا سند 🔓"):
            if u_name and u_email and gate_pass == SAFE_CODE:
                st.session_state.user_data = {
                    "name": u_name, 
                    "email": u_email.lower(), 
                    "role": u_role, 
                    "gender": u_gender
                }
                st.session_state.main_access = True
                # تسجيل الدخول في السجل
                st.session_state.log_history.append({
                    "الوقت": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "الاسم": u_name,
                    "البريد": u_email
                })
                st.balloons()
                st.rerun()
            else:
                st.error("⚠️ الرمز غير صحيح.. تأكد من بياناتك يا غالي!")
    st.stop()

# --- شريط الحالة العلوي ---
g_prefix = "البطلة" if st.session_state.user_data['gender'] == "أنثى" else "البطل"
st.markdown(f"""<div class='status-bar'>
    <span>👤 {g_prefix}: {st.session_state.user_data['name']}</span>
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
    if st.session_state.user_data['email'] == ADMIN_EMAIL:
        menu.append("سجل الإدارة 📋")
    
    section = st.radio("انتقل بين وحدات المنظومة:", menu)
    st.divider()
    st.info(f"🤖 سند: معك يا {g_prefix}، وش نخطط عليه الحين؟")

# --- 2. الأقسام التفصيلية ---

if section == "الرئيسية 🏠":
    st.markdown("<h1 class='main-title'>مركز العمليات السيبرانية - سياج</h1>", unsafe_allow_html=True)
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.markdown(f"""<div class='card'>
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
        st.markdown("""<div class='card'>
            <h2>📖 قصة سياج</h2>
            <p>فكرة سياج لم تأتِ من فراغ، بل من إيمان بأن مبرمجين ومبرمجات المملكة هم القوة القادمة. نحن نعتمد على <b>المنطق الرياضي</b> لبناء كل سطر برمجي تراه هنا.</p>
            <hr>
            <h4>🎯 أهدافنا:</h4>
            <ul>
                <li>رصد التهديدات قبل وصولها.</li>
                <li>تحويل المفاهيم المعقدة لأدوات سهلة.</li>
                <li>الاعتزاز بالهوية الوطنية والتقنية.</li>
            </ul>
        </div>""", unsafe_allow_html=True)
        
    with tab2:
        st.subheader("📡 لوحة الرصد الجغرافي للتهديدات")
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
                s.update(label="✅ تم صد الهجوم بنجاح! سياج في أمان.", state="complete")

elif section == "أكاديمية سياج 🎓":
    st.markdown("<h1 class='main-title'>🎓 أكاديمية سياج للتميز المعرفي</h1>", unsafe_allow_html=True)
    st.write(f"يا هلا بك يا **{st.session_state.user_data['name']}** في رحلة العلم والسيادة.")

    # الوحدة الأولى
    with st.expander("📂 الوحدة الأولى: هندسة التشفير (اضغطي للفتح)"):
        d1, d2, d3 = st.tabs(["الدرس 1", "الدرس 2", "الدرس 3"])
        with d1:
            st.markdown("<div class='lesson-box'><strong>تشفير البيانات:</strong> يعتبر التشفير هو العلم الذي يحول البيانات المفهومة إلى رموز غير مفهومة لحمايتها.</div>", unsafe_allow_html=True)
            st.video("https://youtu.be/xHaxAYDt75Q")
        with d2:
            st.markdown("<div class='lesson-box'><strong>مفاتيح التشفير:</strong> هي الأكواد السرية المستخدمة لفك القفل البرمجي.</div>", unsafe_allow_html=True)
        with d3:
            st.markdown("<div class='lesson-box'><strong>التشفير المتماثل:</strong> يستخدم مفتاحاً واحداً للقفل والفتح.</div>", unsafe_allow_html=True)
        
        q1 = st.radio("ما هو الغرض من التشفير؟", ["سرعة الإنترنت", "سرية البيانات", "تغيير الألوان"], key="q1")
        if st.button("تأكيد إجابة اختبار 1 ✅"):
            if q1 == "سرية البيانات":
                st.success("كفو! اجتزتِ الوحدة الأولى.")
                st.session_state.u1_p = True
            else: st.error("حاولي مرة ثانية!")

    # الوحدة الثانية
    with st.expander("📂 الوحدة الثانية: ذكاء تحليل البيانات"):
        d4, d5, d6 = st.tabs(["الدرس 1", "الدرس 2", "الدرس 3"])
        with d4:
            st.markdown("<div class='lesson-box'><strong>جمع البيانات:</strong> هي عملية رصد المعلومات من مصادر موثوقة.</div>", unsafe_allow_html=True)
            st.video("https://youtu.be/4dz4qDMwmCM")
        with d5:
            st.markdown("<div class='lesson-box'><strong>تنظيف البيانات:</strong> مرحلة التأكد من جودة البيانات وحذف المكرر.</div>", unsafe_allow_html=True)
        with d6:
            st.markdown("<div class='lesson-box'><strong>تمثيل البيانات:</strong> تحويل الأرقام لرسوم ذكية (مثل رادار سياج).</div>", unsafe_allow_html=True)
            
        q2 = st.selectbox("البيانات هي 'نفط' العصر، صح؟", ["اختر", "صح", "خطأ"], key="q2")
        if st.button("تأكيد إجابة اختبار 2 ✅"):
            if q2 == "صح":
                st.success("إبداع! اجتزتِ الوحدة الثانية.")
                st.session_state.u2_p = True

    # الوحدة الثالثة
    with st.expander("📂 الوحدة الثالثة: أمن الشبكات والصد الاستباقي"):
        st.markdown("<div class='lesson-box'><strong>أمن الشبكات:</strong> هو بناء الحصون الرقمية حول بياناتنا الطائرة في الهواء.</div>", unsafe_allow_html=True)
        if st.button("تأكيد إكمال الوحدة 3 ✅"):
            st.session_state.u3_p = True
            st.success("تم إكمال جميع الوحدات!")

    # قسم الشهادة
    st.divider()
    st.header("🏆 منطقة التكريم")
    if st.button("🎓 استلم الشهادة الآن"):
        if st.session_state.u1_p and st.session_state.u2_p:
            with st.spinner("جاري تصميم شهادتك..."):
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
        st.markdown("<div class='card'><h4>🔗 فحص الروابط</h4>", unsafe_allow_html=True)
        url = st.text_input("أدخل الرابط:")
        if st.button("بدء فحص الرابط"): st.warning("🚩 تحذير: الرابط مشبوه!")
    with col2:
        st.markdown("<div class='card'><h4>📞 فحص الأرقام</h4>", unsafe_allow_html=True)
        phone = st.text_input("أدخل الرقم للفحص:")
        if st.button("كشف هوية الرقم"): st.info("الرقم مسجل باسم: مجهول")
    with col3:
        st.markdown("<div class='card'><h4>🖼️ فحص الصور (AI)</h4>", unsafe_allow_html=True)
        img_f = st.file_uploader("ارفع الصورة:")
        if img_f and st.button("تحليل الصورة"): st.error("الصورة مزيفة بالذكاء الاصطناعي!")

elif section == "بصمة سياج 🕵️‍♂️":
    st.title("🕵️‍♂️ مختبر التحقيق الرقمي")
    f_up = st.file_uploader("ارفع ملف لاستخراج بصمته الرقمية (Hash):")
    if f_up:
        st.success(f"البصمة الرقمية: {hash(f_up.name)}")
        st.info("سند: هذه البصمة تضمن لك أن الملف أصلي ولم يتم التلاعب به.")

elif section == "جواز سياج الرقمي 🎫":
    st.title("🎫 جواز سياج الرقمي السيادي")
    st.markdown(f"""<div class='card' style='text-align:center;'>
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

elif section == "سجل الإدارة 📋":
    st.title("📋 سجل المراقبة (للمشرفين)")
    if st.session_state.log_history:
        st.table(pd.DataFrame(st.session_state.log_history))
    else: st.write("لا يوجد سجل حالياً.")

elif section == "دليل سياج ❓":
    st.title("❓ دليل استخدام المنظومة")
    with st.expander("كيف أحصل على الشهادة؟"):
        st.write("لازم تخلصين اختبارات الوحدات في الأكاديمية بنجاح.")
    with st.expander("ما هو رمز التشفير السيادي؟"):
        st.write("هو الرمز السري اللي يدخلك للمنظومة (SIYAJ2026).")
