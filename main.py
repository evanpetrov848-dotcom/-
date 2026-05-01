import streamlit as st
import random

# إعدادات الصفحة
st.set_page_config(page_title="ملهم علاء", page_icon="🌟")

# قائمة الحكم والنصائح (يمكنك إضافة المزيد هنا)
quotes = [
    "النجاح هو الانتقال من فشل إلى فشل دون فقدان الحماس. 💪",
    "أفضل طريقة للتنبؤ بالمستقبل هي أن تخترعه. 🚀",
    "لا تتوقف عندما تتعب، توقف عندما تنتهي. 🔥",
    "كل إنجاز عظيم بدأ بقرار أن تحاول. ✨",
    "المبرمج الناجح هو شخص يرى المشكلة فرصة للتعلم. 💻",
    "البدايات الصعبة تصنع نهايات عظيمة. 🏅",
    "أنت اليوم مبرمج، وغداً ستبني العالم بكودك. 🌍"
]

# تصميم الواجهة
st.title("🌟 تطبيق 'ملهم علاء' الذكي")
st.write("اضغط على الزر في الأسفل لتصلك رسالة إلهام خاصة بك اليوم.")

# زر توليد الحكمة
if st.button("✨ أعطني حكمة اليوم ✨", use_container_width=True):
    # اختيار حكمة عشوائية
    quote = random.choice(quotes)
    
    # عرض الحكمة بشكل أنيق
    st.markdown(f"""
    <div style="background-color: #f0f2f6; padding: 30-px; border-left: 10px solid #ff4b4b; border-radius: 10px; margin-top: 20px;">
        <h2 style="color: #31333F; text-align: center; font-style: italic;">"{quote}"</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # إضافة حركات احتفالية (بالونات وألعاب نارية سحابية)
    st.balloons()
    st.snow() # حركة خفيفة تشبه الثلج

st.write("---")
st.caption("برمجة وتطوير: علاء 2026")
