'''
lesson2_blocks.py
使用 Blocks 创建复杂布局（行、列、标签、Markdown 等）
添加 按钮点击事件
组件间 联动更新
'''

import gradio as gr

# ① 定义加法函数
def add(a, b):
    return a + b

# ② 定义减法函数（演示动态输出）
def subtract(a, b):
    return a - b

# ③ 创建 Blocks 界面
with gr.Blocks() as demo:
    # 页面标题
    gr.Markdown("## 加减法计算器示例 (Blocks)")

    # 水平布局：输入框和按钮在一行
    with gr.Row():
        num1 = gr.Number(label="数字 A", value=1)
        num2 = gr.Number(label="数字 B", value=2)
        add_btn = gr.Button("计算 A + B")
        sub_btn = gr.Button("计算 A - B")

    # 输出框
    add_result = gr.Number(label="A + B 结果")
    sub_result = gr.Number(label="A - B 结果")

    # 绑定按钮点击事件
    add_btn.click(fn=add, inputs=[num1, num2], outputs=add_result)
    sub_btn.click(fn=subtract, inputs=[num1, num2], outputs=sub_result)

# ④ 启动本地 Web 服务
if __name__ == "__main__":
    demo.launch()
