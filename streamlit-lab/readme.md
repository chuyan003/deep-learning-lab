# Streamlit 实战学习项目

本仓库是一个系统化的 **Streamlit 应用开发学习项目**，
 从基础入门到多页 AI 平台实战，涵盖了交互组件、数据可视化、AI 模型推理、表单管理与用户认证等完整功能。

------

## 一、项目组成

```
streamlit-lab/
├── README.md                          # 项目说明文件
├── Streamlit 与 Gradio 对比笔记.md         # 两个框架功能与语法对比笔记
├── streamlit 实战复习笔记.md                # 学习记录与运行截图
└── streamlit-learning/                   # 所有课程源码与资源文件
```

------

## 二、运行环境

建议使用 **Conda 虚拟环境** 来创建独立运行环境。

主要依赖：

```bash
conda create -n streamlit-env python=3.12
conda activate streamlit-env
python -m pip install streamlit pandas plotly torch torchvision ultralytics pyyaml streamlit-authenticator -i https://pypi.tuna.tsinghua.edu.cn/simple
```

------

## 三、项目结构（streamlit-learning）

```
streamlit-learning/
├── lesson1_streamlit.py              # Streamlit 基础入门（Hello Streamlit）
├── lesson2_layout.py                 # 页面布局与交互组件
├── lesson3_form.py                   # 表单输入与状态管理
├── lesson4_data_dashboard.py         # 数据展示与交互图表
├── lesson5_streamlit_ml_hub.py       # 多模型图像智能识别（YOLO + ResNet）
├── lesson6_app/                      # 多页应用与用户登录系统
│   ├── app.py                        # 主入口（登录注册逻辑）
│   ├── config.yaml                   # 用户配置文件
│   └── pages/
│       ├── 1_home.py                 # 首页模块
│       ├── 2_analysis.py             # 数据分析模块
│       └── 3_ai_tools.py             # AI 工具模块
│
├── labels.txt                        # 图像分类标签文件
├── image/                            # 示例图片目录
│   ├── ILSVRC2012_val_00007539.JPEG
│   ├── ILSVRC2012_val_00009247.JPEG
│   ├── ILSVRC2012_val_00014423.JPEG
│   └── ILSVRC2012_val_00020031.JPEG
├── yolov8s-oiv7.pt                   # YOLOv8 目标检测模型权重
├── yolov8s-seg.pt                    # YOLOv8 语义分割模型权重
└── main.py                           # 课程整合入口或主运行文件
```

------

## 四、运行方式

每个 `lesson*.py` 都是一个独立的 Streamlit 示例。

进入项目目录并运行：

```bash
cd streamlit-learning
streamlit run lesson3_form.py
```

**运行成功后，浏览器会自动打开页面。**
 若未自动打开，可手动访问：

```
http://localhost:8501
```

------

## 五、文件说明

| 文件 / 目录                          | 说明                                      |
| ------------------------------------ | ----------------------------------------- |
| `Streamlit 与 Gradio 对比笔记.md`    | 对比 Streamlit 与 Gradio 的功能与语法差异 |
| `streamlit 实战复习笔记.md`          | 详细记录每个 Lesson 的学习要点与示例截图  |
| `labels.txt`                         | 图像分类标签文件                          |
| `image/`                             | 示例图片目录                              |
| `yolov8s-oiv7.pt` / `yolov8s-seg.pt` | YOLOv8 模型权重                           |
| `config.yaml`                        | 登录注册的配置文件                        |
| `main.py`                            | 整合运行或快速测试入口                    |

------

## 七、参考资料

- [Streamlit 官方文档](https://docs.streamlit.io/)
- ChatGPT 辅助学习
- [Streamlit:Streamlit 学习笔记（一）--Streamlit 布局 - 知乎](https://zhuanlan.zhihu.com/p/707786990)