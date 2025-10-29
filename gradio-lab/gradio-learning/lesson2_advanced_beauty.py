'''
lesson2_advanced_beauty.py
再 美化界面：
改按钮颜色、圆角
给结果框加背景色
用 Markdown 给每个运算加标题
'''
import gradio as gr
import time

# -------------------------------
# ① 运算函数
# -------------------------------
def add(a, b):
    return a + b, "完成"

def subtract(a, b):
    return a - b, "完成"

def multiply(a, b):
    return a * b, "完成"

def divide(a, b):
    if b == 0:
        return None, "除数不能为0"
    return a / b, "完成"

# -------------------------------
# ② 创建 Blocks 界面
# -------------------------------
css_style = """
.gr-button { 
    border-radius: 12px; 
    font-weight: bold; 
    padding: 10px 20px; 
}
.add-btn { background-color: #4ade80; color: white; }
.sub-btn { background-color: #f87171; color: white; }
.mul-btn { background-color: #60a5fa; color: white; }
.div-btn { background-color: #facc15; color: white; }
.gr-number { 
    background-color: #f3f4f6; 
    border-radius: 8px; 
    padding: 8px; 
}
.gr-textbox { 
    background-color: #e0f2fe; 
    border-radius: 8px; 
    padding: 8px; 
    font-weight: bold; 
}
"""

with gr.Blocks(css=css_style) as demo:
    gr.Markdown("## 进阶美化计算器 Demo")

    with gr.Row():
        # 左侧：输入 + 按钮
        with gr.Column():
            num1 = gr.Number(label="数字 A", value=1)
            num2 = gr.Number(label="数字 B", value=2)
            status = gr.Textbox(label="状态", value="空闲", interactive=False)

            gr.Markdown("### 运算按钮")
            add_btn = gr.Button("A + B", elem_classes="add-btn")
            sub_btn = gr.Button("A - B", elem_classes="sub-btn")
            mul_btn = gr.Button("A × B", elem_classes="mul-btn")
            div_btn = gr.Button("A ÷ B", elem_classes="div-btn")

        # 右侧：结果显示
        with gr.Column():
            gr.Markdown("### 运算结果")
            add_result = gr.Number(label="A + B 结果")
            sub_result = gr.Number(label="A - B 结果")
            mul_result = gr.Number(label="A × B 结果")
            div_result = gr.Number(label="A ÷ B 结果")

    # -------------------------------
    # ③ 按钮事件
    # -------------------------------
    def add_wrapper(a, b):
        status.value = "计算中..."
        time.sleep(0.5)
        result, msg = add(a, b)
        return result, msg

    def sub_wrapper(a, b):
        status.value = "计算中..."
        time.sleep(0.5)
        result, msg = subtract(a, b)
        return result, msg

    def mul_wrapper(a, b):
        status.value = "计算中..."
        time.sleep(0.5)
        result, msg = multiply(a, b)
        return result, msg

    def div_wrapper(a, b):
        status.value = "计算中..."
        time.sleep(0.5)
        result, msg = divide(a, b)
        return result, msg

    add_btn.click(fn=add_wrapper, inputs=[num1, num2], outputs=[add_result, status])
    sub_btn.click(fn=sub_wrapper, inputs=[num1, num2], outputs=[sub_result, status])
    mul_btn.click(fn=mul_wrapper, inputs=[num1, num2], outputs=[mul_result, status])
    div_btn.click(fn=div_wrapper, inputs=[num1, num2], outputs=[div_result, status])

# -------------------------------
# ④ 启动 Web Demo
# -------------------------------
if __name__ == "__main__":
    demo.launch()
