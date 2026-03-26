import pandas as pd

# 1️⃣ 读取数数 CSV
df_data = pd.read_csv("data.csv")  # 列名: 用户UID, 充值金额

# 2️⃣ 按数数 CSV 中文列名计算每个 UID 的消费总和
df_summary = df_data.groupby("uid", as_index=False)["充值金额"].sum()

# 3️⃣ 读取飞书 UID 顺序 CSV
df_order = pd.read_csv("sheet_order.csv")  # 列名: uid

# 4️⃣ 按飞书 UID 顺序排序
df_final = pd.merge(df_order, df_summary, left_on="uid", right_on="uid", how="left")

# 总和为0的改成 '/'
df_final["充值金额"] = df_final["充值金额"].apply(lambda x: '/' if x == 0 else x)

# 6️⃣ 保存结果
df_final.to_csv("result.csv", index=False)

print("完成！result.csv 已生成，并按照飞书 UID 顺序排列")