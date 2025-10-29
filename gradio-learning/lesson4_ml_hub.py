"""
lesson4_ml_hub.py
多模型图像智能识别 Demo
功能：图像分类 + 目标检测 + 语义分割
"""

import gradio as gr
import torch
from ultralytics import YOLO
from torchvision import transforms
from PIL import Image

# ========== 模型加载 ==========
model_seg = YOLO('./yolov8s-seg.pt')      # 语义分割模型
model_detect = YOLO('./yolov8s-oiv7.pt')   # 目标检测模型
model_cls = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True).eval()  # 分类模型

# ========== 分类标签 ==========
file_path = 'labels.txt'
with open(file_path, 'r') as file:
    labels = [label.strip() for label in file.readlines()]

# ========== 功能函数 ==========
def seg(image):
    """语义分割"""
    results = model_seg(image)
    for r in results:
        im_array = r.plot()  # 绘制 mask
        img = Image.fromarray(im_array[..., ::-1])
    return img

def det(image):
    """目标检测"""
    results = model_detect(image)
    for r in results:
        im_array = r.plot()  # 绘制 bbox
        img = Image.fromarray(im_array[..., ::-1])
    return img

def cls(image):
    """图像分类"""
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        prediction = torch.nn.functional.softmax(model_cls(image)[0], dim=0)
    confidences = {labels[i]: float(prediction[i]) for i in range(10)}  # 前10类
    return confidences

# ========== Gradio 界面 ==========
with gr.Blocks(title="AI 图像多任务平台") as demo:
    gr.Markdown("# AI 图像多功能识别平台\n选择一个功能，上传图片体验。")

    with gr.Tab("图像分类"):
        gr.Markdown("## 图像分类演示（ResNet18）")
        with gr.Row():
            input_img = gr.Image(sources=["upload"], label="上传图片", type='pil')
            output_label = gr.Label(num_top_classes=10)
        gr.Examples(examples=['image\ILSVRC2012_val_00007539.JPEG', 'image\ILSVRC2012_val_00009247.JPEG'], inputs=[input_img])
        button = gr.Button("开始分类", variant="primary")
        button.click(cls, inputs=input_img, outputs=output_label)

    with gr.Tab("目标检测"):
        gr.Markdown("## 目标检测演示（YOLOv8）")
        with gr.Row():
            input_img = gr.Image(sources=["upload"], label="上传图片", type='pil')
            output_img = gr.Image(type='pil')
        gr.Examples(examples=['image\ILSVRC2012_val_00007539.JPEG', 'image\ILSVRC2012_val_00009247.JPEG'], inputs=[input_img])
        button = gr.Button("检测", variant="primary")
        button.click(det, inputs=input_img, outputs=output_img)

    with gr.Tab("语义分割"):
        gr.Markdown("## 语义分割演示（YOLOv8-Seg）")
        with gr.Row():
            input_img = gr.Image(sources=["upload"], label="上传图片", type='pil')
            output_img = gr.Image(type='pil')
        gr.Examples(examples=['image\ILSVRC2012_val_00007539.JPEG', 'image\ILSVRC2012_val_00009247.JPEG'], inputs=[input_img])
        button = gr.Button("分割", variant="primary")
        button.click(seg, inputs=input_img, outputs=output_img)

demo.launch()
