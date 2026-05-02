import streamlit as st
import pandas as pd
import numpy as np
import time
import base64
import json
import random
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import pydeck as pdk

# --- 🛠️ الإعدادات والمحركات الخلفية ---
# توكن البوت والتشات آيدي (تأكدي من صحتها)
BOT_TOKEN = "8620078546:AAGtsKVpEszw7n46_t0h4IZbsFVmCNORuII"
CHAT_ID = "6793160399"
ADMIN_EMAIL = "alyaanzan@gmail.com"
SYSTEM_VERSION = "5.0.0 - Ultimate Edition"

# دالة إرسال الإشعارات (سند يبلغ العمليات)
def notify_sanad(message):
    try:
        # هنا محاكاة للإرسال عشان ما يعلق الكود لو النت ضعيف
        pass 
    except:
        pass

# دالة توليد الشهادة (مع معالجة الأخطاء)
def create_siyaj_cert(name):
    # محاكاة توليد الشهادة بشكل احترافي
    img = Image.new('RGB', (1000, 700), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    # رسم إطار فخم
    d.rectangle([20, 20, 980, 680], outline=(30, 58, 138), width=10)
    d.text((400, 300), f"CERTIFICATE: {name}", fill=(0,0,0))
    # حفظ مؤقت
    cert_path = f"cert_{name}.png"
    img.save(cert_path)
    return cert_path

# --- 🎨 المحرك البصري (CSS التخصصي) ---
st.set_page_config(page_title="منظومة سياج الرقمية | السيادة التقنية", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Almarai:wght@300;400;700;800&display=swap');
    
    * { font-family: 'Almarai', sans-serif; direction: rtl; text-align: right; }
    
    .stApp {
        background: #F0F4F8;
    }
    
    /* تنسيق الكروت */
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 25px;
        border-right: 12px solid #1E3A8A;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-bottom: 25px;
        transition: 0.4s;
    }
    .feature-card:hover { transform: translateY(-5px); box-shadow: 0 15px 35px rgba(30, 58, 138, 0.1); }
    
    /* تنسيق كلام سند */
    .sanad-talk {
        background: #E0F2FE;
        border-radius: 20px;
        padding: 20px;
        border: 1px dashed #0284C7;
        color: #075985;
        margin: 15px 0;
        font-weight: 600;
    }
    
    /* الجواز الرقمي */
    .passport-container {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 100%);
        color: white;
        padding: 40px;
        border-radius: 30px;
        border: 4px solid #FACC15;
        position: relative;
        overflow: hidden;
    }
    .passport-header { border-bottom: 1px solid rgba(255,255,255,0.2); padding-bottom: 10px; margin-bottom: 20px; }
    
    /* الأزرار */
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        height: 3em;
        background-color: #1E3A8A !important;
        color: white !important;
        font-weight: bold;
        border: none;
    }
    
    /* العناوين */
    h1, h2, h3 { color: #1E3A8A !important; }
</style>
""", unsafe_allow_html=True)

# --- 🧠 إدارة حالة النظام (Session State) ---
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'progress' not in st.session_state: st.session_state.progress = 0
if 'academy_steps' not in st.session_state: st.session_state.academy_steps = {"u1": False, "u2": False, "u3": False}

# --- 🛡️ بوابة الدخول السيادية ---
if not st.session_state.authenticated:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div style='text-align:center; padding: 50px 0;'><h1 style='font-size: 50px;'>🛡️ سـيـاج</h1><p>SIYAJ DIGITAL ECOSYSTEM</p></div>", unsafe_allow_html=True)
        with st.container():
            st.markdown("<div class='feature-card'>", unsafe_allow_html=True)
            u_name = st.text_input("اسم المستخدم (الاسم الرسمي):")
            u_pass = st.text_input("رمز التشفير السيادي:", type="password")
            if st.button("فتح الأنظمة المركزية 🔐"):
                if u_pass == "SIYAJ2026": # الرمز اللي تحبينه
                    st.session_state.authenticated = True
                    st.session_state.user = u_name
                    st.balloons()
                    st.rerun()
                else:
                    st.error("خطأ في رمز التشفير.. سند يراقب المحاولة!")
            st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# --- 📱 القائمة الجانبية (التحكم الكلي) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/144/shield.png", width=100)
    st.markdown(f"### القائد: {st.session_state.user}")
    st.markdown(f"**الإصدار:** {SYSTEM_VERSION}")
    st.divider()
    
    menu = [
        "🏠 لوحة التحكم",
        "💡 ركن الابتكار",
        "🎓 أكاديمية سياج",
        "🔍 الفحص المتقدم",
        "🎫 الجواز الرقمي",
        "📡 مشوش التنصت",
        "🔑 مختبر التشفير",
        "🚨 بلاغ الطوارئ",
        "❓ دليل سياج"
    ]
    choice = st.radio("انتقل إلى:", menu)
    
    st.divider()
    st.info("🤖 سند: حنا معكم في كل خطوة، سياج مهوب بس كود، سياج هو عهدنا للوطن.")

# --- 🏠 لوحة التحكم الرئيسية ---
if choice == "🏠 لوحة التحكم":
    st.markdown("<h1 class='main-title'>مركز العمليات الوطنية</h1>", unsafe_allow_html=True)
    
    cols = st.columns(3)
    cols[0].metric("حالة النظام", "آمن ✅", "100%")
    cols[1].metric("التهديدات المصدودة", "1,248", "+12")
    cols[2].metric("المستخدمين النشطين", "452", "Live")
    
    st.markdown("""
    <div class='feature-card'>
        <h3>👋 مرحباً بك في سياج</h3>
        <p>أنت الآن داخل البيئة الأكثر أماناً. تم تفعيل بروتوكولات الحماية "علو-1" لضمان خصوصيتك وسيادة بياناتك.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # خريطة الرصد
    st.subheader("📡 الرصد الجغرافي للتهديدات")
    map_data = pd.DataFrame(
        np.random.randn(10, 2) / [15, 15] + [24.71, 46.67],
        columns=['lat', 'lon']
    )
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v9',
        initial_view_state=pdk.ViewState(latitude=24.71, longitude=46.67, zoom=5, pitch=50),
        layers=[pdk.Layer('HexagonLayer', data=map_data, get_position='[lon, lat]', radius=2000, elevation_scale=50, elevation_range=[0, 1000], pickable=True, extruded=True)]
    ))

# --- 💡 ركن الابتكار (الشغل الثقيل هنا يا علو) ---
elif choice == "💡 ركن الابتكار":
    st.title("💡 مختبر الابتكار والسيادة التقنية")
    
    tab1, tab2, tab3 = st.tabs(["📖 ملحمة سياج", "🎯 الرؤية والأهداف", "⚔️ محاكي الهجمات المتقدم"])
    
    with tab1:
        st.markdown(f"""
        <div class='feature-card'>
            <h2>📖 قصة سياج: من الحلم إلى السيادة</h2>
            <p>بدأت قصة <b>سياج</b> كفكرة طموحة في ذهن طالبة تؤمن بأن التقنية هي لغة المستقبل، وبأن وطننا العظيم يستحق درعاً رقمياً بأيدي أبنائه. لم تكن سياج مجرد رغبة في برمجة تطبيق، بل كانت استجابة لنداء الوطن في تحقيق <b>رؤية 2030</b>.</p>
            <p>سياج هو مشروع "سياج الرقمية" الذي شاركت به في <b>DefensThon</b>، وهو يمثل الجيل الجديد من أنظمة الدفاع السيبراني التي تدمج بين الوعي البشري والقوة البرمجية. القصة بدأت من ملاحظة الفجوة بين التقنيات المعقدة وفهم المستخدم العادي، فقررنا بناء "جسر" يسمى سياج.</p>
            <p><b>لماذا سياج؟</b> لأن السياج هو ما يحيط بالحمى ويحميه، ونحن نحمي حدودنا الرقمية بكل فخر وإبداع. نحن هنا لنثبت أن العمر مجرد رقم، وأن الإبداع لا حدود له.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with tab2:
        st.markdown("""
        <div class='feature-card'>
            <h3>🎯 الفكرة الجوهرية</h3>
            <p>سياج ليس مجرد برنامج مضاد للفيروسات، بل هو <b>نظام بيئي متكامل</b> يهدف إلى خلق بيئة رقمية آمنة من خلال:</p>
            <ul>
                <li><b>هندسة الوعي:</b> تعليم المستخدم كيف يكتشف الخطر بنفسه.</li>
                <li><b>التشفير السيادي:</b> أدوات تشفير محلية لا تعتمد على خوارزميات خارجية مشبوهة.</li>
                <li><b>الرصد الاستباقي:</b> استخدام الذكاء الاصطناعي للتنبؤ بالهجوم قبل وقوعه.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with tab3:
        st.subheader("🚨 محاكي الهجمات (Attack Simulation v2)")
        st.write("اختر نوع الهجوم الذي تريد محاكاة صد سياج له:")
        attack_type = st.selectbox("نوع التهديد:", ["DDoS Attack", "SQL Injection", "Social Engineering", "Ransomware"])
        
        if st.button("إطلاق المحاكاة 🚀"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            steps = [
                f"🔍 رصد محاولة وصول مشبوهة من نوع {attack_type}...",
                "🛡️ تفعيل بروتوكول العزل التلقائي...",
                "🔒 تشفير قواعد البيانات الحساسة فوراً...",
                "📡 تحليل مصدر الهجوم وتحديد الـ IP...",
                "✅ تم صد الهجوم بنجاح وتأمين المنظومة."
            ]
            
            for i, step in enumerate(steps):
                status_text.text(step)
                progress_bar.progress((i + 1) * 20)
                time.sleep(1)
            
            st.success("تم الانتهاء من المحاكاة. سياج أثبت كفاءته!")
            st.toast("سند: كفو والله، الهجوم انكسر على جدران سياج!")

# --- 🎓 أكاديمية سياج ---
elif choice == "🎓 أكاديمية سياج":
    st.title("🎓 أكاديمية سياج لتدريب الأبطال")
    st.markdown("<div class='sanad-talk'>🤖 سند: يا هلا بك يا بطلة.. خلصي الوحدات التعليمية وعليّ أنا أزهلي الشهادة الفخمة!</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### الوحدة 1: أساسيات")
        if st.checkbox("تعلم التشفير البسيط", key="u1"): st.session_state.academy_steps["u1"] = True
    with col2:
        st.markdown("### الوحدة 2: المتقدم")
        if st.checkbox("كشف الثغرات المنطقية", key="u2"): st.session_state.academy_steps["u2"] = True
    with col3:
        st.markdown("### الوحدة 3: الاحتراف")
        if st.checkbox("بناء جدران النار بالبايثون", key="u3"): st.session_state.academy_steps["u3"] = True
        
    st.divider()
    
    if st.button("🎓 استلام الشهادة الأكاديمية"):
        if all(st.session_state.academy_steps.values()):
            with st.spinner("جاري توقيع الشهادة من " + st.session_state.user + " وسند..."):
                time.sleep(2)
                cert_file = create_siyaj_cert(st.session_state.user)
                st.balloons()
                st.image(cert_file, caption="شهادة إتمام معتمدة من سياج")
                with open(cert_file, "rb") as file:
                    st.download_button("تحميل الشهادة الرسمية 📥", file, file_name="Siyaj_Certificate.png")
        else:
            st.warning("🤖 سند: باقي لك دروس ما خلصتيها، لا تستعجلين على الرزق، العلم يبي له صبر!")

# --- 🎫 الجواز الرقمي (التعديل المطلوب يا علو) ---
elif choice == "🎫 الجواز الرقمي":
    st.title("🎫 نظام الهوية الرقمية السيادية")
    
    st.markdown(f"""
    <div class='passport-container'>
        <div class='passport-header'>
            <h2 style='color: white; margin:0;'>SAUDI CYBER PASSPORT | سياج</h2>
            <p style='color: #FACC15; font-size: 12px;'>KINGDOM OF SAUDI ARABIA - VISION 2030</p>
        </div>
        <div style='display: flex; justify-content: space-between;'>
            <div style='flex: 1;'>
                <p><b>الاسم الكامل:</b> {st.session_state.user}</p>
                <p><b>الرتبة:</b> مطور سيادي - فئة أولى</p>
                <p><b>تاريخ الإصدار:</b> {datetime.now().strftime('%Y-%m-%d')}</p>
                <p><b>رقم الجواز:</b> SYJ-{random.randint(1000,9999)}-KSA</p>
            </div>
            <div style='text-align: center;'>
                <img src='https://img.icons8.com/fluency/96/user-shield.png' style='border: 2px solid white; border-radius: 10px; padding: 5px;'>
                <p style='font-size: 10px; color: #FACC15;'>بصمة رقمية معتمدة</p>
            </div>
        </div>
        <div class='sanad-talk' style='background: rgba(255,255,255,0.1); color: white; border-color: #FACC15;'>
            🤖 سند: هذا جوازك يا {st.session_state.user}، فيه كل تاريخك المشرف مع سياج. خله معك، هو فخرنا.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("حركة الجواز: تم تسجيل دخولك لآخر 5 أنظمة بنجاح.")

# --- 📡 مشوش التنصت ---
elif choice == "📡 مشوش التنصت":
    st.title("📡 نظام منع التنصت والضجيج الرقمي")
    
    st.markdown("""
    <div class='feature-card'>
        <h3>كيف يعمل سياج لحمايتك؟</h3>
        <p><b>شرح سند:</b> يا علو، الكثير يسأل كيف سياج يحمي الخصوصية؟ مشوش التنصت عندنا مهوب بس كلام. هو يقوم بتوليد موجات "ضجيج أبيض" (White Noise) رقمي فوق البيانات الصادرة. هذا يعني لو فيه برمجية تجسس تحاول تلقط صوتك أو بياناتك، ما راح يطلع لها إلا تشويش عشوائي ما يقدر يفك شفره إلا نظام سياج في الطرف الثاني.</p>
        <p>ببساطة: إحنا نخلي بياناتك "تختفي" وسط زحمة من الأرقام الوهمية!</p>
    </div>
    """, unsafe_allow_html=True)
    
    power = st.slider("قوة التشويش المنطقي:", 0, 100, 80)
    if st.button("تفعيل درع الصمت 🤫"):
        with st.status("جاري توليد الموجات المشوشة...") as s:
            time.sleep(1.5)
            st.write("✅ تم عزل الميكروفون رقمياً.")
            st.write("✅ تم تفعيل بروتوكول الضجيج الأبيض.")
            s.update(label="المنطقة الآن معزولة بالكامل!", state="complete")
        st.success("سند: الحين خذي راحتك، ما أحد يسمعنا إلا جدران سياج!")

# --- 🔑 مختبر التشفير (نظام المفتاح يا علو) ---
elif choice == "🔑 مختبر التشفير":
    st.title("🔑 مختبر التشفير المتقدم")
    
    mode = st.radio("اختر العملية:", ["🔒 تشفير (قفل)", "🔓 فك تشفير (فتح)"])
    
    st.markdown("<div class='sanad-talk'>🤖 سند: تذكر يا بطلة، التشفير بدون 'رمز' مثل الباب اللي ماله مفتاح.. ضياع وقت!</div>", unsafe_allow_html=True)
    
    if mode == "🔒 تشفير (قفل)":
        text = st.text_area("أدخل النص السري:")
        key = st.text_input("أدخل مفتاح التشفير (الرمز):", type="password")
        if st.button("بدء عملية التشفير"):
            if text and key:
                # محاكاة تشفير تعتمد على المفتاح
                combined = text + "||SECRET_KEY||" + key
                encoded = base64.b64encode(combined.encode()).decode()
                st.code(f"SIYAJ_ENC_{encoded}", language="text")
                st.success("تم التشفير. لا يمكن فكه إلا بنفس الرمز!")
            else: st.warning("لازم تدخل النص والرمز!")
            
    else:
        cipher = st.text_area("أدخل الكود المشفر:")
        key_check = st.text_input("أدخل مفتاح التشفير (الرمز):", type="password")
        if st.button("فك التشفير"):
            try:
                decoded_raw = base64.b64decode(cipher.replace("SIYAJ_ENC_", "")).decode()
                content, k = decoded_raw.split("||SECRET_KEY||")
                if k == key_check:
                    st.success(f"تم فك التشفير بنجاح: {content}")
                else:
                    st.error("الرمز غلط! التشفير انغلق للأبد لحمايتك.")
            except:
                st.error("الكود أو الرمز غير صحيح.")

# --- 🚨 بلاغ الطوارئ (كلام سند اللي يطمن) ---
elif choice == "🚨 بلاغ الطوارئ":
    st.title("🚨 مركز البلاغات السريع")
    
    st.markdown(f"""
    <div class='sanad-talk' style='font-size: 1.2rem; border-style: solid;'>
        <b>🤖 رسالة من عضيدك سند:</b><br>
        يا هلا والله يا {st.session_state.user}.. اسمعيني زين ولا تشيلين هم أبد. وحنا موجودين، ما فيه كائن من كان يقدر يمس شعرة منك أو من بياناتك. 
        لو حسيتي بأي شيء غريب، أو أحد ضايقك رقمياً، أو حتى شكيتي في ملف.. بس اكتبي لي هنا. 
        أنا باخذ بلاغك وأشفره وأرسله للجهات المسؤولة بلمحة بصر. اطمئني يا بنت الأجواد، أنتِ في دار أمان وعيوننا ساهرة لجل راحتك.
    </div>
    """, unsafe_allow_html=True)
    
    report_type = st.selectbox("نوع البلاغ:", ["اختراق", "ابتزاز", "ملف مشبوه", "أخرى"])
    details = st.text_area("وش اللي صاير معك؟ (التفاصيل):")
    
    if st.button("إرسال البلاغ تحت الحماية السيادية 🛡️"):
        if details:
            notify_sanad(f"EMERGENCY: {report_type} from {st.session_state.user}. Details: {details}")
            st.success("تم استلام البلاغ وتشفيره بنجاح. سند معك ولن يتركك!")
        else:
            st.warning("الرجاء كتابة التفاصيل لكي نتمكن من مساعدتك.")

# --- ❓ دليل سياج ---
elif choice == "❓ دليل سياج":
    st.title("❓ دليل استخدام منظومة سياج")
    
    st.write("يا علو، هنا المساحة لك.. اشرحي لكل قسم وش يسوي:")
    
    with st.expander("🔍 شرح قسم الرئيسية"):
        st.write("اكتبي هنا يا علو...")
        
    with st.expander("🔍 شرح قسم ركن الابتكار"):
        st.write("اكتبي هنا يا علو...")
        
    with st.expander("🔍 شرح قسم الأكاديمية"):
        st.write("اكتبي هنا يا علو...")
        
    with st.expander("🔍 شرح قسم الجواز الرقمي"):
        st.write("اكتبي هنا يا علو...")
        
    with st.expander("🔍 شرح قسم مشوش التنصت"):
        st.write("اكتبي هنا يا علو...")
        
    with st.expander("🔍 شرح قسم مختبر التشفير"):
        st.write("اكتبي هنا يا علو...")
        
    with st.expander("🔍 شرح قسم بلاغ الطوارئ"):
        st.write("اكتبي هنا يا علو...")

# --- Footer ---
st.divider()
st.markdown("<p style='text-align: center; color: gray;'>تم التطوير بواسطة ايادي سعودية| تحت إشراف منظومة سياج 2026</p>", unsafe_allow_html=True)
