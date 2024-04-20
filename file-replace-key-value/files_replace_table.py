import os
import open_excel_table as oet
import open_excel_column as oec

'''
打开指定目录下的全部文件，进行遍历，按照表、字段列的KEY/VALUE配置信息，进行批量替换
并且对目录下的文件进行回写保存
'''

def open_and_save(dir_path, key_value):
    count = 0
    print("initial count 0, dir path:" + dir_path)

    # 遍历目录下的所有文件
    for root, dirs, files in os.walk(dir_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            print("file path:" + file_path)

            # 打开文件并读取内容
            with open(file_path, "r", encoding='utf-8') as f:
                content = f.read()

            # 替换键值对
            for key, value in key_value.items():
                content = content.replace(key, value)
                count += 1

            # 将替换后的内容写入文件
            with open(file_path, "w", encoding='utf-8') as f:
                f.write(content)

    return count

print("loading key value")
# 配置 key/value 键值对
table_key_value = oet.key_value_pairs
for key, value in table_key_value.items():
    print(key, value)
# 指定目录路径 path/to/directory
dir = "./workdir"
table_count = open_and_save(dir, table_key_value)
print("Replace table", table_count)
# column_key_value = oec.key_value_pairs
# for key, value in column_key_value.items():
#     print(key, value)
# column_count = open_and_save(dir, column_key_value)
# print("Replace column", column_count)