

------

## 一、Streamlit 基础入门（lesson1_streamlit.py）

### 目标

了解 Streamlit 基本使用方法，能够快速创建网页应用，使用输入组件和按钮交互。

### 核心知识点

| 概念     | 说明                    | 示例                                                         |
| -------- | ----------------------- | ------------------------------------------------------------ |
| 页面标题 | 设置网页标题            | `st.title("Lesson 1")`                                       |
| 文本显示 | 显示普通文本或 Markdown | `st.write("欢迎学习 Streamlit")`                             |
| 输入组件 | 用户输入控件            | `st.text_input("请输入名字")` / `st.slider("选择年龄", 1, 100, 25)` |
| 按钮交互 | 点击按钮触发操作        | `if st.button("生成问候语"):`                                |
| 成功提示 | 显示操作成功信息        | `st.success(f"你好，{name}！")`                              |

### 示例代码

```python
import streamlit as st

st.title("Lesson 1: 我的第一个 Streamlit 网页 Demo")
st.write("欢迎来到 Streamlit 学习课程！")

name = st.text_input("请输入你的名字：")
age = st.slider("请选择你的年龄：", 1, 100, 25)

if st.button("生成问候语"):
    st.success(f"你好，{name or '同学'}！你今年 {age} 岁！")
```

### 使用说明

1. 保存文件为 `lesson1_streamlit.py`
2. 运行命令：`streamlit run lesson1_streamlit.py`
3. 在浏览器中输入名字和年龄，点击按钮生成问候语

------

## 二、Streamlit 布局与交互（lesson2_layout.py）

### 目标

学习页面布局、多列布局、侧边栏使用以及按钮交互逻辑。

### 核心知识点

| 概念         | 说明                       | 示例                                                       |
| ------------ | -------------------------- | ---------------------------------------------------------- |
| 页面设置     | 设置页面标题和布局         | `st.set_page_config(page_title="Lesson 2", layout="wide")` |
| 侧边栏       | 创建独立的输入区域         | `st.sidebar.text_input("姓名")`                            |
| 多列布局     | 将页面分为多列             | `col1, col2 = st.columns(2)`                               |
| 条件逻辑交互 | 根据输入或选择显示不同内容 | `if st.button("生成评价"):`                                |
| 分割线和页脚 | 美化页面                   | `st.markdown("---")` / `st.caption("完成")`                |

### 示例代码

```python
import streamlit as st
import datetime

st.set_page_config(page_title="Lesson 2 布局与交互", layout="wide")

st.title("Lesson 2：布局与交互")

# 侧边栏
st.sidebar.header("侧边栏设置")
name = st.sidebar.text_input("请输入你的名字：")
today = st.sidebar.date_input("选择今天的日期：", datetime.date.today())
mood = st.sidebar.selectbox("此刻心情：", ["开心", "平静", "专注", "疲惫"])

# 主体布局
col1, col2 = st.columns(2)
with col1:
    st.subheader("用户信息")
    st.write(f"姓名：{name or '未填写'}")
    st.write(f"日期：{today}")
    st.write(f"心情：{mood}")
with col2:
    st.subheader("互动功能区")
    number = st.slider("选择一个数字：", 0, 100, 50)
    st.write(f"你选择的数字是：{number}")
    if st.button("生成评价"):
        if mood == "开心":
            st.success("继续保持好心情！")
        elif mood == "平静":
            st.info("平静的心最强大。")
        elif mood == "专注":
            st.warning("保持专注，注意休息。")
        else:
            st.error("喝点水，放松一下吧！")

st.markdown("---")
st.caption("Lesson 2 完成：掌握了 Streamlit 的基础布局。")
```

### 使用说明

1. 保存为 `lesson2_layout.py`
2. 运行命令：`streamlit run lesson2_layout.py`
3. 在侧边栏输入信息，观察两列布局的显示效果
4. 点击按钮测试交互逻辑

------

## 三、Streamlit 表单与输入管理（lesson3_form.py）

### 目标

掌握表单使用、`session_state` 状态管理，以及表单提交后的数据展示。

### 核心知识点

| 概念          | 说明                   | 示例                                        |
| ------------- | ---------------------- | ------------------------------------------- |
| session_state | 页面刷新后保持数据     | `st.session_state.user_name = ""`           |
| 表单创建      | 批量输入控件，统一提交 | `with st.form(key="user_form"):`            |
| 表单提交按钮  | 点击提交表单           | `submitted = st.form_submit_button("提交")` |
| 数据展示      | 显示提交的结果         | `if st.session_state.submitted:`            |

### 示例代码

```python
import streamlit as st

st.set_page_config(page_title="Lesson 3 表单与输入管理", layout="wide")
st.title("Lesson 3：表单与输入管理")

# 初始化 session_state
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "user_age" not in st.session_state:
    st.session_state.user_age = 25
if "user_color" not in st.session_state:
    st.session_state.user_color = "红色"

st.write("请在表单中填写信息，然后一次性提交。")

# 创建表单
with st.form(key="user_form"):
    name = st.text_input("姓名", value=st.session_state.user_name)
    age = st.number_input("年龄", min_value=1, max_value=120, value=st.session_state.user_age)
    color = st.selectbox("喜欢的颜色",
                         ["红色", "蓝色", "绿色"],
                         index=["红色", "蓝色", "绿色"].index(st.session_state.user_color))
    submitted = st.form_submit_button("提交")

# 表单提交处理
if submitted:
    st.session_state.submitted = True
    st.session_state.user_name = name
    st.session_state.user_age = age
    st.session_state.user_color = color

# 显示结果
if st.session_state.submitted:
    st.success("提交成功！")
    st.write(f"姓名：{st.session_state.user_name}")
    st.write(f"年龄：{st.session_state.user_age}")
    st.write(f"喜欢的颜色：{st.session_state.user_color}")
```

### 使用说明

1. 保存为 `lesson3_form.py`
2. 运行命令：`streamlit run lesson3_form.py`
3. 填写表单，点击提交按钮，观察数据展示效果

------

如果你希望，我可以按照 **这个模板**帮你整理 **Lesson 4~6**，然后生成一个 **完整的六节课 Streamlit 实战复习笔记**。

你现在想直接发第四节课代码吗？