'''
lesson1_hello.py
创建一个可交互网页应用
'''
import gradio as gr

# ① 定义一个最简单的函数
def greet(name):
    return f"Hello, {name}!"

# ② 创建一个 Gradio 接口
demo = gr.Interface(
    fn=greet,                         # 要包装的函数
    inputs=gr.Textbox(label="Your name"),   # 输入组件
    outputs=gr.Textbox(label="Greeting"),   # 输出组件
    title="Gradio 入门示例",
    description="输入你的名字，看看 Gradio 如何即时返回问候语。"
)

# ③ 启动本地 Web 服务
if __name__ == "__main__":
    # demo.launch()
    # 如果想公开访问，可以加上 share=True 参数（会生成一个临时公网链接）
    demo.launch(share=True)