import os

def list_dir():
    for item in os.listdir():

        if os.path.isdir(item):
            print(f"[DIR]{item}")
        else:
            print(item)


list_dir()
