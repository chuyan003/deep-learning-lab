'''
lesson4_classify_image.py
集成图像分类模型
用了一个预训练的图像分类模型来识别上传的图片，并显示前五个最可能的类别。
'''
import gradio as gr
from transformers import pipeline

# 加载预训练模型
model = pipeline('image-classification')

# 定义处理函数
def classify_image(img):
    return {i['label']: i['score'] for i in model(img)}

# 创建Gradio界面
iface = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=5))
iface.launch()