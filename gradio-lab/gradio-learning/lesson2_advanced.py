'''
lesson2_advanced.py
进阶版 Gradio Demo，满足以下功能：
加、减、乘、除计算
点击按钮时显示 "计算中..."
左右布局：左侧放输入和按钮，右侧显示结果
'''
import gradio as gr
import time

# -------------------------------
# ① 定义运算函数
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
with gr.Blocks() as demo:
    gr.Markdown("## 进阶版计算器 Demo (加减乘除 + 动态状态 + 左右布局)")

    with gr.Row():
        # 左侧：输入 + 按钮
        with gr.Column():
            num1 = gr.Number(label="数字 A", value=1)
            num2 = gr.Number(label="数字 B", value=2)
            status = gr.Textbox(label="状态", value="空闲", interactive=False)
            
            add_btn = gr.Button("A + B")
            sub_btn = gr.Button("A - B")
            mul_btn = gr.Button("A × B")
            div_btn = gr.Button("A ÷ B")

        # 右侧：显示结果
        with gr.Column():
            add_result = gr.Number(label="A + B 结果")
            sub_result = gr.Number(label="A - B 结果")
            mul_result = gr.Number(label="A × B 结果")
            div_result = gr.Number(label="A ÷ B 结果")

    # -------------------------------
    # ③ 按钮点击事件绑定
    # -------------------------------
    # 动态显示“计算中...”
    # 所有按钮共用同一个 status 文本框，实现动态提示
    # 每个运算函数都用 time.sleep(0.5) 模拟计算延迟，便于看到 "计算中..."
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
