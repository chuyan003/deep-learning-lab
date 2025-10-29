'''
lesson6_chat_interface.py
ChatInterface 是 Gradio 提供的一个简化接口，用来快速做聊天界面。
它要求你传入一个 接收 (message, history) 的函数，并返回 完整的聊天消息（通常是一个字符串或 (用户消息, 机器人回复) 对）。
'''
import gradio as gr
import time

def slow_echo(message, history):
    for i in range(len(message)):
        time.sleep(0.05)
        yield "机器人回复: " + message[: i+1]

demo = gr.ChatInterface(slow_echo).queue()

if __name__ == "__main__":
    demo.launch()