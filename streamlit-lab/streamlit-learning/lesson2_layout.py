'''
lesson2_layout.py
布局与交互
'''
import streamlit as st
import datetime

# 设置页面标题
st.set_page_config(page_title="Lesson 2 布局与交互", layout="wide")

st.title("Lesson 2：布局与交互")
st.write("本节课演示如何使用侧边栏与多列布局。")

# --- 侧边栏部分 ---
st.sidebar.header("侧边栏设置")
name = st.sidebar.text_input("请输入你的名字：")
today = st.sidebar.date_input("选择今天的日期：", datetime.date.today())
mood = st.sidebar.selectbox("此刻心情：", ["开心", "平静", "专注", "疲惫"])

# --- 主体布局 ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("用户信息")
    st.write(f"姓名：{name or '未填写'}")
    st.write(f"日期：{today}")
    st.write(f"心情：{mood}")

with col2:
    st.subheader("互动功能区")
    number = st.slider("选择一个数字：", 0, 100, 50)
    st.write(f"你选择的数字是：{number}")

    if st.button("生成评价"):
        if mood == "开心":
            st.success("继续保持好心情！")
        elif mood == "平静":
            st.info("平静的心最强大。")
        elif mood == "专注":
            st.warning("保持专注，注意休息。")
        else:
            st.error("喝点水，放松一下吧！")

# 页脚
st.markdown("---")
st.caption("Lesson 2 完成：掌握了 Streamlit 的基础布局。")
