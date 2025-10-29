'''
lesson8_data_explore.py
创建一个动态数据探索工具
用户可以上传CSV文件并选择要探索的数据列，应用将展示这些列的交互式散点图。
'''
import gradio as gr
import pandas as pd
import plotly.express as px

def explore_data(dataset, columns):
    df = pd.read_csv(dataset)
    fig = px.scatter(df, x=columns[0], y=columns[1])
    return fig

demo = gr.Interface(
    fn=explore_data,
    inputs=[
        gr.File(label="上传CSV文件"),
        gr.CheckboxGroup(choices=['Column1', 'Column2', 'Column3'], label="选择列")
    ],
    outputs=gr.Plot()
)
demo.launch()