"""
lesson5_streamlit_ml_hub.py
多模型图像智能识别 Demo
功能：图像分类 + 目标检测 + 语义分割
"""

import streamlit as st
from PIL import Image
import torch
from torchvision import transforms
from ultralytics import YOLO
import numpy as np

# ========== 模型加载 ==========
st.sidebar.title("AI 模型选择")
model_task = st.sidebar.radio("选择功能", ["图像分类", "目标检测", "语义分割"])

st.write(f"当前功能：{model_task}")

# 预加载模型（一次性加载，避免重复加载）
@st.cache_resource
def load_models():
    model_seg = YOLO('./yolov8s-seg.pt')      # 语义分割模型
    model_detect = YOLO('./yolov8s-oiv7.pt')  # 目标检测模型
    model_cls = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True).eval()
    # 分类标签
    with open('labels.txt', 'r') as f:
        labels = [l.strip() for l in f.readlines()]
    return model_seg, model_detect, model_cls, labels

model_seg, model_detect, model_cls, labels = load_models()

# ========== 功能函数 ==========
def classify(image: Image.Image):
    transform = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor()
    ])
    img_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        prediction = torch.nn.functional.softmax(model_cls(img_tensor)[0], dim=0)
    confidences = {labels[i]: float(prediction[i]) for i in range(min(10,len(labels)))}
    return confidences

def detect(image: Image.Image):
    results = model_detect(image)
    for r in results:
        im_array = r.plot()
        img = Image.fromarray(im_array[..., ::-1])
    return img

def segment(image: Image.Image):
    results = model_seg(image)
    for r in results:
        im_array = r.plot()
        img = Image.fromarray(im_array[..., ::-1])
    return img

# ========== 文件上传 ==========
uploaded_file = st.file_uploader("上传图片", type=["png","jpg","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="上传的图片", use_column_width=True)

    if model_task == "图像分类":
        if st.button("开始分类"):
            with st.spinner("模型推理中..."):
                result = classify(image)
            st.write("分类结果（前10类）:")
            st.json(result)

    elif model_task == "目标检测":
        if st.button("检测目标"):
            with st.spinner("模型推理中..."):
                result_img = detect(image)
            st.image(result_img, caption="目标检测结果", use_column_width=True)

    elif model_task == "语义分割":
        if st.button("语义分割"):
            with st.spinner("模型推理中..."):
                result_img = segment(image)
            st.image(result_img, caption="语义分割结果", use_column_width=True)
else:
    st.info("请先上传图片以继续。")
