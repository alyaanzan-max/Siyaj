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
import io

def generate_cert(user_name):
    try:
        from bidi.algorithm import get_display
        import arabic_reshaper
        img = Image.open("siyaj_award.png")
        draw = ImageDraw.Draw(img)
        
        # تشبيك الحروف
        reshaped_text = arabic_reshaper.reshape(user_name)
        bidi_text = get_display(reshaped_text)
        
        # محاولة البحث عن خط يدعم العربي في السيرفر
        try:
            # خط DejaVuSans مشهور في السيرفرات ويدعم العربي
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 50)
        except:
            font = ImageFont.load_default()
            
        draw.text((280, 345), bidi_text, fill=(0, 0, 0), font=font)
        
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        return buf.getvalue()
    except:
        return None
# --- 🚀 محرك الإعدادات الكبرى ---
BOT_TOKEN = "8620078546:AAGtsKVpEszw7n46_t0h4IZbsFVmCNORuII"
CHAT_ID = "6793160399"
ADMIN_EMAIL = "alyaanzan@gmail.com"
SYSTEM_VERSION = "6.5.0 - Heavy Duty Edition"

# --- 🎨 محرك التصميم البصري (CSS المتقدم) ---
st.set_page_config(page_title="منظومة سياج | السيادة الرقمية", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Almarai:wght@300;400;700;800&display=swap');
    
    * { font-family: 'Almarai', sans-serif; direction: rtl; text-align: right; }
    
    .stApp { background: #F4F7F9; }
    
    /* المنطقة البيضاء (منطقة سند) */
    .sanad-banner {
        background: white;
        padding: 30px;
        border-radius: 0 0 50px 50px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 40px;
        border-bottom: 5px solid #1E3A8A;
        animation: slideDown 0.8s ease-out;
    }
    
    @keyframes slideDown {
        from { transform: translateY(-100%); }
        to { transform: translateY(0); }
    }

    .sanad-text {
        color: #1E3A8A;
        font-size: 24px;
        font-weight: 800;
        margin: 0;
    }

    /* كروت الواجهة */
    .feature-card {
        background: white;
        padding: 25px;
        border-radius: 20px;
        border-right: 15px solid #1E3A8A;
        box-shadow: 0 8px 20px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    .feature-card:hover { transform: scale(1.02); box-shadow: 0 12px 30px rgba(30, 58, 138, 0.15); }
    
    /* الجواز الرقمي الفخم */
    .passport-box {
        background: linear-gradient(145deg, #0B1E3D 0%, #1E3A8A 100%);
        color: white;
        padding: 45px;
        border-radius: 35px;
        border: 4px solid #D4AF37;
        position: relative;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    }
    
    /* الأزرار السيادية */
    .stButton>button {
        background: linear-gradient(90deg, #1E3A8A, #3B82F6) !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        height: 3.5rem !important;
        font-weight: bold !important;
        font-size: 18px !important;
        transition: 0.3s !important;
    }
    .stButton>button:hover { filter: brightness(1.2); transform: translateY(-2px); }

    /* كلام سند الجانبي */
    .sanad-bubble {
        background: #E0F2FE;
        border: 1px solid #7DD3FC;
        padding: 15px;
        border-radius: 15px 15px 0 15px;
        color: #0369A1;
        font-weight: 600;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# --- 🧠 إدارة المحرك الداخلي ---
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'user_profile' not in st.session_state: st.session_state.user_profile = {}
if 'logs' not in st.session_state: st.session_state.logs = []

def add_log(msg):
    now = datetime.now().strftime("%H:%M:%S")
    st.session_state.logs.append(f"[{now}] {msg}")

# --- 🛡️ المرحلة 1: بوابة الدخول (التعديل المطلوب) ---
if not st.session_state.logged_in:
    # المنطقة البيضاء العلوية (كلام سند)
    st.markdown("""
    <div class='sanad-banner'>
        <p class='sanad-text'>🤖 سند: يا هلا بطلنا.. سياج بانتظارك، سجل هويتك عشان تفتح لك أبواب الحماية!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        st.markdown("<div class='feature-card' style='text-align:center;'>", unsafe_allow_html=True)
        st.image("https://img.icons8.com/fluency/144/shield.png", width=100)
        st.subheader("مركز المصادقة السيادية")
        
        name = st.text_input("اسم المستخدم (الاسم الرسمي):", placeholder="مثلاً: عاليا صالح")
        email = st.text_input("البريد الإلكتروني:", placeholder="example@siyaj.sa")
        gender = st.radio("الجنس:", ["بطل (ذكر)", "بطلة (أنثى)"], horizontal=True)
        
        code = st.text_input("رمز التشفير السيادي (كلمة المرور):", type="password")
        
        if st.button("فتح الأنظمة المركزية 🔐"):
            if name and email and code == "SIYAJ2026":
                st.session_state.user_profile = {
                    "name": name,
                    "email": email,
                    "gender": gender,
                    "level": "مطور سيادي",
                    "id": f"SYJ-{random.randint(1000, 9999)}"
                }
                st.session_state.logged_in = True
                add_log("تم تسجيل الدخول بنجاح.")
                st.balloons()
                st.rerun()
            else:
                st.error("🤖 سند: الرمز غلط أو البيانات ناقصة.. ركز يا بطل!")
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# --- 📱 القائمة الجانبية (مركز التحكم) ---
with st.sidebar:
    st.markdown(f"<h2 style='text-align:center; color:#1E3A8A;'>سياج v{SYSTEM_VERSION}</h2>", unsafe_allow_html=True)
    st.image("https://img.icons8.com/fluency/96/user-shield.png", width=80)
    st.write(f"**المستخدم:** {st.session_state.user_profile['name']}")
    st.write(f"**الرتبة:** {st.session_state.user_profile['level']}")
    
    st.divider()
    menu_options = [
        "🏠 العمليات المركزية",
        "💡 ركن الابتكار",
        "🎓 الأكاديمية الرقمية",
        "🎫 جواز سياج",
        "📡 مشوش التنصت",
        "🔑 مختبر التشفير",
        "🚨 بلاغ الطوارئ",
        "📚 قاموس سياج",
        "⚙️ الإعدادات",
        "❓ الدليل التشغيلي"
    ]
    choice = st.sidebar.radio("انتقل إلى القواطع:", menu_options)
    
    st.divider()
    if st.button("تسجيل الخروج 🚪"):
        st.session_state.logged_in = False
        st.rerun()

# --- 🏠 1. العمليات المركزية ---
if choice == "🏠 العمليات المركزية":
    st.title("🛡️ مركز رصد التهديدات الوطني")
    
    # صف الإحصائيات
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("حالة الدرع", "نشط 100%", "آمن")
    c2.metric("محاولات الاختراق", "3,450", "+15")
    c3.metric("البيانات المشفرة", "1.2 TB", "مؤمن")
    c4.metric("سرعة الاستجابة", "0.02ms", "-0.01")
    
    # خريطة الرصد التفاعلية
    st.subheader("📡 الرصد الجغرافي الحي")
    map_data = pd.DataFrame(
        np.random.randn(15, 2) / [20, 20] + [24.71, 46.67],
        columns=['lat', 'lon']
    )
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(latitude=24.71, longitude=46.67, zoom=5, pitch=45),
        layers=[
            pdk.Layer('ScatterplotLayer', data=map_data, get_position='[lon, lat]', get_color='[30, 58, 138, 160]', get_radius=15000),
            pdk.Layer('ArcLayer', data=map_data, get_source_position='[lon, lat]', get_target_position='[46.67, 24.71]', get_source_color='[200, 30, 0]', get_target_color='[0, 128, 0]')
        ]
    ))
    
    # سجل العمليات (Logs)
    with st.expander("📝 سجل العمليات الأخير (System Logs)"):
        for log in reversed(st.session_state.logs[-10:]):
            st.text(log)

# --- 💡 2. ركن الابتكار (النسخة الكاملة والمفصلة يا علو) ---
elif choice == "💡 ركن الابتكار":
    st.title("💡 فضاء الابتكار والسيادة")
    st.write("مرحباً بك في قلب 'سياج' النابض، حيث تتحول الأفكار إلى دروع رقمية.")

    # تعريف التبويبات الأربعة بشكل منفصل تماماً
    tab_story, tab_vision, tab_idea, tab_sim = st.tabs([
        "📖 ملحمة سياج", 
        "🎯 الرؤية الاستراتيجية", 
        "💡 شاركنا فكرتك", 
        "🛡️ مختبر محاكاة الهجمات"
    ])

    # --- القسم الأول: قصة سياج ---
    with tab_story:
        st.markdown("""
            <div style='text-align: right;'>
                <h2>📖 قصة سياج: من الفكرة إلى الواقع</h2>
                <p>بدأت حكاية <b>سياج</b> في قلب طالبات سعوديات تأكدوا أن حماية الوطن لا تقتصر على الحدود الجغرافية، بل تمتد لتشمل الحدود الرقمية. سياج هو ثمرة شغف بالبرمجة وولاء مطلق لهذه الأرض العظيمة.</p>
                <p><b>لماذا سياج؟</b> لأننا نؤمن أن الأمن السيبراني هو "السياج" الذي يحمي منجزاتنا، ويوفر بيئة آمنة للمبتكرين والمبدعين. سياج هو عهدنا بأن تبقى بياناتنا سيادية، وعقولنا محمية.</p>
            </div>
        """, unsafe_allow_html=True)
            
    # --- القسم الثاني: الرؤية الاستراتيجية ---
    with tab_vision:
        st.markdown("""
            <div class='feature-card' style='padding: 20px; border-radius: 15px; border-left: 5px solid #1E3A8A; background-color: #f8f9fa;'>
                <h3 style='color: #1E3A8A;'>🎯 الرؤية الاستراتيجية لـ سياج</h3>
                <p>سياج ليس مجرد مشروع مدرسي، بل هو رؤية تقنية ترتكز على ثلاث ركائز أساسية:</p>
                <ol style='line-height: 1.8;'>
                    <li><b>الوعي الاستباقي:</b> تحويل المستخدم من ضحية محتملة إلى حارس رقمي يدرك المخاطر قبل وقوعها.</li>
                    <li><b>الاستقلال البرمجي:</b> بناء أدواتنا بأيدينا باستخدام لغة (بايثون) لضمان السيادة الكاملة وعدم وجود أبواب خلفية.</li>
                    <li><b>سهولة الوصول:</b> جعل الأمن السيبراني لغة مفهومة وبسيطة للجميع، وليس فقط للمتخصصين.</li>
                </ol>
            </div>
        """, unsafe_allow_html=True)

    # --- القسم الثالث: شاركنا فكرتك (هنا الربط مع تليجرام) ---
    with tab_idea:
        st.subheader("💡 ركن 'ضع فكرتك'")
        st.write("يا مبدع/ة، رأيك يهمنا! وش الإضافات اللي ودك نشوفها في 'سياج' عشان نحسن أداءه ونطوره؟")
        
        # الفورم داخل التبويب عشان ما يظهر في الأقسام الثانية
        with st.form("idea_form_final", clear_on_submit=True):
            name = st.text_input("اسم المبتكر/ة:")
            idea = st.text_area("اكتب فكرتك البرمجية أو التطويرية هنا:")
            
            st.info("ملاحظة: بمجرد الضغط على إرسال، ستصل فكرتك مباشرة إلى لوحة تحكم 'علو' عبر تليجرام.")
            
            submit = st.form_submit_button("إرسال الفكرة إلى سياج 🚀")
            
            if submit:
                if idea:
                    # نرسل الفكرة فوراً لتليجرام عاليا باستخدام بياناتك الجاهزة
                    try:
                        msg = f"💡 فكرة جديدة لـ سياج v4!\n\n👤 من: {name}\n📝 الفكرة: {idea}\n\nتنبيه: هذه الرسالة مرسلة من موقع سياج الرسمي."
                        send_to_telegram(msg)
                        st.success(f"كفو يا {name}! فكرتك وصلت لـ 'علو' وبيتم دراستها بعناية. ✨")
                        st.balloons() # حركة حلوة للاحتفال بإرسال الفكرة
                    except Exception as e:
                        st.error("حدث خطأ أثناء الإرسال، تأكدي من اتصال الإنترنت.")
                else:
                    st.warning("فضلاً يا بطل/ة، اكتب الفكرة أولاً قبل الإرسال.")

    # --- القسم الرابع: محاكي الهجمات التفاعلي ---
    with tab_sim:
        st.subheader("🛡️ مختبر سياج لمحاكاة الهجمات")
        st.info("هذا القسم مخصص لاستعراض القوة الدفاعية. اضغط على الزر لترى كيف يتعامل 'سياج' مع الاختراقات.")
        
        if st.button("🚀 تشغيل محاكي الهجمات السيبرانية"):
            with st.status("🔍 جاري مراقبة حركة مرور الشبكة...", expanded=True) as status:
                st.write("📡 فحص المنافذ المفتوحة...")
                time.sleep(1.5)
                st.code("SCANNING... [80, 443, 8080, 21, 22]\nRESULT: ALL PORTS SECURED BY SIYAJ FIREWALL", language="bash")
                
                st.write("⚠️ إنذار! اكتشاف محاولة اختراق (SQL Injection)!")
                time.sleep(2)
                st.markdown("<span style='color:red'>[!] Warning: Unauthorized access attempt detected.</span>", unsafe_allow_html=True)
                
                st.write("🛠️ تفعيل بروتوكول التصدي الذكي...")
                time.sleep(2)
                st.code("ACTION: Blocking IP 192.168.x.x\nENCRYPTION: AES-256 ACTIVATED\nSTATUS: ATTACK NEUTRALIZED", language="bash")
                
                status.update(label="✅ تم سحق محاولة الاختراق بنجاح! سياج في أمان دائم.", state="complete", expanded=False)
            st.success("هذا ما يفعله سياج.. نحن نحمي المستقبل الرقمي!")

    st.markdown("---")
    st.caption("سياج v4 - صنع بكل حب وفخر بأيدي سعودية 🇸🇦")
    
# --- 🎓 3. الأكاديمية الرقمية (النسخة النهائية المعتمدة) ---
elif choice == "🎓 الأكاديمية الرقمية":
    st.title("🎓 أكاديمية سياج للتميز الرقمي")
    
    # المنطقة البيضاء (كلام سند)
    st.markdown("""
    <div class='sanad-banner'>
        <p class='sanad-text'>🤖 سند: كفو يا بطلة.. هنا مَصنع الخبراء، ادرسي بتركيز والشهادة تزهى بك!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='feature-card'>", unsafe_allow_html=True)
        st.markdown("### 📚 المسار الأساسي")
        u1 = st.checkbox("مقدمة في لغة بايثون الأمنية", key="class1")
        u2 = st.checkbox("أساسيات التشفير (Cryptography)", key="class2")
        
        # زر شرح الدرس للمسار الأساسي
        if st.button("📖 شرح دروس المسار الأساسي"):
            st.info("""
                تُعد لغة بايثون الخيار الاستراتيجي لتطوير "منظومة سياج"، وذلك لعدة أسباب تقنية:
                1. الكفاءة في الأمن السيبراني: بايثون هي اللغة الرائدة عالمياً في تطوير أدوات الحماية.
                2. سهولة التطوير والقراءة: تسمح للمبرمج بالتركيز على المنطق البرمجي.
                3. تكامل الأنظمة: مكنتنا من ربط الواجهة بخدمات خارجية بسلاسة.

                أساسيات علوم التشفير (Cryptography):
                - ماهية التشفير: تحويل "النص الواضح" إلى "نص مشفر" غير مفهوم.
                - المفتاح (Key): هو العنصر الحاسم؛ وبدونه يستحيل فك التشفير.
                - الأنواع: التشفير المتماثل (مثل AES) والتشفير غير المتماثل.
            """)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='feature-card'>", unsafe_allow_html=True)
        st.markdown("### 🛠️ المسار العملي")
        u3 = st.checkbox("بناء جدران الحماية (Firewalls)", key="class3")
        u4 = st.checkbox("تحليل البرمجيات الخبيثة", key="class4")
        
        # زر شرح الدرس للمسار العملي
        if st.button("📖 شرح دروس المسار العملي"):
            st.success("""
                1. بناء جدار الحماية (Firewall Construction):
                الجدار هو نظام فحص ذكي يعمل كمرشح (Filter) لحركة المرور في الشبكة بناءً على قواعد أمنية.
                التطبيق في سياج: مراقبة العناوين (IPs) المشبوهة وإسقاط الطلبات المحظورة فوراً.

                2. تحليل البرمجيات الخبيثة (Malware Analysis):
                دراسة سلوك الملفات المشبوهة لفهم ضررها.
                - التحليل الساكن: فحص الكود بدون تشغيله.
                - التحليل الديناميكي: تشغيل الملف في بيئة معزولة (Sandbox).
            """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.divider()
    
    # قسم استخراج الشهادة الذكي
    if st.button("🎓 استخراج الشهادة الرسمية"):
        # نتحقق إن كل المربعات (Checkboxes) تم اختيارها
        if u1 and u2 and u3 and u4:
            with st.spinner("🤖 سند: جاري طباعة اسمك الفخم على الشهادة..."):
                name_to_print = st.session_state.user_profile['name']
                final_cert = generate_cert(name_to_print)
                
                if final_cert:
                    st.balloons()
                    st.image(final_cert, caption=f"وسام سياج للتميز الرقمي لـ {name_to_print}")
                    
                    # زر تحميل الشهادة المطبوع عليها الاسم
                    st.download_button(
                        label="تحميل الوسام الخاص بك 📥",
                        data=final_cert,
                        file_name=f"Siyaj_Award_{name_to_print}.png",
                        mime="image/png"
                    )
                else:
                    st.error("🤖 سند: فيه مشكلة! تأكدي إن صورة 'siyaj_award.png' موجودة بنفس المجلد.")
        else:
            st.warning("🤖 سند: هاه؟ باقي دروس ما خلصتيها! كملي تحديد المربعات فوق عشان تستحقين الشهادة.")

# --- 🎫 4. جواز سياج (التصميم الجديد) ---
elif choice == "🎫 جواز سياج":
    st.title("🎫 جواز العبور الرقمي السيادي")
    
    st.markdown(f"""
    <div class='passport-box'>
        <div style='text-align: center; border-bottom: 2px solid rgba(255,255,255,0.2); padding-bottom: 20px; margin-bottom: 30px;'>
            <h1 style='color: white; margin:0;'>SAUDI CYBER PASSPORT</h1>
            <p style='color: #D4AF37; font-size: 14px;'>KINGDOM OF SAUDI ARABIA | سياج الرقمية</p>
        </div>
        <div style='display: flex; justify-content: space-between; align-items: center;'>
            <div style='flex: 2;'>
                <p style='font-size: 20px;'><b>الاسم:</b> {st.session_state.user_profile['name']}</p>
                <p style='font-size: 18px;'><b>البريد:</b> {st.session_state.user_profile['email']}</p>
                <p style='font-size: 18px;'><b>الرتبة:</b> {st.session_state.user_profile['level']}</p>
                <p style='font-size: 18px;'><b>المعرف:</b> {st.session_state.user_profile['id']}</p>
                <p style='font-size: 18px;'><b>تاريخ الإصدار:</b> {datetime.now().strftime('%Y-%m-%d')}</p>
            </div>
            <div style='flex: 1; text-align: center;'>
                <div style='border: 4px solid #D4AF37; border-radius: 15px; padding: 10px; background: rgba(255,255,255,0.1);'>
                    <img src='https://img.icons8.com/fluency/144/user-shield.png' width='120'>
                </div>
                <p style='margin-top:10px; color: #D4AF37;'>بصمة معتمدة</p>
            </div>
        </div>
        <div class='sanad-bubble' style='background: rgba(255,255,255,0.1); color: white; border: 1px solid #D4AF37;'>
            🤖 سند: هذا جوازك يا بطلة.. خليه معك دايم، هو مفتاحك لكل الأنظمة المشفرة.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.markdown("### 📑 سجل حركة الجواز")
    st.write("تم رصد دخول نظام: مركز الرصد - الرياض")
    st.write("تم رصد دخول نظام: مختبر التشفير - مكة المكرمة")

# --- 📡 5. مشوش التنصت (مع شرح سند) ---
elif choice == "📡 مشوش التنصت":
    st.title("📡 نظام العزل والضجيج الرقمي")
    
    st.markdown("""
    <div class='feature-card'>
        <h3>🛡️ كيف يحميك مشوش سياج؟</h3>
        <p><b>شرح سند:</b> اسمعي يا بطلة المشوش هذا ليس مجرد لعبة. هو يستخدم تقنية (Quantum Noise Injection). لما تفعلينه، سياج يرسل بيانات وهمية مشفرة في نفس قناة الاتصال، فإذا فيه أحد يتنصت، ما راح يلقى إلا "هذرة" رقمية ما لها معنى. وبكذا، صوتك وبياناتك تكون في أمان خلف جدار من الضجيج المنظم!</p>
    </div>
    """, unsafe_allow_html=True)
    
    freq = st.slider("تردد التشويش (GHz):", 2.4, 5.8, 3.5)
    if st.button("تفعيل درع الخصوصية 🤫"):
        with st.status("جاري تشغيل المشوش...") as s:
            time.sleep(2)
            st.success("تم تفعيل النطاق الصامت بنجاح.")
            add_log(f"تفعيل المشوش على تردد {freq}")

# --- 🔑 6. مختبر التشفير ---
elif choice == "🔑 مختبر التشفير":
    st.title("🔑 مختبر التشفير السيادي")
    st.markdown("<div class='sanad-bubble'>🤖 سند: التشفير علم وفن.. حطي مفتاحك السري ولا تعلمين به أحد!</div>", unsafe_allow_html=True)
    
    mode = st.radio("العملية:", ["🔒 قفل البيانات (تشفير)", "🔓 فتح البيانات (فك تشفير)"])
    
    raw_text = st.text_area("أدخل النص المراد معالجته:")
    secret_key = st.text_input("مفتاح التشفير الخاص:", type="password", help="هذا هو المفتاح اللي يفتح القفل")
    
    if st.button("تنفيذ العملية"):
        if raw_text and secret_key:
            if mode == "🔒 قفل البيانات (تشفير)":
                # منطق تشفير مبني على المفتاح
                combined = raw_text + "||" + secret_key
                res = base64.b64encode(combined.encode()).decode()
                st.code(f"SYJ_DATA_{res}", language="text")
                st.success("تم القفل بنجاح!")
            else:
                try:
                    raw_data = base64.b64decode(raw_text.replace("SYJ_DATA_", "")).decode()
                    content, k = raw_data.split("||")
                    if k == secret_key:
                        st.success(f"النص الأصلي هو: {content}")
                    else:
                        st.error("المفتاح غلط! التشفير مهوب أي كلام.")
                except:
                    st.error("البيانات أو المفتاح غير صحيح.")

# --- 🚨 7. بلاغ الطوارئ ---
elif choice == "🚨 بلاغ الطوارئ":
    st.title("🚨 مركز البلاغات السريع")
    st.markdown(f"""
    <div class='sanad-bubble' style='background:#FEE2E2; color:#991B1B; border-color:#F87171;'>
        <b>🤖 رسالة من عضيدك سند:</b><br>
        يا هلا بـ {st.session_state.user_profile['name']}.. لا يضيق صدرك ولا تشيلين هم أبد. وحنا موجودين، ما فيه أحد يقدر يمسك بضرر. 
        اكتبي لي وش اللي صار معك، وأنا أزهلها.. بلاغك بيوصل مشفر ومحمي لأعلى سلطة في المنظومة. أنتِ في أمان دارك وعيوننا ساهرة.
    </div>
    """, unsafe_allow_html=True)
    
    urgency = st.select_slider("مدى الاستعجال:", ["منخفض", "متوسط", "عالي", "حرج للغاية"])
    msg = st.text_area("اشرحي الموقف هنا:")
    
    if st.button("إرسال البلاغ فوراً ⚡"):
        if msg:
            add_log(f"بلاغ طوارئ حرج: {urgency}")
            st.success("تم الإرسال وتأمين الموقع. سند معك ولن يتركك!")
        else:
            st.warning("🤖 سند: لا تخلين الخانة فاضية، قولي لي وش اللي صار!")

# --- 📚 8. قاموس سياج (إضافة للثقل) ---
elif choice == "📚 قاموس سياج":
    st.title("📚 معجم المصطلحات السيبرانية")
    st.write("تعلمي لغة الخبراء:")
    
    terms = {
        "السيادة الرقمية": "قدرة الدولة على التحكم في بياناتها وبنيتها التحتية التقنية دون تبعية للخارج.",
        "التشفير (Encryption)": "تحويل البيانات إلى رموز غير مفهومة لمنع غير المصرح لهم من قراءتها.",
        "الهندسة الاجتماعية": "خداع الأشخاص للحصول على معلوماتهم السرية (مثل كلمة السر).",
        "جدار الحماية (Firewall)": "نظام أمني يراقب ويتحكم في حركة المرور الواردة والصادرة من الشبكة."
    }
    
    for t, d in terms.items():
        with st.expander(f"🔹 {t}"):
            st.write(d)

# --- ❓ 9. الدليل التشغيلي (شرح المنظومة بلمسة علو) ---
elif choice == "❓ الدليل التشغيلي":
    st.title("❓ كيف تشغلين منظومة سياج؟")
    st.write("دليل سياج هو عبارة عن كتاب لشرح كل قسم وفوائدة")

    # 1. قسم العمليات
    with st.expander("📖 شرح قسم 🏠 العمليات المركزية:"):
        st.write("""
            هذا القسم يمثل مركز الإدارة والتحكم (Dashboard). تقنياً، هو الشاشة التي تجمع كافة البيانات من الأقسام الأخرى لتعرضها بشكل مركزي. 
            وظيفته هي المراقبة اللحظية، حيث يتم رصد حالة النظام، وتدفق البيانات، والتأكد من أن جميع الدروع الرقمية تعمل بكفاءة. 
            هو باختصار "نقطة المرجعية" لأي قرار أمني يتم اتخاذه داخل المنصة.
        """)

    # 2. قسم ركن الابتكار
    with st.expander("📖 شرح قسم 💡 ركن الابتكار:"):
        st.write("""
            هو بمثابة مختبر التطوير (R&D Lab)، ويحتوي على ثلاث ركائز تقنية:
            - **التوثيق التاريخي:** قصة "سياج" التي تشرح كيف بدأ المشروع.
            - **التكامل البرمجي:** ربط الموقع بالخدمات الخارجية.
            - **بيئة المحاكاة:** تجربة الهجمات الافتراضية.
        """)

    # 3. قسم الأكاديمية الرقمية
    with st.expander("📖 شرح قسم 🎓 الأكاديمية الرقمية:"):
        st.write("""
            هذا القسم متخصص في التوعية الأمنية (Security Awareness). من الناحية التقنية، الأمن السيبراني لا يعتمد فقط على البرمجيات، بل على "العنصر البشري". 
            وظيفته هي تدريب المستخدمين على أسس الدفاع الرقمي، مثل كيفية كشف الروابط الاحتيالية وحماية البيانات الشخصية، ليكون المستخدم نفسه "جدار حماية" بشري.
        """)

    # 4. قسم جواز سياج
    with st.expander("📖 شرح قسم 🎫 جواز سياج:"):
        st.write("""
            هو نظام إدارة الهوية والوصول (IAM - Identity and Access Management). تقنياً، يعمل كبوابة للتحقق من هوية المستخدم وصلاحياته. 
            يضمن هذا القسم أن كل شخص يدخل إلى النظام لديه "تصريح" محدد، مما يمنع الدخول غير المصرح به (Unauthorized Access) للأجزاء الحساسة من المنصة.
        """)

    # 5. قسم مشوش التنصت
    with st.expander("📖 شرح قسم 📡 مشوش التنصت:"):
        st.write("""
            يرمز هذا القسم إلى تقنيات تأمين قنوات الاتصال. وظيفته منع عمليات "اعتراض البيانات" (Sniffing) التي قد يقوم بها المخترقون للتنصت على ما يتم إرساله. 
            تقنياً، يعتمد على عزل البيانات ومنع أي طرف ثالث من استراق السمع أو سحب المعلومات أثناء انتقالها بين المرسل والمستقبل.
        """)

    # 6. قسم مختبر التشفير
    with st.expander("📖 شرح قسم 🔑 مختبر التشفير:"):
        st.write("""
            هذا هو قلب علم التعمية (Cryptography) في المشروع. وظيفته تحويل البيانات من نص مفهوم إلى رموز معقدة باستخدام خوارزميات برمجية (مثل AES). 
            الهدف التقني منه هو حماية "سرية البيانات"؛ بحيث لو استطاع أحد الوصول إلى البيانات، فلن يتمكن من قراءتها أو فهمها بدون امتلاك "مفتاح فك التشفير" الخاص بسياج.
        """)

    # 7. قسم بلاغ الطوارئ
    with st.expander("📖 شرح قسم 🚨 بلاغ الطوارئ:"):
        st.write("""
            يمثل نظام الاستجابة الفورية للحوادث (Incident Response). هو قناة اتصال ذات أولوية قصوى، وظيفتها تقليص "زمن الاكتشاف" و"زمن الاستجابة". 
            تقنياً، يوفر واجهة سريعة لإرسال تنبيهات فورية عند وقوع أي نشاط مشبوه، مما يسمح للنظام أو المشرفين بالتدخل السريع لإيقاف الهجوم قبل تفاقمه.
        """)
# --- ⚙️ 10. الإعدادات ---
elif choice == "⚙️ الإعدادات":
    st.title("⚙️ إعدادات المنظومة")
    st.markdown("<div class='feature-card'>", unsafe_allow_html=True)
    st.write("تعديل البروفايل السيادي:")
    new_name = st.text_input("تعديل الاسم:", value=st.session_state.user_profile['name'])
    new_email = st.text_input("تعديل الإيميل:", value=st.session_state.user_profile['email'])
    if st.button("حفظ التغييرات"):
        st.session_state.user_profile['name'] = new_name
        st.session_state.user_profile['email'] = new_email
        st.success("تم التحديث!")
    st.markdown("</div>", unsafe_allow_html=True)

# --- Footer (توقيع علو) ---
st.divider()
st.markdown(f"<p style='text-align: center; color: gray;'>تم التطوير بواسطة ايادي سعودية 🇸🇦 | جميع الحقوق محفوظة لمنظومة سياج {datetime.now().year}</p>", unsafe_allow_html=True)
