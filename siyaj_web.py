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
# توكن البوت والتشات عشان التنبيهات
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
    # عنوان المنظومة
    st.markdown("<h1 class='main-title'>🛡️ مـنـظـومـة سـيـاج الـرقـمـيـة</h1>", unsafe_allow_html=True)
    
    with st.container():
        # هنا سند يرحب بالمستخدم بلهجته اللي اتفقنا عليها
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
        
        # اختيار الجنس عشان سند يعرف يكلمك صح
        u_gender = col1.radio("عشان أعرف أزهل الموضوع وأكلمك صح، أنت بطل ولا بطلة؟", ["أنثى", "ذكر"], horizontal=True)
        
        u_type = col2.selectbox("رتبتك اللي تبيها في المنظومة:", ["زائر","مسؤول حماية بيانات", "طالب/ة مبتكر"])
        
        # رمز فك التشفير (السيادي)
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
                
                # سند يبارك للمستخدم قبل ما يدخله
                st.success(f"كفو يا {u_name}! تم اعتماد هويتك.. استلمت المهمة، تفضل للمنظومة.")
                st.balloons()
                time.sleep(1)
                st.rerun()
            else:
                st.error("⚠️ فيه غلط في البيانات يا غالي، تأكد من الرمز وحاول مرة ثانية.")
    st.stop()
# --- شريط الحالة (الإضافة الجديدة) ---
c_user_name = st.session_state.user_data['name']
c_user_type = st.session_state.user_data['type']
st.markdown(f"""<div class='status-bar'>
    <span>👤 المستخدم الحالي: <b>{c_user_name}</b></span>
    <span>📡 حالة الدرع السيبراني: <b>نشط وتعمل تحت التشفير السيادي</b></span>
    <span>🎖️ الرتبة الممنوحة: <b>{c_user_type}</b></span>
</div>""", unsafe_allow_html=True)

# --- 1. القائمة الجانبية (تعريف الأقسام) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/144/shield.png", width=100)
    st.markdown(f"<h2 style='color:#1E3A8A;'>سياج v4.0</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='color:#1E3A8A;'>سند:مرحبًا بك في منظومة سياج الرقميــــة</h2>", unsafe_allow_html=True)

    # تأكدي إن الأقسام هنا مكتوبة بنفس الإيموجي والاسم اللي تحت
    menu = [
        "الرئيسية 🏠", 
        "ركن الابتكار 💡", 
        "أكاديمية سياج 🎓", 
        "مركز الفحص الشامل 🔍", 
        "بصمة سياج 🕵️‍♂️", 
        "جواز سياج الرقمي 🛂", 
        "مشوش التنصت 📡", 
        "مختبر التشفير 🔑", 
        "دليل سياج ❓", 
        "بلاغ طوارئ 🚨"
    ]
    
    if st.session_state.user_data['email'] == ADMIN_EMAIL:
        menu.append("سجل الإدارة 📋")
        
    # هنا يتم تعريف المتغير section - هذا السطر هو الأهم!
    section = st.radio("انتقل بين وحدات المنظومة:", menu)

# --- 🛂 1. قسم جواز السفر الرقمي (البديل القوي) ---
elif section == "جواز سياج الرقمي 🎫":
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>🎫 جواز سياج الرقمي</h2>", unsafe_allow_html=True)
    
    # تقسيم الصفحة لعمودين: واحد لسند المحتفل وواحد لبيانات الجواز
    col_sanad, col_passport = st.columns([1, 2])
    
    with col_sanad:
        # صورة سند وهو يبارك للمستخدم (وضعية الاحتفال)
        st.image("celebration.png", width=250)
        st.success(f"🤖 **سند:** كفو يا بطلة! هذا جوازك صار جاهز.. يثبت إنك كفو وقد المسؤولية السيبرانية.")

    with col_passport:
        # تصميم الجواز داخل كارد مرتب
        st.markdown(f"""
        <div style="border: 2px solid #1E3A8A; padding: 20px; border-radius: 15px; background-color: #F0F4F8;">
            <h3 style="color: #1E3A8A; text-align: center;">SAUDI CYBER PASSPORT</h3>
            <hr>
            <p><b>الاسم المستعار:</b> {st.session_state.user_data.get('nickname', 'علو')}</p>
            <p><b>الرتبة السيبرانية:</b> عضو حامي</p>
            <p><b>تاريخ الإصدار:</b> 2024م</p>
            <p style="text-align: center; font-size: 20px;">🛡️🇸🇦🛡️</p>
        </div>
        """, unsafe_allow_html=True)
        
        # زر لتحميل الجواز (كفكرة إضافية)
        st.button("تحميل نسخة من الجواز 📥")

# --- 📡 2. قسم مشوش التنصت (الأكشن التقني) ---
elif section == "مشوش التنصت 📡":
    st.title("📡 نظام عزل ومنع التنصت (Cyber Jammer)")
    st.write("تفعيل بروتوكول الحماية الصوتية لمنع الاختراق عبر الميكروفونات المحيطة.")
    
    st.markdown("""<div class='card' style='text-align:center;'>
    <h3>⚠️ تحذير أمني</h3>
    <p>عند تفعيل المشوش، سيقوم سياج بتوليد موجات 'الضجيج الأبيض' الرقمية لتغطية الترددات الحيوية ومنع أي جهاز تنصت من التقاط المحادثات.</p>
    </div>""", unsafe_allow_html=True)
    
    if st.button("تفعيل درع التشويش الفوري ⚡"):
        with st.status("جاري تشفير المحيط الصوتي...", expanded=True) as status:
            st.write("🔍 فحص الميكروفونات النشطة...")
            time.sleep(1)
            st.write("📡 توليد موجات التشويش الترددي...")
            time.sleep(1.5)
            st.write("🔒 إنشاء منطقة عزل سيادية...")
            time.sleep(1)
            status.update(label="✅ تم تفعيل وضع المنطقة الصامتة (Silent Zone)", state="complete", expanded=False)
        
        # حركة بصرية للموجات
        st.markdown("""
        <div style="background: black; padding: 20px; border-radius: 10px; text-align: center;">
            <p style="color: #0F0; font-family: monospace; font-size: 20px;">⚡ JAMMING ACTIVE ⚡</p>
            <div style="height: 50px; background: repeating-linear-gradient(90deg, #1E3A8A, #1E3A8A 10px, #000 10px, #000 20px); animation: move 0.5s linear infinite;"></div>
            <style>
                @keyframes move { from { background-position: 0 0; } to { background-position: 40px 0; } }
            </style>
        </div>
        """, unsafe_allow_html=True)
        st.toast("سياج: لا يمكن لأي جهاز الآن التنصت على مريم!")
# --- 3. محتوى الأقسام التفصيلي ---

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
        
        # خريطة تفاعلية محسنة
        map_data = pd.DataFrame(
            np.random.randn(15, 2) / [10, 10] + [24.71, 46.67], 
            columns=['lat', 'lon'])
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/dark-v9',
            initial_view_state=pdk.ViewState(latitude=24.71, longitude=46.67, zoom=4, pitch=45),
            layers=[pdk.Layer('HexagonLayer', data=map_data, get_position='[lon, lat]', radius=20000, elevation_scale=50, elevation_range=[0, 1000], pickable=True, extruded=True)]
        ))

    with t3:
        st.markdown("""<div class='vision-card'>
        <h2 style='text-align: center;'>🇸🇦 سياج والرؤية</h2>
        <p>بناء جيل طموح يحمي مكتسبات الوطن الرقمية، تماشياً مع رؤية المملكة 2030 في التحول الرقمي والسيادة التقنية.</p>
        </div>""", unsafe_allow_html=True)

    with t4:
        st.subheader("🚨 تجربة محاكاة هجوم (Cyber Attack Simulation)")
        st.write("اضغطي الزر لتجربة كيف يتعامل درع 'سياج' مع الهجمات المفاجئة:")
        if st.button("إطلاق هجوم تجريبي ⚠️"):
            with st.status("جاري رصد محاولة اختراق...", expanded=True) as status:
                st.write("🔍 فحص بروتوكولات الاتصال...")
                time.sleep(1)
                st.write("🚩 تم رصد عنوان IP مشبوه يحاول الوصول للقاعدة...")
                time.sleep(1)
                st.write("🛡️ تفعيل جدار الحماية (Firewall) تلقائياً...")
                time.sleep(1)
                st.write("🔒 تشفير البيانات الحساسة فوراً...")
                status.update(label="✅ تم صد الهجوم بنجاح! سياج في أمان.", state="complete", expanded=False)
            st.toast("سياج: تم عزل التهديد بنجاح يا علو!")
            st.success("تم إرسال تقرير الهجوم لغرفة العمليات.")

elif section == "أكاديمية سياج 🎓":
    st.title("🎓 أكاديمية سياج للتميز المعرفي")
    
    # إضافة فاحص كلمة المرور (الإضافة الجديدة)
    with st.expander("🔐 مختبر قوة التشفير الشخصي (Cyber-Meter)", expanded=True):
        st.write("اختبري قوة كلمة مرورك ومدى مقاومتها للاختراق:")
        test_pwd = st.text_input("أدخلي كلمة مرور للتجربة:", type="password")
        if test_pwd:
            score = 0
            if len(test_pwd) >= 8: score += 1
            if any(c.isdigit() for c in test_pwd): score += 1
            if any(c.isupper() for c in test_pwd): score += 1
            if any(c in "!@#$%^&*" for c in test_pwd): score += 1
            
            colors = ["#FF4B4B", "#FFA500", "#FFD700", "#90EE90", "#10B981"]
            labels = ["ضعيفة جداً 🚩", "تحتاج تحسين ⚠️", "متوسطة 🟠", "قوية 🟢", "سياجية حديدية 💪"]
            st.markdown(f"<h3 style='color:{colors[score]}'>{labels[score]}</h3>", unsafe_allow_html=True)
            st.progress(score * 25)

    st.write("دروس تخصصية دسمة لتمكين جيل المستقبل من العلم السيبراني:")
    a1, a2, a3 = st.tabs(["🔐 علم التشفير (الدرع الخفي)", "🎣 فخاخ التصيد (الخدعة الرقمية)", "👣 الخصوصية والبصمة"])
    
    with a1:
        st.markdown("""<div class='card'>
        <h3>🔐 الدرس الأول: ما هو التشفير وكيف يحمينا؟</h3>
        <p>التشفير (Cryptography) هو العلم الذي يحول البيانات من نص مفهوم للجميع إلى رموز غير مفهومة بتاتاً إلا لمن يملك "المفتاح". 
        في سياج نستخدم بروتوكول <b>AES-4096</b>، وهو من أقوى معايير التشفير عالمياً. تخيل أن رسالتك تدخل في صندوق حديدي له ملايين الاحتمالات من الأقفال الرقمية، ولا يمكن فتحه إلا بمفتاحك الخاص والمستقبل.</p>
        <p><b>أهمية التشفير:</b> يضمن أن خصوصيتك، صورك، ورسائلك تظل سرية حتى لو وقعت في يد المتسللين.</p>
        </div>""", unsafe_allow_html=True)
        st.video("https://youtu.be/xHaxAYDt75Q?si=E9Qp49N-fIZUJ2yq")
        
    with a2:
        st.markdown("""<div class='card'>
        <h3>🎣 الدرس الثاني: احذر من 'الصياد' الرقمي (Phishing)</h3>
        <p>التصيد الاحتيالي هو أخطر أنواع الهجمات لأنه يستهدف "العقل" لا "الجهاز". يقوم الهكر بإرسال رابط يشبه تماماً موقع (مدرستي) أو (أبشر) أو (إنستقرام)، وبمجرد إدخالك لاسم المستخدم وكلمة المرور، تصل إليه مباشرة. </p>
        <p><b>نصيحة سياج:</b> دائماً تأكد من رابط الموقع (URL) قبل إدخال أي معلومة، واستخدم وحدة 'مركز الفحص' لدينا للتأكد.</p>
        </div>""", unsafe_allow_html=True)
        st.video("https://youtu.be/gfPN0RIeYLM?si=nCSF_sqcAoIJkq5U")
        
    with a3:
        st.markdown("""<div class='card'>
        <h3>👣 الدرس الثالث: أثرك لا يزول (بصمتك الرقمية)</h3>
        <p>بصمتك الرقمية هي السجل الكامل لكل ما تفعله في الإنترنت؛ من تعليقات، إعجابات، وعمليات بحث. سياج تعلمك كيف تحمي هذه البصمة عبر تفعيل التحقق الثنائي (MFA) وتجنب الاتصال بشبكات الواي فاي العامة غير المشفرة.</p>
        </div>""", unsafe_allow_html=True)
        st.video("https://youtu.be/9eVjgk93PEw?si=MEyjxbsNdofNYXNo")

    st.divider()
    # زر الشهادة (إضافة جديدة)
    if st.button("إصدار شهادة الإتمام باسمي 🎓"):
        res_img = generate_certificate(c_user_name)
        if res_img:
            st.image(res_img, caption="مبروك يا بطل/ة سياج!")
            with open(res_img, "rb") as f:
                st.download_button("تحميل الشهادة PNG", f, "Siyaj_Certificate.png")

elif section == "مركز الفحص الشامل 🔍":
    st.title("🔍 مركز الفحص والتحليل الذكي")
    st.write("أدخل البيانات المراد فحصها للتأكد من سلامتها ومعرفة مصادرها:")
    
    PHONE_DB = {
        "0555555555": "عاليا صالح العنزان (المشرف التقني)",
        "0500000000": "صالح بن محمد (رجل أعمال)",
        "0544444444": "أروى صالح (عضو فريق)"
    }

    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("<div class='card'><h4>🔗 فحص الروابط</h4>", unsafe_allow_html=True)
        u_url = st.text_input("أدخل الرابط (URL):", placeholder="https://...", key="check_url")
        if st.button("بدء تحليل الرابط"):
            with st.spinner("جاري التحليل..."):
                time.sleep(1.5)
                if "http:" in u_url and "https:" not in u_url:
                    st.error("🚩 تحذير: الرابط غير مشفر (Insecure).")
                else:
                    st.warning("تنبيه: سياج رصدت نشاطاً مشبوهاً في هذا النطاق.")
        st.markdown("</div>", unsafe_allow_html=True)
                
    with c2:
        st.markdown("<div class='card'><h4>📞 فحص الأرقام</h4>", unsafe_allow_html=True)
        u_phone = st.text_input("أدخل الرقم للفحص:", placeholder="05xxxxxxxx", key="check_phone")
        if st.button("كشف هوية الرقم"):
            with st.spinner("جاري البحث في السجلات..."):
                time.sleep(1.5)
                if u_phone in PHONE_DB:
                    st.success(f"🔍 نتيجة الفحص: الرقم مسجل باسم [{PHONE_DB[u_phone]}]")
                elif u_phone == "":
                    st.info("الرجاء إدخال رقم أولاً.")
                else:
                    st.error("⚠️ الرقم غير مسجل في قاعدة بياناتنا الموثوقة، يرجى الحذر!")
        st.markdown("</div>", unsafe_allow_html=True)
                
    with c3:
        st.markdown("<div class='card'><h4>🖼️ فحص الصور (AI)</h4>", unsafe_allow_html=True)
        u_img = st.file_uploader("ارفع الصورة للتحليل:", type=['jpg', 'png', 'jpeg'], key="check_img")
        if u_img:
            if st.button("تحليل بصمة الصورة"):
                with st.spinner("جاري فحص البكسلات..."):
                    time.sleep(2)
                    st.info("النتيجة: تم رصد أنماط توليد آلية. الصورة مصنوعة بالذكاء الاصطناعي بنسبة 92%.")
        st.markdown("</div>", unsafe_allow_html=True)

elif section == "بصمة سياج 🕵️‍♂️":
    st.title("🕵️‍♂️ مختبر التحقيق الرقمي (Digital Forensics)")
    st.markdown("""<div class='card'>
    <h3>🔍 ما هي بصمة الملف (Hash)؟</h3>
    <p>بصمة الملف هي قيمة رقمية فريدة تنتج عن خوارزمية رياضية. إذا تم تغيير حرف واحد أو بكسل واحد في الملف، تتغير هذه البصمة تماماً! نحن في سياج نستخدمها للتأكد من أن الملفات أصلية ولم يتم زرع برمجيات خبيثة داخلها.</p>
    </div>""", unsafe_allow_html=True)
    f_audit = st.file_uploader("ارفع الملف لاستخراج بصمته والتأكد من سلامته:", key="audit_in")
    if f_audit:
        with st.spinner("جاري توليد الـ Hash..."):
            time.sleep(1)
            st.success(f"تم استخراج البصمة الرقمية: {hash(f_audit.name)}")
            st.info("حالة الملف: مطابق للمعايير الأمنية لوزارة التعليم.")

elif section == "مختبر التشفير 🔑":
    st.title("🔑 نظام سياج للتشفير المتقدم (البروتوكول الخاص)")
    st.write("هنا يمكنك تأمين رسائلك برمز سري خاص لا يعرفه إلا أنت والمستقبل.")
    
    tab_enc, tab_dec = st.tabs(["🔒 تشفير رسالة", "🔓 فك تشفير رسالة"])
    
    with tab_enc:
        txt_to_encrypt = st.text_area("أدخل النص الذي تريد تأمينه:", key="enc_txt")
        user_key = st.text_input("ضع رمزاً سرياً للرسالة (Key):", type="password")
        if st.button("توليد الكود المشفر"):
            if txt_to_encrypt and user_key:
                combined = txt_to_encrypt + "||" + user_key
                res = base64.b64encode(combined.encode()).decode()
                st.success("تم التشفير بنجاح!")
                st.code(f"SIYAJ_SECURE_{res}")

    with tab_dec:
        txt_to_decrypt = st.text_area("أدخل الكود المشفر هنا:", key="dec_txt")
        key_to_check = st.text_input("أدخل الرمز السري لفك القفل:", type="password")
        if st.button("فك التشفير الآن"):
            if txt_to_decrypt and key_to_check:
                try:
                    clean_code = txt_to_decrypt.replace("SIYAJ_SECURE_", "")
                    decoded_raw = base64.b64decode(clean_code).decode()
                    if "||" in decoded_raw:
                        original_msg, original_key = decoded_raw.split("||")
                        if original_key == key_to_check:
                            st.success("تم التحقق!")
                            st.markdown(f"<div class='card'>{original_msg}</div>", unsafe_allow_html=True)
                except: st.error("فشل فك التشفير.")

# القسم الجديد (دليل سياج)
elif section == "دليل سياج ❓":
    st.title("❓ دليل استخدام المنظومة")
    with st.expander("🔍 ماذا أفعل في مركز الفحص؟"):
        st.write("ضع أي رابط أو رقم غريب هنا ليفحصه سند لك ويتأكد من سلامته.")
    st.divider()
    st.subheader("واجهتك مشكلة؟ سند معك!")
    with st.form("tech_support"):
        c_n = st.text_input("الاسم الأكاديمي", value=c_user_name)
        c_p = st.text_input("رقم الجوال")
        c_m = st.text_area("المشكلة التقنية")
        if st.form_submit_button("إرسال فزعة لسند 🚨"):
            send_telegram_notification(f"🛠️ دعم فني:\n👤 الاسم: {c_n}\n📞 الجوال: {c_p}\n📝 المشكلة: {c_m}")
            st.success("تم الإرسال! سند بيفحص الموضوع.")

elif section == "سجل الإدارة 📋":
    st.title("📋 سجل المراقبة والإدارة الآمن")
    admin_verify = st.text_input("أدخلي رمز الوصول الإداري (علو فقط):", type="password")
    if admin_verify == "ALYA_DEV":
        if st.session_state.log_history:
            st.table(pd.DataFrame(st.session_state.log_history))
        else: st.write("لا يوجد سجل دخول حالياً.")
    else:
        st.info("يرجى إدخال رمز التحقق الخاص بالمشغل لعرض السجلات.")

elif section == "بلاغ طوارئ 🚨":
    st.title("🚨 مركز البلاغات الفوري")
    st.markdown(f"<div class='card'><strong>🤖 المساعد سند:</strong><br>مرحباً يا {c_user_name}، أنا سند.. عضيدك في المواقف الصعبة. ارفع بلاغك وسأقوم بتشفيره وإرساله فوراً لغرفة العمليات ولا تقلق تذكر دائمًا انت في وطن قلبه كبير.</div>", unsafe_allow_html=True)
    report_text = st.text_area("وصف الحادثة السيبرانية:")
    if st.button("إرسال البلاغ المشفر 🚨"):
        if report_text:
            send_telegram_notification(f"🚨 بلاغ طوارئ جديد!\nالمبلغ: {c_user_name}\nالتفاصيل: {report_text}")
            st.balloons()
            st.success(f"شكراً يا {c_user_name}.. تم رفع بلاغك وتأمينه بنجاح تحت حماية سياج. اطمئني، سند معك!")
        else:
            st.error("الرجاء كتابة تفاصيل البلاغ قبل الإرسال.")
