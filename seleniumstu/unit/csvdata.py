import csv
import os


def get_data(file_name):
    """获取.csv中的数据"""
    rows = []
    dir_path = os.path.abspath(os.path.join(os.getcwd(), "."))  # 获取当前路径的上一级
    data_file = open(dir_path+"\\data\\"+file_name, "r")
    reader = csv.reader(data_file)
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows
