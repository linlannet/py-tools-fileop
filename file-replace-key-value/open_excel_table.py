import openpyxl

'''
读取表名称的配置信息，存储到对象中
'''

def read_key_value_from_excel(file_path, sheet_name):
    # 打开Excel文件
    workbook = openpyxl.load_workbook(file_path)

    # 选择指定的工作表
    sheet = workbook[sheet_name]

    key_value_pairs = {}

    # 遍历每一行数据，第一、二行为标题和说明，从第三行开始
    for row in sheet.iter_rows(min_row=3, values_only=True):
        # 将第一列作为键，第二列作为值
        key = row[0]
        value = row[1]

        # 如果键和值都存在，则添加到键值对字典中
        if key and value:
            key_value_pairs[key] = value

    # 关闭Excel文件
    workbook.close()

    return key_value_pairs

# 示例用法
file_path = './config/table-key-value.xlsx'  # 替换成你的Excel文件路径
sheet_name = 'table'  # 替换成你的工作表名

key_value_pairs = read_key_value_from_excel(file_path, sheet_name)

# 打印键值对
# for key, value in key_value_pairs.items():
#     print(key, value)