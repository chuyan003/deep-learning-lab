'''
lesson5_process_image.py
实现图片处理应用的动态界面
用户上传图片并选择滤镜类型后，应用会立即处理并显示处理后的图片。这个过程实现了动态交互和实时反馈。
'''
import gradio as gr

def process_image(img, filter_type):
    if filter_type == "Black and White":
        img = img.convert("L")
    return img

iface = gr.Interface(
    fn=process_image,
    inputs=[gr.Image(type="pil"), gr.Radio(["None", "Black and White"])],
    outputs="image"
)
iface.launch()