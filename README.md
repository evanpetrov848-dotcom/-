import streamlit as st

st.set_page_size = "centered"
st.title("📟 حاسبة علاء المطورة")

# شاشة العرض (Display)
if 'result' not in st.session_state:
    st.session_state.result = "0"

st.markdown(f"""
<div style="background-color: #262730; padding: 20px; border-radius: 10px; text-align: right;">
    <h1 style="color: #00FF00; font-family: monospace;">{st.session_state.result}</h1>
</div>
""", unsafe_allow_html=True)

st.write("---")

# ترتيب الأزرار في أعمدة
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7"): st.session_state.result += "7"
    if st.button("4"): st.session_state.result += "4"
    if st.button("1"): st.session_state.result += "1"
    if st.button("C"): st.session_state.result = "0"

with col2:
    if st.button("8"): st.session_state.result += "8"
    if st.button("5"): st.session_state.result += "5"
    if st.button("2"): st.session_state.result += "2"
    if st.button("0"): st.session_state.result += "0"

with col3:
    if st.button("9"): st.session_state.result += "9"
    if st.button("6"): st.session_state.result += "6"
    if st.button("3"): st.session_state.result += "3"
    if st.button("="):
        try:
            st.session_state.result = str(eval(st.session_state.result))
        except:
            st.session_state.result = "Error"

with col4:
    if st.button("/"): st.session_state.result += "/"
    if st.button("*"): st.session_state.result += "*"
    if st.button("-"): st.session_state.result += "-"
    if st.button("+"): st.session_state.result += "+"

st.write("---")
st.info("اضغط على الأزرار لتجربة الحاسبة")
