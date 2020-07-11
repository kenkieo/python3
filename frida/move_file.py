import os
import shutil


def move_dir():
    for root, dirs, files in os.walk(r"H:\模拟器\tmyh\assets"):
        for file in files:
            shutil.move(os.path.join(root, file), os.path.join(r"H:\模拟器\tmyh\source", file))
            print(file)
