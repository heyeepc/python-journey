import pandas as pd
import numpy as np # 导入 numpy 用于处理 NaN

def analyze_excel_for_zeros_and_nans(file_path):
    """
    读取 Excel 文件，统计每列的缺失值 (NaN) 和 0 值数量。

    Args:
        file_path (str): Excel 文件的路径。

    Returns:
        pd.DataFrame: 包含 '缺失值 (NaN) 计数' 和 '0 值计数' 的统计 DataFrame。
    """
    try:
        # 1. 读取 Excel 文件
        # 默认读取第一个工作表
        df = pd.read_excel(file_path)

        # 2. 统计缺失值 (NaN)
        # isnull().sum() 对每一列进行统计
        nan_counts = df.isnull().sum()

        # 3. 统计 0 值
        # (df == 0).sum() 会生成一个布尔型 DataFrame，然后对每一列进行求和 (True=1, False=0)
        # 注意：对于非数值列，这个操作可能会导致警告或不准确的结果，但在精简代码中我们忽略这一点。
        zero_counts = (df == 0).sum()

        # 4. 合并结果
        summary_df = pd.DataFrame({
            '缺失值 (NaN) 计数': nan_counts,
            '0 值计数': zero_counts
        })

        return summary_df

    except FileNotFoundError:
        # 精简异常处理：文件不存在
        print(f"错误：文件未找到，请检查路径是否正确：{file_path}")
        return pd.DataFrame() # 返回空 DataFrame

# --- 示例使用 ---
# 请替换成你的 Excel 文件路径
excel_file_path = '运动者1的跳远位置信息.xlsx'

# 运行分析函数
report = analyze_excel_for_zeros_and_nans(excel_file_path)

# 打印报告
if not report.empty:
    print(f"--- 文件 '{excel_file_path}' 的缺失值和 0 值分析报告 ---")
    print(report)
