# Gradio 实战学习项目

本仓库是一个系统化的 **Gradio 应用开发学习项目**，
从基础入门到多任务 AI 应用实战，涵盖了文本、图像、数据可视化、聊天界面等多种应用场景。

---

## 一、项目组成

```

gradio/
├── readme.md                            # 说明文件
├── Gradio 环境安装与配置（Conda 版）.md    # 环境配置与依赖安装说明
├── Gradio 实战复习笔记.md                   # 详细的学习笔记与代码要点
└── gradio-learning/                         # 所有示例源码与资源文件

```


---

## 二、运行环境

建议使用 **Conda 虚拟环境**。

参考文档：
[Gradio 环境安装与配置（Conda 版）.md](./Gradio%20%E7%8E%AF%E5%A2%83%E5%AE%89%E8%A3%85%E4%B8%8E%E9%85%8D%E7%BD%AE%EF%BC%88Conda%20%E7%89%88%EF%BC%89.md)

主要依赖：

```bash
conda create -n gradio-env python=3.10
conda activate gradio-env
pip install gradio transformers torch torchvision ultralytics plotly seaborn matplotlib pandas
```


---

## 三、项目结构（gradio-learning）

```
gradio-learning/
├── lesson1_hello.py                  # Gradio 基础入门示例
├── lesson2_blocks.py                 # 使用 Blocks 构建多组件布局
├── lesson2_advanced.py               # 加减乘除计算器 + 状态提示
├── lesson2_advanced_beauty.py        # 使用 CSS 美化界面
├── lesson2_advanced_history.py       # 带历史记录的高级计算器
├── lesson3_text_ai.py                # 多功能文本 AI 助手（翻译/情感分析/摘要）
├── lesson4_classify_image.py         # 图像分类模型（Transformers pipeline）
├── lesson4_ml_hub.py                 # 多模型图像识别平台（YOLO + ResNet）
├── lesson5_process_image.py          # 动态图片滤镜处理应用
├── lesson6_chat_interface.py         # 聊天界面（ChatInterface）
├── lesson7_tabbed_interface.py       # 多标签页界面（TabbedInterface）
├── lesson8_data_explore.py           # CSV 数据探索（Plotly 散点图）
├── lesson8_plot_data.py              # 数据可视化（Matplotlib + Seaborn）
│
├── main.py                           # 打印项目结构或整合入口
├── sample_data.csv                   # 示例数据集
├── sample_data.py                    # 数据加载示例
├── labels.txt                        # 图像分类标签
├── yolov8s-oiv7.pt                   # YOLOv8 检测模型
├── yolov8s-seg.pt                    # YOLOv8 分割模型
│
├── .gradio/flagged/dataset1.csv      # Gradio 记录数据示例
└── image/                            # 示例图片资源
```


---

## 四、运行方式

每个 `lesson*.py` 都是一个独立的可运行示例。
进入 `gradio-learning` 目录后运行：

```bash
cd gradio-learning
python lesson3_text_ai.py
```

运行成功后，Gradio 会自动启动本地 Web 服务，
在浏览器中访问：

```
http://127.0.0.1:7860
```


---

## 五、说明

* `.gradio/flagged/` 目录用于 Gradio 自动保存交互数据；
* `image/` 存放图像分类、检测示例图片；
* `labels.txt` 存储分类标签；
* `.pt` 文件为 YOLO 模型权重；
* `sample_data.csv` 是可供数据可视化使用的样例文件。
---

## 六、参考资料

* [Gradio 官方文档](https://www.gradio.app/docs)
* ChatGPT
* 一文搞懂模型展示工具Gradio的所有功能 - APlayBoy的文章 - 知乎 https://zhuanlan.zhihu.com/p/679668818
* 【Gradio系列教程】 https://www.bilibili.com/video/BV19m411U7K8/?p=5\&share_source=copy_web\&vd_source=931127f108ee6e5fff1ebbc61c0a6ae5

