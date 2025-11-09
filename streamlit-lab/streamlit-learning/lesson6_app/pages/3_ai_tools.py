import streamlit as st
from PIL import Image

st.title("AI 工具页面")

if "username" in st.session_state:
    st.info(f"你好，{st.session_state['name']}！可以在这里整合你的 AI 模型。")
    uploaded = st.file_uploader("上传图片以体验 AI 识别", type=["jpg", "png"])
    if uploaded:
        img = Image.open(uploaded)
        st.image(img, caption="上传的图片")
        st.success("这里可以嵌入 Lesson 5 的 AI 模型推理。")
else:
    st.warning("请先登录才能访问此功能。")
