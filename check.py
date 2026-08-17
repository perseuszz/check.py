import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# ตั้งค่าการเชื่อมต่อ Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)
sheet_url = "https://docs.google.com/spreadsheets/d/14PH-ybdwdsU3er5sE9u_n8opIDX6lrWYesPzeXGkG9I/edit?usp=sharing"

st.title("ระบบกรอกข้อมูลนักศึกษาและคำนวณอายุ")

# --- ส่วนที่ 1: ข้อมูลผลการเรียน ---
st.header("1. ข้อมูลผลการเรียน")
name = st.text_input("กรุณากรอกชื่อ:")
lastName = st.text_input("กรุณากรอกนามสกุล:")

if st.button("แสดงผลและบันทึกข้อ 1"):
    if name and lastName:
        result = "A"
        st.success(f"ชื่อ: {name} {lastName} คุณมีผลการเรียนเท่ากับ {result}")
        
        # บันทึกลง Sheets
        new_data = pd.DataFrame([{"Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                                  "User": f"{name} {lastName}", "Message": f"Grade: {result}"}])
        existing_data = conn.read(spreadsheet=sheet_url, usecols=[0, 1, 2])
        conn.update(spreadsheet=sheet_url, data=pd.concat([existing_data, new_data], ignore_index=True))
        st.info("บันทึกข้อมูลเรียบร้อยแล้ว!")
    else:
        st.warning("กรุณากรอกชื่อและนามสกุลให้ครบถ้วน")

st.divider()

# --- ส่วนที่ 2: คำนวณอายุ ---
st.header("2. คำนวณอายุ")
full_name = st.text_input("กรุณากรอกชื่อ-นามสกุลนักศึกษา:")
current_year = st.number_input("ปี พ.ศ. ปัจจุบัน:", min_value=2500, max_value=3000, value=2569, step=1)
birth_year = st.number_input("ปี พ.ศ. เกิด:", min_value=2400, max_value=3000, value=2545, step=1)

if st.button("คำนวณอายุและบันทึก"):
    if full_name:
        age = int(current_year) - int(birth_year)
        st.info(f"ชื่อ-นามสกุล: {full_name}")
        st.success(f"อายุ: {age} ปี")
        
        # บันทึกลง Sheets
        new_data = pd.DataFrame([{"Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                                  "User": full_name, "Message": f"Age: {age} years"}])
        existing_data = conn.read(spreadsheet=sheet_url, usecols=[0, 1, 2])
        conn.update(spreadsheet=sheet_url, data=pd.concat([existing_data, new_data], ignore_index=True))
        st.info("บันทึกข้อมูลเรียบร้อยแล้ว!")
    else:
        st.warning("กรุณากรอกชื่อ-นามสกุลนักศึกษา")
