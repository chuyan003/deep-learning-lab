'''
lesson8_plot_data.py
数据可视化探索工具
场景描述：创建一个数据可视化工具，用户可以上传数据集，选择不同的图表类型进行数据探索。
功能实现：
使用File组件上传数据文件。
利用Dropdown组件让用户选择图表类型，如柱状图、折线图等。
使用Plot组件展示生成的图表。
'''
import gradio as gr
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_data(file, chart_type):
    df = pd.read_csv(file)
    if chart_type == "柱状图":
        plt.figure(figsize=(10, 6))
        sns.barplot(data=df)
    elif chart_type == "折线图":
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df)
    plt.tight_layout()
    return plt

iface = gr.Interface(
    plot_data,
    inputs=[gr.File(), gr.Dropdown(["柱状图", "折线图"])],
    outputs="plot"
)
iface.launch() 