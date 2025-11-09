import streamlit as st

st.set_page_config(page_title="Lesson 3 表单与输入管理", layout="wide")
st.title("Lesson 3：表单与输入管理")

# ----------------------
# 初始化 session_state
# ----------------------
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "user_age" not in st.session_state:
    st.session_state.user_age = 25  # 默认值必须 >= min_value
if "user_color" not in st.session_state:
    st.session_state.user_color = "红色"

st.write("请在表单中填写信息，然后一次性提交。")

# ----------------------
# 创建表单
# ----------------------
with st.form(key="user_form"):
    name = st.text_input("姓名", value=st.session_state.user_name)
    age = st.number_input("年龄", min_value=1, max_value=120, value=st.session_state.user_age)
    color = st.selectbox(
        "喜欢的颜色",
        ["红色", "蓝色", "绿色"],
        index=["红色", "蓝色", "绿色"].index(st.session_state.user_color)
    )
    submitted = st.form_submit_button("提交")  # 必须在 form 内部

# ----------------------
# 表单提交处理
# ----------------------
if submitted:
    st.session_state.submitted = True
    st.session_state.user_name = name
    st.session_state.user_age = age
    st.session_state.user_color = color

# ----------------------
# 显示结果
# ----------------------
if st.session_state.submitted:
    st.success("提交成功！")
    st.write(f"姓名：{st.session_state.user_name}")
    st.write(f"年龄：{st.session_state.user_age}")
    st.write(f"喜欢的颜色：{st.session_state.user_color}")
