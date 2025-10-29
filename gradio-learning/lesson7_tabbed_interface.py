'''
lesson7_tabbed_interface.py
TabbedInterface允许在一个应用中创建多个标签页，每个标签页可以包含不同的界面和功能。
'''
import gradio as gr

def function1(input1):
    return f"处理结果: {input1}"

def function2(input2):
    return f"分析结果: {input2}"

iface1 = gr.Interface(function1, "text", "text")
iface2 = gr.Interface(function2, "text", "text")

tabbed_interface = gr.TabbedInterface([iface1, iface2], ["界面1", "界面2"])
tabbed_interface.launch()