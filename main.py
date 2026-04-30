import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="تطبيقي الأول", page_icon="📱")

st.title("📱 حاسبة علاء الذكية")
st.write("مرحباً بك في أول تطبيق قمت بصناعته بلغة بايثون!")

# تصميم الواجهة
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        n1 = st.number_input("الرقم الأول", value=0.0)
    with col2:
        n2 = st.number_input("الرقم الثاني", value=0.0)

    op = st.selectbox("اختر العملية الحسابية", ["جمع (+)", "طرح (-)", "ضرب (*)", "قسمة (/)"])

    if st.button("احسب الآن", use_container_width=True):
        if op == "جمع (+)": res = n1 + n2
        elif op == "طرح (-)": res = n1 - n2
        elif op == "ضرب (*)": res = n1 * n2
        elif op == "قسمة (/)": res = n1 / n2 if n2 != 0 else "خطأ"
        
        st.balloons() # حركة احتفالية عند النجاح
        st.success(f"النتيجة النهائية هي: {res}")

st.info("تمت البرمجة بواسطة علاء باستخدام Streamlit")
