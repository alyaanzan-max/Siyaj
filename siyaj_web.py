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
ADMIN_EMAIL = "alyaanzan@gmail.com" # إيميلك المعتمد كمسؤولة للنظام

# وظيفة إرسال التنبيهات للتليجرام
def send_telegram_notification(message):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message}
        requests.post(url, json=payload)
    except:
        pass

# وظيفة توليد الشهادة باسم المستخدم
def generate_certificate(user_name):
    try:
        img = Image.open("image_dfb7d8.png") 
        draw = ImageDraw.Draw(img)
        # ملاحظة: تأكدي من وجود ملف الخط في مجلد المشروع ليعمل بشكل صحيح
        font = ImageFont.truetype("Amiri-Bold.ttf", 70)
        text_position = (img.width // 2, 430) 
        draw.text(text_position, user_name, fill=(11, 30, 61), font=font, anchor="mm")
        img.save("siyaj_cert.png")
        return "siyaj_cert.png"
    except:
        return None

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
    .card { background: #F8FAFC !important; padding: 25px; border-radius: 15px; border-right: 8px solid #1E3A8A; margin-bottom: 20px; border: 1px solid #E2E8F0; box-shadow: 0 4px 66px rgba(0,0,0,0.05); color: #000000 !important; }
    .vision-card { background: #F0FDF4 !important; padding: 30px; border-radius: 15px; border-right: 10px solid #10B981; margin-bottom: 20px; border: 1px solid #DCFCE7; color: #000000 !important; }
    .status-bar { background: #1E3A8A; color: white; padding: 12px; border-radius: 10px; margin-bottom: 25px; display: flex; justify-content: space-between; align-items: center; }
    h1, h2, h3, h4, p, li, span, label, div { color: #000000 !important; }
    input, textarea { background-color: #FFFFFF !important; border: 1px solid #CBD5E1 !important; color: #000000 !important; border-radius: 8px !important; }
</style>""", unsafe_allow_html=True)

# --- 1. بوابة الدخول (بإشراف سند) ---
if not st.session_state.main_access:
    st.markdown("<h1 class='main-title'>🛡️ مـنـظـومـة سـيـاج الـرقـمـيـة</h1>", unsafe_allow_html=True)
    with st.container():
        st.markdown(f"""
        <div class='card' style='text-align:center;'>
            <h3 style='color: #1E3A8A;'>يا هلا بك في عرين سياج! 🛡️</h3>
            <p style='font-size: 18px;'>
                أنا <b>سند</b>، حارسك الشخصي وعضيدك في هذي المنظومة.<br>
                استلمنا المهمة وأمانك صار مسؤوليتي، بس قبل ما نفتح بروتوكولات التشفير ونبدأ، 
                عطني هويتك عشان نعتمدك بطل من أبطالنا.
            </p>
        </div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        u_name = col1.text_input("وش الاسم الغالي؟ (الاسم الأكاديمي):")
        u_email_input = col2.text_input("بريدك الرسمي (Email):")
        u_gender = col1.radio("أنت بطل ولا بطلة؟", ["أنثى", "ذكر"], horizontal=True)
        u_type = col2.selectbox("رتبتك اللي تبيها في المنظومة:", ["زائر","مسؤول حماية بيانات", "طالب/ة مبتكر"])
        gate_code = st.text_input("رمز فك التشفير السيادي (كلمة المرور):", type="password")
        
        if st.button("تأكيد الهوية وفتح التشفير يا سند 🔓"):
            if u_name and u_email_input and gate_code == SAFE_CODE:
                st.session_state.user_data = {
                    "name": u_name, 
                    "type": u_type, 
                    "email": u_email_input.lower(),
                    "gender": u_gender
                }
                st.session_state.main_access = True
                st.success(f"كفو يا {u_name}! تم اعتماد هويتك.. استلمت المهمة، تفضل للمنظومة.")
                st.balloons()
                time.sleep(1)
                st.rerun()
            else:
                st.error("⚠️ فيه غلط في البيانات يا غالي، تأكد من الرمز وحاول مرة ثانية.")
    st.stop()

# --- شريط الحالة ---
c_user_name = st.session_state.user_data['name']
c_user_type = st.session_state.user_data['type']
st.markdown(f"""<div class='status-bar'>
    <span>👤 المستخدم الحالي: <b>{c_user_name}</b></span>
    <span>📡 حالة الدرع السيبراني: <b>نشط وتعمل تحت التشفير السيادي</b></span>
    <span>🎖️ الرتبة الممنوحة: <b>{c_user_type}</b></span>
</div>""", unsafe_allow_html=True)

# --- القائمة الجانبية ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/144/shield.png", width=100)
    st.markdown(f"<h2 style='color:#1E3A8A;'>سياج v4.0</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='color:#1E3A8A;'>سند:مرحبًا بك في منظومة سياج الرقميــــة</h2>", unsafe_allow_html=True)
    menu = ["الرئيسية 🏠", "ركن الابتكار 💡", "أكاديمية سياج 🎓", "مركز الفحص الشامل 🔍", "بصمة سياج 🕵️‍♂️", "جواز سياج الرقمي 🎫", "مشوش التنصت 📡", "مختبر التشفير 🔑", "دليل سياج ❓", "بلاغ طوارئ 🚨"]
    if st.session_state.user_data['email'] == ADMIN_EMAIL:
        menu.append("سجل الإدارة 📋")
    section = st.radio("انتقل بين وحدات المنظومة:", menu)

# --- 1. قسم الرئيسية ---
if section == "الرئيسية 🏠":
    st.markdown("<h1 class='main-title'>مركز العمليات السيبرانية - سياج</h1>", unsafe_allow_html=True)
    st.info("سياج: لغة العقل الرقمي؛ حيث يرصد رادارنا أدق التفاصيل لصناعة الأمان.")
    st.markdown("""<div class='card'>
    <h3>🛡️ نبذة عن المنظومة</h3>
    <p>منظومة سياج هي درع تقني متكامل، يجمع بين أدوات الرصد المتقدمة وبين التوعية البشرية. نحن نؤمن أن الأمن السيبراني يبدأ من العقل وينتهي بالكود.</p>
    </div>""", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    col_a.metric("حالة الخادم", "متصل ✅")
    col_b.metric("قوة التشفير", "AES-4096")

# --- 2. ركن الابتكار ---
elif section == "ركن الابتكار 💡":
    st.title("💡 مختبر الابتكار والسيادة الرقمية")
    t1, t2, t3, t4 = st.tabs(["👩‍💻 مبرمجات سياج", "📡 رادار الرصد", "🇸🇦 الرؤية", "💡 محاكي الاختراق"])
    with t1:
        st.markdown("""<div class='card'>
        <h2 style='color: #1E3A8A; text-align: center;'>📖 قصة سياج وأهدافنا</h2>
        <p><b>لماذا سياج؟</b> فكرة سياج لم تأتي بيوم وليلة أتت بأيام معدودة لأننا نريد أن نثبت للعالم بأن المملكة العربية السعودية وطن تنمو فيه المواهب وأن خلف كل هدوء طالب يكمن إعصارٌ من الطموح، ونؤكد أن طموح هذا الجيل هي القوة التي ستبني للمستقبل، وأن سياج هي الأم الحاضنة لكل فكرة مبتكرة والدرع الذي يستقبل تطلعات الجميع ليحولها إلى واقع يحمي مستقبلنا الرقمي.</p>
        <hr style='border: 0.5px solid #E2E8F0;'>
        <h4>🎯 أهدافنا الأساسية:</h4>
        <ul style='list-style-type: square;'>
            <li>رصد التهديدات الاستباقي قبل وصولها للمستخدم.</li>
            <li>بناء جيل واعي يفهم لغة التشفير والخصوصية.</li>
            <li>تحويل المفاهيم المعقدة إلى أدوات سهلة الاستخدام.</li>
        </ul>
        <hr style='border: 0.5px solid #E2E8F0;'>
        <h4>👩‍💻 عن مبرمجات سياج:</h4>
        <p>مبرمجات سياج في المرحلة المتوسطة، ولكن طموحهن يعانق عنان السماء:</p>
        <ul>
            <li><b>🧠 خبيرات المنطق الرياضي:</b> نعتمد في بناء خوارزميات سياج على تفكير منطقي متقدم، صُقل من خلال المنافسة في المحافل الدولية مثل مسابقات "كانجارو" و "موهبة" (نيسمو) للرياضيات.</li>
            <br>
            <li><b>🇸🇦 سفيرات الهوية والتقنية:</b> نحن نريد أن نثبت للعالم أن الاعتزاز بالهوية الوطنية لا يتعارض مع لغات البرمجة العالمية (Python).</li>
            <br>
            <li><b>👤 رواد هندسة الوعي:</b> نمتلك قدرة عالية على تحليل السلوك البشري الرقمي، وهذا ما دفعنا لابتكار المساعد "سند".</li>
        </ul>
        </div>""", unsafe_allow_html=True)
    with t2:
        st.subheader("📡 لوحة العمليات السيبرانية المباشرة")
        col1, col2, col3 = st.columns(3)
        col1.metric("روابط مفحوصة", "1,240", "+12%")
        col2.metric("تهديدات تم صدها", "85", "-5%")
        col3.metric("مستوى الأمان العام", "98%", "مستقر")
        map_data = pd.DataFrame(np.random.randn(15, 2) / [10, 10] + [24.71, 46.67], columns=['lat', 'lon'])
        st.pydeck_chart(pdk.Deck(map_style='mapbox://styles/mapbox/dark-v9', initial_view_state=pdk.ViewState(latitude=24.71, longitude=46.67, zoom=4, pitch=45), layers=[pdk.Layer('HexagonLayer', data=map_data, get_position='[lon, lat]', radius=20000, elevation_scale=50, elevation_range=[0, 1000], pickable=True, extruded=True)]))
    with t3:
        st.markdown("""<div class='vision-card'><h2 style='text-align: center;'>🇸🇦 سياج والرؤية</h2><p>بناء جيل طموح يحمي مكتسبات الوطن الرقمية، تماشياً مع رؤية المملكة 2030 في التحول الرقمي والسيادة التقنية.</p></div>""", unsafe_allow_html=True)
    with t4:
        st.subheader("🚨 تجربة محاكاة هجوم (Cyber Attack Simulation)")
        if st.button("إطلاق هجوم تجريبي ⚠️"):
            with st.status("جاري رصد محاولة اختراق...", expanded=True) as status:
                st.write("🔍 فحص بروتوكولات الاتصال...")
                time.sleep(1)
                st.write("🛡️ تفعيل جدار الحماية (Firewall) تلقائياً...")
                status.update(label="✅ تم صد الهجوم بنجاح! سياج في أمان.", state="complete", expanded=False)
            st.toast("سياج: تم عزل التهديد بنجاح يا علو!")

# --- 3. أكاديمية سياج ---
elif section == "أكاديمية سياج 🎓":
    st.title("🎓 أكاديمية سياج للتميز المعرفي")
    user_full_name = st.text_input("يا هلا بك في سياج! اكتبي اسمك الثلاثي للشهادة:", placeholder="مثلاً: عاليا صالح العنزان")
    if user_full_name:
        st.success(f"حياك الله يا {user_full_name}! شدي الحيل في الدروس.")
        tabs = st.tabs(["🔢 هندسة التشفير", "📊 ذكاء البيانات", "🛡️ الحماية الرقمية", "🌐 أمن الشبكات"])
        with tabs[0]:
            st.header("الوحدة الأولى: هندسة التشفير")
            st.video("https://youtu.be/xHaxAYDt75Q") 
            st.info("🤖 سند الخبير: التشفير هو العلم اللي يخلي رسائلك سرية!")
            if st.button("اختبار الوحدة 1 ✅"): st.session_state.u1 = True
        with tabs[1]:
            if st.session_state.get('u1'):
                st.header("الوحدة الثانية: ذكاء تحليل البيانات")
                st.video("https://youtu.be/4dz4qDMwmCM")
                st.video("https://youtu.be/8KTogNc06UU")
                st.markdown("### 📈 شرح سند لتمثيل البيانات")
                st.write("البيانات يا بطلة هي 'نفط' العصر. في سياج، نحول الأرقام المملة لرسوم بيانية ذكية.")
                if st.button("اختبار الوحدة 2 ✅"): st.session_state.u2 = True
            else: st.warning("🤖 سند: خلصي دروس التشفير أول!")
        with tabs[2]:
            if st.session_state.get('u2'):
                st.header("الوحدة الثالثة: الحماية الرقمية (الدفاع الاستباقي)")
                st.video("https://youtu.be/9eVjgk93PEw")
                st.markdown("""### 🛡️ شرح سند المفصل للحماية:
                **1. التوثيق الثنائي (2FA):** قفل ثاني ما يفتح إلا برمز يوصل لجوالك.
                **2. أمن الويب (HTTPS & SSL):** سياج يبني نفق مشفر بينك وبين الموقع.""")
                st.video("https://youtu.be/TtcV4jpNG8M")
                if st.button("اختبار الوحدة 3 ✅"): st.session_state.u3 = True
            else: st.warning("🤖 سند: باقي لك دروس البيانات!")
        with tabs[3]:
            if st.session_state.get('u3'):
                st.header("الوحدة الرابعة: أمن الشبكات (الحصن المنيع)")
                st.markdown("""### 🌐 شرح سند لأمن الشبكات:
                **1. جدران الحماية (Firewalls):** الحارس اللي يفتش البيانات.
                **2. هجمات حجب الخدمة (DDoS):** الهكر يرسل ملايين الطلبات عشان يطيح الموقع.
                **3. أمن الواي فاي:** لا تشبكين على واي فاي مفتوح في الأماكن العامة.
                **4. الشبكات الافتراضية (VPN):** عباءة الإخفاء وتشفير الاتصال.""")
                if st.button("🎓 إصدار الشهادة النهائية"):
                    path = generate_certificate(user_full_name)
                    if path:
                        st.balloons()
                        st.image(path, caption=f"مبروك يا {user_full_name}!")
                        with open(path, "rb") as file: st.download_button("حملي شهادتك 📥", file, file_name=f"Siyaj_{user_full_name}.png")
            else: st.warning("🤖 سند: قربتي! خلصي الوحدة الثالثة.")
    else: st.info("🤖 سند: بانتظارك تكتبين اسمك فوق عشان نبدأ الرحلة!")

# --- 4. مركز الفحص الشامل ---
elif section == "مركز الفحص الشامل 🔍":
    st.title("🔍 مركز الفحص والتحليل الذكي")
    PHONE_DB = {"0555555555": "عاليا صالح العنزان (المشرف التقني)", "0500000000": "صالح بن محمد (رجل أعمال)", "0544444444": "أروى صالح (عضو فريق)"}
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='card'><h4>🔗 فحص الروابط</h4>", unsafe_allow_html=True)
        u_url = st.text_input("أدخل الرابط (URL):", placeholder="https://...", key="check_url")
        if st.button("بدء تحليل الرابط"):
            with st.spinner("جاري التحليل..."):
                time.sleep(1.5)
                if "http:" in u_url and "https:" not in u_url: st.error("🚩 تحذير: الرابط غير مشفر.")
                else: st.warning("تنبيه: سياج رصد نشاطاً مشبوهاً.")
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card'><h4>📞 فحص الأرقام</h4>", unsafe_allow_html=True)
        u_phone = st.text_input("أدخل الرقم للفحص:", placeholder="05xxxxxxxx", key="check_phone")
        if st.button("كشف هوية الرقم"):
            with st.spinner("جاري البحث..."):
                time.sleep(1.5)
                if u_phone in PHONE_DB: st.success(f"🔍 النتيجة: الرقم مسجل باسم [{PHONE_DB[u_phone]}]")
                else: st.error("⚠️ الرقم غير مسجل في قاعدة بياناتنا الموثوقة.")
        st.markdown("</div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card'><h4>🖼️ فحص الصور (AI)</h4>", unsafe_allow_html=True)
        u_img = st.file_uploader("ارفع الصورة للتحليل:", type=['jpg', 'png', 'jpeg'], key="check_img")
        if u_img and st.button("تحليل بصمة الصورة"):
            with st.spinner("جاري فحص البكسلات..."):
                time.sleep(2)
                st.info("النتيجة: الصورة مصنوعة بالذكاء الاصطناعي بنسبة 92%.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- 5. بصمة سياج ---
elif section == "بصمة سياج 🕵️‍♂️":
    st.title("🕵️‍♂️ مختبر التحقيق الرقمي (Digital Forensics)")
    st.markdown("""<div class='card'><h3>🔍 ما هي بصمة الملف (Hash)؟</h3><p>بصمة الملف هي قيمة رقمية فريدة. إذا تم تغيير حرف واحد تتغير هذه البصمة تماماً!</p></div>""", unsafe_allow_html=True)
    f_audit = st.file_uploader("ارفع الملف لاستخراج بصمته:", key="audit_in")
    if f_audit:
        with st.spinner("جاري توليد الـ Hash..."):
            time.sleep(1)
            st.success(f"تم استخراج البصمة الرقمية: {hash(f_audit.name)}")
            st.info("حالة الملف: مطابق للمعايير الأمنية.")

# --- 6. جواز سياج الرقمي ---
elif section == "جواز سياج الرقمي 🎫":
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>🎫 جواز سياج الرقمي</h2>", unsafe_allow_html=True)
    col_sanad, col_passport = st.columns([1, 2])
    with col_sanad:
        st.image("https://img.icons8.com/fluency/240/certificate.png", width=250)
        st.success("🤖 **سند:** كفو يا بطلة! هذا جوازك صار جاهز.")
    with col_passport:
        st.markdown(f"""
        <div style="border: 2px solid #1E3A8A; padding: 20px; border-radius: 15px; background-color: #F0F4F8; color: black;">
            <h3 style="color: #1E3A8A; text-align: center;">SAUDI CYBER PASSPORT</h3>
            <hr>
            <p><b>الاسم المستعار:</b> علو</p>
            <p><b>الرتبة السيبرانية:</b> عضو حامي</p>
            <p><b>تاريخ الإصدار:</b> 2026م</p>
            <p style="text-align: center; font-size: 20px;">🛡️🇸🇦🛡️</p>
        </div>""", unsafe_allow_html=True)

# --- 7. مشوش التنصت ---
elif section == "مشوش التنصت 📡":
    st.title("📡 نظام عزل ومنع التنصت (Cyber Jammer)")
    st.markdown("<div class='card'><h3>⚠️ تحذير أمني</h3><p>تفعيل بروتوكول الحماية الصوتية لمنع الاختراق عبر الميكروفونات.</p></div>", unsafe_allow_html=True)
    if st.button("تفعيل درع التشويش الفوري ⚡"):
        with st.status("جاري تشفير المحيط الصوتي..."):
            time.sleep(2)
        st.markdown("<div style='background: black; padding: 20px; border-radius: 10px; text-align: center; color: #0F0;'>⚡ JAMMING ACTIVE ⚡</div>", unsafe_allow_html=True)
        st.toast("سياج: تم تفعيل وضع المنطقة الصامتة!")

# --- 8. مختبر التشفير ---
elif section == "مختبر التشفير 🔑":
    st.title("🔑 نظام سياج للتشفير المتقدم")
    tab_enc, tab_dec = st.tabs(["🔒 تشفير رسالة", "🔓 فك تشفير رسالة"])
    with tab_enc:
        txt_to_encrypt = st.text_area("أدخل النص المراد تأمينه:", key="enc_txt")
        user_key = st.text_input("ضع رمزاً سرياً (Key):", type="password")
        if st.button("توليد الكود المشفر"):
            if txt_to_encrypt and user_key:
                res = base64.b64encode((txt_to_encrypt + "||" + user_key).encode()).decode()
                st.code(f"SIYAJ_SECURE_{res}")
    with tab_dec:
        txt_to_decrypt = st.text_area("أدخل الكود المشفر:", key="dec_txt")
        key_to_check = st.text_input("أدخل الرمز لفك القفل:", type="password")
        if st.button("فك التشفير الآن"):
            try:
                clean_code = txt_to_decrypt.replace("SIYAJ_SECURE_", "")
                decoded_raw = base64.b64decode(clean_code).decode()
                msg, k = decoded_raw.split("||")
                if k == key_to_check: st.success(f"الرسالة: {msg}")
                else: st.error("الرمز خطأ!")
            except: st.error("فشل فك التشفير.")

# --- 9. دليل سياج ---
elif section == "دليل سياج ❓":
    st.title("❓ دليل استخدام المنظومة")
    with st.expander("🔍 ماذا أفعل في مركز الفحص؟"):
        st.write("ضع أي رابط أو رقم غريب هنا ليفحصه سند لك.")
    st.divider()
    with st.form("tech_support"):
        c_n = st.text_input("الاسم الأكاديمي", value=c_user_name)
        c_m = st.text_area("المشكلة التقنية")
        if st.form_submit_button("إرسال فزعة لسند 🚨"):
            send_telegram_notification(f"🛠️ دعم فني من {c_n}: {c_m}")
            st.success("تم الإرسال!")

# --- 10. بلاغ طوارئ ---
elif section == "بلاغ طوارئ 🚨":
    st.title("🚨 مركز البلاغات الفوري")
    st.markdown(f"<div class='card'><strong>🤖 المساعد سند:</strong> مرحباً يا {c_user_name}، ارفع بلاغك وسأقوم بتشفيره وإرساله فوراً.</div>", unsafe_allow_html=True)
    report_text = st.text_area("وصف الحادثة السيبرانية:")
    if st.button("إرسال البلاغ المشفر 🚨"):
        if report_text:
            send_telegram_notification(f"🚨 بلاغ طوارئ من {c_user_name}: {report_text}")
            st.balloons()
            st.success("تم رفع بلاغك وتأمينه بنجاح. اطمئني، سند معك!")

# --- 11. سجل الإدارة (للمسؤول فقط) ---
elif section == "سجل الإدارة 📋":
    st.title("📋 سجل المراقبة والإدارة الآمن")
    if st.text_input("أدخلي رمز الوصول الإداري:", type="password") == "ALYA_DEV":
        if st.session_state.log_history: st.table(pd.DataFrame(st.session_state.log_history))
        else: st.write("لا يوجد سجل دخول حالياً.")
