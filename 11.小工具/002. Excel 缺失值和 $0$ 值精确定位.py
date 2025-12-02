import pandas as pd
import numpy as np


def col_to_excel_letter(col_index):
    """
    将 pandas 的列索引 (0-based) 转换为 Excel 的列字母 (A, B, C...)。
    """
    # 简单的实现，只支持到 ZZZ 列，对于大部分情况足够
    letter = ''
    while col_index >= 0:
        col_index, remainder = divmod(col_index, 26)
        letter = chr(65 + remainder) + letter
        col_index -= 1
    return letter


def analyze_excel_with_cell_ranges(file_path):
    """
    读取 Excel 文件，并输出包含缺失值 (NaN) 或 0 值的具体单元格范围。

    Args:
        file_path (str): Excel 文件的路径。
    """
    try:
        # 1. 读取 Excel 文件
        # header=None 用于获取基于 0 的列索引，方便计算 Excel 列字母
        df = pd.read_excel(file_path, header=None)

        # 2. 找出所有缺失值 (NaN) 和 0 值的单元格
        # 创建一个布尔型 DataFrame，标记所有“有问题”的单元格
        # .fillna(False) 是为了确保 df == 0 在非数值列上不会出错
        is_nan = df.isnull()
        is_zero = (df.fillna(np.nan) == 0)  # 只有数值列才检查 0

        # 逻辑 OR (|) 找出所有问题单元格
        problem_cells = is_nan | is_zero

        # 3. 遍历行，合并连续的问题区域并输出报告
        print(f"--- 文件 '{file_path}' 的缺失/0 值单元格区域报告 ---")

        problem_rows_count = 0

        # 遍历每一行 (axis=1) 的布尔Series
        for row_index, row_problems in problem_cells.iterrows():
            # 找到该行中所有 True (有问题) 的列索引 (0-based)
            problem_col_indices = row_problems[row_problems].index.tolist()

            if not problem_col_indices:
                continue  # 该行没有问题，跳过

            problem_rows_count += 1

            # Excel 的行号是基于 1 的，所以是 row_index + 1
            excel_row_num = row_index + 1

            # 用于存储合并后的 Excel 单元格范围，例如 ['B126', 'D126:F126']
            ranges = []

            # 4. 合并连续的列索引
            start_col_index = None

            for i in range(len(problem_col_indices)):
                current_col_index = problem_col_indices[i]

                if start_col_index is None:
                    # 开始一个新的连续区域
                    start_col_index = current_col_index

                # 检查下一个列索引是否连续
                if i + 1 < len(problem_col_indices) and problem_col_indices[i + 1] == current_col_index + 1:
                    # 连续，继续寻找下一个
                    continue
                else:
                    # 遇到不连续点或到达列表末尾，结束当前区域
                    end_col_index = current_col_index

                    start_col_letter = col_to_excel_letter(start_col_index)
                    end_col_letter = col_to_excel_letter(end_col_index)

                    if start_col_index == end_col_index:
                        # 单个单元格，例如 B126
                        ranges.append(f"{start_col_letter}{excel_row_num}")
                    else:
                        # 连续范围，例如 B126:BO126
                        ranges.append(f"{start_col_letter}{excel_row_num}:{end_col_letter}{excel_row_num}")

                    # 重置开始索引
                    start_col_index = None

            # 打印该行的问题区域
            print(f"第 {excel_row_num} 行问题区域：{', '.join(ranges)}")

        print("\n--- 总结 ---")
        print(f"总计包含缺失值或 0 值的行数: {problem_rows_count}")
        print("--------------------")

    except FileNotFoundError:
        print(f"错误：文件未找到，请检查路径是否正确：{file_path}")
    except Exception as e:
        # 其他精简异常处理
        print(f"处理文件时发生错误: {e}")


# --- 示例使用 ---
# 请替换成你的 Excel 文件路径
excel_file_path = '运动者1的跳远位置信息.xlsx'

# 运行分析函数
analyze_excel_with_cell_ranges(excel_file_path)
