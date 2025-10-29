import pandas as pd

# 构建示例数据
data = {
    "Column1": [10, 15, 20, 25, 30, 35, 40, 45, 50],
    "Column2": [5, 7, 8, 10, 12, 13, 15, 16, 18],
    "Column3": [100, 150, 200, 250, 300, 350, 400, 450, 500]
}

# 转换为 DataFrame
df = pd.DataFrame(data)

# 保存为 CSV 文件
df.to_csv("sample_data.csv", index=False)

print("示例文件已生成: sample_data.csv")
