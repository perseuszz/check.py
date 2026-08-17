import streamlit as st

st.title("ระบบกรอกข้อมูลนักศึกษาและคำนวณอายุ")

st.header("1. ข้อมูลผลการเรียน")
name = st.text_input("กรุณากรอกชื่อ:")
lastName = st.text_input("กรุณากรอกนามสกุล:")

if st.button("แสดงผลข้อ 1"):
    if name and lastName:
        st.success(f"ชื่อ: {name} {lastName} คุณมีผลการเรียนเท่ากับ A")
    else:
        st.warning("กรุณากรอกชื่อและนามสกุลให้ครบถ้วน")

st.divider()

st.header("2. คำนวณอายุ")
full_name = st.text_input("กรุณากรอกชื่อ-นามสกุลนักศึกษา:")
current_year = st.number_input("ปี พ.ศ. ปัจจุบัน:", min_value=2500, max_value=3000, value=2569, step=1)
birth_year = st.number_input("ปี พ.ศ. เกิด:", min_value=2400, max_value=3000, value=2545, step=1)

if st.button("คำนวณอายุ"):
    if full_name:
        age = int(current_year) - int(birth_year)
        st.info(f"ชื่อ-นามสกุล: {full_name}")
        st.success(f"อายุ: {age} ปี")
    else:
        st.warning("กรุณากรอกชื่อ-นามสกุลนักศึกษา")