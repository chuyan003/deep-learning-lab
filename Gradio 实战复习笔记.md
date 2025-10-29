# Gradio 实战复习笔记

---

## 一、Gradio 基础入门（lesson1_hello.py）

### 目标

了解 Gradio 的基本结构，能快速创建交互式网页应用。

### 核心知识点

| 概念 | 说明 | 示例 |
| :-- | :-- | :-- |
| `Interface` | 将函数快速包装为网页界面 | `gr.Interface(fn=greet, inputs=..., outputs=...)` |
| 输入组件 | 用户输入的控件，如 `Textbox`、`Number` 等 | `gr.Textbox(label="Your name")` |
| 输出组件 | 展示函数返回值的控件 | `gr.Textbox(label="Greeting")` |
| 启动服务 | 启动本地或公网访问 | `demo.launch()` / `demo.launch(share=True)` |

### 示例代码

```python
import gradio as gr

def greet(name):
    return f"Hello, {name}!"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Your name"),
    outputs=gr.Textbox(label="Greeting"),
    title="Gradio 入门示例",
    description="输入你的名字，看看 Gradio 如何即时返回问候语。"
)

if __name__ == "__main__":
    demo.launch(share=True)
```

**运行示例：**

![image-20251029213530398](C:\Users\86183\AppData\Roaming\Typora\typora-user-images\image-20251029213530398.png)


---

## 二、Blocks 高级布局（lesson2_blocks.py）

### 目标

掌握 `Blocks` 的使用，实现复杂布局和组件联动。

### 核心知识点

| 概念 | 说明 | 示例 |
| :-- | :-- | :-- |
| `gr.Blocks()` | 用于构建多组件交互的容器 | `with gr.Blocks() as demo:` |
| `gr.Row()` / `gr.Column()` | 控制横向、纵向布局 | `with gr.Row():` |
| `gr.Markdown()` | 插入标题或说明文字 | `gr.Markdown("### 运算结果")` |
| 事件绑定 | 响应组件事件 | `button.click(fn=func, inputs=..., outputs=...)` |

### 示例代码

```python
import gradio as gr

def add(a, b): return a + b
def subtract(a, b): return a - b

with gr.Blocks() as demo:
    gr.Markdown("## 加减法计算器示例 (Blocks)")

    with gr.Row():
        num1 = gr.Number(label="数字 A", value=1)
        num2 = gr.Number(label="数字 B", value=2)
        add_btn = gr.Button("计算 A + B")
        sub_btn = gr.Button("计算 A - B")

    add_result = gr.Number(label="A + B 结果")
    sub_result = gr.Number(label="A - B 结果")

    add_btn.click(fn=add, inputs=[num1, num2], outputs=add_result)
    sub_btn.click(fn=subtract, inputs=[num1, num2], outputs=sub_result)

if __name__ == "__main__":
    demo.launch()
```


---

## 三、进阶交互与状态（lesson2_advanced.py）

### 目标

实现带动态状态提示的加减乘除计算器。

### 核心知识点

| 内容 | 说明 |
| :-- | :-- |
| 多输入/输出组件 | 函数可同时返回多个结果 |
| 动态状态提示 | 返回状态文本框实现状态反馈 |
| 模拟计算延迟 | 使用 `time.sleep()` 观察状态变化 |
| 左右布局 | 用 `gr.Row()` + `gr.Column()` 实现分区布局 |

### 示例代码

```python
import gradio as gr
import time

def add(a, b): return a + b, "完成"
def subtract(a, b): return a - b, "完成"
def multiply(a, b): return a * b, "完成"
def divide(a, b): return None, "除数不能为0" if b == 0 else (a / b, "完成")

with gr.Blocks() as demo:
    gr.Markdown("## 进阶版计算器 Demo")

    with gr.Row():
        with gr.Column():
            num1 = gr.Number(label="数字 A", value=1)
            num2 = gr.Number(label="数字 B", value=2)
            status = gr.Textbox(label="状态", value="空闲", interactive=False)
            add_btn = gr.Button("A + B")
            sub_btn = gr.Button("A - B")
            mul_btn = gr.Button("A × B")
            div_btn = gr.Button("A ÷ B")

        with gr.Column():
            add_result = gr.Number(label="A + B 结果")
            sub_result = gr.Number(label="A - B 结果")
            mul_result = gr.Number(label="A × B 结果")
            div_result = gr.Number(label="A ÷ B 结果")

    def wrap(fn, a, b):
        time.sleep(0.5)
        return fn(a, b)

    add_btn.click(lambda a,b: wrap(add, a,b), [num1,num2],[add_result,status])
    sub_btn.click(lambda a,b: wrap(subtract,a,b), [num1,num2],[sub_result,status])
    mul_btn.click(lambda a,b: wrap(multiply,a,b), [num1,num2],[mul_result,status])
    div_btn.click(lambda a,b: wrap(divide,a,b), [num1,num2],[div_result,status])

if __name__ == "__main__":
    demo.launch()
```

**运行示例：**

![image-20251029213610691](C:\Users\86183\AppData\Roaming\Typora\typora-user-images\image-20251029213610691.png)


---

## 四、界面美化（lesson2_advanced_beauty.py）

### 目标

掌握 CSS 自定义样式，优化界面外观。

### 核心知识点

| 内容 | 说明 |
| :-- | :-- |
| 自定义 CSS | 通过 `css=` 传入全局样式字符串 |
| 组件类名 | 用 `elem_classes` 绑定样式 |
| 常用样式 | 圆角、背景色、字体、间距等 |
| Markdown 标题 | 分区说明更清晰 |

### 示例代码

```python
css_style = """
.gr-button { border-radius: 12px; font-weight: bold; padding: 10px 20px; }
.add-btn { background-color: #4ade80; color: white; }
.sub-btn { background-color: #f87171; color: white; }
.mul-btn { background-color: #60a5fa; color: white; }
.div-btn { background-color: #facc15; color: white; }
"""

with gr.Blocks(css=css_style) as demo:
    gr.Markdown("## 美化计算器 Demo")
```


---

## 五、历史记录功能（lesson2_advanced_history.py）

### 目标

使用 `gr.State` 和 `gr.Dataframe` 保存与展示历史记录。

### 核心知识点

| 概念 | 说明 | 示例 |
| :-- | :-- | :-- |
| `gr.State()` | 存储不可见的中间变量 | `history_state = gr.State([])` |
| 状态更新 | 输入/输出中传递 `State` | `inputs=[num1, num2, gr.State("+"), history_state]` |
| `gr.Dataframe` | 显示历史数据表格 | `gr.Dataframe(headers=[...])` |
| 限制数量 | 控制长度：`history = history[-5:]` |  |

**运行示例：**

![image-20251029213704187](C:\Users\86183\AppData\Roaming\Typora\typora-user-images\image-20251029213704187.png)


---

## 六、AI 文本助手（lesson3_text_ai.py）

### 目标

结合 Hugging Face Transformers 模型，实现多功能文本处理。

### 核心知识点

| 功能 | 模型 | 说明 |
| :-- | :-- | :-- |
| 中英互译 | `Helsinki-NLP/opus-mt-en-zh` | 自动识别语言方向 |
| 情感分析（英文） | `distilbert-base-uncased-finetuned-sst-2-english` | 英文情感分析 |
| 情感分析（中文） | `uer/roberta-base-finetuned-jd-binary-chinese` | 中文情感分析 |
| 文本摘要 | `facebook/bart-large-cnn` | 长文本摘要 |

### Gradio 技巧

| 技巧 | 说明 |
| :-- | :-- |
| `gr.Tab()` | 多功能分区界面 |
| `gr.themes.Soft()` | 使用柔和主题 |
| 输入检测 | 判断空输入或语言类型 |
| 多模型独立 | 各 Tab 内按钮独立绑定函数 |

### 示例结构

```python
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 多功能 AI 文本助手")
    with gr.Tab("中英互译"):
        ...
    with gr.Tab("情感分析"):
        ...
    with gr.Tab("文本摘要"):
        ...
```

**运行示例：**

![img](file:///C:\Users\86183\AppData\Local\Temp\ksohtml7972\wps3.jpg)  

![img](file:///C:\Users\86183\AppData\Local\Temp\ksohtml7972\wps6.jpg) 

![img](file:///C:\Users\86183\AppData\Local\Temp\ksohtml7972\wps7.jpg) 

**同一个意思，中文和英文的置信度差别较大，考虑到调用的模型的训练数据侧重于英语，换个中文适用的模型：**

![img](file:///C:\Users\86183\AppData\Local\Temp\ksohtml7972\wps8.jpg) 

![img](file:///C:\Users\86183\AppData\Local\Temp\ksohtml7972\wps9.jpg) 

 

![img](file:///C:\Users\86183\AppData\Local\Temp\ksohtml7972\wps10.jpg) 


---

## Lesson 4：图像智能识别应用

### 4.1 图像分类（lesson4_classify_image.py）

**目标**
集成预训练图像分类模型，实现图片上传后的类别识别。

**核心知识点**


| 内容 | 说明 |
| :-- | :-- |
| `pipeline('image-classification')` | 直接加载 Hugging Face 图像分类模型 |
| `gr.Image` | 用于上传图片，可设置 `type="pil"` 获取 PIL 图像对象 |
| `gr.Label` | 用于输出分类结果，支持显示前 n 个类别 |
| 结果格式 | 返回 `{label: score}` 的字典即可自动显示分类概率 |

**示例代码**

```python
import gradio as gr
from transformers import pipeline

model = pipeline('image-classification')

def classify_image(img):
    return {i['label']: i['score'] for i in model(img)}

iface = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=5)
)
iface.launch()
```

**运行示例：**

![image-20251029214132148](C:\Users\86183\AppData\Roaming\Typora\typora-user-images\image-20251029214132148.png)


---

### 4.2 多模型图像智能识别平台（lesson4_ml_hub.py）

**目标**
构建一个多功能图像识别平台，实现分类、检测与分割。

**核心知识点**


| 功能 | 模型 | 实现 |
| :-- | :-- | :-- |
| 图像分类 | ResNet18（torchvision） | Softmax 输出置信度 |
| 目标检测 | YOLOv8 | 绘制 bbox 可视化 |
| 语义分割 | YOLOv8-Seg | 绘制 mask 区域 |

**主要技术点**

* 多任务分区：`gr.Tab()` 用于创建多个功能页
* 复用上传组件：各 Tab 独立绑定不同函数
* 使用 `torch.hub.load()` 加载模型
* 结果绘制：YOLO `r.plot()` 返回绘制后图像数组

**界面要点**


| Gradio 元素 | 说明 |
| :-- | :-- |
| `gr.Image` | 图片上传组件 |
| `gr.Label` | 分类概率显示 |
| `gr.Examples` | 提供示例图片 |
| `gr.Button` | 触发推理执行 |
| `gr.Blocks` | 管理整体布局 |

**运行示例：**

![image-20251029214349365](C:\Users\86183\AppData\Roaming\Typora\typora-user-images\image-20251029214349365.png)

![image-20251029214326012](C:\Users\86183\AppData\Roaming\Typora\typora-user-images\image-20251029214326012.png)

![image-20251029214301257](C:\Users\86183\AppData\Roaming\Typora\typora-user-images\image-20251029214301257.png)


---

## Lesson 5：图片处理与动态界面（lesson5_process_image.py）

**目标**
实现动态图片处理应用，支持实时交互。

**核心知识点**


| 内容 | 说明 |
| :-- | :-- |
| 多输入组件 | 可同时接收图片与单选项 |
| `gr.Radio` | 单选组件，用于切换滤镜类型 |
| 实时反馈 | 每次用户操作都会触发函数执行 |
| 输出类型 | 输出图片可直接返回 PIL 对象 |

**示例代码**

```python
import gradio as gr

def process_image(img, filter_type):
    if filter_type == "Black and White":
        img = img.convert("L")
    return img

iface = gr.Interface(
    fn=process_image,
    inputs=[gr.Image(type="pil"), gr.Radio(["None", "Black and White"])],
    outputs="image"
)
iface.launch()
```


---

## Lesson 6：聊天界面（lesson6_chat_interface.py）

**目标**
了解 `ChatInterface` 的用法，实现流式聊天界面。

**核心知识点**


| 内容 | 说明 |
| :-- | :-- |
| `gr.ChatInterface` | 专门用于聊天对话的快速构建接口 |
| 函数签名 | `(message, history)` → `str` 或 `yield str` |
| `yield` | 支持逐字输出，实现流式响应 |
| `.queue()` | 启用异步队列，保证多用户处理 |

**示例代码**

```python
import gradio as gr
import time

def slow_echo(message, history):
    for i in range(len(message)):
        time.sleep(0.05)
        yield "机器人回复: " + message[: i+1]

demo = gr.ChatInterface(slow_echo).queue()

if __name__ == "__main__":
    demo.launch()
```


---

## Lesson 7：多标签界面（lesson7_tabbed_interface.py）

**目标**
使用 `TabbedInterface` 创建多功能标签页应用。

**核心知识点**


| 内容 | 说明 |
| :-- | :-- |
| `gr.TabbedInterface` | 可将多个独立 `Interface` 合并为一个多页应用 |
| 每个标签页 | 独立的输入输出逻辑 |
| 适用场景 | 多模型、多功能的集合型应用 |

**示例代码**

```python
import gradio as gr

def function1(input1):
    return f"处理结果: {input1}"

def function2(input2):
    return f"分析结果: {input2}"

iface1 = gr.Interface(function1, "text", "text")
iface2 = gr.Interface(function2, "text", "text")

tabbed_interface = gr.TabbedInterface([iface1, iface2], ["界面1", "界面2"])
tabbed_interface.launch()
```


---

## Lesson 8：数据可视化与探索

### 8.1 动态数据探索（lesson8_data_explore.py）

**目标**
实现 CSV 文件上传与选列绘图功能。

**核心知识点**


| 内容 | 说明 |
| :-- | :-- |
| 文件上传 | 使用 `gr.File()` 接收 CSV 文件 |
| 列选择 | 使用 `gr.CheckboxGroup()` 多选列 |
| 动态绘图 | 使用 Plotly 绘制交互式图表 |
| 输出组件 | `gr.Plot()` 用于输出 Plotly 图像 |

**示例代码**

```python
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
```


---

### 8.2 数据可视化工具（lesson8_plot_data.py）

**目标**
构建通用数据可视化工具，支持柱状图与折线图切换。

**核心知识点**


| 内容 | 说明 |
| :-- | :-- |
| `gr.Dropdown` | 用于选择图表类型 |
| `matplotlib` 与 `seaborn` | 绘制静态图形 |
| 输出类型 `"plot"` | 自动识别并展示绘制结果 |
| 文件输入 | `gr.File()` 读取用户上传数据集 |

**示例代码**

```python
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
```

运行示例：

![image-20251029214207513](C:\Users\86183\AppData\Roaming\Typora\typora-user-images\image-20251029214207513.png)


---
