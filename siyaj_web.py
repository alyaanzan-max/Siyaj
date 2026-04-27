import streamlit as st
import base64

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="منصة سياج الرقمية", layout="wide")

# --- 2. دالة الخلفية (siyaj.info) ---
def add_bg(image_file):
    try:
        with open(image_file, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded}");
                background-size: cover;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except:
        pass

add_bg("siyaj.info") 

# --- 3. نظام الدخول ---
if 'attempts' not in st.session_state:
    st.session_state.attempts = 3
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

st.markdown("<h1 style='text-align: center; color: white; text-shadow: 2px 2px 5px #000;'>🛡️ مـنـصـة سـيـاج الـرقمـية</h1>", unsafe_allow_html=True)

if not st.session_state.logged_in:
    if st.session_state.attempts <= 0:
        st.error("🚨 تم حظر الوصول مؤقتاً! استنفدتِ جميع المحاولات.")
    else:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.info(f"⚠️ متبقي لكِ: {st.session_state.attempts} محاولات")
            pwd_input = st.text_input("🔑 شفرة الوصول الأمن:", type="password")
            if st.button("تـأكـيـد الـدخـول"):
                if pwd_input == "28132812":
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.session_state.attempts -= 1
                    st.error("🚨 الشفرة غير صحيحة!")
                    st.rerun()

# --- 4. محتوى الموقع بعد الدخول بنجاح ---
if st.session_state.logged_in:
    # الرسالة الفخمة اللي كتبتيها
    st.success("🔒 تم تأمين الوصول بنجاح. أهلاً بكم في سياج الرقمية؛ حيث هنا تبدأ لغة العقل الرقمي، حيث يرصد رادارنا أدق التفاصيل، ويقود الفحص الشامل معارك الحماية، لتتحول المهام إلى دروعٍ ذكية تستبق التحديات وتصنع الأمان.")
    
    tab1, tab2, tab3 = st.tabs(["📊 الرادار اللحظي", "🔍 الفحص الشامل", "📋 الهيكل التنظيمي"])
    
    with tab1:
        st.markdown("### 📝 شرح توتا (ليان) للرادار")
        st.info("هنا بنحط كلام توتا عن رصد التهديدات السيبرانية...")
        
    with tab2:
        st.markdown("### 📝 شرح توتا (ليان) للفحص")
        st.info("هنا تفاصيل معارك الحماية وفحص الثغرات...")
        
    with tab3:
        st.markdown("### 📋 دروع سياج (توزيع المهام)")
        st.table([
            {"العضوة": "عاليا صالح العنزان", "الدور": "القائدة والمبرمجة", "المهمة": "تطوير الكود والواجهة الرقمية"},
            {"العضوة": "ليان عمر الشريف", "الدور": "محللة المحتوى", "المهمة": "كتابة الشروحات العلمية والبيانات"},
            {"العضوة": "المى عمر الشريف", "الدور": "المصممة", "المهمة": "تنسيق الهوية البصرية والتصميم"}
        ])