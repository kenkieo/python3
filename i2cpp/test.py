import os
import json

from i2cpp.block.Basic import Basic
from i2cpp.block.Header import Header

GLOBAL_METADATA_NAME = 'global-metadata.dat'
JSON_RESULT = 'result.json'


def check_path(func):
    def run(global_metadata_dir):
        if os.path.isdir(global_metadata_dir):
            global_metadata_dir = os.path.join(global_metadata_dir, GLOBAL_METADATA_NAME)
        if not os.path.exists(global_metadata_dir):
            print('文件或目录不存在')
            return
        func(global_metadata_dir)

    return run


@check_path
def decode(global_metadata_dir):
    json_path = os.path.join(os.path.dirname(global_metadata_dir), JSON_RESULT)
    Basic.read_f = open(global_metadata_dir, 'rb')
    header = Header()
    header.decode()
    header.close()
    write_json(json_path, dict.fromkeys(header.string_data, ''))


@check_path
def encode(global_metadata_dir):
    json_path = os.path.join(os.path.dirname(global_metadata_dir), JSON_RESULT)
    Basic.read_f = open(global_metadata_dir, 'rb')
    dir_name, file_name = os.path.split(global_metadata_dir)
    ok_dir = os.path.join(dir_name, 'OK')
    if not os.path.exists(ok_dir):
        os.mkdir(ok_dir)
    Basic.write_f = open(os.path.join(ok_dir, file_name), 'wb')
    Basic.json_result = read_json(json_path)
    header = Header()
    header.decode()
    header.encode()
    header.close()


# 写入JSON数据，格式化
def write_json(json_path, json_result, format=True):
    with open(json_path, 'w', encoding='utf-8') as load_f:
        if format:
            json.dump(json_result, load_f, indent=4, separators=(',', ':'), ensure_ascii=False)
        else:
            json.dump(json_result, load_f, ensure_ascii=False)


def read_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as load_f:
        json_result = json.load(load_f)
    return json_result


if __name__ == '__main__':
    while True:
        f_path = input('请输入文件路径:\n ')
        if f_path.startswith("'"):
            f_path = f_path[1:-1]
        print(f_path, os.path.exists(f_path))
        if not (f_path and os.path.exists(f_path)):
            print('文件不存在!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n\n')
            continue
        f_dir = os.path.dirname(f_path)
        result = input("请输入模式，1：解析，2：编译\n")
        json_path = os.path.join(f_dir, 'result.json')
        if str(result).__eq__('1'):
            decode(f_path.strip())
            print('解码成功!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n\n')
        elif str(result).__eq__('2'):
            encode(f_path.strip())
            print('编译成功!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n\n')
        else:
            print('输入不正确!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n\n')
