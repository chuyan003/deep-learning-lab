'''
lesson1_streamlit.py
我的第一个 Streamlit 网页 Demo
'''
import streamlit as st

st.title("Lesson 1: 我的第一个 Streamlit 网页 Demo")
st.write("欢迎来到 Streamlit 学习课程！")

# 输入组件
name = st.text_input("请输入你的名字：")
age = st.slider("请选择你的年龄：", 1, 100, 25)

# 按钮交互
if st.button("生成问候语"):
    st.success(f"你好，{name or '同学'}！你今年 {age} 岁！")
