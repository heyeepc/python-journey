import os

def rename_txt_files(path):
    i = 0

    for name in os.listdir(path):
        if name.endswith(".txt"):          # 只处理 txt
            i += 1

            old_path = os.path.join(path, name)
            new_path = os.path.join(path, f"file_{i}.txt")

            os.rename(old_path, new_path)

# 正确调用
rename_txt_files(".")
