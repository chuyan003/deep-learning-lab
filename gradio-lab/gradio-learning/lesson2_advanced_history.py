'''
lesson2_advanced_history.py
每次点击运算按钮后，结果自动累加到历史记录表格
可以显示最近 5 次计算记录
'''
import gradio as gr
import time

# -------------------------------
# ① 运算函数
# -------------------------------
def calculate(a, b, op, history):
    """执行运算并更新历史记录"""
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "×":
        result = a * b
    elif op == "÷":
        if b == 0:
            return None, "除数不能为0", history
        result = a / b
    else:
        return None, "未知操作", history

    # 更新历史记录（保持最多 5 条）
    new_entry = [a, op, b, result]
    history.append(new_entry)
    history = history[-5:]

    return result, "完成", history


# -------------------------------
# ② 自定义 CSS 样式
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


# -------------------------------
# ③ 构建 Gradio Blocks
# -------------------------------
with gr.Blocks(css=css_style) as demo:
    gr.Markdown("## 高级版计算器 Demo (带历史记录)")

    # 用于存储历史记录
    history_state = gr.State([])

    with gr.Row():
        # 左侧输入区
        with gr.Column():
            num1 = gr.Number(label="数字 A", value=1)
            num2 = gr.Number(label="数字 B", value=2)
            status = gr.Textbox(label="状态", value="空闲", interactive=False)

            gr.Markdown("### 运算按钮")
            add_btn = gr.Button("A + B", elem_classes="add-btn")
            sub_btn = gr.Button("A - B", elem_classes="sub-btn")
            mul_btn = gr.Button("A × B", elem_classes="mul-btn")
            div_btn = gr.Button("A ÷ B", elem_classes="div-btn")

        # 右侧结果区
        with gr.Column():
            gr.Markdown("### 运算结果")
            result_box = gr.Number(label="结果")
            gr.Markdown("### 最近 5 次计算记录")
            history_table = gr.Dataframe(
                headers=["A", "操作", "B", "结果"],
                datatype=["number", "str", "number", "number"],
                interactive=False,
                wrap=True,
                value=[],
                row_count=(5, "dynamic"),
            )

    # -------------------------------
    # ④ 绑定按钮事件
    # -------------------------------
    def wrap_operation(a, b, op, history):
        # 让用户看到“计算中...”
        time.sleep(0.4)
        return calculate(a, b, op, history)

    add_btn.click(fn=wrap_operation, inputs=[num1, num2, gr.State("+"), history_state],
                  outputs=[result_box, status, history_table])
    sub_btn.click(fn=wrap_operation, inputs=[num1, num2, gr.State("-"), history_state],
                  outputs=[result_box, status, history_table])
    mul_btn.click(fn=wrap_operation, inputs=[num1, num2, gr.State("×"), history_state],
                  outputs=[result_box, status, history_table])
    div_btn.click(fn=wrap_operation, inputs=[num1, num2, gr.State("÷"), history_state],
                  outputs=[result_box, status, history_table])


# -------------------------------
# ⑤ 启动服务
# -------------------------------
if __name__ == "__main__":
    demo.launch()
