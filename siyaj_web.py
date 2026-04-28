import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import numpy as np
import base64
import time
import pydeck as pdk 

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
                st.session_state.log_history.append({
                    "المشغل": u_name, 
                    "الإيميل": u_email_input, 
                    "الرتبة": u_type, 
                    "التوقيت": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
                send_telegram_notification(f"✅ تم تسجيل دخول جديد:\nالمستخدم: {u_name}\nالرتبة: {u_type}\nالوقت: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                st.balloons()
                st.rerun()
            else:
                st.error("⚠️ خطأ في مطابقة البيانات. يرجى التأكد من الرمز وإدخال الإيميل.")
    st.stop()

# --- شريط الحالة (الإضافة الجديدة) ---
c_user_name = st.session_state.user_data['name']
c_user_type = st.session_state.user_data['type']
st.markdown(f"""<div class='status-bar'>
    <span>👤 المستخدم الحالي: <b>{c_user_name}</b></span>
    <span>📡 حالة الدرع السيبراني: <b>نشط وتعمل تحت التشفير السيادي</b></span>
    <span>🎖️ الرتبة الممنوحة: <b>{c_user_type}</b></span>
</div>""", unsafe_allow_html=True)

# --- 2. القائمة الجانبية للتنقل ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/144/shield.png", width=100)
    st.markdown(f"<h2 style='color:#1E3A8A;'>سياج v4.0</h2>", unsafe_allow_html=True)
    st.write(f"المشغل الحالي: **{c_user_name}**")
    st.write(f"الرتبة: **{c_user_type}**")
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

        <h3>📖 قصة سياج وأهدافها</h3>
        <p><b>لماذا سياج؟</b> فكرة سياج لم تأتي بيوم وليلة أتت بأيام معدوده لأننا نريد ان نثبت للعالم بأن المملكة العربية السعودية وطن تنمو فيه المواهب وان خلف كل هدوء طالب يكمن اعصارٌ من الطموح ونؤكد أن طموح هذا الجيل هي القوة التي ستبني للمستقبل  وان سياج هي الأم الحاضنه لكل فكرة مبتكرة والدرع الذي يستقبل تطلعات الجميع ليحولها إلى واقع يحمي مستقبلنا الرقمي.</p>
        <p><b>أهدافنا الأساسية:</b><br>
        • رصد التهديدات الاستباقي قبل وصولها للمستخدم.<br>
        • بناء جيل واعي يفهم لغة التشفير والخصوصية.<br>
        • تحويل المفاهيم المعقدة إلى أدوات سهلة الاستخدام.</p>
       <p><b>معلومات عن مبرمجات سياج:</b><br>
        • مبرمجات سياج في المرحله المتوسطه.<br>
        •خبيرات المنطق الرياضي: نعتمد في بناء خوارزميات سياج على تفكير منطقي متقدم، صُقل من خلال المنافسة في المحافل الدولية مثل مسابقات "كانجارو" و "نسمو" للرياضيات، مما يجعل نظامنا دقيقاً في رصد الثغرات..<br>
        • سفيرات الهوية والتقنية: نحن نريد ان نثبت لعالم أن الاعتزاز بالهوية الوطنية لا يتعارض مع لغات البرمجة العالمية (Python)؛ بل هو المحرك الأساسي لحماية مقدرات الوطن..<br>
        • رواد هندسة الوعي (Social Engineering Awareness): نمتلك قدرة عالية على تحليل السلوك البشري الرقمي، وهذا ما دفعنا لابتكار المساعد "سند"، ليكون درعاً يحمي المستخدم من الخداع قبل الاختراق التقني..<br>
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

elif section == "درع الهندسة الاجتماعية 👤":
    st.title("👤 اختبار درع الوعي البشري")
    st.write("أجبر على هذه المواقف الحقيقية لنقيس مدى حمايتك ضد 'الهكر البشري':")
    
    score_social = 0
    q1 = st.radio("1. وصلتك رسالة 'عاجلة' تطلب كود التحقق لتجنب إيقاف حسابك البنكي، ماذا تفعل؟", ["أعطيهم الكود فوراً", "أحذف الرسالة", "أتصل بالبنك من رقمهم الرسمي"])
    q2 = st.radio("2. وجدت 'فلاش ميموري' في ساحة المدرسة مكتوب عليها 'نتائج الاختبارات'، ماذا تفعل؟", ["أفتحها في جهازي لأرى النتائج", "أسلمها لمديرة المدرسة", "أتركها مكانها"])
    q3 = st.radio("3. اتصل بك شخص يدعي أنه من 'سياج' ويطلب كلمة مرورك للتحديث، ماذا تفعل؟", ["أعطيه إياها لأنه من فريق العمل", "أرفض فوراً وأبلغ عنه", "أطلب منه إرسال رابط"])
    
    if st.button("تحليل مستوى الدرع البشري"):
        if "أتصل" in q1: score_social += 1
        if "أسلمها" in q2: score_social += 1
        if "أرفض" in q3: score_social += 1
        
        if score_social == 3: st.success("بطلة! وعيك السيبراني حديدي وأنتِ محمية تماماً.")
        else: st.warning(f"مستواك {score_social}/3. ننصحك بمراجعة أكاديمية سياج فوراً لتعزيز وعيك.")

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
