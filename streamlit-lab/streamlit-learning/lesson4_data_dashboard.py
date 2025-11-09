import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Lesson 4 数据展示与交互图表", layout="wide")
st.title("Lesson 4：数据展示、图表与下载功能")

st.write("请上传一个 CSV 文件，系统将自动展示数据和交互图表。")

# ----------------------
# 文件上传
# ----------------------
uploaded_file = st.file_uploader("选择 CSV 文件", type=["csv"])
if uploaded_file is not None:
    # 读取数据
    df = pd.read_csv(uploaded_file)
    st.success("文件读取成功！")

    # ----------------------
    # 数据预览
    # ----------------------
    st.subheader("数据预览")
    st.dataframe(df)

    # ----------------------
    # 数据筛选
    # ----------------------
    st.subheader("数据筛选")
    all_columns = df.columns.tolist()
    selected_columns = st.multiselect("选择要显示的列", all_columns, default=all_columns)
    filtered_df = df[selected_columns]

    # 按列范围筛选行（仅对数值列）
    numeric_columns = filtered_df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    for col in numeric_columns:
        min_val = float(filtered_df[col].min())
        max_val = float(filtered_df[col].max())
        user_range = st.slider(f"筛选 {col} 范围", min_val, max_val, (min_val, max_val))
        filtered_df = filtered_df[(filtered_df[col] >= user_range[0]) & (filtered_df[col] <= user_range[1])]

    st.dataframe(filtered_df)

    # ----------------------
    # 绘制散点图
    # ----------------------
    st.subheader("散点图绘制")
    if len(numeric_columns) >= 2:
        x_axis = st.selectbox("选择 X 轴", numeric_columns, index=0)
        y_axis = st.selectbox("选择 Y 轴", numeric_columns, index=1)
        fig_scatter = px.scatter(filtered_df, x=x_axis, y=y_axis, color=filtered_df.columns[0],
                                 title=f"{y_axis} vs {x_axis}")
        st.plotly_chart(fig_scatter, use_container_width=True)
    else:
        st.warning("数据中没有足够的数值列用于散点图绘制。")

    # ----------------------
    # 绘制柱状图
    # ----------------------
    st.subheader("柱状图绘制")
    if len(numeric_columns) >= 1:
        bar_col = st.selectbox("选择数值列绘制柱状图", numeric_columns, index=0)
        fig_bar = px.bar(filtered_df, x=filtered_df.columns[0], y=bar_col,
                         title=f"{bar_col} 柱状图")
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.warning("数据中没有数值列用于柱状图绘制。")

    # ----------------------
    # 下载功能
    # ----------------------
    st.subheader("下载筛选后的数据")
    csv_data = filtered_df.to_csv(index=False)
    st.download_button("下载 CSV", csv_data, file_name="filtered_data.csv", mime="text/csv")

else:
    st.info("请先上传 CSV 文件以继续。")
