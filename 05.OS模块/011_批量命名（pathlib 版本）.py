from pathlib import Path

def rename_txt_files(path):
    p = Path(path)
    i = 0

    for file in p.iterdir():
        if file.is_file() and file.suffix == ".txt":
            i += 1
            new_name = p / f"file_{i}.txt"
            file.rename(new_name)

rename_txt_files(".")
