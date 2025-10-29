'''
lesson3_text_ai.py
多功能 AI 文本助手
中英互译、情感分析、文本摘要
'''
import gradio as gr
from transformers import pipeline

# ---------------------------------------
# ① 初始化模型（加载较轻的预训练模型）
# ---------------------------------------
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-zh")
translator_zh2en = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en")
sentiment_analyzer = pipeline("sentiment-analysis")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
# 英文模型
sentiment_en = pipeline("sentiment-analysis")
# 中文模型
sentiment_zh = pipeline("sentiment-analysis", model="uer/roberta-base-finetuned-jd-binary-chinese")



# ---------------------------------------
# ② 定义功能函数
# ---------------------------------------
def translate_text(text):
    """自动判断语言方向进行翻译"""
    if not text.strip():
        return "请输入内容"
    # 简单判断是否中文
    if any("\u4e00" <= ch <= "\u9fff" for ch in text):
        # 中文 → 英文
        result = translator_zh2en(text, max_length=200)
        return result[0]["translation_text"]
    else:
        # 英文 → 中文
        result = translator(text, max_length=200)
        return result[0]["translation_text"]


# def analyze_sentiment(text):
#     """情感分析"""
#     if not text.strip():
#         return "请输入内容"
#     result = sentiment_analyzer(text)[0]
#     label = result["label"]
#     score = result["score"]
#     return f"情感: {label}，置信度: {score:.2f}"

def analyze_sentiment(text):
    """自动中英识别的情感分析"""
    if not text.strip():
        return "请输入内容"
    # 判断是否中文
    if any("\u4e00" <= ch <= "\u9fff" for ch in text):
        result = sentiment_zh(text)[0]
    else:
        result = sentiment_en(text)[0]
    label = result["label"]
    score = result["score"]
    return f"情感: {label}，置信度: {score:.2f}"

def summarize_text(text):
    """文本摘要"""
    if not text.strip():
        return "请输入内容"
    result = summarizer(text, max_length=80, min_length=20, do_sample=False)
    return result[0]["summary_text"]


# ---------------------------------------
# ③ 创建 Gradio 界面
# ---------------------------------------
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 多功能 AI 文本助手")
    gr.Markdown("支持：中英互译、情感分析、文本摘要。")

    with gr.Tab("中英互译"):
        input_text1 = gr.Textbox(label="输入文本", lines=5, placeholder="输入中文或英文...")
        output_text1 = gr.Textbox(label="翻译结果", lines=5)
        btn1 = gr.Button("开始翻译", variant="primary")
        btn1.click(fn=translate_text, inputs=input_text1, outputs=output_text1)

    with gr.Tab("情感分析"):
        input_text2 = gr.Textbox(label="输入句子", lines=3, placeholder="例如：I love learning AI!")
        output_text2 = gr.Textbox(label="分析结果")
        btn2 = gr.Button("开始分析", variant="secondary")
        btn2.click(fn=analyze_sentiment, inputs=input_text2, outputs=output_text2)

    with gr.Tab("文本摘要"):
        input_text3 = gr.Textbox(label="输入一段长文本", lines=8, placeholder="Paste an article or paragraph here...")
        output_text3 = gr.Textbox(label="摘要结果", lines=5)
        btn3 = gr.Button("生成摘要", variant="secondary")
        btn3.click(fn=summarize_text, inputs=input_text3, outputs=output_text3)

# ---------------------------------------
# ④ 启动服务
# ---------------------------------------
if __name__ == "__main__":
    demo.launch()
